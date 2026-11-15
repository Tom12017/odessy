# SQL and SQLite in Odessy

This folder contains developer documentation, not live databases or a new database service.

## Storage ownership and source baseline

**Developer Preview · v0.5.0-alpha**

Reviewed November 15, 2026; see the [source baseline](../current-status.md).

| Code | Storage | Purpose |
| --- | --- | --- |
| `develop` at `80f2580` | `usage-history.sqlite3` | Provider-reported token usage and cost; no prompt text |
| `develop` at `80f2580` | JSON session records and `.bak` files | Application session identity, queued/settled turn state and bounded client-visible history (`application/durable.py`) |
| Merged PR #67 implementation (`b89361b`, merged to develop) | `conversations.sqlite3` | Durable projects, conversations, message/activity records, search, explicit memory and indexed documents |

**PR #67 is merged into remote develop at `3a52fcc`; the local `80f2580` checkout predates it.** This documentation-only update does not synchronize source or enable features. Runtime-owned Harness history remains separate. Saved history alone does not establish that an engine can continue a conversation; the PR explicitly advertises Custom continuation and Harness history-only behavior.

## What SQL does

SQL is a language for reading and changing structured data. SQLite is the database engine executing that SQL inside the Python process. It stores tables and indexes in a local file; no PostgreSQL/MySQL server, account, network connection or paid service is needed.

A table contains rows (records) and columns (fields). A primary key identifies a row. A foreign key relates rows, such as messages belonging to a conversation. An index accelerates selected lookups; it is not a separate authoritative copy of the conversation.

The main operations are:

```sql
-- Read recent metadata; this does not send prompts or resume an engine.
SELECT id, title, engine, updated_at
FROM conversations
ORDER BY updated_at DESC, id DESC
LIMIT 20;

-- Read events from one conversation in their recorded order.
SELECT sequence, kind, payload_json
FROM conversation_events
WHERE conversation_id = ?
ORDER BY sequence
LIMIT ?;
```

`?` placeholders bind values separately from SQL text. In Python:

```python
rows = db.execute(
    'SELECT sequence, kind FROM conversation_events '
    'WHERE conversation_id = ? ORDER BY sequence LIMIT ?',
    (conversation_id, 50),
).fetchall()
```

Never concatenate user input into SQL. `INSERT` adds a row, `UPDATE` changes fields, and `DELETE` removes rows. Application services validate these operations and enforce ownership/revisions; direct database edits bypass those checks.

## Where files live

`models/usage_history.py:default_history_path()` places usage history beside an explicit `ODESSY_CONFIG_FILE`, otherwise under `~/.config/odessy/`.

In the merged conversation implementation, `ConversationStore.default_store_path()` follows the same rule for `conversations.sqlite3`. The application composition also accepts a configuration path and places the database beside that path. Isolated tests inject temporary paths. Do not assume the repository folder, working directory or `D:/Odessy` is the active user profile.

On Windows, `~` means the account's home directory. Installed processes and tests may use an isolated profile, so inspect the actual configuration before diagnosing a missing history file.

## Conversation schema

| Table | Owner and contents |
| --- | --- |
| `projects` | Project IDs and labels |
| `conversations` | Project, engine, profile, title, pin/archive flags and revision |
| `conversation_events` | Ordered user/assistant, partial text, tool/activity, attachment and interruption records; structured payloads are JSON text |
| `conversation_events_fts` | Optional SQLite FTS5 index used for text search |
| `conversation_workspace_bindings` | Trusted workspace identity for a saved conversation; not a grant |
| `schema_extensions` | Version records for independently owned schema extensions |
| `memory_facts` | Explicit project memory with enabled flag and revision |
| `context_summaries`, `context_usage` | Bounded summaries and records of context used |
| `retrieval_documents`, `retrieval_chunks` | Opt-in document metadata, source hashes and bounded excerpts |
| `retrieval_chunks_fts` | Optional full-text index for document excerpts |

Core schema: `src/odessy/application/conversations/store.py`. Extension schema: `src/odessy/application/context/schema.py`. Composition and workspace bindings: `src/odessy/application/basics_integration.py`. These paths are in PR #67 until merged.

The usage database is separate: `usage_requests` records provider/model, time, token counts and reported cost. Checkpoints use owned Git references and metadata files; terminal process handles and effective access-mode grants are live state, not database authority.

## What happens when you chat?

1. The authenticated application selects a live session, engine and workspace.
2. The recorder persists an admitted user message and subsequent public events. Event IDs make repeated appends idempotent rather than duplicating history.
3. Public assistant results settle into saved history. Streaming deltas and interrupted turns remain distinguishable from a completed answer.
4. History/search views query saved records. They do not replay tools or execute commands.
5. Custom continuation creates or resolves an authorized live controller and supplies saved context. Workspace identity, engine/profile availability and current grants are checked separately.

Memory, retrieval excerpts and transcripts can contain private user content. Redaction is defense in depth, not database encryption. Do not commit live databases, exports, credentials or private fixture data.

## Transactions, revisions and failures

A transaction groups related changes so they commit together or roll back. PR #67's core write helper serializes writes and begins `BEGIN IMMEDIATE` before reading/changing a reviewed revision. Each operation owns its connection; callers must not share one SQLite connection across threads. A connection context by itself does not guarantee a transaction before a `SELECT`.

A revision is an optimistic concurrency check. For example, updating a row only when `revision = expected_revision` prevents an older settings/history view overwriting a newer change. A mismatch returns a conflict; reload before retrying. It must not silently succeed.

The conversation store enables foreign keys, requests WAL journaling and uses a five-second busy timeout. WAL permits readers alongside a writer; it does not permit unlimited simultaneous writes. SQLite may create `-wal` and `-shm` sidecar files. Slow/busy storage can still fail, and blocking SQL/file work must stay off the service event loop.

Core migrations use `PRAGMA user_version`; context/memory/retrieval extensions use `schema_extensions`. A newer or corrupt schema is refused instead of being silently reset. Conversation deletion cascades conversation-owned rows and must clean derived search records; project memory/documents and arbitrary workspace files have different lifecycles.

## Safe inspection and backup

Prefer the supported history/export and usage interfaces. For diagnosis, use an existing Python interpreter and open an existing file read-only (replace the example path):

```python
from pathlib import Path
import sqlite3

path = Path(r'C:/path/to/profile/conversations.sqlite3').resolve(strict=True)
with sqlite3.connect(path.as_uri() + '?mode=ro', uri=True) as db:
    db.execute('PRAGMA query_only = ON')
    print(db.execute('PRAGMA user_version').fetchone())
    print(db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall())
```

This example does not create a missing database. Read-only opening does not grant access to someone else's profile. A diagnostic `PRAGMA quick_check` is available but may be slow on a large file.

Use SQLite's backup API for a consistent database backup; copying just the main file while WAL writes are active can omit recent changes. Alternatively stop the owning service cleanly before taking a consistent profile backup. Preserve configuration and other profile-owned files separately. Do not delete `-wal`/`-shm` files to unlock a running application, overwrite a live database, or run manual migrations against user data.

## Contributor verification

On develop, the existing usage history tests exercise the supported SQL path:

```powershell
python -m pytest -q tests/test_usage_history.py
```

On a source revision containing the merged conversation services, use the existing cached/project environment and relevant tests, for example:

```powershell
python -m pytest -q tests/test_conversation_store.py tests/test_memory_service.py tests/test_retrieval_service.py tests/test_context_service.py
```

These are source checks. They do not qualify installed packages, real providers, hardware, migrations from arbitrary released profiles, or complete CI. Check the live PR and qualification receipts for those results.
