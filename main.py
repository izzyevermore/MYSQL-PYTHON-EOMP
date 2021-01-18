#Importing all operations
from tkinter import *
import mysql.connector
from tkinter import messagebox

# Creating GUI that allows log in into lifechoices data bases and displays log in info
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost', database='lifechoicesonline')

mycursor = mydb.cursor()

app = Tk()
app.title("Lifechoices User System")
app.geometry("600x600")
app.config(bg="black")

# Creating Lifechoices logo
label_logo = Label(app, text="LIFECHOICES", width=40, font=("Helvetica", 20), bg="light green")
label_logo.place(x=0, y=0)

#Creating username and password entry for users
life_label = Label(app, text="Username")
life_label.place(x=260, y=100)

life_entry = Entry(app, width=40)
life_entry.place(x=150, y=150)

life_pass = Label(app, text="Password")
life_pass.place(x=260, y=200)

user_password = Entry(app, width=40, show="*")
user_password.place(x=150, y=250)

# Defining the login button that shows when a user has logged in as well as when they fail.
def logged():
    messagebox.showinfo("SUCCESS", "You have successfully logged in " + life_entry.get())

def failed():
    messagebox.showerror("UNSUCCESSFUL", "Try Again!")
    life_entry.delete(0, END)
    user_password.delete(0, END)

def login():
    user = life_entry.get()
    password = user_password.get()

    if password == str:
        raise ValueError
    else:
        sql = 'Select * from Users where Username = %s and Password = %s'
        mycursor.execute(sql, [(user), (password)])
        results = mycursor.fetchall()


        if results:
            for i in results:
                logged()
                break
        else:
            failed()

login_button = Button(app, text="Login", width=20, command=login)
login_button.place(x=50, y=350)

# Creating the register button that allows user to create new user




app.mainloop()