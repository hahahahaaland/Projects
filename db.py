import sqlite3

def init_db():
    conn = sqlite3.connect("training.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        )
    """)

    conn.commit()
    conn.close()
    print("Database and students table created successfully!")

if __name__ == "__main__":
    init_db()
