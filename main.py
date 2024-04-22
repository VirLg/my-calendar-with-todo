import tkinter as tk
import customtkinter
import sqlite3

root = customtkinter.CTk()

root.title("Working space")
root.wm_attributes("-alpha", 0.9)
root.geometry("800x800")

root.resizable(0, 0 )

def dbStart ():
    global conn,cur
    conn  = sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY, note TEXT, complited BOOLEAN)""")

def updateTodoList():
    todoList.delete(0,customtkinter.END)
    cur.execute("SELECT * FROM notes")
    notes = cur.fetchall()
    for note in notes:
        noteText = note[1]
        todoList.insert(customtkinter.END,noteText)





todoLableName = customtkinter.CTkLabel(root, text="name")
todoLableName.pack(pady=5)

todoLableAria = customtkinter.CTkLabel(root, text="text")
todoLableAria.pack(pady=5)

check_var = customtkinter.StringVar(value="off")
my_check = customtkinter.CTkCheckBox(root, text="Complited",variable=check_var)
my_check.pack(pady=5)

saveBtn = customtkinter.CTkButton(root, text="Add")
saveBtn.pack(pady=5)

deleteBtn = customtkinter.CTkButton(root, text="Delete")
deleteBtn.pack(pady=5)

todoList = tk.Listbox(root, width=130,height=50)
todoList.pack(pady=5)







dbStart()
updateTodoList()
root.mainloop()
conn.close()