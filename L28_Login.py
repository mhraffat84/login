# Updated Version
# This is new version of the file

import tkinter as tk
from tkinter import messagebox

# إنشاء دالة تسجيل الدخول
def login():
    username = username_entry.get() # to get uesrname
    password = password_entry.get() # to get password

    if username == "Admin" and password == "password":
        messagebox.showinfo("Login Succesful", "Welcome. Admin!") # 1) Title   2) Content
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# إنشاء دالة الإلغاء
def cancel():
    window.destroy()

# إنشاء النافذة الرئيسية
window = tk.Tk()
window.title("Login Form")
window.geometry("300x200")
window.resizable(False,False) # width - Height

#إنشاء إطار للعنوان الرئيسي
title_frame = tk.Frame(window)
title_frame.pack(pady=10)
title_label = tk.Label(title_frame, text="Login Form", font=("Arial", 16))
title_label.pack()

# إنشاء إطار أدوات الإدخال
form_frame = tk.Frame(window)
form_frame.pack(pady=10)
username_label = tk.Label(form_frame, text="UserName: ")
username_label.grid(row=0, column=0, padx=5, pady=5) # row 0 = First Row
username_entry = tk.Entry(form_frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)
password_label = tk.Label(form_frame, text="Password: ")
password_label.grid(row=1, column=0, padx=5, pady=5) # row 1 = Second Row
password_entry = tk.Entry(form_frame, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# إنشاء إطار الأزرار
button_frame = tk.Frame(window)
button_frame.pack(pady=10)
login_button = tk.Button(button_frame, text="Login", command=login)
login_button.grid(row=0, column=0, padx=5)
cancel_button = tk.Button(button_frame, text="Cancel", command=cancel)
cancel_button.grid(row=0, column=1, padx=5)

# Run
window.mainloop()