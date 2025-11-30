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
#توابع اصلی

def save_rehn_maskkoni():#ذخیره پنجره راجاره مسکونی
    pass
def save_rehn_edari():#ذخیره پنجره راجاره اداری
    pass
def save_rehn_bagh():#ذخیره پنجره راجاره زمین و باغ
    pass
def save_forosh_bagh():# ذخیره پنجره فروش باغ و زمین 
    pass
def save_bz_option():
   pass
def open_option():
    option_file_frame.deiconify()
    ejareh_rehn_page.withdraw()
selected_trees=[]
def add_tree():# برای اضافه کردن درخت به صورت دستی
    t=type_tree_combo.get()
    if t and t not in selected_trees:
        selected_trees.append(t)
        label_result_add.config(text=','.join(selected_trees))
selected_option=[]
def add_option():
    op=option_bagh_combo.get()
    if op and op not in selected_option:
        selected_option.append(op)
        label_result2_add.config(text=','.join(selected_option))

def home_true_false1(): # برای فعال یا غیر فعال کردن ویجت های خونه باغ در اجاره
    if var0.get()==1:
        metraj_vila_bagh_entry.config(state="normal")
        year_vila_bagh_entry.config(state="normal")
        type_vila_combo.config(state="normal")
        toilet_bagh_combo.config(state="normal")
        hamam_bagh_combo.config(state="normal")
        sanad_bagh_combo.config(state="normal")
        option_bagh_combo.config(state="normal")
        javaz_bagh.config(state="normal")
        mohavate_bagh.config(state="normal")
    else:
        metraj_vila_bagh_entry.config(state="disabled")
        year_vila_bagh_entry.config(state="disabled")
        type_vila_combo.config(state="disabled")
        toilet_bagh_combo.config(state="disabled")
        hamam_bagh_combo.config(state="disabled")
        sanad_bagh_combo.config(state="disabled")
        option_bagh_combo.config(state="disabled")
        javaz_bagh.config(state="disabled")
        mohavate_bagh.config(state="disabled")
        
def home_true_false2(): #برای فعال یا غیر فعال کردن ویجت های خونه باغ در فروش
    if var0.get()==1:
        metraj_vila_forosh_bagh_entry.config(state="normal")
        year_vila_forosh_bagh_entry.config(state="normal")
        type_vila_forosh_bagh_combo.config(state="normal")
        toilet_forosh_bagh_combo.config(state="normal")
        hamam_forosh_bagh_combo.config(state="normal")
        sanad_forosh_bagh_combo.config(state="normal")
        option_forosh_bagh_combo.config(state="normal")
        javaz_forosh_bagh.config(state="normal")
        mohavate_forosh_bagh.config(state="normal")
    else:
        metraj_vila_forosh_bagh_entry.config(state="disabled")
        year_vila_forosh_bagh_entry.config(state="disabled")
        type_vila_forosh_bagh_combo.config(state="disabled")
        toilet_forosh_bagh_combo.config(state="disabled")
        hamam_forosh_bagh_combo.config(state="disabled")
        sanad_forosh_bagh_combo.config(state="disabled")
        option_forosh_bagh_combo.config(state="disabled")
        javaz_forosh_bagh.config(state="disabled")
        mohavate_forosh_bagh.config(state="disabled")


def add_tree2():
    # برای اضافه کردن درخت به صورت دستی در فروش
    pass
def add_option2():
    pass
    #برای اضافه کردن امکانات تفریحی به صورت دستی در فروش


        





#--------------------------------------------------------------------
def open_option2():
    option_file_frame_forosh_maskoni.deiconify()
    forosh_rehn_page.withdraw()

def open_option3():
    option_file_frame_ejareh_et.deiconify()
    ejareh_et.withdraw() 

def open_option4():
    option_file_frame_forosh_et.deiconify()
    forosh_et.withdraw()   

def open_option5():
    option_file_frame_ejareh_bz.deiconify()
    ejareh_bz.withdraw() 

def open_option6():
    option_file_frame_forosh_bz.deiconify()
    forosh_bz.withdraw() 

def back_to_buy_page():
    option_file_frame.withdraw()
    ejareh_rehn_page.deiconify()

def back_to_forosh_maskoni_page():
    option_file_frame_forosh_maskoni.withdraw()
    forosh_rehn_page.deiconify()

def back_to_ejareh_et():
    option_file_frame_ejareh_et.withdraw()
    ejareh_et.deiconify()

def back_to_forosh_et():
    option_file_frame_forosh_et.withdraw()
    forosh_et.deiconify()

def back_f_exit():
    box_forosh.withdraw()
    root.deiconify()

def back_rehn_e_exit():
    box_rehn_ejareh.withdraw()
    root.deiconify()

def back_home_ejareh_bagh():
    ejareh_bz.withdraw()
    root.deiconify()

def  back_to_ejareh_bz():
     option_file_frame_ejareh_bz.withdraw()
     ejareh_bz.deiconify()

def  back_to_forosh_bz():
     option_file_frame_forosh_bz.withdraw()
     forosh_bz.deiconify()
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
    box_rehn_ejareh.withdraw()
    ejareh_et.deiconify()  

def ejareh_bz():
    box_rehn_ejareh.withdraw()
    ejareh_bz.deiconify()  
def ejareh_sk():
    pass

def forosh_rehn_page():
    box_forosh.withdraw()
    forosh_rehn_page.deiconify() 

def forosh_et():
    box_forosh.withdraw()
    forosh_et.deiconify()

def forosh_bz():
    box_forosh.withdraw()
    forosh_bz.deiconify()  

def forosh_sk():
    pass

def change_bagh_zamin1(event):
    co=bagh_type2_combo.get()
    if co=="باغ":
        fram_option1_zamin.place_forget()
        fram_option1_bagh.place(x=60,y=60)
    else:
        fram_option1_bagh.place_forget()
        fram_option1_zamin.place(x=60,y=60)

def change_bagh_zamin_forosh_bagh(event):
    co=bagh_type2_forosh_bagh_combo.get()
    if co=="باغ":
        fram_option_forosh_zamin.place_forget()
        fram_option_forosh_bagh.place(x=60,y=60)
    else:
        fram_option_forosh_bagh.place_forget()
        fram_option_forosh_zamin.place(x=60,y=60)       
        


# لیست کشویی فیلد گزارش ها
def excel():
    pass
def gharardadeha():
    pass

#بازگشت های صفحات

def back_home_ejare_maskoni():
#main_page delete Entry and Combo
    entry_melk_Pricelimit.delete(0,tk.END)
    entry_melk_width_lable.delete(0,tk.END)
    entry_melk_area_lable.delete(0,tk.END)
    combo1.set("")
    combo2.set("")
#ejare_rehn_page delete Entry
    root.deiconify()
    ejareh_rehn_page.withdraw()
    year_ejare_maskoni_entry.delete(0,tk.END)
    addrres_ejare_maskoni_entry.delete(0,tk.END)
    floor_ejare_maskoni_entry.delete(0,tk.END)
    vahed_ejare_maskoni_entry.delete(0,tk.END)
    room_ejare_maskoni_entry.delete(0,tk.END)
    price_ejare_ejare_maskoni_entry.delete(0,tk.END)
    price_pish_ejare_maskoni_entry.delete(0,tk.END)
    
def back_home_forosh_maskoni():
#main_page delete Entry and Combo
    entry_melk_Pricelimit.delete(0,tk.END)
    entry_melk_width_lable.delete(0,tk.END)
    entry_melk_area_lable.delete(0,tk.END)
    combo1.set("")
    combo2.set("")
#forosh_rehn_page delete Entry
    root.deiconify()
    forosh_rehn_page.withdraw()
    year_forosh_maskoni_entry.delete(0,tk.END)
    addrres_forosh_maskoni_entry.delete(0,tk.END)
    floor_forosh_maskoni_entry.delete(0,tk.END)
    vahed_forosh_maskoni_entry.delete(0,tk.END)
    room_forosh_maskoni_entry.delete(0,tk.END)
    price_forosh_maskoni_entry.delete(0,tk.END)

def back_home_ejareh_et():
#main_page delete Entry and Combo
    entry_melk_Pricelimit.delete(0,tk.END)
    entry_melk_width_lable.delete(0,tk.END)
    entry_melk_area_lable.delete(0,tk.END)
    combo1.set("")
    combo2.set("")
    #ejareh_et_page delete Entry
    root.deiconify()
    ejareh_et.withdraw()
    year_ejareh_et_entry.delete(0,tk.END)
    addrres_ejareh_et_entry.delete(0,tk.END)
    floor_ejareh_et_entry.delete(0,tk.END)
    vahed_ejareh_et_entry.delete(0,tk.END)
    price_ejareh_et_entry.delete(0,tk.END) 

def back_home_forosh_et():
#main_page delete Entry and Combo
    entry_melk_Pricelimit.delete(0,tk.END)
    entry_melk_width_lable.delete(0,tk.END)
    entry_melk_area_lable.delete(0,tk.END)
    combo1.set("")
    combo2.set("")
#ejareh_et_page delete Entry
    root.deiconify()
    forosh_et.withdraw()
    year_forosh_et_entry.delete(0,tk.END)
    addrres_forosh_et_entry.delete(0,tk.END)
    floor_forosh_et_entry.delete(0,tk.END)
    vahed_forosh_et_entry.delete(0,tk.END)
    price_forosh_et_entry.delete(0,tk.END)

