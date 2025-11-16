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

def open_option():
    option_file_frame.deiconify()
    buy_page.withdraw()
def back_to_buy_page():
    pass


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
root.geometry("1100x700")
#تصاویر پروژه
plus=tk.PhotoImage(file="pluse.png")
##----------------------------------------------------------------------------------------------##
# root.attributes("-fullscreen", True) <<<-----  App فول اسکرین شدن
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



#پنجره های فرعی فایل
buy_page = tk.Toplevel(root)
buy_page.title("")
buy_page.geometry("800x600")
buy_page.configure(bg="#0D4D34")#نیما رنگ بگراندشو خودت انتخاب کن
 
#option_file
option_file_frame=tk.Toplevel(buy_page)
option_file_frame.title(" ")
buy_page.geometry("700x700")



buy_page_frme1=tk.Frame(buy_page,width=490,height=800,bg="#5d6059",border=2)
buy_page_frme1.place(x=500,y=50)


melktype_buy=tk.Label(buy_page_frme1,text="نوع ملک",bg="#0F6E6E",fg="#ffffff",width=10)
melktype_buy.grid(padx=8,pady=15,sticky="e",row=0,column=1)

combo_melktype= ttk.Combobox(buy_page_frme1)
combo_melktype["values"] = ("مسکونی","مغازه/ تجاری"," باغ / زمین","سوله / کارگاه")
combo_melktype.grid(padx=8, pady=15,row=0,column=0,sticky="w") 

year_buy=tk.Label(buy_page_frme1,text="سال ساخت",bg="#0F6E6E",fg="#ffffff",width=10)
year_buy.grid(padx=8,pady=10,sticky="e",row=1,column=1)

year_buy_entry=tk.Entry(buy_page_frme1,text=" ",bg="#C2C2C2",  fg="#180202",font=("Arial", 10))
year_buy_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

addrres_buy=tk.Label(buy_page_frme1,text="آدرس",bg="#0F6E6E",fg="#ffffff",width=10)
addrres_buy.grid(padx=8,pady=15,sticky="e",row=2,column=1)

addrres_buy_entry=tk.Entry(buy_page_frme1,text=" ",bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
addrres_buy_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

floor_buy=tk.Label(buy_page_frme1,text="طبقه",bg="#0F6E6E",fg="#ffffff",width=10)
floor_buy.grid(padx=8,pady=15,sticky="e",row=3,column=1)

floor_buy_entry=tk.Entry(buy_page_frme1,text=" ",bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
floor_buy_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

vahed_buy=tk.Label(buy_page_frme1,text="واحد",bg="#0F6E6E",fg="#ffffff",width=10)
vahed_buy.grid(padx=8,pady=15,sticky="e",row=4,column=1)

vahed_buy_entry=tk.Entry(buy_page_frme1,text=" ",bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
vahed_buy_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

room_buy=tk.Label(buy_page_frme1,text="اتاق",bg="#0F6E6E",fg="#ffffff",width=10)
room_buy.grid(padx=8,pady=15,sticky="e",row=5,column=1)

room_buy_entry=tk.Entry(buy_page_frme1,text=" ",bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
room_buy_entry.grid(padx=8,pady=15,sticky="w",row=5,column=0)

price_buy=tk.Label(buy_page_frme1,text="قیمت",bg="#0F6E6E",fg="#ffffff",width=10)
price_buy.grid(padx=8,pady=15,sticky="e",row=6,column=1)

price_buy_entry=tk.Entry(buy_page_frme1,text=" ",bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
price_buy_entry.grid(padx=8,pady=15,sticky="w",row=6,column=0)

photo_box=tk.Frame(buy_page,width=410,height=450,background="#e4dde3")
photo_box.place(x=40,y=40)
photo_lbl2 = tk.Label(photo_box, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2.place(x=30,y=45)
add_img_btn = tk.Button(photo_box, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn.place(x=40,y=330)
#ساخت پنجره امکانات
option_frame=tk.Frame(buy_page,width=300,height=30,background="#d9d3d3")
option_frame.place(x=520,y=460)

option_label=tk.Label(option_frame,text='افزودن امکانات فایل',font=("B Nazanin",12,"bold"),background="#FFFFFF",fg="#000000")
option_label.pack(side="right",padx=1)

button_label=tk.Label(option_frame)
button_label.pack(side="left",padx=1)
plus_button=tk.Button(option_frame,image=plus,command=option_file_frame,border=0)
plus_button.pack()

root.protocol("WM_DELETE_WINDOW",close_window)
# اجرای برنامه
root.mainloop()

