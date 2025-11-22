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
    ejareh_rehn_page.withdraw()
def back_to_buy_page():
    option_file_frame.withdraw()
    ejareh_rehn_page.deiconify()


# لیست کشویی فیلد فایل 
def kharid():
    pass
def forosh():
    root.withdraw()
    box_forosh.deiconify()
def rahn():
    root.withdraw()
    box_rehn_ejareh.deiconify()
def mosharecat():
    pass

def ejareh_rehn_page():
    box_rehn_ejareh.withdraw()
    ejareh_rehn_page.deiconify()

def ejareh_et():
    pass  #این صفحه با بقا

def ejareh_bz():
    pass

def ejareh_sk():
    pass

def forosh_rehn_page():
    pass   #این صفحه با سبحانه

def forosh_et():
    pass   #این صفحه با عماد

def forosh_bz():
    pass

def forosh_sk():
    pass




# لیست کشویی فیلد گزارش ها
def excel():
    pass
def gharardadeha():
    pass

#بازگشت های صفحات

def back_home():
    root.deiconify()
    ejareh_rehn_page.withdraw()
    entry_melk_Pricelimit.delete(0,tk.END)
    entry_melk_width_lable.delete(0,tk.END)
    entry_melk_area_lable.delete(0,tk.END)
    year_buy_entry.delete(0,tk.END)
    addrres_buy_entry.delete(0,tk.END)
    floor_buy_entry.delete(0,tk.END)
    vahed_buy_entry.delete(0,tk.END)
    room_buy_entry.delete(0,tk.END)
    price_buy_entry.delete(0,tk.END)
    combo1.delete(0,tk.END)
    combo2.delete(0,tk.END)
#---#----#----#----#----#----------  گرافیک   ----------#----#----#----#-----#-----------


# پنجره اصلی (باکس مادر)

root = tk.Tk()
root.title("")
root.geometry("1100x700")
#تصاویر پروژه
plus=tk.PhotoImage(file="pluse.png")
elvator_pic=tk.PhotoImage(file="elvator.png")
parking_pic=tk.PhotoImage(file="parking.png")
warehouse_pic=tk.PhotoImage(file="anbari.png")#انبار
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
entry_melk_Pricelimit = tk.Entry(Box3,bg="#C2C2C2", fg="#FFFFFF",font=("Arial", 14))
entry_melk_Pricelimit.pack(padx=20,pady=10)

melk_Area_lable = tk.Label(Box3,text=" متراژ",bg="#0F6E6E", fg="#FFFFFF",font=("Arial", 14))
melk_Area_lable.pack(padx=5, pady=1)
entry_melk_width_lable = tk.Entry(Box3,bg="#C2C2C2", fg="#FFFFFF",font=("Arial", 14))
entry_melk_width_lable.pack(padx=20,pady=10)

melk_Area_lable = tk.Label(Box3,text=" منطقه / آدرس",bg="#0F6E6E", fg="#FFFFFF",font=("Arial", 14))
melk_Area_lable.pack(padx=5, pady=1)
entry_melk_area_lable = tk.Entry(Box3,bg="#C2C2C2", fg="#FFFFFF",font=("Arial", 14))
entry_melk_area_lable.pack(padx=20,pady=10)

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

malek = tk.Label(right_frame,text="مالک ",bg="#272B61", fg="#F7F7FA",font=("Arial", 14))
malek.pack(padx=6,pady=4)

entry_malek = tk.Entry(right_frame,bg="#C2C2C2", fg="#FFFFFF",font=("Arial", 14))
entry_malek.pack(padx=20,pady=4)

malek_phone_number = tk.Label(right_frame,text="شماره تماس مالک ",bg="#272B61", fg="#F7F7FA",font=("Arial", 14))
malek_phone_number.pack(padx=6,pady=4)

