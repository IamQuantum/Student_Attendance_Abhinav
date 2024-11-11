import tkinter as tk
from tkinter import messagebox
from backend_code import add_student, mark_attendance, fetch_students, fetch_attendance, delete_student

root = tk.Tk()
root.title("Student Attendance System")
root.geometry("500x400")

def add_student_gui():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    if name and age and gender:
        add_student(name, int(age), gender)
        messagebox.showinfo("Success", "Student added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

def mark_attendance_gui():
    student_id = entry_attendance_id.get()
    status = entry_status.get()
    if student_id and status:
        mark_attendance(int(student_id), status)
        messagebox.showinfo("Success", "Attendance marked successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

def view_students_gui():
    students = fetch_students()
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Students:\n")
    for student in students:
        output_text.insert(tk.END, f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Gender: {student[3]}\n")

def view_attendance_gui():
    student_id = entry_view_attendance_id.get()
    if student_id:
        attendance_records = fetch_attendance(int(student_id))
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Attendance:\n")
        for record in attendance_records:
            output_text.insert(tk.END, f"Date: {record[2]}, Status: {record[3]}\n")
    else:
        messagebox.showwarning("Input Error", "Please provide a student ID.")

def delete_student_gui():
    student_id = entry_delete_id.get()
    if student_id:
        delete_student(int(student_id))
        messagebox.showinfo("Success", "Student deleted successfully!")
    else:
        messagebox.showwarning("Input Error", "Please provide a student ID.")

tk.Label(root, text="Add Student").pack()
entry_name = tk.Entry(root)
entry_name.insert(0, "Name")
entry_name.pack()
entry_age = tk.Entry(root)
entry_age.insert(0, "Age")
entry_age.pack()
entry_gender = tk.Entry(root)
entry_gender.insert(0, "Gender")
entry_gender.pack()
tk.Button(root, text="Add Student", command=add_student_gui).pack()

tk.Label(root, text="Mark Attendance").pack()
entry_attendance_id = tk.Entry(root)
entry_attendance_id.insert(0, "Student ID")
entry_attendance_id.pack()
entry_status = tk.Entry(root)
entry_status.insert(0, "Status (Present/Absent)")
entry_status.pack()
tk.Button(root, text="Mark Attendance", command=mark_attendance_gui).pack()

tk.Label(root, text="View All Students").pack()
tk.Button(root, text="View Students", command=view_students_gui).pack()

tk.Label(root, text="View Attendance").pack()
entry_view_attendance_id = tk.Entry(root)
entry_view_attendance_id.insert(0, "Student ID")
entry_view_attendance_id.pack()
tk.Button(root, text="View Attendance", command=view_attendance_gui).pack()

tk.Label(root, text="Delete Student").pack()
entry_delete_id = tk.Entry(root)
entry_delete_id.insert(0, "Student ID")
entry_delete_id.pack()
tk.Button(root, text="Delete Student", command=delete_student_gui).pack()

output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()
