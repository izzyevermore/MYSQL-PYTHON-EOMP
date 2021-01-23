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
    # Creating and Defining the signin button for users to enter their number
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

# If users details is wrong
def failed():
    messagebox.showerror("UNSUCCESSFUL", "Try Again!")
    life_entry.delete(0, END)
    user_password.delete(0, END)

# Creating and defining the login button that allows user to singin and stores their time
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

# Creating and defining the signout button that stores users logout time
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
            messagebox.showinfo("GOODBYE", "You have successfully signed out")
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



# Creating and defining the admin sigin button
    def admin_login():

        username = admin_entry.get()
        userpass = admin_entry2.get()
        sql = 'Select * from Admin where Username = %s and Password = %s'
        mycursor.execute(sql, [(username), (userpass)])
        results = mycursor.fetchall()

        if results:
            sql = 'UPDATE Admin SET Login_time = NOW() WHERE Username = %s'
            mycursor.execute(sql, [username])
            mydb.commit()

            if mycursor.rowcount > 0:
                # update was success
                pass

            for i in results:
                messagebox.showinfo("Welcome Admin", "Welcome to the Admin")
                window.destroy()
                root = Tk()
                root.title("Lifechoices Admin System")
                root.geometry("800x800")
                root.config(bg="black")

                label_logo2 = Label(root, text="LIFECHOICES", width=55, font=("Helvetica", 20), bg="light green")
                label_logo2.place(x=0, y=0)

                # Creating and defining the logout button for the admin
                def logout():
                    sql = 'Select * from Admin where Username = %s and Password = %s'
                    mycursor.execute(sql, [(username), (userpass)])
                    results = mycursor.fetchall()

                    if results:
                        sql = 'UPDATE Admin SET Logout_time = NOW() WHERE Username = %s'
                        mycursor.execute(sql, [username])
                        mydb.commit()

                        if mycursor.rowcount > 0:
                            # update was success
                            pass

                        for i in results:
                            messagebox.showinfo("GOODBYE")
                            root.destroy()
                            python = sys.executable
                            os.execl(python, python, *sys.argv)

                            break
                        else:
                            admin_entry.delete(0, END)
                            admin_entry2.delete(0, END)

                logout_btn = Button(root, text="Logout", width=20, command=logout)
                logout_btn.place(x=0, y=400)

                listBox = Listbox(root, width=70)
                listBox.place(x=150, y=500)

                # Creating adn defining the listbox that updates new users
                def populatebox():
                    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost',
                                                   database='lifechoicesonline')
                    mycursor = mydb.cursor()
                    sql = "select UserId, Fullname, Username, Password, Login_time, Logout_time from Users"
                    mycursor.execute(sql)
                    for i in mycursor:
                        listBox.insert("end", i)

                update_btn = Button(root, text="Update list", command=lambda: populatebox())
                update_btn.place(x=350, y=700)


                # Creating and defining the add user button that adds a user
                def add_User():
                    add = Tk()
                    add.title("Add user by admin")
                    add.geometry("300x300")

                    # widgets
                    head_lbl = Label(add)
                    fname_lbl = Label(add, text="Full Name:")
                    uname_lbl = Label(add, text="Username:")
                    passw_lbl = Label(add, text="Password:")
                    fname = Entry(add)
                    uname = Entry(add)
                    passw = Entry(add)

                    # Creating and defining the button that creates a new user and stores their time
                    def create():
                        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                                                       host='localhost', database='lifechoicesonline')

                        mycursor = mydb.cursor()

                        x = fname.get()
                        y = uname.get()
                        z = passw.get()

                        if x=='' or y=='' or z=='':
                            messagebox.showerror("TRY AGAIN", "Please do not leave the fields empty")
                            add.destroy()
                            create()
                        else:
                            mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                                                       host='localhost', database='lifechoicesonline')

                            try:
                                mycursor = mydb.cursor()
                                sql = "INSERT INTO Users(Fullname, Username, Password) VALUES(%s, %s, %s)"
                                mycursor.execute(sql, [(x), (y), (z)])
                                mydb.commit()
                            except:
                                messagebox.showerror("OOPS", "Error connecting to databases")
                            messagebox.showinfo("SUCCESS " + x + " has been added to the server")
                            add.destroy()
                    create_btn = Button(add, text="Add User", command=create)

                    # placements
                    fname_lbl.place(x=5, y=5)
                    uname_lbl.place(x=5, y=45)
                    passw_lbl.place(x=5, y=85)
                    fname.place(x=5, y=25)
                    uname.place(x=5, y=65)
                    passw.place(x=5, y=105)
                    create_btn.place(x=25, y=130)

                add_userbtn = Button(root, text="Add User", width=20, command=add_User)
                add_userbtn.place(x=0, y=300)

                # Creating and defining the delete user button that deletes a user

                def delete_user():
                    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost',
                                                   database='lifechoicesonline')
                    mycursor = mydb.cursor()

                    win = Tk()
                    win.title("DELETE")
                    win.geometry("200x200")

                    name = Label(win, text="Full Name:")
                    name.place(x=0, y=0)

                    fname = Entry(win)
                    fname.place(x=0, y=20)

                    name_user= Label(win, text="Username:")
                    name_user.place(x=0, y=40)

                    uname = Entry(win)
                    uname.place(x=0, y=60)

                    passw_lbl = Label(win, text="Password:")
                    passw_lbl.place(x=0, y=80)

                    passw = Entry(win)
                    passw.place(x=0, y=100)


                    def deleting():
                        fullname1 = fname.get()
                        sql = "DELETE from Users where Fullname = %s"
                        mycursor.execute(sql, (fullname1,))
                        mydb.commit()
                        messagebox.showinfo("DELETED", "Delete was a success")
                        win.destroy()

                    btn_delete = Button(win, text="Delete", width=20, command=deleting)
                    btn_delete.place(x=0, y=150)

                delete_userbtn = Button(root, text="Delete User", width=20, command=delete_user)
                delete_userbtn.place(x=0, y=350)

    adminbtn = Button(window, text="Login", width=20, command=admin_login)
    adminbtn.place(x=0, y=250)


register_button = Button(app, text="Register Here", width=20, command=register)
register_button.place(x=580, y=350)
# Creating a listbox that lists the users
listBox = Listbox(app, width=70)
listBox.place(x=150, y=500)

def populatebox():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost',
                                   database='lifechoicesonline')
    mycursor = mydb.cursor()
    sql="select UserId, Fullname, Username, Password, Login_time, Logout_time from Users"
    mycursor.execute(sql)
    for i in mycursor:
        listBox.insert("end", i)

update_btn = Button(app, text="Update list", command = lambda: populatebox())
update_btn.place(x=350, y=700)



app.mainloop()