entry_malek_phone_number = tk.Entry(right_frame,bg="#C2C2C2", fg="#FFFFFF",font=("Arial", 14))
entry_malek_phone_number.pack(padx=20,pady=4)

metr = tk.Label(right_frame,text="متراژ ",bg="#272B61", fg="#F7F7FA",font=("Arial", 14))
metr.pack(padx=6,pady=4)

entry_metr = tk.Entry(right_frame,bg="#C2C2C2", fg="#FFFFFF",font=("Arial", 14))
entry_metr.pack(padx=20,pady=4)

melk_price = tk.Label(right_frame,text="قیمت ",bg="#272B61", fg="#F7F7FA",font=("Arial", 14))
melk_price.pack(padx=6,pady=4)

entry_melk_price= tk.Entry(right_frame,bg="#C2C2C2", fg="#FFFFFF",font=("Arial", 14))
entry_melk_price.pack(padx=20,pady=4)

extension = tk.Label(right_frame,text="توضیحات ",bg="#272B61", fg="#F7F7FA",font=("Arial", 14))
extension.pack(padx=6,pady=4)

entry_extension = tk.Entry(right_frame,bg="#C2C2C2", fg="#FFFFFF",font=("Arial", 14))
entry_extension.pack(padx=20,pady=4)

#نوع انتخاب ثبتی فایل برای پنجره های رهن و اجاره

box_rehn_ejareh=tk.Toplevel(root)
box_rehn_ejareh.title("انتخاب نوع ملک رهن و اجاره")
box_rehn_ejareh.geometry("420x180")
box_rehn_ejareh.withdraw()
box_rehn_ejareh.configure(bg="#0F6E6E")
label_box1=tk.Label(box_rehn_ejareh,text="لطفا نوع ملک رهن و اجاره را انتخاب کنید",font=("B Nazanin",17),bg="#0F6E6E",fg="#fff")
label_box1.place(x=75,y=10)

file_button2= tk.Button(box_rehn_ejareh, text="ثبت", bg="#ffffff", relief="flat",width=20)
file_button2.place(x=140,y=60)

file_list_box2 = tk.Menu(box_rehn_ejareh, tearoff=0, font=("Arial", 12))
file_list_box2.add_command(label="اجاره مسکونی", command=ejareh_rehn_page)
file_list_box2.add_command(label="اجاره اداری/تجاری", command=ejareh_et)  #پنجره بقا
file_list_box2.add_command(label="اجاره باغ/زمین",command=ejareh_bz)
file_list_box2.add_command(label="اجاره سوله/کارگاه",command=ejareh_sk)
def show_file_list_box1(event):
    file_list_box2.tk_popup(event.x_root, event.y_root)

file_button2.bind("<Button-1>",show_file_list_box1)

#نوع انتخاب ثبتی فایل برای پنجره های فروش

box_forosh=tk.Toplevel(root)
box_forosh.title("انتخاب نوع ملک فروش")
box_forosh.geometry("420x180")
box_forosh.withdraw()
box_forosh.configure(bg="#0F6E6E")
label_box2=tk.Label(box_forosh,text="لطفا نوع ملک فروش را انتخاب کنید",font=("B Nazanin",17),bg="#0F6E6E",fg="#fff")
label_box2.place(x=100,y=10)

file_button3= tk.Button(box_forosh, text="ثبت", bg="#ffffff", relief="flat",width=20)
file_button3.place(x=140,y=60)

file_list_box3 = tk.Menu(box_forosh, tearoff=0, font=("Arial", 12))
file_list_box3.add_command(label="فروش مسکونی", command=forosh_rehn_page)  #پنجره سبحان
file_list_box3.add_command(label="فروش اداری/تجاری", command=forosh_et)    #پنجره عماد
file_list_box3.add_command(label="فروش باغ/زمین",command=forosh_bz)
file_list_box3.add_command(label="فروش سوله/کارگاه",command=forosh_sk)
def show_file_list_box3(event):
    file_list_box3.tk_popup(event.x_root, event.y_root)

