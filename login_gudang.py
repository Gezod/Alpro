from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


#pip install Pillow
kesempatan=0

def login():
    global kesempatan
    name = txt_user.get()
    passw = txt_pass.get()
    
    with open('login_data.txt', 'r') as file:
        text = file.read()
        a,b = text.split(',')
        b = b.strip()
        if (a == name and b == passw):
            messagebox.showinfo("",'Berhasil login! silahkan masuk')
            root.destroy()
            import tubes
        else:
            kesempatan += 1
            messagebox.showinfo("Login Gudang",f"ID atau password anda salah, silahkan mengulangi lagi Kesempatan {kesempatan}")
            if kesempatan == 3:
                messagebox.showinfo("Gagal Login",f"Sudah 3 Kali Kesempatan, Program Terhenti")
                root.destroy()
    


def logout():
    root.destroy()


#Tampilan 
root = Tk()
root.title("Login Dashboard Inventory Gudang")
root.geometry("700x600")
img = ImageTk.PhotoImage(Image.open("gudang.jpg"))  
Label(root, image=img).place(x=0, y=0 , relwidth=1, relheight=1)

#Membuat Frame
frame_login = Frame(root, bg="lightgrey")
frame_login.place(x = 150, y = 150, height=340, width = 500)

#Judul
title= Label(frame_login, text="Silahkan Login", font=('Impact',35,"bold"),
            fg = "black", bg= "gray").place(x = 90, y = 30)

#Label User
label_user = Label(frame_login, text= "ID", font=(" Goudy old style",15,"bold"),
            fg="white", bg = 'gray').place(x=90, y= 130)

txt_user = Entry(frame_login, font=("Times New Roman",15), bg="lightgray")
txt_user.place(x = 90 ,y = 170 , width= 350, height=35)

#Label Password
label_pass = Label(frame_login, text= "Password", font=(" Goudy old style",15,"bold"),
            fg="white", bg = 'gray').place(x=90, y= 210)

txt_pass = Entry(frame_login, font=("Times New Roman",15), bg="lightgray")
txt_pass.place(x = 90 ,y = 240 , width= 350, height=35)

#Tombol login
logout_btn = Button(frame_login, command=logout, text="Logout", fg= "white", bg = "red",
            font=("Times New Roman", 20)).place(x=300, y = 280)

login_btn = Button(frame_login, command=login, text="Login", fg= "white", bg = "darkblue",
            font=("Times New Roman", 20)).place(x=200, y = 280)


root.mainloop()