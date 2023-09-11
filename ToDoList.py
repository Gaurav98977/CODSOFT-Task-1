
# Importing the necessary modules
from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)

# Creating the Window
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('Your To-Do List')
ws.config(bg='#ffcc00')  # Customize the background color
ws.resizable(width=False, height=False)

# Now we Creating a frame
frame = Frame(ws)
frame.pack(pady=5)

#  Next we Adding a Listbox
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 20),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)

lb.pack(side=LEFT, fill=BOTH)


#Now I Adds my dummy data 
#which i do every day

task_list = [
    'Do CodSoft Internship',
    'Go to the Gym',
    'Computer Class',
    'Attend Online Meeting',
    'Lunch',
    'Some Gaming Time',
    'Play Cricket',
    'Friends Meeting',
    'Self Learning Time'
]

for item in task_list:
    lb.insert(END, item)

#Adding the  Scroll-bars so we can easily navigate the task 
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#Adding the Entry Box for adding any new task
my_entry = Entry(
    ws,
    font=('times', 24)
)
my_entry.pack(pady=30)


# Adding another frame for buttons
button_frame = Frame(ws)
button_frame.pack(pady=20)

#Adding 'Add Your Task' Buttons

addTask_btn = Button(
    button_frame,
    text='Add Your Task',
    font=('times 18'),
    bg='#007acc',  # Customize the button background color
    fg='white',     # Customize the button text color
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# Delete task Button

delTask_btn = Button(
    button_frame,
    text='Delete Your Task',
    font=('times 18'),
    bg='#ff3300',  # Customize the button background color
    fg='white',     # Customize the button text color
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