file_button3.bind("<Button-1>",show_file_list_box3)

#==========WINS_BOX1_REHN_EJAREH======================
#win_ejareh_rehn
ejareh_rehn_page = tk.Toplevel(root)
ejareh_rehn_page.title("رهن و اجاره مسکونی")
ejareh_rehn_page.geometry("800x600")
ejareh_rehn_page.withdraw()
ejareh_rehn_page.configure(bg="#0F6E6E")

 
#option_file
option_file_frame=tk.Toplevel(ejareh_rehn_page,background="#bbfbd1" )
option_file_frame.title(" ")
option_file_frame.geometry("500x370")
option_file_frame.pack_propagate(False)
option_file_frame.withdraw()



rehn_page_frame1=tk.Frame(ejareh_rehn_page,width=490,height=800,bg="#5d6059",border=2)
rehn_page_frame1.place(x=500,y=50)


melktype_buy=tk.Label(rehn_page_frame1,text="نوع ملک",bg="#0F6E6E",fg="#ffffff",width=10)
melktype_buy.grid(padx=8,pady=15,sticky="e",row=0,column=1)

melk_type_rehn_maskoni=tk.Entry(rehn_page_frame1,text="اجاره مسکونی",bg="#C2C2C2", fg="#180202",font=("Arial", 10))
melk_type_rehn_maskoni.grid(padx=8, pady=15,row=0,column=0,sticky="w") 


year_buy=tk.Label(rehn_page_frame1,text="سال ساخت",bg="#0F6E6E",fg="#ffffff",width=10)
year_buy.grid(padx=8,pady=10,sticky="e",row=1,column=1)

year_buy_entry=tk.Entry(rehn_page_frame1,bg="#C2C2C2", fg="#180202",font=("Arial", 10))
year_buy_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

addrres_buy=tk.Label(rehn_page_frame1,text="آدرس",bg="#0F6E6E",fg="#ffffff",width=10)
addrres_buy.grid(padx=8,pady=15,sticky="e",row=2,column=1)

