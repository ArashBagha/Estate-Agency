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

# لیست کشویی فیلد فایل 
def kharid():
    pass
def forosh():
    pass
def rahn():
    pass
def mosharecat():
    pass

# لیست کشویی فیلد گزارش ها
def excel():
    pass
def gharardadeha():
    pass

#---#----#----#----#----#----------  گرافیک   ----------#----#----#----#-----#-----------

# پنجره اصلی (باکس مادر)

root = tk.Tk()
root.title("")
root.geometry("1100x700")#------------------------
##----------------------------------------------------------------------------------------------##
# root.attributes("-fullscreen", True) <<<-----  App فول اسکرین شدن
##----------------------------------------------------------------------------------------------##
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
menu_frame=tk.Frame(main_frame,bg="#ffffff", relief="flat",height=1)#رنگ موقتی
menu_frame.pack(padx=2, pady=2, fill="both", expand=True)

# دکمه فایل با منوی کشویی 
file_button = tk.Button(menu_frame, text="ثبت فایل ها", bg="#ffffff", relief="flat")
file_button.pack(padx=5, pady=5, side="left")

file_popup = tk.Menu(root, tearoff=0, font=("Arial", 12))
file_popup.add_command(label="خرید", command=kharid)
file_popup.add_command(label="فروش", command=forosh)
file_popup.add_command(label="رهن/اجاره", command=rahn)
file_popup.add_command(label="مشارکت", command=mosharecat)

def show_file_popup(event):
    file_popup.tk_popup(event.x_root, event.y_root)

file_button.bind("<Button-1>", show_file_popup)
 

# اضافه کردن فیلد قرارداد 
file_button = tk.Button(menu_frame, text="قرارداد ", bg="#ffffff", relief="flat")
file_button.pack(padx=10, pady=5, side="left")

# دکمه گزارش ها با منوی کشویی  
file_button = tk.Button(menu_frame, text="گزارش ها", bg="#ffffff", relief="flat")
file_button.pack(padx=10, pady=10, side="left")

file_popup1 = tk.Menu(root, tearoff=0, font=("Arial", 12))
file_popup1.add_command(label="خروجی اکسل", command=excel)
file_popup1.add_command(label="قرارداد ها", command=gharardadeha)

def show_file_popup(event):
    file_popup1.tk_popup(event.x_root, event.y_root)

file_button.bind("<Button-1>", show_file_popup)

# اضافه کردن فیلد درخواست ها  
file_button = tk.Button(menu_frame, text="درخواست ها", bg="#ffffff", relief="flat")
file_button.pack(padx=10, pady=5, side="left")

#اضافه کردن فیلد کاربران 
file_button = tk.Button(menu_frame, text="کاربران ", bg="#ffffff", relief="flat")
file_button.pack(padx=10, pady=5, side="left")
#--------------------------------------------------------------------------------------------------------

# باکس سمت چپ - جستجو در فایل های ملک

left_frame = tk.LabelFrame(root, text="جستجوی ملک", width=200, bg="#575353",fg="#F8F7F7", font=("Arial", 16))
left_frame.pack(side="left", fill="y", padx=6, pady=15)

Box1 = tk.Frame(left_frame,bg="#0F6E6E")
Box1.pack(padx=6, pady=15)

filetype = tk.Label(Box1,text="نوع فایل",bg="#0F6E6E", fg="#FFFFFF",font=("Arial", 14))
filetype.pack(padx=15,pady=10, side="right")
combo1= ttk.Combobox(Box1)
combo1["values"] = ("رهن/اجاره","خرید","فروش","مشارکت",)
combo1.pack(padx=10, pady=10) 

Box3 = tk.Frame(left_frame,bg="#0F6E6E")
Box3.pack(padx=6, pady=15)

melktypelable = tk.Label(Box3,text="نوع ملک",bg="#0F6E6E", fg="#FFFFFF",font=("Arial", 14))
melktypelable.pack(padx=15,pady=10, side="right")
combo2= ttk.Combobox(Box3)
combo2["values"] = ("مسکونی","مغازه/ تجاری"," باغ / زمین","سوله / کارگاه")
combo2.pack(padx=10, pady=10) 

Box3 = tk.Frame(left_frame,bg="#0F6E6E")
Box3.pack(padx=6, pady=5)

melk_Pricelimit_lable = tk.Label(Box3,text="محدوده قیمت",bg="#0F6E6E", fg="#FFFFFF",font=("Arial", 14))
melk_Pricelimit_lable.pack(padx=5, pady=1)
entry_melk_Pricelimit = tk.Entry(Box3,text=" ",bg="#C2C2C2", fg="#FFFFFF",font=("Arial", 14))
entry_melk_Pricelimit.pack(padx=20,pady=10)

melk_Area_lable = tk.Label(Box3,text=" متراژ",bg="#0F6E6E", fg="#FFFFFF",font=("Arial", 14))
melk_Area_lable.pack(padx=5, pady=1)
entry_melk_Area_lable = tk.Entry(Box3,text=" ",bg="#C2C2C2", fg="#FFFFFF",font=("Arial", 14))
entry_melk_Area_lable.pack(padx=20,pady=10)

melk_Area_lable = tk.Label(Box3,text=" منطقه / آدرس",bg="#0F6E6E", fg="#FFFFFF",font=("Arial", 14))
melk_Area_lable.pack(padx=5, pady=1)
entry_melk_Area_lable = tk.Entry(Box3,text=" ",bg="#C2C2C2", fg="#FFFFFF",font=("Arial", 14))
entry_melk_Area_lable.pack(padx=20,pady=10)

# دکمه جستجوی ملک
search_btn = tk.Button(left_frame, text="    جستجو    " , bg="#94c6dd", fg="#201F1F", font=("Arial", 14), command=open_file)
search_btn.pack(pady=10)
#--------------------------------------------------------------------------------------------------------

# باکس وسط - نمایش جستجوی قراردادها

center_frame = tk.LabelFrame(root, text="لیست املاک", bg="#ffffff", font=("Arial", 14))
center_frame.pack(side="left", fill="both", expand=True, padx=4, pady=15)

columns = ["آدرس", "قیمت ", "نوع ملک ", "متراژ"]
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


right_fields = [" مالک ", " شماره تماس مالک "," متراژ " , " قیمت ", " توضیحات "]
entries = {}

for field in right_fields:
    lbl = tk.Label(right_frame, text=field, bg="#272B61", fg="#F7F7FA",font=("Arial", 14))
    lbl.pack(fill="x", padx=6, pady=4)
    entry = tk.Entry(right_frame)
    entry.pack( padx=20, pady=5)
    entries[field] = entry

# دکمه برای افزودن عکس به ملک
#add_img_btn = tk.Button(right_frame, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file)
#add_img_btn.pack(pady=10)

root.protocol("WM_DELETE_WINDOW",close_window)
# اجرای برنامه
root.mainloop()

