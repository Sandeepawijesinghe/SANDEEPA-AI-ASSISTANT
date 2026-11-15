import sqlite3
from pathlib import Path
from datetime import datetime

# Keep the existing database file. Do not delete it during upgrades.
DATABASE_PATH = Path(__file__).parent / "sandeepa_ai.db"

def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def init_db():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS chats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (chat_id) REFERENCES chats(id) ON DELETE CASCADE
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL UNIQUE,
                created_at TEXT NOT NULL
            )
        """)
    print("SANDEEPA AI Database Ready!")

def create_chat(title="New Conversation"):
    with get_connection() as connection:
        cursor = connection.execute(
            "INSERT INTO chats (title, created_at) VALUES (?, ?)",
            (title, datetime.now().isoformat())
        )
        return cursor.lastrowid

def add_message(chat_id, role, content):
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO messages (chat_id, role, content, created_at) VALUES (?, ?, ?, ?)",
            (chat_id, role, content, datetime.now().isoformat())
        )

def get_chats():
    with get_connection() as connection:
        rows = connection.execute("SELECT * FROM chats ORDER BY id DESC").fetchall()
        return [dict(row) for row in rows]

def get_messages(chat_id):
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM messages WHERE chat_id = ? ORDER BY id ASC", (chat_id,)
        ).fetchall()
        return [dict(row) for row in rows]

def delete_chat(chat_id):
    with get_connection() as connection:
        connection.execute("DELETE FROM chats WHERE id = ?", (chat_id,))

def save_memory(content):
    content = content.strip()
    if not content:
        return False
    with get_connection() as connection:
        connection.execute(
            "INSERT OR IGNORE INTO memories (content, created_at) VALUES (?, ?)",
            (content, datetime.now().isoformat())
        )
    return True

def get_memories():
    with get_connection() as connection:
        rows = connection.execute("SELECT * FROM memories ORDER BY id DESC").fetchall()
        return [dict(row) for row in rows]

def delete_memory(memory_id):
    with get_connection() as connection:
        connection.execute("DELETE FROM memories WHERE id = ?", (memory_id,))

if __name__ == "__main__":
    init_db()