addrres_buy_entry=tk.Entry(rehn_page_frame1,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
addrres_buy_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

floor_buy=tk.Label(rehn_page_frame1,text="طبقه",bg="#0F6E6E",fg="#ffffff",width=10)
floor_buy.grid(padx=8,pady=15,sticky="e",row=3,column=1)

floor_buy_entry=tk.Entry(rehn_page_frame1,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
floor_buy_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

vahed_buy=tk.Label(rehn_page_frame1,text="واحد",bg="#0F6E6E",fg="#ffffff",width=10)
vahed_buy.grid(padx=8,pady=15,sticky="e",row=4,column=1)

vahed_buy_entry=tk.Entry(rehn_page_frame1,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
vahed_buy_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

room_buy=tk.Label(rehn_page_frame1,text="اتاق",bg="#0F6E6E",fg="#ffffff",width=10)
room_buy.grid(padx=8,pady=15,sticky="e",row=5,column=1)

room_buy_entry=tk.Entry(rehn_page_frame1,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
room_buy_entry.grid(padx=8,pady=15,sticky="w",row=5,column=0)

price_buy=tk.Label(rehn_page_frame1,text="قیمت",bg="#0F6E6E",fg="#ffffff",width=10)
price_buy.grid(padx=8,pady=15,sticky="e",row=6,column=1)

price_buy_entry=tk.Entry(rehn_page_frame1,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
price_buy_entry.grid(padx=8,pady=15,sticky="w",row=6,column=0)

back_to_home=tk.Button(ejareh_rehn_page,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home)
back_to_home.place(x=650,y=535)

photo_box=tk.Frame(ejareh_rehn_page,width=410,height=450,background="#e4dde3")
photo_box.place(x=40,y=40)
photo_lbl2 = tk.Label(photo_box, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2.place(x=30,y=45)
add_img_btn = tk.Button(photo_box, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn.place(x=40,y=330)
#ساخت پنجره امکانات
option_frame=tk.Frame(ejareh_rehn_page,width=300,height=30,background="#bbfbd1")
option_frame.place(x=520,y=460)

option_label=tk.Label(option_frame,text='افزودن امکانات فایل',font=("B Nazanin",12,"bold"),background="#FFFFFF",fg="#000000")
option_label.pack(side="right",padx=1)

button_label=tk.Label(option_frame)
button_label.pack(side="left",padx=1)
plus_button=tk.Button(option_frame,image=plus,command=open_option,border=0)
plus_button.pack()

option_frame1=tk.Frame(option_file_frame,width=400,height=100,background="#bbfbd1")
option_frame1.pack(padx=10,pady=15)

parking_ch_btn=tk.Checkbutton(option_frame1,image=parking_pic,background="#022578")
parking_ch_btn.pack(padx=15,side="left")

elvator_ch_btn=tk.Checkbutton(option_frame1,image=elvator_pic,background="#022578")
elvator_ch_btn.pack(padx=15,side="left")

warehouse_ch_btn=tk.Checkbutton(option_frame1,image=warehouse_pic,background="#022578")
warehouse_ch_btn.pack(padx=15,side="right")

option_frame2=tk.Frame(option_file_frame,width=400,height=400,background="#bbfbd1",border=1)
option_frame2.pack(padx=10,pady=15)

#balcon_ch_btn=tk.Checkbutton(option_frame2,text="تراس")

sarmaesh=tk.Label(option_frame2,text="سرمایش",background="#025578",fg="#ffffff")
sarmaesh.grid(row=0,column=1,padx=15,pady=5)
sarmaesh_combo=ttk.Combobox(option_frame2)
sarmaesh_combo["values"] = ("ندارد","پنکه سقفی","کولر ابی","کولر گازی ","ابی/گازی")
sarmaesh_combo.grid(row=0,column=0,padx=15,pady=5)

garmaesh=tk.Label(option_frame2,text="گرمایش",background="#025578",fg="#ffffff")
garmaesh.grid(row=1,column=1,padx=15,pady=5)
garmaesh_combo=ttk.Combobox(option_frame2)
garmaesh_combo["values"] = ("ندارد","بخاری"," شوفاژ","گرمایش از کف ")
garmaesh_combo.grid(row=1,column=0,padx=15,pady=5)

kaf=tk.Label(option_frame2,text="کف",background="#025578",fg="#ffffff")
kaf.grid(row=2,column=1,padx=15,pady=5)
kaf_combo=ttk.Combobox(option_frame2)
kaf_combo["values"] = ("سرامیک","موزاییک","پارکت")
kaf_combo.grid(row=2,column=0,padx=15,pady=5)

toilet=tk.Label(option_frame2,text="سرویس بهداشتی",background="#025578",fg="#ffffff")
toilet.grid(row=3,column=1,padx=5,pady=5)
toilet_combo=ttk.Combobox(option_frame2)
toilet_combo["values"] = ("ایرانی","فرنگی","هردو")
toilet_combo.grid(row=3,column=0,padx=15,pady=5)

save_optoin1=tk.Button(option_file_frame,text="ذخیره",command=None,background="#079BDB",fg="#ffffff",width=8)
save_optoin1.place(x=170,y=330)

back_to_buy=tk.Button(option_file_frame,text="بازگشت",command=back_to_buy_page,background="#079BDB",fg="#ffffff",width=8)
back_to_buy.place(x=95,y=330)

#win_ejareh_et===bagha








#==========WINS_BOX2_FOROSH==================
#win_forosh_rehn_page===sobhan














#win_forosh_et===emad


# اجرای برنامه
root.protocol("WM_DELETE_WINDOW",close_window)
option_file_frame.mainloop()
root.mainloop()

