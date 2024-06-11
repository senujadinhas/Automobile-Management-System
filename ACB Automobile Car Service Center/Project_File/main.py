from subprocess import call
import tkinter
import customtkinter
from tkinter import messagebox
from tkinter import * 



def button_callback():
    g_username = str(optionmenu_1.get())

    if(g_username == "---Select One---"):
        
        messagebox.showerror("Error", "Please select a type")
    elif (g_username == "Admin"):
        app.destroy()
        call(["python","Project_File\\admin\\admin_login.py"])
    else:
        try:
            app.destroy()
            call(["python","Project_File\\mechanic\\mechanic_login.py"])
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return
  

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


app = customtkinter.CTk()
app.geometry("1000x639")
app.title("ABC Auto Mechanic Car Service Center")
app.iconbitmap('icon.ico')
app.state('zoomed')


img = PhotoImage(file="logo.png")
b_img = PhotoImage(file="bottom_logo.png")

frame_1 = customtkinter.CTkFrame(master=app,fg_color="#e0ebff")
frame_1.pack(pady=0, padx=0, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, image=img,text="")
label_1.pack(pady=(100, 10), padx=10)

frame_12 = customtkinter.CTkFrame(master=frame_1,fg_color="#bad1ff")
frame_12.pack()



label_1 = customtkinter.CTkLabel(master=frame_12, justify=tkinter.LEFT,text="Choose Your Type",text_color="#144272")
label_1.pack(pady=(95, 1), padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_12, values=["---Select One---","Admin", "User"],width=200)
optionmenu_1.pack(pady=10, padx=50)
optionmenu_1.set("---Select One---")

button_1 = customtkinter.CTkButton(hover_color="#144272", text="Submit",master=frame_12, command=button_callback,width=75,fg_color="#144272")
button_1.pack(pady=(10, 100), padx=10)


app.mainloop()  