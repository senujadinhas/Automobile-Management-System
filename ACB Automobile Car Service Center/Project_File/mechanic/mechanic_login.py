import tkinter
import customtkinter
import pymysql
from tkinter import messagebox
from tkinter import * 
from customtkinter import * 
from subprocess import call




def back():
  app.destroy()
  call(["python","Project_File\\main.py"])

def connection():
  conn = pymysql.connect(host="localhost", user="root", password="Senuja@123",db="abc")
  return conn

def button_callback():
    g_username = str(username.get())
    g_pwd = str(pwd.get())

      

    if (g_username == "" or g_username == " ") or (g_pwd == "" or g_pwd == " "):
        messagebox.showerror("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection() 
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user WHERE username=%s and pwd=%s",(g_username,g_pwd))
            row = cursor.fetchone()
            if row == None:
              messagebox.showerror("Error", "Username or Password is incorrect")
            else:

              with open("data.txt", "w") as f:
                f.write(g_username)

              app.destroy()
              call(["python","Project_File\\mechanic\\dashboard.py"])
            conn.commit()
            conn.close()
        except:
            messagebox.showerror("Error", "Database Connection Is Lost")
            return
 

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("1000x639")
app.title("ABC Auto Mechanic Car Service Center")
app.state('zoomed')
app.iconbitmap('icon.ico')

img = PhotoImage(file="logo.png")
b_img = PhotoImage(file="bottom_logo.png")

frame_1 = customtkinter.CTkFrame(master=app,fg_color="#e0ebff")
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, image=img,text="")
label_1.pack(pady=(70, 20), padx=10)

frame_12 = customtkinter.CTkFrame(master=frame_1,fg_color="#bad1ff")
frame_12.pack()


label_1 = customtkinter.CTkLabel(master=frame_12, justify=tkinter.LEFT,text="Username:",text_color="#144272")
label_1.pack(pady=(20, 1), padx=10)

username = customtkinter.CTkEntry(master=frame_12, placeholder_text="Your Username",width=200,height=35)
username.pack(pady=(10, 1), padx=10)

label_1 = customtkinter.CTkLabel(master=frame_12, justify=tkinter.LEFT,text="Password:",text_color="#144272")
label_1.pack(pady=(10, 1), padx=10)

pwd = customtkinter.CTkEntry(master=frame_12, placeholder_text="Your Password",width=200,height=35,show="*")
pwd.pack(pady=10, padx=60)

button_1 = customtkinter.CTkButton(text="Submit",master=frame_12, command=button_callback,width=75,fg_color="#144272")
button_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(hover_color="#144272", text="Back",master=frame_12, command=back,width=50,fg_color="#144272")
button_1.pack(pady=(10, 50), padx=10)





app.mainloop()  