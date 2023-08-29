import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to the database
conn = sqlite3.connect('people.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS people
             (name text, age integer)''')

#add a person to the database
def add_person():
    name = name_entry.get()
    age = age_entry.get()
    if not name or not age:
        messagebox.showerror("Error", "Please enter a name and age")
        return
    c.execute("INSERT INTO people VALUES (?, ?)", (name, int(age)))
    conn.commit()
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Person added successfully")

#view all people in the database
def view_people():
    c.execute("SELECT * FROM people")
    rows = c.fetchall()
    result = ""
    for row in rows:
        result += f"Name: {row[0]}, Age: {row[1]}\n"
    messagebox.showinfo("People", result)

#remove a person from the database by name
def remove_person():
    name = remove_entry.get()
    if not name:
        messagebox.showerror("Error", "Please enter a name")
        return
    c.execute("DELETE FROM people WHERE name=?", (name,))
    conn.commit()
    remove_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Person removed successfully")

#  main window of UI
root = tk.Tk()
root.title("People Database")

# input name
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

#  input age
age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

# add button
add_button = tk.Button(root, text="Add Person", command=add_person)
add_button.pack()

# view button
view_button = tk.Button(root, text="View People", command=view_people)
view_button.pack()

# remove field 
remove_label = tk.Label(root, text="Remove by Name:")
remove_label.pack()
remove_entry = tk.Entry(root)
remove_entry.pack()

# remove button
remove_button = tk.Button(root, text="Remove Person", command=remove_person)
remove_button.pack()

root.mainloop()

conn.close()