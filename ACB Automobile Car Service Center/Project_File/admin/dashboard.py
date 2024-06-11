from cmath import e
from datetime import datetime,date
from sqlalchemy import create_engine
import tkinter.messagebox
import customtkinter
import pymysql
from tkinter import ttk
from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from subprocess import call

customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



now = datetime.now().strftime("%d-%m-%y  %H:%M:%S")


with open("data.txt", "r") as f:
    name = f.read()
    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

      

 

        # configure window
        self.title("ABC Auto Mechanic Car Service Center")
        my_tree = ttk.Treeview(self)
        self.iconbitmap('icon.ico')
        def on_closing():
            with open("data.txt", "w") as f:
                    f.write(" ")
            self.destroy()

        self.protocol("WM_DELETE_WINDOW", on_closing)
      
        self.geometry(f"{1100}x{580}")
        self.state('zoomed')

        def select_record(e):
            self.m_id.delete(0, END)
            self.m_name.delete(0, END)
            self.m_address.delete(0, END)
            self.m_phone.delete(0, END)

            selected = m_treeview.focus()
            values = m_treeview.item(selected,'values')

            self.m_id.insert(0, values[0])
            self.m_name.insert(0, values[1])
            self.m_address.insert(0, values[2])
            self.m_phone.insert(0, values[3])
             
        def select_u_record(e):
            self.u_id.delete(0, END)
            self.u_name.delete(0, END)
            self.u_phone.delete(0, END)
            self.u_username.delete(0, END)
            self.u_password.delete(0, END)
 

            selected = u_treeview.focus()
            values = u_treeview.item(selected,'values')

            self.u_id.insert(0, values[0])
            self.u_name.insert(0, values[1])
            self.u_phone.insert(0, values[2])
            self.u_username.insert(0, values[3])
            self.u_password.insert(0, values[4])

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

       

        self.tabview = customtkinter.CTkTabview(self,height=1000,fg_color="#bdd3de",segmented_button_fg_color="#47b9ff",segmented_button_unselected_color="#2069A4",segmented_button_selected_color="#257cc2",segmented_button_selected_hover_color="#257cc2",segmented_button_unselected_hover_color="#257cc2")
        self.tabview.grid(row=0, column=1, padx=(10, 10), pady=(5, 50), sticky="nsew")
        self.tabview.add("User Details")
        self.tabview.add("Mechanics Details")
        self.tabview.add("Service Booking")
        self.tabview.add("Complete Payment")
        self.tabview.add("My Profile")

       
        frame_7 = customtkinter.CTkFrame(self.tabview.tab("User Details"),fg_color="transparent")
        frame_7.grid(row=1,column=0,padx=(0,50))

        frame_8 = customtkinter.CTkFrame(self.tabview.tab("User Details"),width=1500,height=250,fg_color="transparent")
        frame_8.grid(row=1,column=9)

        frame_1 = customtkinter.CTkFrame(self.tabview.tab("Mechanics Details"),fg_color="transparent")
        frame_1.grid(row=1,column=0,padx=(0,50))

        frame_2 = customtkinter.CTkFrame(self.tabview.tab("Mechanics Details"),width=1500,height=250,fg_color="transparent")
        frame_2.grid(row=1,column=9)

        frame_3 = customtkinter.CTkFrame(self.tabview.tab("Service Booking"),fg_color="transparent",width=400,height=500)
        frame_3.grid(row=1,column=0,padx=(0,50))
     
        frame_4 = customtkinter.CTkFrame(self.tabview.tab("Service Booking"), width=1900,height=500,fg_color="transparent")
        frame_4.grid(row=1,column=5)

        frame_5 = customtkinter.CTkFrame(self.tabview.tab("Complete Payment"),width=400,height=500,fg_color="transparent")
        frame_5.grid(row=1,padx=(0,25))

        frame_6 = customtkinter.CTkFrame(self.tabview.tab("Complete Payment"),width=1200,height=580,fg_color="transparent")
        frame_6.grid(row=1,column=9)

        frame_9 = customtkinter.CTkFrame(self.tabview.tab("My Profile"),width=400,height=500,fg_color="transparent")
        frame_9.grid(row=1,padx=(0,25))

      

        

        self.u_id_label= customtkinter.CTkLabel(frame_7, text="User ID:")
        self.u_name_label= customtkinter.CTkLabel(frame_7, text="User Name:")
        self.u_phone_label = customtkinter.CTkLabel(frame_7, text=" User Phone Number:",anchor=W)
        self.u_username_label = customtkinter.CTkLabel(frame_7, text="Username:",anchor=W)
        self.u_password_label = customtkinter.CTkLabel(frame_7, text="Password:",anchor=W)

        

        self.u_id= customtkinter.CTkEntry(frame_7, placeholder_text="User ID",width=200,height=35)
        self.u_name= customtkinter.CTkEntry(frame_7, placeholder_text="User Name",width=200,height=35)
        self.u_phone= customtkinter.CTkEntry(frame_7, placeholder_text="User Phone Number",width=200,height=35)
        self.u_username= customtkinter.CTkEntry(frame_7, placeholder_text="Username",width=200,height=35)
        self.u_password= customtkinter.CTkEntry(frame_7, placeholder_text="Password",width=200,height=35)


        self.u_search= customtkinter.CTkEntry(frame_7, placeholder_text="Search",width=200,height=35)
        self.u_search.grid(row=9,column=1,columnspan=3,pady=(50,7))


        self.u_id_label.grid(row=1,column=0,padx=10,pady=10)
        self.u_name_label.grid(row=2,column=0,padx=10,pady=10)
        self.u_phone_label.grid(row=3,column=0,padx=10,pady=10)
        self.u_username_label.grid(row=4,column=0,padx=10,pady=10)
        self.u_password_label.grid(row=5,column=0,padx=10,pady=10)


        self.u_id.grid(row=1,column=1,columnspan=3,padx=5,pady=5)
        self.u_name.grid(row=2,column=1,columnspan=3,padx=5,pady=5)
        self.u_phone.grid(row=3,column=1,columnspan=3,padx=5,pady=5)
        self.u_username.grid(row=4,column=1,columnspan=3,padx=5,pady=5)
        self.u_password.grid(row=5,column=1,columnspan=3,padx=5,pady=5)


        

        tree_style = ttk.Style()
        tree_style.configure("mystyle.Treeview",font=('Helvetica', 11))
        tree_style.configure("mystyle.Treeview.Heading",font=(15))
        tree_style.configure('Treeview', rowheight=25)
        tree_style.theme_use("clam")

        
        u_treeview = ttk.Treeview(frame_8,show='headings',style="mystyle.Treeview",height=10)
        u_treeview.place(width=1600, height=700)
  
        u_treeview["columns"] = ("User ID", "User Name", "User Phone Number","Username","Password")
        u_treeview.column('#0', anchor=W, width=40,stretch=tk.NO)
        u_treeview.column('User ID', anchor=W, width=1)
        u_treeview.column('User Name', anchor=W, width=100)
        u_treeview.column('User Phone Number', anchor=W, width=100)
        u_treeview.column('Username', anchor=W, width=50)
        u_treeview.column('Password', anchor=W, width=200)
        u_treeview.heading('#0', text='',anchor=W)
        u_treeview.heading('User ID', text='User ID',anchor=W)
        u_treeview.heading('User Name', text='User Name',anchor=W)
        u_treeview.heading('User Phone Number', text='User Phone Number',anchor=W)
        u_treeview.heading('Username', text='Username',anchor=W)
        u_treeview.heading('Password', text='Password',anchor=W)

        
 
        conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
        cur = conn.cursor()
        cur.execute("SELECT * FROM user")

        for row in cur:
            u_treeview.insert("", "end", values=row)

  
       
   


        def add_record():

            g_u_id = str(self.u_id.get())
            g_u_name = str(self.u_name.get())
            g_u_phone = str(self.u_phone.get())
            g_u_username = str(self.u_username.get())
            g_u_password = str(self.u_password.get())

            if(g_u_id == "" or g_u_id == " ")or (g_u_name == "" or g_u_name == " ") or (g_u_phone == "" or g_u_phone == " ") or (g_u_username == "" or g_u_username == " ") or (g_u_password == "" or g_u_password == " "):
               messagebox.showerror("Error", "Please fill up the blank entry")
               return
            else:
                try:
                   
                   cursor = conn.cursor()
                   cursor.execute("INSERT INTO user (id, u_name, u_phone, username, pwd) VALUES (%s, %s, %s, %s, %s)", (g_u_id, g_u_name, g_u_phone,g_u_username,g_u_password))
                   conn.commit()
                   cursor.close()
                   

                   
                   self.u_id.delete(0, END)
                   self.u_name.delete(0, END)
                   self.u_phone.delete(0, END)
                   self.u_username.delete(0, END)
                   self.u_password.delete(0, END)
                   
                   u_refresh_tree_view()
                
                   

                except:

                    messagebox.showerror("Error", "The data you entered is incorrect. Check the id and phone number again.")
                    return

        def update_record():

            g_u_id = str(self.u_id.get())
            g_u_name = str(self.u_name.get())
            g_u_phone = str(self.u_phone.get())
            g_u_username = str(self.u_username.get())
            g_u_password = str(self.u_password.get())

            if(g_u_id == "" or g_u_id == " ")or (g_u_name == "" or g_u_name == " ") or (g_u_phone == "" or g_u_phone == " ") or (g_u_username == "" or g_u_username == " ") or (g_u_password == "" or g_u_password == " "):
               messagebox.showerror("Error", "Please fill up the blank entry")
               return
            else:
                try:
                   
                   cursor = conn.cursor()
                   cursor.execute("UPDATE user SET id=%s,u_name=%s, u_phone=%s, username=%s, pwd=%s WHERE id=%s", (g_u_id, g_u_name, g_u_phone,g_u_username,g_u_password,g_u_id))
                   conn.commit()
                   cursor.close()
                   

                   
                   self.u_id.delete(0, END)
                   self.u_name.delete(0, END)
                   self.u_phone.delete(0, END)
                   self.u_username.delete(0, END)
                   self.u_password.delete(0, END)
                   
                   u_refresh_tree_view()
                   
                   

                except:

                    messagebox.showerror("Error", "The data you entered is incorrect. Check the id and phone number again.")
                    return

        def delete_record():
            
            
            g_u_id = str(self.u_id.get())
            g_u_name = str(self.u_name.get())
            g_u_phone = str(self.u_phone.get())
            g_u_username = str(self.u_username.get())
            g_u_password = str(self.u_password.get())

            if(g_u_id == "" or g_u_id == " ")or (g_u_name == "" or g_u_name == " ") or (g_u_phone == "" or g_u_phone == " ") or (g_u_username == "" or g_u_username == " ") or (g_u_password == "" or g_u_password == " "):
               messagebox.showerror("Error", "Please select a record")
               return
            else:
                try:
                   alert =  messagebox.askyesno("Message","Do you want to delete this record?")
                   if alert == 0:
                    u_refresh_tree_view()
                   else:

                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM user WHERE id=%s", (g_u_id))
                    conn.commit()
                    cursor.close()
                   

                   
                   self.u_id.delete(0, END)
                   self.u_name.delete(0, END)
                   self.u_phone.delete(0, END)
                   self.u_username.delete(0, END)
                   self.u_password.delete(0, END)
                   
                   u_refresh_tree_view()
                   
                   

                except:

                    messagebox.showerror("Error", "The data you entered is incorrect. Check again.")
                    return

        
        def u_refresh_tree_view():

            u_treeview.delete(*u_treeview.get_children())

            conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT * FROM user")
            conn.commit()
            for row in cur:
                u_treeview.insert("", "end", values=row)
           
        def search():
            g_u_search = str(self.u_search.get())
            u_treeview.delete(*u_treeview.get_children())

            conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT * FROM user WHERE u_name=%s or u_phone=%s or username=%s ", (g_u_search,g_u_search,g_u_search))
            conn.commit()
            for row in cur:
                u_treeview.insert("", "end", values=row)
        
        def clear_search():

            u_treeview.delete(*u_treeview.get_children())

            conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT * FROM user")
            conn.commit()
            for row in cur:
                u_treeview.insert("", "end", values=row)
            self.u_search.delete(0, END)

        self.add_button = customtkinter.CTkButton(frame_7,width=50 , text="Add",  command=add_record)
        self.add_button.grid(row=7, column=1,columnspan=1)
        
        self.update_button = customtkinter.CTkButton(frame_7,width=50 , text="Update",  command=update_record)
        self.update_button.grid(row=7, column=2,columnspan=1)
        
        self.delete_button = customtkinter.CTkButton(frame_7,width=50 , text="Delete",  command=delete_record)
        self.delete_button.grid(row=7, column=3,columnspan=1)

        self.search_btn = customtkinter.CTkButton(frame_7,width=50 , text="Search", command=search)
        self.search_btn.grid(row=10, column=1,columnspan=1)

        self.clear_search = customtkinter.CTkButton(frame_7,width=50 , text="Clear", command=clear_search)
        self.clear_search.grid(row=10, column=2,columnspan=1)
            

       

        u_treeview.bind("<ButtonRelease-1>", select_u_record)

        #---------------------------------------------------------------------------------------

        self.m_id_label= customtkinter.CTkLabel(frame_1, text="Mechanic ID:")
        self.m_name_label= customtkinter.CTkLabel(frame_1, text="Mechanic Name:")
        self.m_address_label = customtkinter.CTkLabel(frame_1, text="Mechanic Address:",anchor=W)
        self.m_phone_label = customtkinter.CTkLabel(frame_1, text=" Mechanic Phone Number:",anchor=W)

        self.m_id= customtkinter.CTkEntry(frame_1, placeholder_text="ID",width=200,height=35)
        self.m_name= customtkinter.CTkEntry(frame_1, placeholder_text="Name",width=200,height=35)
        self.m_address= customtkinter.CTkEntry(frame_1, placeholder_text="Address",width=200,height=35)
        self.m_phone= customtkinter.CTkEntry(frame_1, placeholder_text="Phone Number",width=200,height=35)

        self.m_phone1= customtkinter.CTkEntry(frame_1, placeholder_text="Search",width=200,height=35)
        self.m_phone1.grid(row=9,column=1,columnspan=3,pady=(50,7))


        self.m_id_label.grid(row=1,column=0,padx=10,pady=10)
        self.m_name_label.grid(row=2,column=0,padx=10,pady=10)
        self.m_address_label.grid(row=3,column=0,padx=10,pady=10)
        self.m_phone_label.grid(row=4,column=0,padx=10,pady=10)

        self.m_id.grid(row=1,column=1,columnspan=3,padx=5,pady=5)
        self.m_name.grid(row=2,column=1,columnspan=3,padx=5,pady=5)
        self.m_address.grid(row=3,column=1,columnspan=3,padx=5,pady=5)
        self.m_phone.grid(row=4,column=1,columnspan=3,padx=5,pady=5)

        

        tree_style = ttk.Style()
        tree_style.configure("mystyle.Treeview",font=('Helvetica', 11))
        tree_style.configure("mystyle.Treeview.Heading",font=(15))
        tree_style.configure('Treeview', rowheight=25)
        
        
        m_treeview = ttk.Treeview(frame_2,show='headings',style="mystyle.Treeview",height=10)
        m_treeview.place(width=1600, height=700)
  
        m_treeview["columns"] = ("ID", "Mechanic Name", "Mechanic Address","Mechanic Phone Number")
        m_treeview.column('#0', anchor=W, width=40,stretch=tk.NO)
        m_treeview.column('ID', anchor=W, width=1)
        m_treeview.column('Mechanic Name', anchor=W, width=200)
        m_treeview.column('Mechanic Address', anchor=W, width=200)
        m_treeview.column('Mechanic Phone Number', anchor=W, width=200)
        m_treeview.heading('#0', text='',anchor=W)
        m_treeview.heading('ID', text='ID',anchor=W)
        m_treeview.heading('Mechanic Name', text='Mechanic Name',anchor=W)
        m_treeview.heading('Mechanic Address', text='Mechanic Address',anchor=W)
        m_treeview.heading('Mechanic Phone Number', text='Mechanic Pho. Nu.',anchor=W)

        
 
        conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
        cur = conn.cursor()
        cur.execute("SELECT * FROM mechanics_details")

        for row in cur:
            m_treeview.insert("", "end", values=row)

  
       
   


        def add_record():

            g_id = str(self.m_id.get())
            g_name = str(self.m_name.get())
            g_address = str(self.m_address.get())
            g_phone = str(self.m_phone.get())

            if(g_id == "" or g_id == " ")or (g_name == "" or g_name == " ") or (g_address == "" or g_address == " ") or (g_phone == "" or g_phone == " "):
               messagebox.showerror("Error", "Please fill up the blank entry")
               return
            else:
                try:
                   
                   cursor = conn.cursor()
                   cursor.execute("INSERT INTO mechanics_details (m_id, m_name, m_address, m_phone) VALUES (%s, %s, %s, %s)", (g_id, g_name, g_address,g_phone))
                   conn.commit()
                   cursor.close()
                   

                   
                   self.m_id.delete(0, END)
                   self.m_name.delete(0, END)
                   self.m_address.delete(0, END)
                   self.m_phone.delete(0, END)
                   
                   refresh_tree_view()
                
                   

                except:

                    messagebox.showerror("Error", "The data you entered is incorrect. Check the id and phone number again.")
                    return

        def update_record():

            g_id = str(self.m_id.get())
            g_name = str(self.m_name.get())
            g_address = str(self.m_address.get())
            g_phone = str(self.m_phone.get())

            if(g_id == "" or g_id == " ")or (g_name == "" or g_name == " ") or (g_address == "" or g_address == " ") or (g_phone == "" or g_phone == " "):
               messagebox.showerror("Error", "Please fill up the blank entry")
               return
            else:
                try:
                   
                   cursor = conn.cursor()
                   cursor.execute("UPDATE mechanics_details SET m_id=%s,m_name=%s, m_address=%s, m_phone=%s WHERE m_id=%s", (g_id, g_name, g_address,g_phone,g_id))
                   conn.commit()
                   cursor.close()
                   

                   
                   self.m_id.delete(0, END)
                   self.m_name.delete(0, END)
                   self.m_address.delete(0, END)
                   self.m_phone.delete(0, END)
                   
                   refresh_tree_view()
                   
                   

                except:

                    messagebox.showerror("Error", "The data you entered is incorrect. Check the id and phone number again.")
                    return

        def delete_record():
            
            
            g_id = str(self.m_id.get())
            g_name = str(self.m_name.get())
            g_address = str(self.m_address.get())
            g_phone = str(self.m_phone.get())

            if(g_id == "" or g_id == " ")or (g_name == "" or g_name == " ") or (g_address == "" or g_address == " ") or (g_phone == "" or g_phone == " "):
               messagebox.showerror("Error", "Please select a record")
               return
            else:
                try:
                   alert =  messagebox.askyesno("Message","Do you want to delete this record?")
                   if alert == 0:
                    refresh_tree_view()
                   else:

                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM mechanics_details WHERE m_id=%s", (g_id))
                    conn.commit()
                    cursor.close()
                   

                   
                   self.m_id.delete(0, END)
                   self.m_name.delete(0, END)
                   self.m_address.delete(0, END)
                   self.m_phone.delete(0, END)
                   
                   refresh_tree_view()
                   
                   

                except:

                    messagebox.showerror("Error", "The data you entered is incorrect. Check again.")
                    return

        
        def refresh_tree_view():

            m_treeview.delete(*m_treeview.get_children())

            conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT * FROM mechanics_details")
            conn.commit()
            for row in cur:
                m_treeview.insert("", "end", values=row)
           
        def search():
            g_search = str(self.m_phone1.get())
            m_treeview.delete(*m_treeview.get_children())

            conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT * FROM mechanics_details WHERE m_name=%s or m_phone=%s or m_address=%s or m_id=%s", (g_search,g_search,g_search,g_search))
            conn.commit()
            for row in cur:
                m_treeview.insert("", "end", values=row)
        
        def clear_search():

            m_treeview.delete(*m_treeview.get_children())

            conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT * FROM mechanics_details")
            conn.commit()
            for row in cur:
                m_treeview.insert("", "end", values=row)
            self.m_phone1.delete(0, END)

        self.add_button = customtkinter.CTkButton(frame_1,width=50 , text="Add",  command=add_record)
        self.add_button.grid(row=7, column=1,columnspan=1)
        
        self.update_button = customtkinter.CTkButton(frame_1,width=50 , text="Update",  command=update_record)
        self.update_button.grid(row=7, column=2,columnspan=1)
        
        self.delete_button = customtkinter.CTkButton(frame_1,width=50 , text="Delete",  command=delete_record)
        self.delete_button.grid(row=7, column=3,columnspan=1)

        self.search_btn = customtkinter.CTkButton(frame_1,width=50 , text="Search", command=search)
        self.search_btn.grid(row=10, column=1,columnspan=1)

        self.clear_search = customtkinter.CTkButton(frame_1,width=50 , text="Clear", command=clear_search)
        self.clear_search.grid(row=10, column=2,columnspan=1)
            

       

        m_treeview.bind("<ButtonRelease-1>", select_record)

        #---------------------------------------------------------------------------------------

        tree_style = ttk.Style()
        
        tree_style.configure("mystyle.Treeview",font=('Helvetica', 11))
        tree_style.configure("mystyle.Treeview.Heading",font=(15))

    
        treeview = ttk.Treeview(frame_4,show='headings',style="mystyle.Treeview")
        treeview.place(width=1320, height=700)
     

        
      
        treeview["columns"] = ("Service ID", "Payment R OR N", "Service Date And Time","Customer Name","Vehicle Registration No.","Vehicle Make","Vehicle Model","Vehicle Type","Vehicle Engine Size","mechanic")
        treeview.column('#0', anchor=W, width=40,stretch=tk.NO)
        treeview.column('Service ID', anchor=W, width=0)
        treeview.column('Payment R OR N', anchor=W, width=50)
        treeview.column('Service Date And Time', anchor=W, width=110)
        treeview.column('Customer Name', anchor=W, width=120)
        treeview.column('Vehicle Registration No.', anchor=W, width=130)
        treeview.column('Vehicle Make', anchor=W, width=110)
        treeview.column('Vehicle Model', anchor=W, width=110)
        treeview.column('Vehicle Type', anchor=W, width=100)
        treeview.column('Vehicle Engine Size', anchor=W, width=100)
        treeview.column('mechanic', anchor=W, width=100)

        treeview.heading('#0', text='',anchor=W)
        treeview.heading('Service ID', text='ID',anchor=W)
        treeview.heading('Payment R OR N', text='Payment',anchor=W)
        treeview.heading('Service Date And Time', text='Date And Time',anchor=W)
        treeview.heading('Customer Name', text='Customer Name',anchor=W)
        treeview.heading('Vehicle Registration No.', text='Vehicle Reg. No.',anchor=W)
        treeview.heading('Vehicle Make', text='Vehicle Make',anchor=W)
        treeview.heading('Vehicle Model', text='Vehicle Model',anchor=W)
        treeview.heading('Vehicle Type', text='Vehicle Type',anchor=W)
        treeview.heading('Vehicle Engine Size', text='Vehicle Engine Size',anchor=W)
        treeview.heading('mechanic', text='Mechanic',anchor=W)
      

        conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
        cur = conn.cursor()
        cur.execute("SELECT * FROM service_booking")

        for row in cur:
            treeview.insert("", "end", values=row)

        

        def s_select_record(e):
            self.s_id.delete(0, END)
            self.s_date.delete(0, END)
            self.s_name.delete(0, END)
            self.s_register.delete(0, END)
          
            self.s_model.delete(0, END)
      
            self.s_engine.delete(0, END)

            selected = treeview.focus()
            values = treeview.item(selected,'values')

            self.s_id.insert(0, values[0])
            self.optionmenu_1.set(values[1])
            self.s_date.insert(0, values[2])
            self.s_register.insert(0, values[4])
            self.s_make.set(values[5])
            self.s_model.insert(0, values[6])
            self.s_type.set(values[7])
            self.s_engine.insert(0, values[8])
            self.optionmenu_2.set(values[9])
            self.s_name.insert(0, values[3])
        
        def delete_s_record():
            
            
            g_p_id = str(self.s_id.get())
            g_p_optionmenu_1 = str(self.optionmenu_1.get())
            g_p_date     = str(self.s_date.get())
            g_p_name  = str(self.s_name.get())
            g_s_register = str(self.s_register.get())
            g_s_make = str(self.s_make.get())
            g_s_model = str(self.s_model.get())
            g_s_type = str(self.s_type.get())
            g_s_engine = str(self.s_engine.get())

            if(g_p_id == "" or g_p_id == " ")or (g_p_optionmenu_1 == "" or g_p_optionmenu_1 == " ") or (g_p_date     == "" or g_p_date   == " ") or (g_s_register == "" or g_s_register == " ")or (g_s_make == "" or g_s_make == " ")or (g_s_model == "" or g_s_model == " ")or (g_s_type == "" or g_s_type == " ")or (g_s_engine == "" or g_s_engine == " ") or (g_p_name == "" or g_p_name == " "):
               messagebox.showerror("Error", "Please select a record")
               return
            else:
                try:
                   alert =  messagebox.askyesno("Message","Do you want to delete this record?")
                   if alert == 0:
                    s_refresh_tree_view()
                   else:

                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM service_booking WHERE s_id=%s", (g_p_id))
                    conn.commit()
                    cursor.close()
                   

                   
                   self.s_id.delete(0, END)
                   self.optionmenu_1.set(" ")
                   self.s_date.delete(0, END)
                   self.s_name.delete(0, END)
                   self.s_register.delete(0, END)
                   self.s_make.set(" ")
                   self.s_model.delete(0, END)
                   self.s_type.set(" ")
                   self.s_engine.delete(0, END)
                   self.optionmenu_2.set(" ")
                   
                   self.s_date.insert(0, now)
                   
                   s_refresh_tree_view()

                except:

                    messagebox.showerror("Error", "The data you entered is incorrect. Check the id again.")
                    return
        
     

        def s_refresh_tree_view():

            treeview.delete(*treeview.get_children())
        
            conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT * FROM service_booking")

            for row in cur:
                treeview.insert("", "end", values=row)

        def add_s_record():

            g_p_id = str(self.s_id.get())
            g_p_optionmenu_1 = str(self.optionmenu_1.get())
            g_p_date = str(self.s_date.get())
            g_p_name  = str(self.s_name.get())
            g_s_register = str(self.s_register.get())
            g_s_make = str(self.s_make.get())
            g_s_model = str(self.s_model.get())
            g_s_type = str(self.s_type.get())
            g_s_engine = str(self.s_engine.get())
            g_s_optionmenu_2 = str(self.optionmenu_2.get())

            if(g_p_id == "" or g_p_id == " ")or (g_p_optionmenu_1 == "" or g_p_optionmenu_1 == " ") or (g_p_date     == "" or g_p_date   == " ") or (g_s_register == "" or g_s_register == " ")or (g_s_make == "" or g_s_make == " ")or (g_s_model == "" or g_s_model == " ")or (g_s_type == "" or g_s_type == " ")or (g_s_engine == "" or g_s_engine == " ") or (g_p_name == "" or g_p_name == " "):
               messagebox.showerror("Error", "Please fill up the blank entry")
               return
            else:
                try:
                   
                   cursor = conn.cursor()
                   cursor.execute("INSERT INTO service_booking (s_id, paymentRON, datetime, v_regno, v_make, v_model, v_type, v_engine,machanic,c_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (g_p_id, g_p_optionmenu_1, g_p_date  ,g_s_register,g_s_make,g_s_model,g_s_type,g_s_engine,g_s_optionmenu_2,g_p_name))
                   conn.commit()
                   cursor.close()
                   

                   
                   self.s_id.delete(0, END)
                   self.optionmenu_1.set(" ")
                   self.s_date.delete(0, END)
                   self.s_name.delete(0, END)
                   self.s_register.delete(0, END)
                   self.s_make.set(" ")
                   self.s_model.delete(0, END)
                   self.s_type.set(" ")
                   self.s_engine.delete(0, END)
                   self.optionmenu_2.set(" ")
                   
                   self.s_date.insert(0, now)
                   
                   s_refresh_tree_view()
                   

                except:

                    messagebox.showerror("Error", "The data you entered is incorrect. Check the id again.")
                    return

        def update_s_record():

            g_p_id = str(self.s_id.get())
            g_p_optionmenu_1 = str(self.optionmenu_1.get())
            g_p_date     = str(self.s_date.get())
            g_p_name  = str(self.s_name.get())
            g_s_register = str(self.s_register.get())
            g_s_make = str(self.s_make.get())
            g_s_model = str(self.s_model.get())
            g_s_type = str(self.s_type.get())
            g_s_engine = str(self.s_engine.get())
            g_s_optionmenu_2 = str(self.optionmenu_2.get())

            if(g_p_id == "" or g_p_id == " ")or (g_p_optionmenu_1 == "" or g_p_optionmenu_1 == " ") or (g_p_date     == "" or g_p_date   == " ") or (g_s_register == "" or g_s_register == " ")or (g_s_make == "" or g_s_make == " ")or (g_s_model == "" or g_s_model == " ")or (g_s_type == "" or g_s_type == " ")or (g_s_engine == "" or g_s_engine == " ") or (g_p_name == "" or g_p_name == " "):
               messagebox.showerror("Error", "Please fill up the blank entry")
               return
            else:
                try:
                   
                   cursor = conn.cursor()
                   cursor.execute("UPDATE service_booking SET s_id=%s,paymentRON=%s, datetime=%s, v_regno=%s, v_make=%s,v_model=%s, v_type=%s, v_engine=%s, machanic=%s, c_name=%s WHERE s_id=%s", (g_p_id, g_p_optionmenu_1, g_p_date ,g_s_register,g_s_make,g_s_model,g_s_type,g_s_engine,g_s_optionmenu_2,g_p_name,g_p_id))
                   conn.commit()
                   cursor.close()
                   

                   
                   self.s_id.delete(0, END)
                   self.optionmenu_1.set(" ")
                   self.s_date.delete(0, END)
                   self.s_name.delete(0, END)
                   self.s_register.delete(0, END)
                   self.s_make.set(" ")
                   self.s_model.delete(0, END)
                   self.s_type.set(" ")
                   self.s_engine.delete(0, END)
                   self.optionmenu_2.set(" ")
                   
                   self.s_date.insert(0, now)
                   s_refresh_tree_view()
                   

                except:

                    messagebox.showerror("Error", "The data you entered is incorrect. Check the id again.")
                    return
        
        def search_s():
            g_search_s = str(self.search_name.get())
            treeview.delete(*treeview.get_children())

            conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT * FROM service_booking WHERE c_name=%s or v_regno=%s", (g_search_s, g_search_s))
            conn.commit()
            for row in cur:
                treeview.insert("", "end", values=row)
        
        def clear_search_s():

            treeview.delete(*treeview.get_children())

            conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT * FROM service_booking")
            conn.commit()
            for row in cur:
                treeview.insert("", "end", values=row)
            self.search_name.delete(0, END)

        conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
        cur = conn.cursor()
        cur.execute("SELECT m_name FROM mechanics_details")
                

        my_list = [r for r, in cur]
        

        self.s_id_label= customtkinter.CTkLabel(frame_3, text="Service ID:")
        self.s_payment_label= customtkinter.CTkLabel(frame_3, text="Payment Received or Not:")
        self.s_date_label = customtkinter.CTkLabel(frame_3, text="Service Date And Time:")
        self.s_name_label = customtkinter.CTkLabel(frame_3, text="Customer Name:")
        self.s_register_label= customtkinter.CTkLabel(frame_3, text="Vehicle Regis. No:")
        self.s_make_label= customtkinter.CTkLabel(frame_3, text="Vehicle Make:")
        self.s_model_label = customtkinter.CTkLabel(frame_3, text="Vehicle Model:")
        self.s_type_label = customtkinter.CTkLabel(frame_3, text="Vehicle Type:")
        self.s_engine_label = customtkinter.CTkLabel(frame_3, text="Vehicle Engine Size:")
        self.s_machanic_label = customtkinter.CTkLabel(frame_3, text="Machanic:")

        self.s_id_label.grid(row=1,column=0,padx=10,pady=10)
        self.s_payment_label.grid(row=2,column=0,padx=10,pady=10)
        self.s_date_label.grid(row=3,column=0,padx=10,pady=10)
        self.s_name_label.grid(row=4,column=0,padx=10,pady=10)
        self.s_register_label.grid(row=5,column=0,padx=10,pady=10)
        self.s_make_label.grid(row=6,column=0,padx=10,pady=10)
        self.s_model_label.grid(row=7,column=0,padx=10,pady=10)
        self.s_type_label.grid(row=8,column=0,padx=10,pady=10)
        self.s_engine_label.grid(row=9,column=0,padx=10,pady=10)
        self.s_machanic_label.grid(row=10,column=0,padx=10,pady=10)
        
        

        self.s_id= customtkinter.CTkEntry(frame_3, placeholder_text="Service ID",width=200,height=35)
        self.optionmenu_1 = customtkinter.CTkComboBox(frame_3, values=["No", "Yes"],width=200,height=35)
        self.s_date= customtkinter.CTkEntry(frame_3, placeholder_text="Date and Time",width=200,height=35)
        self.s_name= customtkinter.CTkEntry(frame_3, placeholder_text="Customer Name",width=200,height=35)
        self.s_register= customtkinter.CTkEntry(frame_3, placeholder_text="Vehicle Regis. No.",width=200,height=35)
        self.s_make= customtkinter.CTkComboBox(frame_3,values=[
          
            "Toyota",
            "Nissan",
            "Honda",
            "Suzuki",
            "Mitsubishi",
            "Mazda",
            "Hyundai",
            "Bajaj",
            "Isuzu",
            "Peugeot",
            "Daihatsu",
            "Daewoo",
            "Tata",
            "Yamaha",
            "Tvs",
            "Hero-Honda",
            "Mahindra",
            "Micro",
            "Volkswagen",
            "Ford"

            ],width=200,height=35)
        self.s_model= customtkinter.CTkEntry(frame_3, placeholder_text="Vehicle Model",width=200,height=35)
        self.s_type=  customtkinter.CTkComboBox(frame_3, values=[
            "Car",
            "Van",
            "SUV/Jeep",
            "Pickup/Double Cab",
            "Bus",
            "Lorry/Tipper",
            "Three Wheel",
            "Tractor",
            "Motorcycle",
            "Bicycle"
        ],width=200,height=35)
        self.s_engine= customtkinter.CTkEntry(frame_3, placeholder_text="Vehicle Engine Size",width=200,height=35)
        self.optionmenu_2 = customtkinter.CTkComboBox(frame_3,values=my_list,width=200,height=35)

        self.search_name= customtkinter.CTkEntry(frame_3, placeholder_text="Search",width=200,height=35)
        self.search_name.grid(row=12,column=1,columnspan=3,pady=(50,7))

        self.s_date.insert(0, now)

        
        self.s_id.grid(row=1,column=1,columnspan=3,padx=5,pady=5)
        self.optionmenu_1.grid(row=2,column=1,columnspan=3,pady=5)
        self.s_date.grid(row=3,column=1,columnspan=3,pady=5)
        self.s_name.grid(row=4,column=1,columnspan=3,pady=5)
        self.s_register.grid(row=5,column=1,columnspan=3,pady=5)
        self.s_make.grid(row=6,column=1,columnspan=3,pady=5)
        self.s_model.grid(row=7,column=1,columnspan=3,pady=5)
        self.s_type.grid(row=8,column=1,columnspan=3,pady=5)
        self.s_engine.grid(row=9,column=1,columnspan=3,padx=5,pady=5)
        self.optionmenu_2.grid(row=10,column=1,columnspan=3,pady=5)
        


        self.s_add_button = customtkinter.CTkButton(frame_3,width=50 , text="Add",  command=add_s_record)
        self.s_add_button.grid(row=11, column=1,columnspan=1)
        
        self.s_update_button = customtkinter.CTkButton(frame_3,width=50 , text="Update",  command=update_s_record)
        self.s_update_button.grid(row=11, column=2,columnspan=1)
        
        self.s_delete_button = customtkinter.CTkButton(frame_3,width=50 , text="Delete",  command=delete_s_record)
        self.s_delete_button.grid(row=11, column=3,columnspan=1)

        self.search_btn_s = customtkinter.CTkButton(frame_3,width=50 , text="Search", command=search_s)
        self.search_btn_s.grid(row=14, column=1,columnspan=1)

        self.clear_search_s = customtkinter.CTkButton(frame_3,width=50 , text="Clear", command=clear_search_s)
        self.clear_search_s.grid(row=14, column=2,columnspan=1)

        treeview.bind("<ButtonRelease-1>", s_select_record)

    #---------------------------------------------------------------------------------------

        tree_style = ttk.Style()
        
        tree_style.configure("mystyle.Treeview",font=('Helvetica', 11))
        tree_style.configure("mystyle.Treeview.Heading",font=(15))

    
        p_treeview = ttk.Treeview(frame_6,show='headings',style="mystyle.Treeview")
        p_treeview.place(width=1550, height=700)
        
        

        
      
        p_treeview["columns"] = ("Service ID", "Payment R OR N", "Vehicle Milage","Manufacturer Details","Other Model Details","Customer NIC","Customer Gender","Customer Email","Customer Phone No","City","State")
        p_treeview.column('#0', anchor=W, width=40,stretch=tk.NO)
        p_treeview.column('Service ID', anchor=W, width=50)
        p_treeview.column('Payment R OR N', anchor=W, width=100)
        p_treeview.column('Vehicle Milage', anchor=W, width=145)
        p_treeview.column('Manufacturer Details', anchor=W, width=140)
        p_treeview.column('Other Model Details', anchor=W, width=120)
        p_treeview.column('Customer NIC', anchor=W, width=120)
        p_treeview.column('Customer Gender', anchor=W, width=110)
        p_treeview.column('Customer Email', anchor=W, width=140)
        p_treeview.column('Customer Phone No', anchor=W, width=120)
        p_treeview.column('City', anchor=W, width=90)
        p_treeview.column('State', anchor=W, width=250)

        p_treeview.heading('#0', text='',anchor=W)
        p_treeview.heading('Service ID', text='ID',anchor=W)
        p_treeview.heading('Payment R OR N', text='Payment',anchor=W)
        p_treeview.heading('Vehicle Milage', text='Vehicle Milage',anchor=W)
        p_treeview.heading('Manufacturer Details', text='Manu. Details',anchor=W)
        p_treeview.heading('Other Model Details', text='Other Details',anchor=W)
        p_treeview.heading('Customer NIC', text='Cus. NIC',anchor=W)
        p_treeview.heading('Customer Gender', text='Cus. Gender',anchor=W)
        p_treeview.heading('Customer Email', text='Cus. Email',anchor=W)
        p_treeview.heading('Customer Phone No', text='Cus. Phone No',anchor=W)
        p_treeview.heading('City', text='City',anchor=W)
        p_treeview.heading('State', text='State',anchor=W)
      

        conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
        cur = conn.cursor()
        cur.execute("SELECT  s_id,paymentRON,v_milage, manufacturer_d, other_m_d, c_nic, c_gender, c_email, c_phone, c_city, c_state FROM service_booking")

        for row in cur:
            p_treeview.insert("", "end", values=row)

        
        def p_select_record(e):
            self.p_id.set(" ")
            self.p_optionmenu_1.set(" ")
            self.p_milage.delete(0, END)
            self.p_manufacturer.delete(0, END)
            self.p_other.delete(0, END)
            self.p_nic.delete(0, END)
            self.p_gender.set(" ")
            self.p_phone.delete(0, END)
            self.p_email.delete(0, END)
            self.p_city.delete(0, END)
            self.p_state.delete(0, END)
           

            selected = p_treeview.focus()
            values = p_treeview.item(selected,'values')

            self.p_id.set(values[0])
            self.p_optionmenu_1.set(values[1])
            self.p_milage.insert(0, values[2])
            self.p_manufacturer.insert(0, values[3])
            self.p_other.insert(0, values[4])
            self.p_nic.insert(0, values[5])
            self.p_gender.set(values[6])
            self.p_email.insert(0, values[7])
            self.p_phone.insert(0, values[8])
            self.p_city.insert(0, values[9])
            self.p_state.insert(0, values[10])
        
        def delete_p_record():
            
            
            g_p_id = str(self.p_id.get())
            g_p_optionmenu_1 = str(self.p_optionmenu_1.get())
            g_p_milage = str(self.p_milage.get())
            g_s_manufacturer = str(self.p_manufacturer.get())
            g_s_other= str(self.p_other.get())
            g_s_nic = str(self.p_nic.get())
            g_s_gender= str(self.p_gender.get())
            g_s_email= str(self.p_email.get())
            g_s_phone = str(self.p_phone.get())
            g_s_city= str(self.p_city.get())
            g_s_state = str(self.p_state.get())

            if(g_p_id == "" or g_p_id == " ")or (g_p_optionmenu_1 == "" or g_p_optionmenu_1 == " ") or (g_p_milage     == "" or g_p_milage   == " ") or (g_s_manufacturer == "" or g_s_manufacturer == " ")or (g_s_other == "" or g_s_other == " ")or (g_s_nic == "" or g_s_nic == " ")or (g_s_gender == "" or g_s_gender == " ")or (g_s_phone == "" or g_s_phone == " ")or (g_s_city == "" or g_s_city == " ")or (g_s_state == "" or g_s_state == " ")or (g_s_email == "" or g_s_email == " "):
               messagebox.showerror("Error", "Please select a record")
               return
            else:
                try:
                   alert =  messagebox.askyesno("Message","Do you want to delete this record?")
                   if alert == 0:
                    p_refresh_tree_view()
                   else:

                    cursor = conn.cursor()
                    cursor.execute("UPDATE service_booking SET s_id=%s,paymentRON=%s,v_milage=%s, manufacturer_d=%s, other_m_d=%s, c_nic=%s, c_gender=%s, c_email=%s, c_phone=%s, c_city=%s, c_state=%s WHERE s_id=%s", (g_p_id, 'No', 'None' ,'None','None','None','None','None','0','None','None',g_p_id))
                    conn.commit()
                    cursor.close()
                   self.p_id.set(" ")
                   self.p_optionmenu_1.set(" ")
                   self.p_milage.delete(0, END)
                   self.p_manufacturer.delete(0, END)
                   self.p_other.delete(0, END)
                   self.p_nic.delete(0, END)
                   self.p_gender.set(" ")
                   self.p_email.delete(0, END)
                   self.p_city.delete(0, END)
                   self.p_state.delete(0, END)
                   self.p_phone.delete(0, END)
                   
                   p_refresh_tree_view()

                   

                except:

                    messagebox.showerror("Error", "The data you entered is incorrect. Check the phone number again.")
                    return
        
     

        def p_refresh_tree_view():

            p_treeview.delete(*p_treeview.get_children())

            conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT  s_id,paymentRON,v_milage, manufacturer_d, other_m_d, c_nic, c_gender, c_email, c_phone, c_city, c_state FROM service_booking")
            conn.commit()
            for row in cur:
                p_treeview.insert("", "end", values=row)


        def update_p_record():

            g_p_id = str(self.p_id.get())
            g_p_optionmenu_1 = str(self.p_optionmenu_1.get())
            g_p_milage = str(self.p_milage.get())
            g_s_manufacturer = str(self.p_manufacturer.get())
            g_s_other= str(self.p_other.get())
            g_s_nic = str(self.p_nic.get())
            g_s_gender= str(self.p_gender.get())
            g_s_email= str(self.p_email.get())
            g_s_phone = str(self.p_phone.get())
            g_s_city= str(self.p_city.get())
            g_s_state = str(self.p_state.get())

            if(g_p_id == "" or g_p_id == " ")or (g_p_optionmenu_1 == "" or g_p_optionmenu_1 == " ") or (g_p_milage     == "" or g_p_milage   == " ") or (g_s_manufacturer == "" or g_s_manufacturer == " ")or (g_s_other == "" or g_s_other == " ")or (g_s_nic == "" or g_s_nic == " ")or (g_s_gender == "" or g_s_gender == " ")or (g_s_phone == "" or g_s_phone == " ")or (g_s_city == "" or g_s_city == " ")or (g_s_state == "" or g_s_state == " ")or (g_s_email == "" or g_s_email == " "):
               messagebox.showerror("Error", "Please fill up the blank entry")
               return
            else:
                try:
                   
                   cursor = conn.cursor()
                   cursor.execute("UPDATE service_booking SET s_id=%s,paymentRON=%s,v_milage=%s, manufacturer_d=%s, other_m_d=%s, c_nic=%s, c_gender=%s, c_email=%s, c_phone=%s, c_city=%s, c_state=%s WHERE s_id=%s", (g_p_id, g_p_optionmenu_1, g_p_milage ,g_s_manufacturer,g_s_other,g_s_nic,g_s_gender,g_s_email,g_s_phone,g_s_city,g_s_state,g_p_id))
                   conn.commit()
                   cursor.close()
                   

                   
                   self.p_id.set(" ")
                   self.p_optionmenu_1.set(" ")
                   self.p_milage.delete(0, END)
                   self.p_manufacturer.delete(0, END)
                   self.p_other.delete(0, END)
                   self.p_nic.delete(0, END)
                   self.p_gender.set(" ")
                   self.p_email.delete(0, END)
                   self.p_phone.delete(0, END)
                   self.p_city.delete(0, END)
                   self.p_state.delete(0, END)
                   
                   p_refresh_tree_view()
                   
                   

                except:

                    messagebox.showerror("Error", "The data you entered is incorrect. Check the phone number again.")
                    return
        

        

        
        

        self.p_id_label= customtkinter.CTkLabel(frame_5, text="Service ID:")
        self.p_payment_label= customtkinter.CTkLabel(frame_5, text="Payment Received or Not:")
        self.p_vehicle_milage_label= customtkinter.CTkLabel(frame_5, text="Vehicle Milage:")
        self.p_manufacturer_label= customtkinter.CTkLabel(frame_5, text="Manufacturer Details:")
        self.p_other_label = customtkinter.CTkLabel(frame_5, text="Other Model Details:")
        self.p_nic_label = customtkinter.CTkLabel(frame_5, text="Customer NIC:")
        self.p_gender_label = customtkinter.CTkLabel(frame_5, text="Customer Gender:")
        self.p_email_label = customtkinter.CTkLabel(frame_5, text="Customer Email:")
        self.p_phone_label = customtkinter.CTkLabel(frame_5, text="Customer Phone No:")
        self.p_city_label = customtkinter.CTkLabel(frame_5, text="City:")
        self.p_state_label = customtkinter.CTkLabel(frame_5, text="State:")

        self.p_id_label.grid(row=1,column=0,padx=10,pady=10)
        self.p_payment_label.grid(row=2,column=0,padx=10,pady=10)
        self.p_vehicle_milage_label.grid(row=3,column=0,padx=10,pady=10)
        self.p_manufacturer_label.grid(row=4,column=0,padx=10,pady=10)
        self.p_other_label.grid(row=5,column=0,padx=10,pady=10)
        self.p_nic_label.grid(row=6,column=0,padx=10,pady=10)
        self.p_gender_label.grid(row=7,column=0,padx=10,pady=10)
        self.p_email_label.grid(row=8,column=0,padx=10,pady=10)
        self.p_phone_label.grid(row=9,column=0,padx=10,pady=10)
        self.p_city_label.grid(row=10,column=0,padx=10,pady=10)
        self.p_state_label.grid(row=11,column=0,padx=10,pady=10)
        
        conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
        cur = conn.cursor()
        cur.execute("SELECT s_id FROM service_booking")
                

        my_list_p = [r for r, in cur] 

        self.p_id = customtkinter.CTkComboBox(frame_5, values=my_list_p, width=200,height=35)
        self.p_optionmenu_1 = customtkinter.CTkComboBox(frame_5, values=["No", "Yes"],width=200,height=35)
        self.p_milage= customtkinter.CTkEntry(frame_5, placeholder_text="Vehicle Milage",width=200,height=35)
        self.p_manufacturer= customtkinter.CTkEntry(frame_5, placeholder_text="Manufacturer Details",width=200,height=35)
        self.p_other= customtkinter.CTkEntry(frame_5,placeholder_text="Other Model Details",width=200,height=35)
        self.p_nic= customtkinter.CTkEntry(frame_5, placeholder_text="Customer NIC",width=200,height=35)
        self.p_gender=  customtkinter.CTkComboBox(frame_5, values=["Male", "Female"],width=200,height=35)
        self.p_email= customtkinter.CTkEntry(frame_5, placeholder_text="Customer Email",width=200,height=35)
        self.p_phone= customtkinter.CTkEntry(frame_5, placeholder_text="Customer Phone No",width=200,height=35)
        self.p_city=  customtkinter.CTkEntry(frame_5, placeholder_text="City",width=200,height=35)
        self.p_state= customtkinter.CTkEntry(frame_5, placeholder_text="State",width=200,height=35)

        self.search_entry= customtkinter.CTkEntry(frame_5, placeholder_text="Search",width=200,height=35)
        self.search_entry.grid(row=13,column=1,columnspan=3,pady=(50,7))

        def aaa():
            conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT s_id FROM service_booking")
            my_list = [r for r, in cur]
            self.p_id.set(" ")
            self.p_id.configure(values=my_list)

            p_refresh_tree_view()


        self.tabview.configure(command=aaa)

        def search_p():
            g_search_entry = str(self.search_entry.get())
            p_treeview.delete(*p_treeview.get_children())

            conn9 = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur9 = conn9.cursor()
            cur9.execute("SELECT  s_id,paymentRON,v_milage, manufacturer_d, other_m_d, c_nic, c_gender, c_email, c_phone, c_city, c_state FROM service_booking WHERE c_nic = %s or c_email = %s ",(g_search_entry,g_search_entry))
            conn9.commit()
            for row9 in cur9:
                p_treeview.insert("", "end", values=row9)
         

        def clear_p_search():

            p_treeview.delete(*p_treeview.get_children())

            conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT s_id,paymentRON,v_milage, manufacturer_d, other_m_d, c_nic, c_gender, c_email, c_phone, c_city, c_state FROM service_booking")
            conn.commit()
            for row in cur:
                p_treeview.insert("", "end", values=row)
            self.search_entry.delete(0, END)

        self.p_id.grid(row=1,column=1,columnspan=3,padx=5,pady=5)
        self.p_optionmenu_1.grid(row=2,column=1,columnspan=3,pady=5)
        self.p_milage.grid(row=3,column=1,columnspan=3,pady=5)
        self.p_manufacturer.grid(row=4,column=1,columnspan=3,pady=5)
        self.p_other.grid(row=5,column=1,columnspan=3,pady=5)
        self.p_nic.grid(row=6,column=1,columnspan=3,pady=5)
        self.p_gender.grid(row=7,column=1,columnspan=3,pady=5)
        self.p_email.grid(row=8,column=1,columnspan=3,pady=5)
        self.p_phone.grid(row=9,column=1,columnspan=3,padx=5,pady=5)
        self.p_city.grid(row=10,column=1,columnspan=3,pady=5)
        self.p_state.grid(row=11,column=1,columnspan=3,pady=5)

      
        
        self.p_update_button = customtkinter.CTkButton(frame_5,width=50 , text="Update",  command=update_p_record)
        self.p_update_button.grid(row=12, column=1,columnspan=1)
        
        self.p_delete_button = customtkinter.CTkButton(frame_5,width=50 , text="Delete",  command=delete_p_record)
        self.p_delete_button.grid(row=12, column=3,columnspan=1)

        self.search_btn = customtkinter.CTkButton(frame_5,width=50 , text="Search", command=search_p)
        self.search_btn.grid(row=14, column=1,columnspan=1)

        self.clear_search = customtkinter.CTkButton(frame_5,width=50 , text="Clear", command=clear_p_search)
        self.clear_search.grid(row=14, column=2,columnspan=1)

        p_treeview.bind("<ButtonRelease-1>", p_select_record)


        #------------------------------------------------------------------------------------
        def connection():
            conn = pymysql.connect(host="localhost", user="root", password="Senuja@123",db="abc")
            return conn
        
        def sign_out_btn():
            alert =  messagebox.askyesno("Message","Do you want to sign out?")
            if alert == 0:
                NONE
            else:
                with open("data.txt", "w") as f:
                    f.write(" ")
                self.destroy()
                call(["python","Project_File\\main.py"])


        def change_to_new():
            dialog1 = customtkinter.CTkInputDialog(text="New Password:", title="Change Password")
            dialog1.iconbitmap('icon.ico')
            
            i_dialog1 = dialog1.get_input()
            if (i_dialog1 == "" or i_dialog1 == " "):
                messagebox.showerror("Error", "Please fill up the blank entry")
                return
            else:
                try:
                    
        
                    cursor = conn.cursor()
                    cursor.execute("UPDATE admin SET pwd=%s WHERE id=%s ",(i_dialog1, ddd))
                    conn.commit()
                    cursor.close()
                    messagebox.showinfo("Success", "Password is changed")
                except:
                    messagebox.showerror("Error", "Unknown error occurred")
                    return
        
        def aaa():
            conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT m_name FROM mechanics_details")
            my_list = [r for r, in cur]
            self.optionmenu_2.set(" ")
            self.optionmenu_2.configure(values=my_list)
            s_refresh_tree_view()
            self.p_id.set(" ")
            cur.execute("SELECT s_id FROM service_booking")
            my_list = [r for r, in cur]
            self.p_id.configure(values=my_list)
            p_refresh_tree_view()


        self.tabview.configure(command=aaa)

        def button_click_event():
            dialog = customtkinter.CTkInputDialog(text="Current Password:", title="Change Password")
            dialog.iconbitmap('icon.ico')
            i_dialog = dialog.get_input()
            

            if (i_dialog == "" or i_dialog == " "):
                messagebox.showerror("Error", "Please fill up the blank entry")
                return
            else:
                try:
                    conn = connection() 
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM admin WHERE pwd=%s",(i_dialog))
                    row = cursor.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "Password is incorrect")
                    else:
                        change_to_new()
                except:
                    messagebox.showerror("Error", "Unknown error occurred")
                    return

        self.u_id_label= customtkinter.CTkLabel(frame_9, text="ID:")
        self.u_name_label= customtkinter.CTkLabel(frame_9, text="Name:")
        self.u_username_label = customtkinter.CTkLabel(frame_9, text="Username:",anchor=W)
        self.u_password_label = customtkinter.CTkLabel(frame_9, text="Password:",anchor=W)


        self.u_id1= customtkinter.CTkEntry(frame_9, placeholder_text="ID",width=200,height=35)
        self.u_name1= customtkinter.CTkEntry(frame_9, placeholder_text="Name",width=200,height=35)
        self.u_usernae1= customtkinter.CTkEntry(frame_9, placeholder_text="Username",width=200,height=35)
        self.u_password1= customtkinter.CTkEntry(frame_9, placeholder_text="Password",width=200,height=35,show="*")
        
        

        self.u_id_label.grid(row=1,column=0,padx=10,pady=10)
        self.u_name_label.grid(row=2,column=0,padx=10,pady=10)
        self.u_username_label.grid(row=4,column=0,padx=10,pady=10)
        self.u_password_label.grid(row=5,column=0,padx=10,pady=10)

        self.u_id1.grid(row=1,column=1,columnspan=3,padx=5,pady=5)
        self.u_name1.grid(row=2,column=1,columnspan=3,padx=5,pady=5)
        self.u_usernae1.grid(row=4,column=1,columnspan=3,padx=5,pady=5)
        self.u_password1.grid(row=5,column=1,columnspan=3,padx=5,pady=5)

        self.p_update_button = customtkinter.CTkButton(frame_9,width=50 , text="Change Password", command=button_click_event)
        self.p_update_button.grid(row=7,column=1,columnspan=3,padx=5,pady=4)

        self.p_update_button = customtkinter.CTkButton(frame_9,width=50 , text="Sign Out", command=sign_out_btn)
        self.p_update_button.grid(row=8,column=1,columnspan=3,padx=5,pady=4)

        conn = pymysql.connect(db='abc', user='root', password='Senuja@123', host='localhost')
        cur = conn.cursor()
        cur.execute("SELECT * FROM admin WHERE username=%s", (name))
        conn.commit()
        for row in cur:
            global ddd
            ddd = row[0]
            self.u_id1.insert(0, row[0])
            self.u_name1.insert(0, row[1])
            self.u_usernae1.insert(0, row[2])
            self.u_password1.insert(0, row[3])
        
        self.u_id1.configure(state="disabled") 
        self.u_name1.configure(state="disabled")
        self.u_usernae1.configure(state="disabled")
        self.u_password1.configure(state="disabled") 

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkScrollbar(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


    def sidebar_button_event(self):
        print("sidebar_button click")

    
if __name__ == "__main__":
    app = App()
    app.mainloop()