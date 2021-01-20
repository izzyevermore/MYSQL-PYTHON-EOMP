#Importing all operations
from tkinter import *
import mysql.connector
from tkinter import messagebox
import sys
import os

# Creating GUI that allows log in into lifechoices data bases and displays log in info
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost', database='lifechoicesonline')

mycursor = mydb.cursor()

app = Tk()
app.title("Lifechoices User System")
app.geometry("800x800")
app.config(bg="black")

# Creating Lifechoices logo
label_logo = Label(app, text="LIFECHOICES", width=55, font=("Helvetica", 20), bg="light green")
label_logo.place(x=0, y=0)

# Creating username and password entry for users
life_label = Label(app, text="Username")
life_label.place(x=350, y=100)

life_entry = Entry(app, width=40)
life_entry.place(x=250, y=150)

life_pass = Label(app, text="Password")
life_pass.place(x=350, y=200)

user_password = Entry(app, width=40, show="*")
user_password.place(x=250, y=250)

# Defining the login button that shows when a user has logged in as well as when they fail.
def logged():
    messagebox.showinfo("SUCCESS", "You have successfully logged in " + life_entry.get())
    # Creating a labelframe that allows user to enter their number to sign in
    app2 = Tk()
    app2.title("Mobile Entry")
    app2.geometry("300x200")
    app2.config(bg="black")

    number_label = Label(app2, text="Please enter your mobile number: ")
    number_label.place(x=0, y=0)

    number_entry = Entry(app2, width=20)
    number_entry.place(x=0, y=40)

    def sigin():
        try:
            x = int(number_entry.get())
            messagebox.showinfo("SUCCESS", "You have signed in, Have a great day " + life_entry.get())

            # This part if for the user that once they click on sign in it will record their time
            app2.destroy()
        except ValueError:
            messagebox.showerror("ValueError", "Please enter numbers only " + life_entry.get())


    signin_button = Button(app2, text="Sign-in", width=10, command=sigin)
    signin_button.place(x=0, y=100)


def failed():
    messagebox.showerror("UNSUCCESSFUL", "Try Again!")
    life_entry.delete(0, END)
    user_password.delete(0, END)

def login():
    user = life_entry.get()
    password = user_password.get()
    sql = 'Select * from Users where Username = %s and Password = %s'
    mycursor.execute(sql, [(user), (password)])
    results = mycursor.fetchall()


    if results:
        sql = 'UPDATE Users SET Login_time = NOW() WHERE Username = %s'
        mycursor.execute(sql, [user])
        mydb.commit()

        if mycursor.rowcount > 0:
            #update was success
            pass

        for i in results:
            logged()
            break
        else:
            failed()


login_button = Button(app, text="Login", width=20, command=login)
login_button.place(x=50, y=350)

def signout():
    username = life_entry.get()
    userpass = user_password.get()
    sql = 'Select * from Users where Username = %s and Password = %s'
    mycursor.execute(sql, [(username), (userpass)])
    results = mycursor.fetchall()

    if results:
        sql = 'UPDATE Users SET Logout_time = NOW() WHERE Username = %s'
        mycursor.execute(sql, [username])
        mydb.commit()

        if mycursor.rowcount > 0:
            # update was success
            pass

        for i in results:
            messagebox.showinfo("GOODBYE")
            break
        else:
            life_entry.delete(0, END)
            user_password.delete(0, END)


signout_button = Button(app, text="Sign-out", width=20, command=signout)
signout_button.place(x=300, y=450)



# Creating the register button that takes user to the admin for them to signin
def register():
    app.destroy()
    messagebox.showinfo("!!!!!!!!!!", "Please sign in as admin")
    window = Tk()
    window.title("Admin Sign-in")
    window.geometry("300x300")
    window.config(bg="black")

    admin_username = Label(window, text="Please enter your username: ")
    admin_username.place(x=0, y=0)

    admin_entry = Entry(window, width=20)
    admin_entry.place(x=0, y=30)

    admin_password = Label(window, text="Please enter your password: ")
    admin_password.place(x=0, y=80)

    admin_entry2 = Entry(window, width=20)
    admin_entry2.place(x=0, y=110)




    def admin_login():
        window.destroy()
        root = Tk()
        root.title("Lifechoices Admin System")
        root.geometry("800x800")
        root.config(bg="black")

        label_logo2 = Label(root, text="LIFECHOICES", width=55, font=("Helvetica", 20), bg="light green")
        label_logo2.place(x=0, y=0)

    adminbtn = Button(window, text="Login", width=20, command=admin_login)
    adminbtn.place(x=0, y=250)









register_button = Button(app, text="Register Here", width=20, command=register)
register_button.place(x=580, y=350)
# Creating a listbox that lists the users
listBox = Listbox(app)
listBox.place(x=350, y=500)

listOfUsers = [[1, 'isaiah'], [2, 'nick'], [3, 'sallie']]

def populatebox():
    for i in listOfUsers:
        listBox.insert("end", i)

btn = Button(app, text="Update list", command = lambda: populatebox())
btn.pack()

# Creating the register button that allows user to create new user




app.mainloop()