from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route("/students", methods=["GET"])
def get_students():
    conn = sqlite3.connect("training.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    students = []
    for row in rows:
        students.append({
            "id": row[0],
            "name": row[1],
            "age": row[2]
        })

    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Both name and age are required"}), 400

    conn = sqlite3.connect("training.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)",
        (data["name"], data["age"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Student added successfully"}), 201

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()

    conn = sqlite3.connect("training.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name=?, age=? WHERE id=?",
        (data["name"], data["age"], id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Student updated successfully"})

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = sqlite3.connect("training.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return jsonify({"message": "Student deleted successfully"})

print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)
