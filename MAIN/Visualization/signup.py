import tkinter as tk
from tkinter import messagebox
import mysql.connector as con
import pygame

db=con.connect(host='localhost',user='root',passwd='harish123')
if db.is_connected():
    print('connection established')
mycursor=db.cursor()
mycursor.execute("USE test")
mycursor.execute("CREATE DATABASE if not exists password_manager")
mycursor.execute("CREATE TABLE if not exists info(username VARCHAR(100),password VARCHAR(100))")

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("1000x550")

        # Create a label with image background
        self.bg_image = tk.PhotoImage(file="MAIN/Assets/niceblue.png")
        self.background_label = tk.Label(master, image=self.bg_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a canvas
        self.canvas = tk.Canvas(master, bg="black", width=800, height=400)

        # Create labels
        self.label_username = tk.Label(self.canvas, text="Username:", font=("Arial", 14), bg="black", fg="white")
        self.label_password = tk.Label(self.canvas, text="Password:", font=("Arial", 14), bg="black", fg="white")
        
        # Create entry widgets
        self.entry_username = tk.Entry(self.canvas, width=40, font=("Arial", 14))
        self.entry_password = tk.Entry(self.canvas, show="*", width=40, font=("Arial", 14))
        
        # Create buttons
        self.button_login = tk.Button(self.canvas, text="Login", command=self.login, width=12, font=("Arial", 14))
        self.button_register = tk.Button(self.canvas, text="Register", command=self.open_signup_page, width=12, font=("Arial", 14))

        # Center the canvas
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")
        
        # Place labels and entry widgets in canvas
        self.label_username.place(relx=0.3, rely=0.4, anchor="e")
        self.entry_username.place(relx=0.33, rely=0.38)
        self.label_password.place(relx=0.3, rely=0.6, anchor="e")
        self.entry_password.place(relx=0.33, rely=0.57)
        self.button_login.place(relx=0.5, rely=0.73, anchor="center")
        self.button_register.place(relx=0.5, rely=0.86, anchor="center")

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        
        #fetching username and pass from db
        mycursor.execute(f"select username from info where username='{username}'")
        usern = mycursor.fetchone()
        mycursor.execute(f"select password from info where password='{password}'")
        passw = mycursor.fetchone()
        # You can add your authentication logic here
        if not (username and password):
            messagebox.showerror("Login Failed", "Enter username and password")
        elif not usern:
            messagebox.showerror("Login Failed", "Invalid username")
        elif not passw:
            messagebox.showerror("Login Failed", "Invalid password")
        else:
            messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
            self.master.destroy()  # Close the login window
            import menu
           
    def open_signup_page(self):
        self.master.destroy()  # Close the login window
        signup_window = tk.Tk()
        signup_page = SignUpPage(signup_window)
        signup_window.mainloop()

class SignUpPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Sign Up")
        self.master.geometry("1000x550")

        # Create a label with image background
        self.bg_image = tk.PhotoImage(file="MAIN/Assets/niceblue.png")
        self.background_label = tk.Label(master, image=self.bg_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a canvas
        self.canvas = tk.Canvas(master, bg="black", width=800, height=400)

        # Create labels
        self.label_username = tk.Label(self.canvas, text="Username:", font=("Arial", 14), bg="black", fg="white")
        self.label_password = tk.Label(self.canvas, text="Password:", font=("Arial", 14), bg="black", fg="white")
        self.label_email = tk.Label(self.canvas, text="Email:", font=("Arial", 14), bg="black", fg="white")
        
        # Create entry widgets
        self.entry_username = tk.Entry(self.canvas, width=40, font=("Arial", 14))
        self.entry_password = tk.Entry(self.canvas, show="*", width=40, font=("Arial", 14))
        self.entry_email = tk.Entry(self.canvas, width=40, font=("Arial", 14))
        
        # Create button
        self.button_signup = tk.Button(self.canvas, text="Sign Up", command=self.signup, width=15, font=("Arial", 14))

        # Center the canvas
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")
        
        # Place labels and entry widgets in canvas
        self.label_username.place(relx=0.3, rely=0.35, anchor="e")
        self.entry_username.place(relx=0.33, rely=0.32)
        self.label_password.place(relx=0.3, rely=0.45, anchor="e")
        self.entry_password.place(relx=0.33, rely=0.42)
        self.label_email.place(relx=0.3, rely=0.55, anchor="e")
        self.entry_email.place(relx=0.33, rely=0.52)
        self.button_signup.place(relx=0.5, rely=0.68, anchor="center")

    def signup(self):
        user = self.entry_username.get()
        passwo = self.entry_password.get()
        email = self.entry_email.get()

        # You can add your signup logic here
        mycursor.execute(f'insert into info(username,password) values("{user}","{passwo}")')
        db.commit()
        messagebox.showinfo("Sign Up Successful", "You have successfully signed up, {}".format(user))
        self.master.destroy()  # Close the signup window
        import menu

def main():
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()