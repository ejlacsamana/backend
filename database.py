import sqlite3

def init_db():
    # Connect to the db
    conn = sqlite3.connect("workout_tracker.db")

    # Create cursor object
    c = conn.cursor()

    # Create the table using SQL
    c.execute("""
    CREATE TABLE IF NOT EXISTS workouts (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              date TEXT,
              exercise_name TEXT,
              set_order INTEGER,
              reps INTEGER,
              weight REAL
    )""")

    conn.commit()
    conn.close()

init_db()