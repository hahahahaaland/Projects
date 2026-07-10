import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789"
)

cursor = connection.cursor()

def run_query(query):
    cursor.execute(query)
    return cursor.fetchall()


def run_query_no_output(query):
    cursor.execute(query)
    connection.commit()


def run_query_one(query):
    cursor.execute(query)
    return cursor.fetchone()

# Create database
run_query_no_output("CREATE DATABASE IF NOT EXISTS students_db")
run_query_no_output("USE students_db")

# Create table
run_query_no_output("""
CREATE TABLE IF NOT EXISTS students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    marks INT
)
""")

# Clear old data (optional, avoids duplicates when rerunning)
run_query_no_output("DELETE FROM students")

# Insert records
run_query_no_output("""
INSERT INTO students(name, marks)
VALUES('Alice',90)
""")

run_query_no_output("""
INSERT INTO students(name, marks)
VALUES('Bob',75)
""")

run_query_no_output("""
INSERT INTO students(name, marks)
VALUES('Charlie',65)
""")

# Print all students
students = run_query("SELECT * FROM students")

print("All Students:")
for student in students:
    print(student)

# Find one student
student = run_query_one("""
SELECT *
FROM students
WHERE name='Alice'
""")

print("\nAlice:")
print(student)

# Student not found
student = run_query_one("""
SELECT *
FROM students
WHERE name='David'
""")

print("\nDavid:")
print(student)

cursor.close()
connection.close()