def back_home_forosh_bagh():
#main_page delete Entry and Combo
    entry_melk_Pricelimit.delete(0,tk.END)
    entry_melk_width_lable.delete(0,tk.END)
    entry_melk_area_lable.delete(0,tk.END)
    combo1.set("")
    combo2.set("")
#forosh_bz_page delete Entry
    forosh_bz.withdraw()
    root.deiconify()    
    metraj_zamin_forosh_bagh_entry.delete(0,tk.END)
    bagh_loctaion_forosh_bagh_entry.delete(0,tk.END)
    bagh_price_forosh_bagh_entry.delete(0,tk.END)
    bagh_price_forosh_bagh2_entry.delete(0,tk.END)
    metraj_tree_forosh_bagh_entry.delete(0,tk.END)
    tree_count_forosh_bagh_entry.delete(0,tk.END)
    metraj_vila_forosh_bagh_entry.delete(0,tk.END)
    year_vila_forosh_bagh_entry.delete(0,tk.END)



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
back_to_home_reh=tk.Button(box_rehn_ejareh,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_rehn_e_exit)
back_to_home_reh.place(x=290,y=110)

box_rehn_ejareh.protocol("WM_DELETE_WINDOW", lambda: None)
box_rehn_ejareh.resizable(False, False) 

file_button2= tk.Button(box_rehn_ejareh, text="ثبت", bg="#ffffff", relief="flat",width=20)
file_button2.place(x=140,y=60)

file_list_box2 = tk.Menu(box_rehn_ejareh, tearoff=0, font=("Arial", 12))
file_list_box2.add_command(label="اجاره مسکونی", command=ejareh_rehn_page)
file_list_box2.add_command(label="اجاره اداری/تجاری", command=ejareh_et) 
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

back_to_home_f=tk.Button(box_forosh,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_f_exit)
back_to_home_f.place(x=290,y=110)
box_forosh.protocol("WM_DELETE_WINDOW", lambda: None)
box_forosh.resizable(False, False) 

file_button3= tk.Button(box_forosh, text="ثبت", bg="#ffffff", relief="flat",width=20)
file_button3.place(x=140,y=60)

file_list_box3 = tk.Menu(box_forosh, tearoff=0, font=("Arial", 12))
file_list_box3.add_command(label="فروش مسکونی", command=forosh_rehn_page) 
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
rehn_page_frame1.place(x=450,y=40)


melktype_ejare_maskoni=tk.Label(rehn_page_frame1,text="نوع ملک",bg="#0F6E6E",fg="#ffffff",width=10)
melktype_ejare_maskoni.grid(padx=8,pady=15,sticky="e",row=0,column=1)

melk_type_rehn_maskoni=tk.Entry(rehn_page_frame1,text="اجاره مسکونی",bg="#C2C2C2", fg="#180202",font=("Arial", 10))
melk_type_rehn_maskoni.grid(padx=8, pady=15,row=0,column=0,sticky="w") 


year_ejare_maskoni=tk.Label(rehn_page_frame1,text="سال ساخت",bg="#0F6E6E",fg="#ffffff",width=10)
year_ejare_maskoni.grid(padx=8,pady=10,sticky="e",row=1,column=1)

year_ejare_maskoni_entry=tk.Entry(rehn_page_frame1,bg="#C2C2C2", fg="#180202",font=("Arial", 10))
year_ejare_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

addrres_buy=tk.Label(rehn_page_frame1,text="آدرس",bg="#0F6E6E",fg="#ffffff",width=10)
addrres_buy.grid(padx=8,pady=15,sticky="e",row=2,column=1)

