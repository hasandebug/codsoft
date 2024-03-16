import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkinter as tk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x500")
app.title("To-do-List")

tasks = []


def updatelistbox():

    task_listbox.delete(0, "end")

    for task in tasks:
        task_listbox.insert("end", f"{task}")


def addTasks():
    task = inputBar.get().strip()
    if task:
        tasks.append(task)
        updatelistbox()
        inputBar.delete(0, "end")
    else:
        msg = CTkMessagebox(
            title="Warning!",
            message="Please input something",
            icon="warning",
            option_1="Cancel",
            option_2="Retry",
        )


def deleteTasks():
    selected_index = task_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        try:
            tasks.pop(selected_index)
            updatelistbox()
        except IndexError:
            msg = CTkMessagebox(
                title="Warning!",
                message="Invalid selection",
                icon="warning",
                option_1="Cancel",
            )
    else:

        msg = CTkMessagebox(
            title="Warning!",
            message="Please select a task to remove",
            icon="warning",
            option_1="Cancel",
        )


def updatetasks():

    selected_item_text = task_listbox.get(tk.ACTIVE)
    if selected_item_text:
        dialog = ctk.CTkInputDialog(text="Enter your New task", title="New Task")
        newEntry = dialog.get_input()
        if newEntry:
            index = tasks.index(selected_item_text)
            tasks[index] = newEntry
            updatelistbox()
        else:
            msg = CTkMessagebox(
                title="Warning!",
                message="Please add a new task",
                icon="warning",
                option_1="Cancel",
            )
    else:
        msg = CTkMessagebox(
            title="Warning!",
            message="Please select a task to update",
            icon="warning",
            option_1="Cancel",
        )


def exits():
    app.destroy()


label = ctk.CTkLabel(app, text="TO-DO-LIST", font=("verdana", 16))
label.pack()

inputBar = ctk.CTkEntry(
    app,
    border_width=1,
    border_color="black",
    placeholder_text="Enter a new task",
    width=300,
    height=30,
)
inputBar.pack(side="top", pady=5)

addTaskBtn = ctk.CTkButton(
    app, text="Add Task", command=addTasks, border_color="black", text_color="black"
)
addTaskBtn.pack(pady=5)

task_listbox = tk.Listbox(app, width=50, height=12)
task_listbox.pack(pady=5)

removeTaskBtn = ctk.CTkButton(
    app,
    text="Remove Task",
    command=deleteTasks,
    border_color="black",
    text_color="black",
)
removeTaskBtn.pack(pady=5)

updateTaskbtn = ctk.CTkButton(
    app, text="Update Task", command=updatetasks, text_color="black"
)
updateTaskbtn.pack(pady=5)

exitBtn = ctk.CTkButton(
    app, text="Exit Task", command=exits, border_color="black", text_color="black"
)
exitBtn.pack(pady=5)

app.mainloop()
