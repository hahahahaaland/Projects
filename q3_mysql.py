import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="students_db"
)

cursor = connection.cursor()

cursor.execute("""
SELECT name, marks
FROM students
WHERE marks > 70
ORDER BY marks DESC
""")

students = cursor.fetchall()

print("Students scoring above 70:")
for student in students:
    print(student)

cursor.close()
connection.close()