addrres_ejare_maskoni_entry=tk.Entry(rehn_page_frame1,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
addrres_ejare_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

floor_ejare_maskoni=tk.Label(rehn_page_frame1,text="طبقه",bg="#0F6E6E",fg="#ffffff",width=10)
floor_ejare_maskoni.grid(padx=8,pady=15,sticky="e",row=3,column=1)

floor_ejare_maskoni_entry=tk.Entry(rehn_page_frame1,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
floor_ejare_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

vahed_ejare_maskoni=tk.Label(rehn_page_frame1,text="واحد",bg="#0F6E6E",fg="#ffffff",width=10)
vahed_ejare_maskoni.grid(padx=8,pady=15,sticky="e",row=4,column=1)

vahed_ejare_maskoni_entry=tk.Entry(rehn_page_frame1,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
vahed_ejare_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

room_ejare_maskoni=tk.Label(rehn_page_frame1,text="اتاق",bg="#0F6E6E",fg="#ffffff",width=10)
room_ejare_maskoni.grid(padx=8,pady=15,sticky="e",row=5,column=1)

room_ejare_maskoni_entry=tk.Entry(rehn_page_frame1,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
room_ejare_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=5,column=0)


price_ejare_ejare_maskoni=tk.Label(rehn_page_frame1,text="مبلغ اجاره",bg="#0F6E6E",fg="#ffffff",width=10)
price_ejare_ejare_maskoni.grid(padx=8,pady=15,sticky="e",row=7,column=0)

price_pish_ejare_maskoni=tk.Label(rehn_page_frame1,text="مبلغ پیش",bg="#0F6E6E",fg="#ffffff",width=10)
price_pish_ejare_maskoni.grid(padx=8,pady=15,sticky="e",row=7,column=1)

price_ejare_ejare_maskoni_entry=tk.Entry(rehn_page_frame1,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
price_ejare_ejare_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=8,column=0)

price_pish_ejare_maskoni_entry=tk.Entry(rehn_page_frame1,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
price_pish_ejare_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=8,column=1)

back_to_home=tk.Button(ejareh_rehn_page,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_ejare_maskoni)
back_to_home.place(x=320,y=520)

save_button_re_maskooni=tk.Button(ejareh_rehn_page,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_rehn_maskkoni)
save_button_re_maskooni.place(x=220,y=520)

photo_box_ejare_maskoni=tk.Frame(ejareh_rehn_page,width=410,height=450,background="#e4dde3")
photo_box_ejare_maskoni.place(x=30,y=40)
photo_lbl2_ejare_maskoni = tk.Label(photo_box_ejare_maskoni, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_ejare_maskoni.place(x=30,y=45)
add_img_btn_ejare_maskoni = tk.Button(photo_box_ejare_maskoni, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_ejare_maskoni.place(x=40,y=330)
#ساخت پنجره امکانات
option_frame_ejare_maskoni=tk.Frame(ejareh_rehn_page,width=300,height=30,background="#bbfbd1")
option_frame_ejare_maskoni.place(x=525,y=500)

option_label_ejare_maskoni=tk.Label(option_frame_ejare_maskoni,text='افزودن امکانات فایل',font=("B Nazanin",12,"bold"),background="#FFFFFF",fg="#000000")
option_label_ejare_maskoni.pack(side="right",padx=1)

button_label_ejare_maskoni=tk.Label(option_frame_ejare_maskoni)
button_label_ejare_maskoni.pack(side="left",padx=1)
plus_button_ejare_maskoni=tk.Button(option_frame_ejare_maskoni,image=plus,command=open_option,border=0)
plus_button_ejare_maskoni.pack()

option_frame1=tk.Frame(option_file_frame,width=400,height=100,background="#bbfbd1")
option_frame1.pack(padx=10,pady=15)

parking_ch_btn_ejare_maskoni=tk.Checkbutton(option_frame1,image=parking_pic,background="#022578")
parking_ch_btn_ejare_maskoni.pack(padx=15,side="left")

elvator_ch_btn_ejare_maskoni=tk.Checkbutton(option_frame1,image=elvator_pic,background="#022578")
elvator_ch_btn_ejare_maskoni.pack(padx=15,side="left")

warehouse_ch_btn_ejare_maskoni=tk.Checkbutton(option_frame1,image=warehouse_pic,background="#022578")
warehouse_ch_btn_ejare_maskoni.pack(padx=15,side="right")

option_frame2=tk.Frame(option_file_frame,width=400,height=400,background="#bbfbd1",border=1)
option_frame2.pack(padx=10,pady=15)

#balcon_ch_btn=tk.Checkbutton(option_frame2,text="تراس")

sarmaesh_ejare_maskoni=tk.Label(option_frame2,text="سرمایش",background="#025578",fg="#ffffff")
sarmaesh_ejare_maskoni.grid(row=0,column=1,padx=15,pady=5)
sarmaesh_ejare_maskoni_combo=ttk.Combobox(option_frame2)
sarmaesh_ejare_maskoni_combo["values"] = ("ندارد","پنکه سقفی","کولر ابی","کولر گازی ","ابی/گازی")
sarmaesh_ejare_maskoni_combo.grid(row=0,column=0,padx=15,pady=5)

garmaesh_ejare_maskoni=tk.Label(option_frame2,text="گرمایش",background="#025578",fg="#ffffff")
garmaesh_ejare_maskoni.grid(row=1,column=1,padx=15,pady=5)
garmaesh_ejare_maskoni_combo=ttk.Combobox(option_frame2)
garmaesh_ejare_maskoni_combo["values"] = ("ندارد","بخاری"," شوفاژ","گرمایش از کف ")
garmaesh_ejare_maskoni_combo.grid(row=1,column=0,padx=15,pady=5)

kaf_ejare_maskoni=tk.Label(option_frame2,text="کف",background="#025578",fg="#ffffff")
kaf_ejare_maskoni.grid(row=2,column=1,padx=15,pady=5)
kaf_ejare_maskoni_combo=ttk.Combobox(option_frame2)
kaf_ejare_maskoni_combo["values"] = ("سرامیک","موزاییک","پارکت")
kaf_ejare_maskoni_combo.grid(row=2,column=0,padx=15,pady=5)

toilet_ejare_maskoni=tk.Label(option_frame2,text="سرویس بهداشتی",background="#025578",fg="#ffffff")
toilet_ejare_maskoni.grid(row=3,column=1,padx=5,pady=5)
toilet_ejare_maskoni_combo=ttk.Combobox(option_frame2)
toilet_ejare_maskoni_combo["values"] = ("ایرانی","فرنگی","هردو")
toilet_ejare_maskoni_combo.grid(row=3,column=0,padx=15,pady=5)

save_optoin1=tk.Button(option_file_frame,text="ذخیره",command=None,background="#079BDB",fg="#ffffff",width=8)
save_optoin1.place(x=170,y=330)

back_to_ejare_maskoni=tk.Button(option_file_frame,text="بازگشت",command=back_to_buy_page,background="#079BDB",fg="#ffffff",width=8)
back_to_ejare_maskoni.place(x=95,y=330)


#==========WINS_BOX3_REHN_EJAREH======================
#win_ejareh_et

ejareh_et = tk.Toplevel(root)
ejareh_et.title("رهن و اجاره اداری / تجاری")
ejareh_et.geometry("800x600")
ejareh_et.withdraw()
ejareh_et.configure(bg="#0F6E6E")

#option_file
option_file_frame_ejareh_et=tk.Toplevel(ejareh_et,background="#bbfbd1" )
option_file_frame_ejareh_et.title(" ")
option_file_frame_ejareh_et.geometry("500x370")
option_file_frame_ejareh_et.pack_propagate(False)
option_file_frame_ejareh_et.withdraw()

rehn_page_frame3=tk.Frame(ejareh_et,width=490,height=800,bg="#5d6059",border=2)
rehn_page_frame3.place(x=500,y=50)

melktype_ejareh_et=tk.Label(rehn_page_frame3,text="متراژ ملک ",bg="#0F6E6E",fg="#ffffff",width=10)
melktype_ejareh_et.grid(padx=8,pady=15,sticky="e",row=0,column=1)

melk_type_rehn_et=tk.Entry(rehn_page_frame3,bg="#C2C2C2", fg="#180202",font=("Arial", 10))
melk_type_rehn_et.grid(padx=8, pady=15,sticky="w",row=0,column=0) 

year_ejareh_et=tk.Label(rehn_page_frame3,text="سال ساخت",bg="#0F6E6E",fg="#ffffff",width=10)
year_ejareh_et.grid(padx=8,pady=10,sticky="e",row=1,column=1)

year_ejareh_et_entry=tk.Entry(rehn_page_frame3,bg="#C2C2C2", fg="#180202",font=("Arial", 10))
year_ejareh_et_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

addrres_ejareh_et=tk.Label(rehn_page_frame3,text="آدرس",bg="#0F6E6E",fg="#ffffff",width=10)
addrres_ejareh_et.grid(padx=8,pady=15,sticky="e",row=2,column=1)

addrres_ejareh_et_entry=tk.Entry(rehn_page_frame3,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
addrres_ejareh_et_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)
floor_ejareh_et=tk.Label(rehn_page_frame3,text="طبقه",bg="#0F6E6E",fg="#ffffff",width=10)
floor_ejareh_et.grid(padx=8,pady=15,sticky="e",row=3,column=1)

floor_ejareh_et_entry=tk.Entry(rehn_page_frame3,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
floor_ejareh_et_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

vahed_ejareh_et=tk.Label(rehn_page_frame3,text="واحد",bg="#0F6E6E",fg="#ffffff",width=10)
vahed_ejareh_et.grid(padx=8,pady=15,sticky="e",row=4,column=1)

vahed_ejareh_et_entry=tk.Entry(rehn_page_frame3,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
vahed_ejareh_et_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)


price_ejareh_et=tk.Label(rehn_page_frame3,text="مبلغ ودیعه",bg="#0F6E6E",fg="#ffffff",width=10)
price_ejareh_et.grid(padx=8,pady=15,sticky="e",row=5,column=1)

price_ejareh_et_entry=tk.Entry(rehn_page_frame3,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
price_ejareh_et_entry.grid(padx=8,pady=15,sticky="w",row=5,column=0)

Monthly_fee_ejareh_et=tk.Label(rehn_page_frame3,text=" مبلغ اجاره",bg="#0F6E6E",fg="#ffffff",width=10)
Monthly_fee_ejareh_et.grid(padx=8,pady=15,sticky="e",row=6,column=1)

Monthly_fee_ejareh_et_entry=tk.Entry(rehn_page_frame3,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
Monthly_fee_ejareh_et_entry.grid(padx=8,pady=15,sticky="w",row=6,column=0)

Full_mortgage_ejareh_et=tk.Label(rehn_page_frame3,text=" رهن کامل؟ ",bg="#0F6E6E",fg="#ffffff",width=10)
Full_mortgage_ejareh_et.grid(padx=8,pady=15,sticky="e",row=7,column=1)

Full_mortgage_ch_btn_ejareh_et=tk.Checkbutton(rehn_page_frame3,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
Full_mortgage_ch_btn_ejareh_et.grid(padx=8,pady=15,sticky="w",row=7,column=0)

back_to_home=tk.Button(ejareh_et,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_ejareh_et)
back_to_home.place(x=650,y=535)

save_button_re_edari=tk.Button(ejareh_et,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_rehn_edari)
save_button_re_edari.place(x=550,y=532)



photo_box_ejareh_et=tk.Frame(ejareh_et,width=410,height=450,background="#e4dde3")
photo_box_ejareh_et.place(x=40,y=40)
photo_lbl2_ejareh_et = tk.Label(photo_box_ejareh_et, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_ejareh_et.place(x=30,y=45)
add_img_btn_ejareh_et = tk.Button(photo_box_ejareh_et, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_ejareh_et.place(x=40,y=330)

# (ejareh_et)  ===>> ساخت پنجره امکانات (رهن و اجاره اداری/تجاری)

option_frame_ejareh_et=tk.Frame(ejareh_et,width=300,height=30,background="#bbfbd1")
option_frame_ejareh_et.place(x=520,y=475)

option_label_ejareh_et=tk.Label(option_frame_ejareh_et,text='افزودن امکانات فایل',font=("B Nazanin",12,"bold"),background="#FFFFFF",fg="#000000")
option_label_ejareh_et.pack(side="right",padx=1)

button_label_ejareh_et=tk.Label(option_frame_ejareh_et)
button_label_ejareh_et.pack(side="left",padx=1)
plus_button_ejareh_et=tk.Button(option_frame_ejareh_et,image=plus,command=open_option3,border=0)
plus_button_ejareh_et.pack()

option_frame6=tk.Frame(option_file_frame_ejareh_et,width=400,height=100,background="#bbfbd1")
option_frame6.pack(padx=10,pady=15)

parking_ch_btn_forosh_maskoni=tk.Checkbutton(option_frame6,image=parking_pic,background="#022578")
parking_ch_btn_forosh_maskoni.pack(padx=15,side="left")

elvator_ch_btn_forosh_maskoni=tk.Checkbutton(option_frame6,image=elvator_pic,background="#022578")
elvator_ch_btn_forosh_maskoni.pack(padx=15,side="left")

warehouse_ch_btn_forosh_maskoni=tk.Checkbutton(option_frame6,image=warehouse_pic,background="#022578")
warehouse_ch_btn_forosh_maskoni.pack(padx=15,side="right")

option_frame7=tk.Frame(option_file_frame_ejareh_et,width=400,height=400,background="#bbfbd1",border=1)
option_frame7.pack(padx=10,pady=15)


aab_va_gaz_emkanat_ejareh_et=tk.Label(option_frame7,text="وضعیت آب و گاز",background="#0F6E6E",fg="#ffffff",width=17)
aab_va_gaz_emkanat_ejareh_et.grid(padx=8,pady=15,row=0,column=1)

aab_va_gaz_combo_emkanat_ejareh_et=ttk.Combobox(option_frame7)
aab_va_gaz_combo_emkanat_ejareh_et["values"] = ("فقط گاز دارد","فقط آب دارد","آب و گاز دارد")
aab_va_gaz_combo_emkanat_ejareh_et.grid(padx=8,pady=15,row=0,column=0)

sarmayesh_emkanat_ejareh_et=tk.Label(option_frame7,text="سیستم سرمایش",background="#0F6E6E",fg="#ffffff",width=17)
sarmayesh_emkanat_ejareh_et.grid(padx=8,pady=15,row=4,column=1)

sarmayesh_combo_emkanat_ejareh_et=ttk.Combobox(option_frame7)
sarmayesh_combo_emkanat_ejareh_et["values"] = (" کولر گازی"," کولرآبی","پنکه سقفی","ندارد")
sarmayesh_combo_emkanat_ejareh_et.grid(padx=8,pady=15,row=4,column=0)

garmayesh_emkanat_ejareh_et=tk.Label(option_frame7,text="سیستم گرمایش",background="#0F6E6E",fg="#ffffff",width=17)
garmayesh_emkanat_ejareh_et.grid(padx=8,pady=15,row=5,column=1)

garmayesh_combo_emkanat_ejareh_et=ttk.Combobox(option_frame7)
garmayesh_combo_emkanat_ejareh_et["values"] = (" شوفاژ"," بخاری","ندارد")
garmayesh_combo_emkanat_ejareh_et.grid(padx=8,pady=15,row=5,column=0)

save_optoin3=tk.Button(option_file_frame_ejareh_et,text="ذخیره",command=None,background="#079BDB",fg="#ffffff",width=8)
save_optoin3.place(x=170,y=330)

back_to_home_ejareh_et=tk.Button(option_file_frame_ejareh_et,text="بازگشت",command=back_to_ejareh_et,background="#079BDB",fg="#ffffff",width=8)
back_to_home_ejareh_et.place(x=95,y=330)


#win_ejareh_bagh_zamin
ejareh_bz = tk.Toplevel(root)
ejareh_bz.title(" اجاره باغ و زمین")
ejareh_bz.geometry("800x600")
ejareh_bz.withdraw()
ejareh_bz.configure(bg="#0F6E6E")

ejareh_bagh_frame=tk.Frame(ejareh_bz,width=490,height=800,bg="#5d6059",border=2)
ejareh_bagh_frame.place(x=500,y=90)

metraj_zamin=tk.Label(ejareh_bagh_frame,text="متراژ",bg="#0F6E6E",fg="#ffffff",width=10)
metraj_zamin.grid(padx=8,pady=15,sticky="e",row=0,column=1)

metraj_zamin_entry=tk.Entry(ejareh_bagh_frame,bg="#C2C2C2", fg="#180202",font=("Arial", 10),textvariable="متر مربع")
metraj_zamin_entry.grid(padx=8,pady=15,sticky="w",row=0,column=0)

bagh_type=tk.Label(ejareh_bagh_frame,text="کاربری زمین",bg="#0F6E6E",fg="#ffffff",width=10)
bagh_type.grid(padx=8,pady=15,sticky="e",row=1,column=1)

bagh_type_combo=ttk.Combobox(ejareh_bagh_frame,state="readonly")
bagh_type_combo["values"]=("باغ","زمین کشاورزی")
bagh_type_combo.set("باغ")
bagh_type_combo.grid(padx=8,pady=15,sticky="w",row=1,column=0)

bagh_loctaion=tk.Label(ejareh_bagh_frame,text="منطقه و ادرس ",bg="#0F6E6E",fg="#ffffff",width=10)
bagh_loctaion.grid(padx=8,pady=15,sticky="e",row=2,column=1)

bagh_loctaion_entry=tk.Entry(ejareh_bagh_frame,bg="#C2C2C2", fg="#180202",font=("Arial", 10))
bagh_loctaion_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

bagh_price_ejareh=tk.Label(ejareh_bagh_frame,text='ودیعه',bg="#0F6E6E",fg="#ffffff",width=10)
bagh_price_ejareh.grid(padx=8,pady=15,sticky="e",row=3,column=1)

bagh_price_ejareh_ent=tk.Entry(ejareh_bagh_frame,bg="#C2C2C2", fg="#180202",font=("Arial", 10))
bagh_price_ejareh_ent.grid(padx=8,pady=15,sticky="w",row=3,column=0)

bagh_price_ejareh2=tk.Label(ejareh_bagh_frame,text='قیمت هر متر',bg="#0F6E6E",fg="#ffffff",width=10)
bagh_price_ejareh2.grid(padx=8,pady=15,sticky="e",row=4,column=1)

bagh_price_ejareh2_ent=tk.Entry(ejareh_bagh_frame,bg="#C2C2C2", fg="#180202",font=("Arial", 10))
bagh_price_ejareh2_ent.grid(padx=8,pady=15,sticky="w",row=4,column=0)

time_bagh_ejareh=tk.Label(ejareh_bagh_frame,text="مدت اجاره",bg="#0F6E6E",fg="#ffffff",width=10)
time_bagh_ejareh.grid(padx=8,pady=15,sticky="e",row=5,column=1)

bagh_time_combo=ttk.Combobox(ejareh_bagh_frame,state="readonly")
bagh_time_combo["values"]=("بلندمدت","کوتاه مدت","فصلی","سالانه")
bagh_time_combo.set("فصلی")
bagh_time_combo.grid(padx=8,pady=15,sticky="w",row=5,column=0)

photo_box_ejareh_bagh=tk.Frame(ejareh_bz,width=410,height=450,background="#e4dde3")
photo_box_ejareh_bagh.place(x=50,y=40)

photo_lbl2_ejareh_bagh = tk.Label(photo_box_ejareh_bagh, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_ejareh_bagh.place(x=30,y=45)
add_img_btn_ejareh_bagh = tk.Button(photo_box_ejareh_bagh, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_ejareh_bagh.place(x=40,y=330)

back_to_home_bagh=tk.Button(ejareh_bz,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_ejareh_bagh)
back_to_home_bagh.place(x=320,y=520)

save_button_re_bagh=tk.Button(ejareh_bz,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_rehn_bagh)
save_button_re_bagh.place(x=220,y=520)

# (ejareh_et)  ===>> ساخت پنجره امکانات (باغ)

option_frame_ejareh_bz=tk.Frame(ejareh_bz,width=300,height=30,background="#bbfbd1")
option_frame_ejareh_bz.place(x=550,y=450)

option_label_ejareh_bz=tk.Label(option_frame_ejareh_bz,text='افزودن امکانات فایل',font=("B Nazanin",12,"bold"),background="#FFFFFF",fg="#000000")
option_label_ejareh_bz.pack(side="right",padx=1)

button_label_ejareh_bz=tk.Label(option_frame_ejareh_et)
button_label_ejareh_bz.pack(side="left",padx=1)
plus_button_ejareh_bz=tk.Button(option_frame_ejareh_bz,image=plus,command=open_option5,border=0)
plus_button_ejareh_bz.pack()

option_file_frame_ejareh_bz=tk.Toplevel(ejareh_bz,background="#bbfbd1")
option_file_frame_ejareh_bz.title(" ")
option_file_frame_ejareh_bz.geometry("640x630")
option_file_frame_ejareh_bz.pack_propagate(False)
option_file_frame_ejareh_bz.withdraw()
mini_frame=tk.Frame(option_file_frame_ejareh_bz)
mini_frame.place(x=290,y=20)
bagh_type2=tk.Label(mini_frame,text="کاربری زمین",bg="#0F6E6E",fg="#ffffff",width=10)
bagh_type2.pack(padx=5,pady=5,side="right")

bagh_type2_combo=ttk.Combobox(mini_frame,state="readonly")
bagh_type2_combo["values"]=("باغ","زمین کشاورزی")
bagh_type2_combo.set("باغ")
bagh_type2_combo.pack(padx=5,pady=5,side="left")

bagh_type2_combo.bind("<<ComboboxSelected>>",change_bagh_zamin1)

fram_option1_bagh=tk.Frame(option_file_frame_ejareh_bz,width=430,height=290,background="#d1e0df")
fram_option1_bagh.place(x=60,y=60)

metraj_tree=tk.Label(fram_option1_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="متراژ درخت کاری")
metraj_tree.grid(padx=10,pady=5,row=0,column=4)

metraj_tree_entry=tk.Entry(fram_option1_bagh,width=10,bg="#746f6f",fg="#ffffff")
metraj_tree_entry.grid(padx=10,pady=5,row=0,column=3)

tree_count=tk.Label(fram_option1_bagh,bg="#0F6E6E",fg="#ffffff",width=10,text="تعداد درخت")
tree_count.grid(padx=10,pady=5,row=1,column=4)

tree_count_entry=tk.Entry(fram_option1_bagh,width=10,bg="#746f6f",fg="#ffffff")
tree_count_entry.grid(padx=10,pady=5,row=1,column=3)

abyari=tk.Label(fram_option1_bagh,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع ابیاری")
abyari.grid(padx=10,pady=5,row=2,column=4)

abyari_combo=ttk.Combobox(fram_option1_bagh)
abyari_combo["values"]=("سطحی","بارانی","قطره ای","تحت فشار")
abyari_combo.set("سطحی")
abyari_combo.grid(padx=10,pady=5,row=2,column=3)

type_tree=tk.Label(fram_option1_bagh,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع درخت")
type_tree.grid(padx=10,pady=5,row=3,column=4)

type_tree_combo=ttk.Combobox(fram_option1_bagh)
type_tree_combo["values"]=(" ","پسته","بادام","گردو","شلیل","هلو","سیب","انگور"
                           ,"انجیر","زردالو","گیلاس","البالو")
type_tree_combo.set("گردو")
type_tree_combo.grid(padx=10,pady=5,row=3,column=3)
add_tree_button=tk.Button(fram_option1_bagh,text="افزودن درخت",command=add_tree,bg="#007acc",width=10)
add_tree_button.grid(padx=10,pady=5,row=4,column=4)

label_result_add=tk.Label(fram_option1_bagh,text="")
label_result_add.grid(padx=10,pady=5,row=4,column=3)

chah_bagh=tk.Checkbutton(fram_option1_bagh,text="چاه",background="#d6d0d0")
chah_bagh.grid(padx=0,pady=5,row=5,column=0)

estakhr_bagh=tk.Checkbutton(fram_option1_bagh,text="استخر",background="#d6d0d0")
estakhr_bagh.grid(padx=0,pady=5,row=5,column=1)

loleh_bagh=tk.Checkbutton(fram_option1_bagh,text="اب لوله کشی",background="#d6d0d0")
loleh_bagh.grid(padx=0,pady=5,row=5,column=2)

bargh_bagh=tk.Checkbutton(fram_option1_bagh,text="برق کشی",background="#d6d0d0")
bargh_bagh.grid(padx=0,pady=5,row=5,column=3)

gas_bagh=tk.Checkbutton(fram_option1_bagh,text="گاز کشی",background="#d6d0d0")
gas_bagh.grid(padx=0,pady=5,row=5,column=4)

var0=tk.IntVar(value=0)#چک باتن پیش فرض تیک نخورده باشه


room_bagh_ch=tk.Checkbutton(fram_option1_bagh,variable=var0,image=warehouse_pic,background="#022578",text="ساختمان",command=home_true_false1)
room_bagh_ch.grid(padx=10,pady=5,row=6,column=4)

metraj_vila_bagh=tk.Label(fram_option1_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="متراژ سازه")
metraj_vila_bagh.grid(padx=10,pady=5,row=7,column=4)

metraj_vila_bagh_entry=tk.Entry(fram_option1_bagh,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
metraj_vila_bagh_entry.grid(padx=10,pady=5,row=7,column=3)

year_vila_bagh=tk.Label(fram_option1_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="سال ساخت")
year_vila_bagh.grid(padx=10,pady=5,row=8,column=4)

year_vila_bagh_entry=tk.Entry(fram_option1_bagh,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
year_vila_bagh_entry.grid(padx=10,pady=5,row=8,column=3)

type_vila_bagh=tk.Label(fram_option1_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="نوع سازه")
type_vila_bagh.grid(padx=10,pady=5,row=9,column=4)

type_vila_combo=ttk.Combobox(fram_option1_bagh,state="disabled")
type_vila_combo["values"]=("آجری","بلوکی","کانکس","چوبی")
type_vila_combo.set("آجری")
type_vila_combo.grid(padx=10,pady=5,row=9,column=3)

toilet_bagh=tk.Label(fram_option1_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="سرویس بهداشتی")
toilet_bagh.grid(padx=10,pady=5,row=10,column=4)

toilet_bagh_combo=ttk.Combobox(fram_option1_bagh,state="disabled")
toilet_bagh_combo["values"]=(" ","ندارد","فرنگی","ایرانی","هردو")
toilet_bagh_combo.set("")
toilet_bagh_combo.grid(padx=10,pady=5,row=10,column=3)

hamam_bagh=tk.Label(fram_option1_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="حمام")
hamam_bagh.grid(padx=10,pady=5,row=11,column=4)

hamam_bagh_combo=ttk.Combobox(fram_option1_bagh,state="disabled")
hamam_bagh_combo["values"]=(" ","ندارد","دارد")
hamam_bagh_combo.set(" ")
hamam_bagh_combo.grid(padx=10,pady=5,row=11,column=3)

sanad_bagh=tk.Label(fram_option1_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="سند")
sanad_bagh.grid(padx=10,pady=5,row=12,column=4)

sanad_bagh_combo=ttk.Combobox(fram_option1_bagh,state="disabled")
sanad_bagh_combo["values"]=(" ","ندارد","تک برگ","قولنامه ای","مشاع")
sanad_bagh_combo.set(" ")
sanad_bagh_combo.grid(padx=10,pady=5,row=12,column=3)

option_bagh=tk.Label(fram_option1_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="امکانات تفریحی")
option_bagh.grid(padx=10,pady=5,row=13,column=4)

option_bagh_combo=ttk.Combobox(fram_option1_bagh,state="disabled")
option_bagh_combo["values"]=(" ","استخر","جکوزی","باربیکیو")
option_bagh_combo.set(" ")
option_bagh_combo.grid(padx=10,pady=5,row=13,column=3)
add_option_button=tk.Button(fram_option1_bagh,text="افزودن امکانات",command=add_option,bg="#007acc",width=10)
add_option_button.grid(padx=10,pady=5,row=13,column=2)
label_result2_add=tk.Label(fram_option1_bagh,text="")
label_result2_add.grid(padx=10,pady=5,row=13,column=1)

javaz_bagh=tk.Checkbutton(fram_option1_bagh,text="مجوز ساختن",background="#d6d0d0",state="disabled")
javaz_bagh.grid(padx=10,pady=5,row=14,column=4)

mohavate_bagh=tk.Checkbutton(fram_option1_bagh,text="محوطه سازی",background="#d6d0d0",state="disabled")
mohavate_bagh.grid(padx=10,pady=5,row=14,column=3)

divar_bagh=tk.Checkbutton(fram_option1_bagh,text="دیوار کشی",background="#d6d0d0")
divar_bagh.grid(padx=10,pady=5,row=14,column=2)

save_button_bz_option=tk.Button(option_file_frame_ejareh_bz,text="ذخیره",command=save_bz_option,background="#079BDB",fg="#ffffff",width=8)
save_button_bz_option.place(x=170,y=580)

back_to_ejareh_bz=tk.Button(option_file_frame_ejareh_bz,text="بازگشت",command=back_to_ejareh_bz,background="#079BDB",fg="#ffffff",width=8)
back_to_ejareh_bz.place(x=95,y=580)

#zamin_frame_option_ejareh

fram_option1_zamin=tk.Frame(option_file_frame_ejareh_bz,width=430,height=290,background="#d1e0df")
fram_option1_zamin.place_forget()


#==========WINS_BOX2_FOROSH==================
#win_forosh_rehn_page

forosh_rehn_page = tk.Toplevel(root)
forosh_rehn_page.title("فروش مسکونی")
forosh_rehn_page.geometry("800x600")
forosh_rehn_page.withdraw()
forosh_rehn_page.configure(bg="#0F6E6E")

#option_file === (Forosh_rehn_page)
option_file_frame_forosh_maskoni=tk.Toplevel(forosh_rehn_page,background="#bbfbd1" )
option_file_frame_forosh_maskoni.title(" ")
option_file_frame_forosh_maskoni.geometry("500x370")
option_file_frame_forosh_maskoni.pack_propagate(False)
option_file_frame_forosh_maskoni.withdraw()



rehn_page_frame2=tk.Frame(forosh_rehn_page,width=490,height=800,bg="#5d6059",border=2)
rehn_page_frame2.place(x=500,y=50)


melktype_forosh_maskoni=tk.Label(rehn_page_frame2,text="نوع ملک",bg="#0F6E6E",fg="#ffffff",width=10)
melktype_forosh_maskoni.grid(padx=8,pady=15,sticky="e",row=0,column=1)

melk_type_forosh_maskoni=tk.Entry(rehn_page_frame2,text="فروش مسکونی",bg="#C2C2C2", fg="#180202",font=("Arial", 10))
melk_type_forosh_maskoni.grid(padx=8, pady=15,row=0,column=0,sticky="w") 


year_forosh_maskoni=tk.Label(rehn_page_frame2,text="سال ساخت",bg="#0F6E6E",fg="#ffffff",width=10)
year_forosh_maskoni.grid(padx=8,pady=10,sticky="e",row=1,column=1)

year_forosh_maskoni_entry=tk.Entry(rehn_page_frame2,bg="#C2C2C2", fg="#180202",font=("Arial", 10))
year_forosh_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

addrres_forosh_maskoni=tk.Label(rehn_page_frame2,text="آدرس",bg="#0F6E6E",fg="#ffffff",width=10)
addrres_forosh_maskoni.grid(padx=8,pady=15,sticky="e",row=2,column=1)

addrres_forosh_maskoni_entry=tk.Entry(rehn_page_frame2,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
addrres_forosh_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

floor_forosh_maskoni=tk.Label(rehn_page_frame2,text="طبقه",bg="#0F6E6E",fg="#ffffff",width=10)
floor_forosh_maskoni.grid(padx=8,pady=15,sticky="e",row=3,column=1)

floor_forosh_maskoni_entry=tk.Entry(rehn_page_frame2,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
floor_forosh_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

vahed_forosh_maskoni=tk.Label(rehn_page_frame2,text="واحد",bg="#0F6E6E",fg="#ffffff",width=10)
vahed_forosh_maskoni.grid(padx=8,pady=15,sticky="e",row=4,column=1)

vahed_forosh_maskoni_entry=tk.Entry(rehn_page_frame2,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
vahed_forosh_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

room_forosh_maskoni=tk.Label(rehn_page_frame2,text="اتاق",bg="#0F6E6E",fg="#ffffff",width=10)
room_forosh_maskoni.grid(padx=8,pady=15,sticky="e",row=5,column=1)

room_forosh_maskoni_entry=tk.Entry(rehn_page_frame2,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
room_forosh_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=5,column=0)

price_forosh_maskoni=tk.Label(rehn_page_frame2,text="قیمت",bg="#0F6E6E",fg="#ffffff",width=10)
price_forosh_maskoni.grid(padx=8,pady=15,sticky="e",row=6,column=1)

price_forosh_maskoni_entry=tk.Entry(rehn_page_frame2,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
price_forosh_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=6,column=0)

back_to_home_forosh_maskoni=tk.Button(forosh_rehn_page,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_forosh_maskoni)
back_to_home_forosh_maskoni.place(x=650,y=535)

photo_box_forosh_maskoni=tk.Frame(forosh_rehn_page,width=410,height=450,background="#e4dde3")
photo_box_forosh_maskoni.place(x=40,y=40)
photo_lbl2_forosh_maskoni = tk.Label(photo_box_forosh_maskoni, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_forosh_maskoni.place(x=30,y=45)
add_img_btn_forosh_maskoni = tk.Button(photo_box_forosh_maskoni, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_forosh_maskoni.place(x=40,y=330)

# (Forosh_rehn_page) === ساخت پنجره امکانات 

option_frame3=tk.Frame(forosh_rehn_page,width=300,height=30,background="#bbfbd1")
option_frame3.place(x=520,y=460)

option_label_forosh_maskoni=tk.Label(option_frame3,text='افزودن امکانات فایل',font=("B Nazanin",12,"bold"),background="#FFFFFF",fg="#000000")
option_label_forosh_maskoni.pack(side="right",padx=1)

button_label_forosh_maskoni=tk.Label(option_frame3)
button_label_forosh_maskoni.pack(side="left",padx=1)
plus_button_forosh_maskoni=tk.Button(option_frame3,image=plus,command=open_option2,border=0)
plus_button_forosh_maskoni.pack()

option_frame4=tk.Frame(option_file_frame_forosh_maskoni,width=400,height=100,background="#bbfbd1")
option_frame4.pack(padx=10,pady=15)

parking_ch_btn_forosh_maskoni=tk.Checkbutton(option_frame4,image=parking_pic,background="#022578")
parking_ch_btn_forosh_maskoni.pack(padx=15,side="left")

elvator_ch_btn_forosh_maskoni=tk.Checkbutton(option_frame4,image=elvator_pic,background="#022578")
elvator_ch_btn_forosh_maskoni.pack(padx=15,side="left")

warehouse_ch_btn_forosh_maskoni=tk.Checkbutton(option_frame4,image=warehouse_pic,background="#022578")
warehouse_ch_btn_forosh_maskoni.pack(padx=15,side="right")

option_frame5=tk.Frame(option_file_frame_forosh_maskoni,width=400,height=400,background="#bbfbd1",border=1)
option_frame5.pack(padx=10,pady=15)

#balcon_ch_btn=tk.Checkbutton === (Forosh_rehn_page)(option_frame2,text="تراس")

sarmaesh_forosh_maskoni=tk.Label(option_frame5,text="سرمایش",background="#025578",fg="#ffffff")
sarmaesh_forosh_maskoni.grid(row=0,column=1,padx=15,pady=5)
sarmaesh_combo_forosh_maskoni=ttk.Combobox(option_frame5)
sarmaesh_combo_forosh_maskoni["values"] = ("ندارد","پنکه سقفی","کولر ابی","کولر گازی ","ابی/گازی")
sarmaesh_combo_forosh_maskoni.grid(row=0,column=0,padx=15,pady=5)

garmaesh_forosh_maskoni=tk.Label(option_frame5,text="گرمایش",background="#025578",fg="#ffffff")
garmaesh_forosh_maskoni.grid(row=1,column=1,padx=15,pady=5)
garmaesh_combo_forosh_maskoni=ttk.Combobox(option_frame5)
garmaesh_combo_forosh_maskoni["values"] = ("ندارد","بخاری"," شوفاژ","گرمایش از کف ")
garmaesh_combo_forosh_maskoni.grid(row=1,column=0,padx=15,pady=5)

kaf_forosh_maskoni=tk.Label(option_frame5,text="کف",background="#025578",fg="#ffffff")
kaf_forosh_maskoni.grid(row=2,column=1,padx=15,pady=5)
kaf_combo_forosh_maskoni=ttk.Combobox(option_frame5)
kaf_combo_forosh_maskoni["values"] = ("سرامیک","موزاییک","پارکت")
kaf_combo_forosh_maskoni.grid(row=2,column=0,padx=15,pady=5)
toilet_forosh_maskoni=tk.Label(option_frame5,text="سرویس بهداشتی",background="#025578",fg="#ffffff")
toilet_forosh_maskoni.grid(row=3,column=1,padx=5,pady=5)
toilet_combo_forosh_maskoni=ttk.Combobox(option_frame5)
toilet_combo_forosh_maskoni["values"] = ("ایرانی","فرنگی","هردو")
toilet_combo_forosh_maskoni.grid(row=3,column=0,padx=15,pady=5)

save_optoin2=tk.Button(option_file_frame_forosh_maskoni,text="ذخیره",command=None,background="#079BDB",fg="#ffffff",width=8)
save_optoin2.place(x=170,y=330)

back_to_home_forosh_maskoni=tk.Button(option_file_frame_forosh_maskoni,text="بازگشت",command=back_to_forosh_maskoni_page,background="#079BDB",fg="#ffffff",width=8)
back_to_home_forosh_maskoni.place(x=95,y=330)

#win_forosh_et===emad

forosh_et = tk.Toplevel(root)
forosh_et.title(" فروش اداری / تجاری")
forosh_et.geometry("800x600")
forosh_et.withdraw()
forosh_et.configure(bg="#0F6E6E")

# option_file forosh_et

option_file_frame_forosh_et=tk.Toplevel(forosh_et,background="#bbfbd1" )
option_file_frame_forosh_et.title(" ")
option_file_frame_forosh_et.geometry("500x370")
option_file_frame_forosh_et.pack_propagate(False)
option_file_frame_forosh_et.withdraw()

rehn_page_frame8=tk.Frame(forosh_et,width=490,height=800,bg="#5d6059",border=2)
rehn_page_frame8.place(x=500,y=50)

melktype_forosh_et=tk.Label(rehn_page_frame8,text="متراژ ملک ",bg="#0F6E6E",fg="#ffffff",width=10)
melktype_forosh_et.grid(padx=8,pady=15,sticky="e",row=0,column=1)

melk_type_rehn_et=tk.Entry(rehn_page_frame8,bg="#C2C2C2", fg="#180202",font=("Arial", 10))
melk_type_rehn_et.grid(padx=8, pady=15,sticky="w",row=0,column=0) 

year_forosh_et=tk.Label(rehn_page_frame8,text="سال ساخت",bg="#0F6E6E",fg="#ffffff",width=10)
year_forosh_et.grid(padx=8,pady=10,sticky="e",row=1,column=1)

year_forosh_et_entry=tk.Entry(rehn_page_frame8,bg="#C2C2C2", fg="#180202",font=("Arial", 10))
year_forosh_et_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

addrres_forosh_et=tk.Label(rehn_page_frame8,text="آدرس",bg="#0F6E6E",fg="#ffffff",width=10)
addrres_forosh_et.grid(padx=8,pady=15,sticky="e",row=2,column=1)

addrres_forosh_et_entry=tk.Entry(rehn_page_frame8,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
addrres_forosh_et_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)
floor_forosh_et=tk.Label(rehn_page_frame8,text="طبقه",bg="#0F6E6E",fg="#ffffff",width=10)
floor_forosh_et.grid(padx=8,pady=15,sticky="e",row=3,column=1)

floor_forosh_et_entry=tk.Entry(rehn_page_frame8,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
floor_forosh_et_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

vahed_forosh_et=tk.Label(rehn_page_frame8,text="واحد",bg="#0F6E6E",fg="#ffffff",width=10)
vahed_forosh_et.grid(padx=8,pady=15,sticky="e",row=4,column=1)

vahed_forosh_et_entry=tk.Entry(rehn_page_frame8,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
vahed_forosh_et_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)


price_forosh_et=tk.Label(rehn_page_frame8,text="مبلغ ودیعه",bg="#0F6E6E",fg="#ffffff",width=10)
price_forosh_et.grid(padx=8,pady=15,sticky="e",row=5,column=1)

price_forosh_et_entry=tk.Entry(rehn_page_frame8,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
price_forosh_et_entry.grid(padx=8,pady=15,sticky="w",row=5,column=0)

Monthly_fee_forosh_et=tk.Label(rehn_page_frame8,text=" مبلغ اجاره",bg="#0F6E6E",fg="#ffffff",width=10)
Monthly_fee_forosh_et.grid(padx=8,pady=15,sticky="e",row=6,column=1)

Monthly_fee_forosh_et_entry=tk.Entry(rehn_page_frame8,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
Monthly_fee_forosh_et_entry.grid(padx=8,pady=15,sticky="w",row=6,column=0)

Full_mortgage_forosh_et=tk.Label(rehn_page_frame8,text=" رهن کامل؟ ",bg="#0F6E6E",fg="#ffffff",width=10)
Full_mortgage_forosh_et.grid(padx=8,pady=15,sticky="e",row=7,column=1)

Full_mortgage_ch_btn_forosh_et=tk.Checkbutton(rehn_page_frame8,bg="#C2C2C2", fg="#180202",font=("Arial", 10),)
Full_mortgage_ch_btn_forosh_et.grid(padx=8,pady=15,sticky="w",row=7,column=0)

back_to_home=tk.Button(forosh_et,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_forosh_et)
back_to_home.place(x=650,y=535)

photo_box_forosh_et=tk.Frame(forosh_et,width=410,height=450,background="#e4dde3")
photo_box_forosh_et.place(x=40,y=40)
photo_lbl2_forosh_et = tk.Label(photo_box_forosh_et, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_forosh_et.place(x=30,y=45)
add_img_btn_forosh_et = tk.Button(photo_box_forosh_et, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_forosh_et.place(x=40,y=330)

# (Forosh_et) === ساخت پنجره امکانات 

option_frame_forosh_et=tk.Frame(forosh_et,width=300,height=30,background="#bbfbd1")
option_frame_forosh_et.place(x=520,y=475)

option_label_forosh_et=tk.Label(option_frame_forosh_et,text='افزودن امکانات فایل',font=("B Nazanin",12,"bold"),background="#FFFFFF",fg="#000000")
option_label_forosh_et.pack(side="right",padx=1)

button_label_forosh_et=tk.Label(option_frame_forosh_et)
button_label_forosh_et.pack(side="left",padx=1)
plus_button_forosh_et=tk.Button(option_frame_forosh_et,image=plus,command=open_option4,border=0)
plus_button_forosh_et.pack()

option_frame9=tk.Frame(option_file_frame_forosh_et,width=400,height=100,background="#bbfbd1")
option_frame9.pack(padx=10,pady=15)

parking_ch_btn_forosh_maskoni=tk.Checkbutton(option_frame9,image=parking_pic,background="#022578")
parking_ch_btn_forosh_maskoni.pack(padx=15,side="left")

elvator_ch_btn_forosh_maskoni=tk.Checkbutton(option_frame9,image=elvator_pic,background="#022578")
elvator_ch_btn_forosh_maskoni.pack(padx=15,side="left")

warehouse_ch_btn_forosh_maskoni=tk.Checkbutton(option_frame9,image=warehouse_pic,background="#022578")
warehouse_ch_btn_forosh_maskoni.pack(padx=15,side="right")

option_frame10=tk.Frame(option_file_frame_forosh_et,width=400,height=400,background="#bbfbd1",border=1)
option_frame10.pack(padx=10,pady=15)


aab_va_gaz_emkanat_forosh_et=tk.Label(option_frame10,text="وضعیت آب و گاز",background="#0F6E6E",fg="#ffffff",width=17)
aab_va_gaz_emkanat_forosh_et.grid(padx=8,pady=15,row=0,column=1)

aab_va_gaz_combo_emkanat_forosh_et=ttk.Combobox(option_frame10)
aab_va_gaz_combo_emkanat_forosh_et["values"] = ("فقط گاز دارد","فقط آب دارد","آب و گاز دارد")
aab_va_gaz_combo_emkanat_forosh_et.grid(padx=8,pady=15,row=0,column=0)

sarmayesh_emkanat_forosh_et=tk.Label(option_frame10,text="سیستم سرمایش",background="#0F6E6E",fg="#ffffff",width=17)
sarmayesh_emkanat_forosh_et.grid(padx=8,pady=15,row=4,column=1)

sarmayesh_combo_emkanat_forosh_et=ttk.Combobox(option_frame10)
sarmayesh_combo_emkanat_forosh_et["values"] = (" کولر گازی"," کولرآبی","پنکه سقفی","ندارد")
sarmayesh_combo_emkanat_forosh_et.grid(padx=8,pady=15,row=4,column=0)

garmayesh_emkanat_forosh_et=tk.Label(option_frame10,text="سیستم گرمایش",background="#0F6E6E",fg="#ffffff",width=17)
garmayesh_emkanat_forosh_et.grid(padx=8,pady=15,row=5,column=1)

garmayesh_combo_emkanat_forosh_et=ttk.Combobox(option_frame10)
garmayesh_combo_emkanat_forosh_et["values"] = (" شوفاژ"," بخاری","ندارد")
garmayesh_combo_emkanat_forosh_et.grid(padx=8,pady=15,row=5,column=0)

save_optoin4=tk.Button(option_file_frame_forosh_et,text="ذخیره",command=None,background="#079BDB",fg="#ffffff",width=8)
save_optoin4.place(x=170,y=330)

back_to_home_forosh_et=tk.Button(option_file_frame_forosh_et,text="بازگشت",command=back_to_forosh_et,background="#079BDB",fg="#ffffff",width=8)
back_to_home_forosh_et.place(x=95,y=330)

# win_forosh_bagh_zamin
forosh_bz = tk.Toplevel(root)
forosh_bz.title("فروش باغ و زمین")
forosh_bz.geometry("800x600")
forosh_bz.withdraw()
forosh_bz.configure(bg="#0F6E6E")

forosh_bagh_frame=tk.Frame(forosh_bz,width=490,height=800,bg="#5d6059",border=2)
forosh_bagh_frame.place(x=500,y=90)

metraj_zamin_forosh_bagh=tk.Label(forosh_bagh_frame,text="متراژ",bg="#0F6E6E",fg="#ffffff",width=10)
metraj_zamin_forosh_bagh.grid(padx=8,pady=15,sticky="e",row=0,column=1)

metraj_zamin_forosh_bagh_entry=tk.Entry(forosh_bagh_frame,bg="#C2C2C2", fg="#180202",font=("Arial", 10),textvariable="متر مربع")
metraj_zamin_forosh_bagh_entry.grid(padx=8,pady=15,sticky="w",row=0,column=0)

bagh_type_forosh_bagh=tk.Label(forosh_bagh_frame,text="کاربری زمین",bg="#0F6E6E",fg="#ffffff",width=10)
bagh_type_forosh_bagh.grid(padx=8,pady=15,sticky="e",row=1,column=1)

bagh_type_forosh_bagh_combo=ttk.Combobox(forosh_bagh_frame,state="readonly")
bagh_type_forosh_bagh_combo["values"]=("باغ","زمین کشاورزی")
bagh_type_forosh_bagh_combo.set("باغ")
bagh_type_forosh_bagh_combo.grid(padx=8,pady=15,sticky="w",row=1,column=0)

bagh_loctaion_forosh_bagh=tk.Label(forosh_bagh_frame,text="منطقه و ادرس ",bg="#0F6E6E",fg="#ffffff",width=10)
bagh_loctaion_forosh_bagh.grid(padx=8,pady=15,sticky="e",row=2,column=1)

bagh_loctaion_forosh_bagh_entry=tk.Entry(forosh_bagh_frame,bg="#C2C2C2", fg="#180202",font=("Arial", 10))
bagh_loctaion_forosh_bagh_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

bagh_price_forosh_bagh=tk.Label(forosh_bagh_frame,text='ودیعه',bg="#0F6E6E",fg="#ffffff",width=10)
bagh_price_forosh_bagh.grid(padx=8,pady=15,sticky="e",row=3,column=1)

bagh_price_forosh_bagh_entry=tk.Entry(forosh_bagh_frame,bg="#C2C2C2", fg="#180202",font=("Arial", 10))
bagh_price_forosh_bagh_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

bagh_price_forosh_bagh2=tk.Label(forosh_bagh_frame,text='قیمت هر متر',bg="#0F6E6E",fg="#ffffff",width=10)
bagh_price_forosh_bagh2.grid(padx=8,pady=15,sticky="e",row=4,column=1)

bagh_price_forosh_bagh2_entry=tk.Entry(forosh_bagh_frame,bg="#C2C2C2", fg="#180202",font=("Arial", 10))
bagh_price_forosh_bagh2_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

time_bagh_forosh_bagh=tk.Label(forosh_bagh_frame,text="مدت اجاره",bg="#0F6E6E",fg="#ffffff",width=10)
time_bagh_forosh_bagh.grid(padx=8,pady=15,sticky="e",row=5,column=1)

bagh_time_forosh_bagh_combo=ttk.Combobox(forosh_bagh_frame,state="readonly")
bagh_time_forosh_bagh_combo["values"]=("بلندمدت","کوتاه مدت","فصلی","سالانه")
bagh_time_forosh_bagh_combo.set("فصلی")
bagh_time_forosh_bagh_combo.grid(padx=8,pady=15,sticky="w",row=5,column=0)

photo_box_forosh_bagh=tk.Frame(forosh_bz,width=410,height=450,background="#e4dde3")
photo_box_forosh_bagh.place(x=50,y=40)

photo_lbl2_forosh_bagh = tk.Label(photo_box_forosh_bagh, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_forosh_bagh.place(x=30,y=45)
add_img_btn_forosh_bagh = tk.Button(photo_box_forosh_bagh, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_forosh_bagh.place(x=40,y=330)

back_to_home_forosh_bagh=tk.Button(forosh_bz,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_forosh_bagh)
back_to_home_forosh_bagh.place(x=320,y=520)

save_button_forosh_bagh=tk.Button(forosh_bz,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_forosh_bagh)
save_button_forosh_bagh.place(x=220,y=520)

# (forosh_bz)  ===>> ساخت پنجره امکانات (باغ)

option_frame_forosh_bz=tk.Frame(forosh_bz,width=300,height=30,background="#bbfbd1")
option_frame_forosh_bz.place(x=550,y=450)

option_label_forosh_bz=tk.Label(option_frame_forosh_bz,text='افزودن امکانات فایل',font=("B Nazanin",12,"bold"),background="#FFFFFF",fg="#000000")
option_label_forosh_bz.pack(side="right",padx=1)

button_label_forosh_bz=tk.Label(option_frame_forosh_et)
button_label_forosh_bz.pack(side="left",padx=1)
plus_button_forosh_bz=tk.Button(option_frame_forosh_bz,image=plus,command=open_option6,border=0)
plus_button_forosh_bz.pack()

option_file_frame_forosh_bz=tk.Toplevel(forosh_bz,background="#bbfbd1")
option_file_frame_forosh_bz.title(" ")
option_file_frame_forosh_bz.geometry("640x630")
option_file_frame_forosh_bz.pack_propagate(False)
option_file_frame_forosh_bz.withdraw()
mini_frame_forosh_bagh=tk.Frame(option_file_frame_forosh_bz)
mini_frame_forosh_bagh.place(x=290,y=20)
bagh_type2_forosh_bagh=tk.Label(mini_frame_forosh_bagh,text="کاربری زمین",bg="#0F6E6E",fg="#ffffff",width=10)
bagh_type2_forosh_bagh.pack(padx=5,pady=5,side="right")

bagh_type2_forosh_bagh_combo=ttk.Combobox(mini_frame_forosh_bagh,state="readonly")
bagh_type2_forosh_bagh_combo["values"]=("باغ","زمین کشاورزی")
bagh_type2_forosh_bagh_combo.set("باغ")
bagh_type2_forosh_bagh_combo.pack(padx=5,pady=5,side="left")

bagh_type2_forosh_bagh_combo.bind("<<ComboboxSelected>>",change_bagh_zamin_forosh_bagh)

fram_option_forosh_bagh=tk.Frame(option_file_frame_forosh_bz,width=430,height=290,background="#d1e0df")
fram_option_forosh_bagh.place(x=60,y=60)

metraj_tree_forosh_bagh=tk.Label(fram_option_forosh_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="متراژ درخت کاری")
metraj_tree_forosh_bagh.grid(padx=10,pady=5,row=0,column=4)

metraj_tree_forosh_bagh_entry=tk.Entry(fram_option_forosh_bagh,width=10,bg="#746f6f",fg="#ffffff")
metraj_tree_forosh_bagh_entry.grid(padx=10,pady=5,row=0,column=3)

tree_count_forosh_bagh=tk.Label(fram_option_forosh_bagh,bg="#0F6E6E",fg="#ffffff",width=10,text="تعداد درخت")
tree_count_forosh_bagh.grid(padx=10,pady=5,row=1,column=4)

tree_count_forosh_bagh_entry=tk.Entry(fram_option_forosh_bagh,width=10,bg="#746f6f",fg="#ffffff")
tree_count_forosh_bagh_entry.grid(padx=10,pady=5,row=1,column=3)

abyari_forosh_bagh=tk.Label(fram_option_forosh_bagh,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع ابیاری")
abyari_forosh_bagh.grid(padx=10,pady=5,row=2,column=4)

abyari_forosh_bagh_combo=ttk.Combobox(fram_option_forosh_bagh)
abyari_forosh_bagh_combo["values"]=("سطحی","بارانی","قطره ای","تحت فشار")
abyari_forosh_bagh_combo.set("سطحی")
abyari_forosh_bagh_combo.grid(padx=10,pady=5,row=2,column=3)

type_tree_forosh_bagh=tk.Label(fram_option_forosh_bagh,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع درخت")
type_tree_forosh_bagh.grid(padx=10,pady=5,row=3,column=4)

type_tree_forosh_bagh_combo=ttk.Combobox(fram_option_forosh_bagh)
type_tree_forosh_bagh_combo["values"]=(" ","پسته","بادام","گردو","شلیل","هلو","سیب","انگور"
                           ,"انجیر","زردالو","گیلاس","البالو")
type_tree_forosh_bagh_combo.set("گردو")
type_tree_forosh_bagh_combo.grid(padx=10,pady=5,row=3,column=3)
type_tree_forosh_bagh_combo=tk.Button(fram_option_forosh_bagh,text="افزودن درخت",command=add_tree,bg="#007acc",width=10)
type_tree_forosh_bagh_combo.grid(padx=10,pady=5,row=4,column=4)

label_result_add_forosh_bagh=tk.Label(fram_option_forosh_bagh,text="")
label_result_add_forosh_bagh.grid(padx=10,pady=5,row=4,column=3)

chah_forosh_bagh=tk.Checkbutton(fram_option_forosh_bagh,text="چاه",background="#d6d0d0")
chah_forosh_bagh.grid(padx=0,pady=5,row=5,column=0)

estakhr_forosh_bagh=tk.Checkbutton(fram_option_forosh_bagh,text="استخر",background="#d6d0d0")
estakhr_forosh_bagh.grid(padx=0,pady=5,row=5,column=1)

loleh_forosh_bagh=tk.Checkbutton(fram_option_forosh_bagh,text="اب لوله کشی",background="#d6d0d0")
loleh_forosh_bagh.grid(padx=0,pady=5,row=5,column=2)

bargh_forosh_bagh=tk.Checkbutton(fram_option_forosh_bagh,text="برق کشی",background="#d6d0d0")
bargh_forosh_bagh.grid(padx=0,pady=5,row=5,column=3)

gas_forosh_bagh=tk.Checkbutton(fram_option_forosh_bagh,text="گاز کشی",background="#d6d0d0")
gas_forosh_bagh.grid(padx=0,pady=5,row=5,column=4)

var0_forosh_bsgh=tk.IntVar(value=0)#چک باتن پیش فرض تیک نخورده باشه


room_forosh_bagh_check=tk.Checkbutton(fram_option_forosh_bagh,variable=var0,image=warehouse_pic,background="#022578",text="ساختمان",command=home_true_false2)
room_forosh_bagh_check.grid(padx=10,pady=5,row=6,column=4)

metraj_vila_forosh_bagh=tk.Label(fram_option_forosh_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="متراژ سازه")
metraj_vila_forosh_bagh.grid(padx=10,pady=5,row=7,column=4)

metraj_vila_forosh_bagh_entry=tk.Entry(fram_option_forosh_bagh,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
metraj_vila_forosh_bagh_entry.grid(padx=10,pady=5,row=7,column=3)

year_vila_forosh_bagh=tk.Label(fram_option_forosh_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="سال ساخت")
year_vila_forosh_bagh.grid(padx=10,pady=5,row=8,column=4)

year_vila_forosh_bagh_entry=tk.Entry(fram_option_forosh_bagh,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
year_vila_forosh_bagh_entry.grid(padx=10,pady=5,row=8,column=3)

type_vila_forosh_bagh=tk.Label(fram_option_forosh_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="نوع سازه")
type_vila_forosh_bagh.grid(padx=10,pady=5,row=9,column=4)

type_vila_forosh_bagh_combo=ttk.Combobox(fram_option_forosh_bagh,state="disabled")
type_vila_forosh_bagh_combo["values"]=("آجری","بلوکی","کانکس","چوبی")
type_vila_forosh_bagh_combo.set("آجری")
type_vila_forosh_bagh_combo.grid(padx=10,pady=5,row=9,column=3)

toilet_forosh_bagh=tk.Label(fram_option_forosh_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="سرویس بهداشتی")
toilet_forosh_bagh.grid(padx=10,pady=5,row=10,column=4)

toilet_forosh_bagh_combo=ttk.Combobox(fram_option_forosh_bagh,state="disabled")
toilet_forosh_bagh_combo["values"]=(" ","ندارد","فرنگی","ایرانی","هردو")
toilet_forosh_bagh_combo.set("")
toilet_forosh_bagh_combo.grid(padx=10,pady=5,row=10,column=3)

hamam_forosh_bagh=tk.Label(fram_option_forosh_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="حمام")
hamam_forosh_bagh.grid(padx=10,pady=5,row=11,column=4)

hamam_forosh_bagh_combo=ttk.Combobox(fram_option_forosh_bagh,state="disabled")
hamam_forosh_bagh_combo["values"]=(" ","ندارد","دارد")
hamam_forosh_bagh_combo.set(" ")
hamam_forosh_bagh_combo.grid(padx=10,pady=5,row=11,column=3)

sanad_forosh_bagh=tk.Label(fram_option_forosh_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="سند")
sanad_forosh_bagh.grid(padx=10,pady=5,row=12,column=4)

sanad_forosh_bagh_combo=ttk.Combobox(fram_option_forosh_bagh,state="disabled")
sanad_forosh_bagh_combo["values"]=(" ","ندارد","تک برگ","قولنامه ای","مشاع")
sanad_forosh_bagh_combo.set(" ")
sanad_forosh_bagh_combo.grid(padx=10,pady=5,row=12,column=3)

option_forosh_bagh=tk.Label(fram_option_forosh_bagh,bg="#0F6E6E",fg="#ffffff",width=13,text="امکانات تفریحی")
option_forosh_bagh.grid(padx=10,pady=5,row=13,column=4)

option_forosh_bagh_combo=ttk.Combobox(fram_option_forosh_bagh,state="disabled")
option_forosh_bagh_combo["values"]=(" ","استخر","جکوزی","باربیکیو")
option_forosh_bagh_combo.set(" ")
option_forosh_bagh_combo.grid(padx=10,pady=5,row=13,column=3)
add_option_button_forosh_bagh=tk.Button(fram_option_forosh_bagh,text="افزودن امکانات",command=add_option,bg="#007acc",width=10)
add_option_button_forosh_bagh.grid(padx=10,pady=5,row=13,column=2)
label_result2_add_forosh_bagh=tk.Label(fram_option_forosh_bagh,text="")
label_result2_add_forosh_bagh.grid(padx=10,pady=5,row=13,column=1)

javaz_forosh_bagh=tk.Checkbutton(fram_option_forosh_bagh,text="مجوز ساختن",background="#d6d0d0",state="disabled")
javaz_forosh_bagh.grid(padx=10,pady=5,row=14,column=4)

mohavate_forosh_bagh=tk.Checkbutton(fram_option_forosh_bagh,text="محوطه سازی",background="#d6d0d0",state="disabled")
mohavate_forosh_bagh.grid(padx=10,pady=5,row=14,column=3)

divar_forosh_bagh=tk.Checkbutton(fram_option_forosh_bagh,text="دیوار کشی",background="#d6d0d0")
divar_forosh_bagh.grid(padx=10,pady=5,row=14,column=2)

save_button_bz_option_forosh_bagh=tk.Button(option_file_frame_forosh_bz,text="ذخیره",command=save_bz_option,background="#079BDB",fg="#ffffff",width=8)
save_button_bz_option_forosh_bagh.place(x=170,y=580)

back_to_forosh_bz=tk.Button(option_file_frame_forosh_bz,text="بازگشت",command=back_to_forosh_bz,background="#079BDB",fg="#ffffff",width=8)
back_to_forosh_bz.place(x=95,y=580)

#zamin_frame_option_forosh

fram_option_forosh_zamin=tk.Frame(option_file_frame_forosh_bz,width=430,height=290,background="#d1e0df")
fram_option_forosh_zamin.place_forget()


# اجرای برنامه
root.protocol("WM_DELETE_WINDOW",close_window)
option_file_frame.mainloop()
root.mainloop()