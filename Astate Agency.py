import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox,font
import subprocess
import os

#---#----#----#----#----#----------  توابع   ----------#----#----#----#-------------
def close_window():#این تابع بعد از اتصال دیتابیس تکمیل مشود 
    response=messagebox.askyesno("تایید خروج","آیا از خارج شدن اطمینان دارید؟")
    if response:
        root.destroy()
    else:
        return
# تابع فراخوانی ادرس با دکمه 

def open_file_folder():
    file_path = filedialog.askopenfilename()
    if file_path:
        folder_path = os.path.dirname(file_path)
        subprocess.run(['explorer', '/select,', file_path])

# تابع انتخاب فایل

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        os.startfile(file_path)

#---#----#----#----#----#----------  گرافیک   ----------#----#----#----#-----#-----------

# پنجره اصلی (باکس مادر)

root = tk.Tk()
root.title("")
root.geometry("1100x700")
root.configure(bg="#0D4D34")
#-----------------------------------------------------فریم مادر------------------------------------------------
main_frame=tk.Frame(root)
main_frame.pack(fill="both",expand=True)
#------------------------فریم هدر --------------
header=tk.Frame(main_frame,bg="#404040",height=60)
header.pack(fill='x')
title_font=font.Font(family="B Nazanin",size=22,weight="bold")
title_label=tk.Label(header,text="آژانس املاک",fg="#FFFFFF",bg="#404040",font=title_font)
title_label.pack(pady=10)

#---------------------فریم منو----------------------
#بخش مربوط به عماد لطفا لیست باکس ها رو پر کن
menu_frame=tk.Frame(main_frame,bg="#ffffff", relief="ridge",height=1)#رنگ موقتی
menu_frame.pack(padx=2, pady=2, fill="both", expand=True)
listbox1=tk.Listbox(menu_frame,height=1,width=5,bg="#ffffff",border=0)
listbox1.insert(tk.END,"فایل")
listbox1.pack(padx=5,pady=5,side="left")

listbox2=tk.Listbox(menu_frame,height=1,width=8,bg="#ffffff",border=0)
listbox2.insert(tk.END,"قرارداد")
listbox2.pack(padx=10,pady=5,side="left")

listbox3=tk.Listbox(menu_frame,height=1,width=8,bg="#ffffff",border=0)
listbox3.insert(tk.END,"گزارش ها")
listbox3.pack(padx=10,pady=5,side="left")

listbox4=tk.Listbox(menu_frame,height=1,width=12,bg="#ffffff",border=0)
listbox4.insert(tk.END,"درخواست ها")
listbox4.pack(padx=10,pady=5,side="left")

# باکس سمت چپ - جستجو در فایل های ملک

left_frame = tk.LabelFrame(root, text="جستجوی ملک", width=200, bg="#575353",fg="#F8F7F7", font=("Arial", 16))
left_frame.pack(side="left", fill="y", padx=6, pady=15)

left_fields = ["کد ملک", "نوع ملک" ,"وضعیت", "محدوده قیمت", "منطقه / آدرس"]
entries = {}

for field in left_fields:
    lbl = tk.Label(left_frame, text=field, bg="#A08D70", fg="#252527",font=("Arial", 14))
    lbl.pack(fill="x", padx=10, pady=2)
    entry = tk.Entry(left_frame)
    entry.pack( padx=16, pady=5)
    entries[field] = entry

# دکمه جستجوی ملک
search_btn = tk.Button(left_frame, text="    جستجو    " , bg="#94c6dd", fg="#201F1F", font=("Arial", 14), command=open_file)
search_btn.pack(pady=10)
#--------------------------------------------------------------------------------------------------------

# باکس وسط - نمایش جستجوی قراردادها

center_frame = tk.LabelFrame(root, text="لیست املاک", bg="#ffffff", font=("Arial", 14))
center_frame.pack(side="left", fill="both", expand=True, padx=4, pady=15)

columns = ["آدرس", "متراژ", "قیمت ", "نوع ملک ", "وضعیت"]
tree = ttk.Treeview(center_frame, columns=columns, show="headings")
for textt in columns:
    tree.heading(textt,text=textt)
    tree.column(textt, width=100)
tree.pack(fill="both", expand=True)
#--------------------------------------------------------------------------------------------------------

# باکس سمت راست - نمایش جزئیات فایل های موجود املاک

right_frame = tk.LabelFrame(root, text="جزئیات ملک", width=200, bg="#ffffff", font=("Arial", 14))
right_frame.pack(side="right", fill="y", padx=6, pady=15)

photo_lbl = tk.Label(right_frame, text="[تصویر ملک]", bg="gray", width=20, height=10)
photo_lbl.pack(pady=10)


right_fields = [" مالک ", " متراژ " ," قیمت ", " وضعیت ملک ", " توضیحات "]
entries = {}

for field in right_fields:
    lbl = tk.Label(right_frame, text=field, bg="#272B61", fg="#F7F7FA",font=("Arial", 14))
    lbl.pack(fill="x", padx=6, pady=4)
    entry = tk.Entry(right_frame)
    entry.pack( padx=20, pady=5)
    entries[field] = entry

# دکمه برای افزودن عکس به ملک
add_img_btn = tk.Button(right_frame, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file)
add_img_btn.pack(pady=10)

root.protocol("WM_DELETE_WINDOW",close_window)
# اجرای برنامه
root.mainloop()
