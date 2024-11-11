import mysql.connector
from datetime import date

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aditya123",
    database="attendance_system"
)
cursor = db.cursor()

def add_student(name, age, gender):
    query = "INSERT INTO students (name, age, gender) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, gender))
    db.commit()

def mark_attendance(student_id, status):
    query = "INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)"
    cursor.execute(query, (student_id, date.today(), status))
    db.commit()

def fetch_students():
    query = "SELECT * FROM students"
    cursor.execute(query)
    return cursor.fetchall()

def fetch_attendance(student_id):
    query = "SELECT * FROM attendance WHERE student_id = %s"
    cursor.execute(query, (student_id,))
    return cursor.fetchall()

def delete_student(student_id):
    query = "DELETE FROM students WHERE student_id = %s"
    cursor.execute(query, (student_id,))
    db.commit()