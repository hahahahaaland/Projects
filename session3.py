import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

def run_query(query):
    cursor.execute(query)
    return cursor.fetchall()

def run_query_no_output(query):
    cursor.execute(query)
    connection.commit()

# Create table
run_query_no_output("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Clear old data
run_query_no_output("DELETE FROM students")

# Insert fresh data
run_query_no_output("INSERT INTO students(name,marks) VALUES('Alice',90)")
run_query_no_output("INSERT INTO students(name,marks) VALUES('Bob',75)")
run_query_no_output("INSERT INTO students(name,marks) VALUES('Charlie',65)")

students = run_query("SELECT * FROM students")

for student in students:
    print(student)

def run_query_one(query):
    cursor.execute(query)
    return cursor.fetchone()

student = run_query_one(
"""
SELECT *
FROM students
WHERE name='Alice'
"""
)

print(student)

student = run_query_one(
"""
SELECT *
FROM students
WHERE name='David'
"""
)

print(student)


result = run_query("""
SELECT name, marks
FROM students
WHERE marks > 70
ORDER BY marks DESC
""")

print(result)