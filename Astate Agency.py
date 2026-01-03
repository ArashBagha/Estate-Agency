

#-------------------------------------  کتابخانه ها-----------------
#region
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox,font,scrolledtext
import subprocess
import os
#endregion
#---#----#----#----#----#----------  توابع   ----------#----#----#----#-------------
#-------------------------تابع بستن پروژه-----------------
#region
def close_window():#این تابع بعد از اتصال دیتابیس تکمیل مشود 
    response=messagebox.askyesno("تایید خروج","آیا از خارج شدن اطمینان دارید؟")
    if response:
        root.destroy()
    else:
        return
#endregion
# -------------------------------------تابع فراخوانی ادرس با دکمه-----------
#region
def open_file_folder():
    file_path = filedialog.askopenfilename()
    if file_path:
        folder_path = os.path.dirname(file_path)
        subprocess.run(['explorer', '/select,', file_path])
#endregion
#  ------------------------------------------تابع انتخاب فایل عکس------------
#region
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        os.startfile(file_path)
#endregion
#---------تابع پاک کردن فرم اصلی----------------
#region
def delete_root():
    melk_mahdode_gheimat_entry.delete(0,tk.END) 
    metraj_entry.delete(0,tk.END)
    metraj_entry.delete(0,tk.END)
    combo_file_type.set("")
    melk_type_combo.set("")
#endregion
#===================================================
#------------توابع اصلی ذخیره----------------------
#region
def save_rehn_maskkoni():#ذخیره پنجره اجاره مسکونی
    pass
def save_forosh_maskkoni():#ذخیره پنجره فروش مسکونی
    pass
def save_rehn_edari():#ذخیره پنجره اجاره اداری
    pass
def save_forosh_edari():#ذخیره پنجره فروش اداری
    pass
def save_rehn_bagh():#ذخیره پنجره اجاره زمین و باغ
    pass
def save_forosh_bagh():# ذخیره پنجره فروش باغ و زمین 
    pass
def save_ejareh_karghah():# ذخیره پنجره اجاره کارگاه 
    pass
def save_forosh_karghah():# ذخیره پنجره فروش کارگاه 
    pass
def save_kharid_karghah():# ذخیره پنجره خرید کارگاه
    pass
#endregion
#===================================================
#----------توابع نگه داری امکانات فایل ها-----------

#========================================================
# ------------پنجره اصلی--------
#region
root = tk.Tk()
root.title("Astate Agency")
root.geometry("1100x700")
#تصاویر پروژه
plus=tk.PhotoImage(file="pluse.png")
elvator_pic=tk.PhotoImage(file="elvator.png")
parking_pic=tk.PhotoImage(file="parking.png")
warehouse_pic=tk.PhotoImage(file="anbari.png")
# root.attributes("-fullscreen", True) <<<-----  App فول اسکرین شدن
root.configure(bg="#0D4D34")
main_frame=tk.Frame(root)
main_frame.pack(fill="both",expand=True)
#endregion
#------------------------فریم هدر --------------
#region
header=tk.Frame(main_frame,bg="#404040",height=60)
header.pack(fill='x')
title_font=font.Font(family="Shabnam",size=22,weight="bold")
title_label=tk.Label(header,text="آژانس املاک",fg="#FFFFFF",bg="#404040",font=title_font)
title_label.pack(pady=25)
#endregion
#-----------قسمت منوبار پروژه------------------------
#---------------------فریم منو----------------------
#region
menu_frame=tk.Frame(main_frame,bg="#ffffff", relief="flat",height=1)
menu_frame.pack(padx=2, pady=2, fill="both", expand=True)
#endregion
# ------------- لیست کشویی فیلد فایل های ثبتی-----------
#region
def kharid():
    box_kharid.deiconify()
    box_kharid.grab_set()

def forosh():
    box_forosh.deiconify()
    box_forosh.grab_set()

def rahn():
    box_rehn_ejareh.deiconify()
    box_rehn_ejareh.grab_set()

def mosharecat():
    box_mosharekat.deiconify()
    box_mosharekat.grab_set()
#endregion
#---------------------------توابع باز و بستن کردن امکانات فایل ها---------------------------
#region
def open_option1():
    option_file_frame_ejareh_maskoni.deiconify()
    ejareh_rehn_page.withdraw()

def open_option2():
    option_file_frame_forosh_maskoni.deiconify()
    forosh_rehn_page.withdraw()

def open_option3():
    option_file_frame_ejareh_edari_tajari.deiconify()
    ejareh_edari_tejari.withdraw() 

def open_option4():
    option_file_frame_forosh_edari_tejari.deiconify()
    forosh_edari_tejari.withdraw()   

def open_option5():
    option_file_frame_ejareh_bagh_zamin.deiconify()
    ejareh_bagh_zamin.withdraw() 

def open_option6():
    option_file_frame_forosh_bagh_zamin.deiconify()
    forosh_bagh_zamin.withdraw()

def open_option7():
    option_file_frame_ejareh_kargah.deiconify()
    ejareh_karghah.withdraw 

def open_option8():
    option_file_frame_forosh_kargah.deiconify()
    forosh_karghah.withdraw 

def open_option9():
    option_file_frame_kharid_maskoni.deiconify()
    kharid_maskoni_page.withdraw()

def open_option10():
    option_file_frame_kharid_edari_tejari.deiconify()
    kharid_edari_tejari.withdraw() 

def open_option11():
    option_file_frame_kharid_bagh_zamin.deiconify()
    kharid_bagh_zamin.withdraw()

def open_option12():
    option_file_frame_kharid_kargah.deiconify()
    kharid_kargah.withdraw()

#endregion
#=======================================================
#-----------توابع برگشت صفحات ثبتی به فرم اصلی----------
#-----برگشت از صفحه اجاره مسکونی-------------------------
#region
def back_home_ejare_maskoni():
    root.deiconify()
    ejareh_rehn_page.withdraw()
    #خالی کردن  باکس های اجاره مسکونی
    sal_sakht_ejareh_maskoni_entry.delete(0,tk.END)
    addrres_ejare_maskoni_entry.delete(0,tk.END)
    tabaghe_ejare_maskoni_entry.delete(0,tk.END)
    vahed_ejare_maskoni_entry.delete(0,tk.END)
    otagh_ejare_maskoni_entry.delete(0,tk.END)
    gheimat_ejare_ejare_maskoni_entry.delete(0,tk.END)
    gheimat_pish_ejare_maskoni_entry.delete(0,tk.END)
    delete_root()
#endregion
#-----برگشت از صفحه فروش مسکونی-------------------------
#region
def back_home_forosh_maskoni():
    root.deiconify()
    forosh_rehn_page.withdraw()
    sal_sakht_forosh_maskoni_entry.delete(0,tk.END)
    addrres_forosh_maskoni_entry.delete(0,tk.END)
    tabaghe_forosh_maskoni_entry.delete(0,tk.END)
    vahed_forosh_maskoni_entry.delete(0,tk.END)
    otagh_forosh_maskoni_entry.delete(0,tk.END)
    gheimat_forosh_maskoni_entry.delete(0,tk.END)
    delete_root()
#endregion
#------------------------برگشت از صفحه اجاره اداری/تجاری---------------------
#region
def back_home_ejareh_edari_tejari():
    root.deiconify()
    ejareh_edari_tejari.withdraw()
    sal_sakht_ejareh_edari_tejari_entry.delete(0,tk.END)
    addrres_ejareh_edari_tejari_entry.delete(0,tk.END)
    tabaghe_ejareh_edari_tejari_entry.delete(0,tk.END)
    vahed_ejareh_edari_tejari_entry.delete(0,tk.END)
    mablagh_ejare_ejareh_edari_tejari_entry.delete(0,tk.END)
    mablagh_pish_ejareh_edari_tejari_entry.delete(0,tk.END) 
    delete_root()
#endregion
#---------------------------برگشت از صفحه فروش اداری/تجاری--------------------
def back_home_forosh_edari_tejari():
    root.deiconify()
    forosh_edari_tejari.withdraw()
    sal_sakht_forosh_edari_tejari_entry.delete(0,tk.END)
    addrres_forosh_edari_tejari_entry.delete(0,tk.END)
    tabaghe_forosh_edari_tejari_entry.delete(0,tk.END)
    vahed_forosh_edari_tejari_entry.delete(0,tk.END)
    mablagh_ejare_forosh_edari_tejari_entry.delete(0,tk.END)
    mablagh_pish_forosh_edari_tejari_entry.delete(0,tk.END)
    delete_root()
#---------------------------برگشت از صفحه خرید اداری/تجاری--------------------
def back_home_kharid_edari_tejari():
    root.deiconify()
    kharid_edari_tejari.withdraw()
    sal_sakht_kharid_edari_tejari_entry.delete(0,tk.END)
    addrres_kharid_edari_tejari_entry.delete(0,tk.END)
    tabaghe_kharid_edari_tejari_entry.delete(0,tk.END)
    vahed_kharid_edari_tejari_entry.delete(0,tk.END)
    mablagh_ejare_kharid_edari_tejari_entry.delete(0,tk.END)
    mablagh_pish_kharid_edari_tejari_entry.delete(0,tk.END)
    delete_root()
#----------------------------برگشت از صفحه اجاره باغ / زمین------------------
def back_to_ejareh_bagh_zamin():
    option_file_frame_ejareh_bagh_zamin.withdraw()
    ejareh_bagh_zamin.deiconify()
#-----------------------------برگشت از صفحه فروش باغ / زمین------------------
def back_home_forosh_bagh():
    forosh_bagh_zamin.withdraw()
    root.deiconify()    
    metraj_zamin_forosh_bagh_zamin_entry.delete(0,tk.END)
    bagh_loctaion_forosh_bagh_zamin_entry.delete(0,tk.END)
    mablagh_ejare_forosh_edari_tejari_entry.delete(0,tk.END)
    mablagh_ejare_forosh_edari_tejari_entry.delete(0,tk.END)
    metraj_derakht_forosh_bagh_zamin_entry.delete(0,tk.END)
    tedad_derakht_forosh_bagh_zamin_entry.delete(0,tk.END)
    metraj_vila_forosh_bagh_zamin_entry.delete(0,tk.END)
    sal_sakht_vila_forosh_bagh_zamin_entry.delete(0,tk.END)
    delete_root()
#=========================================================
#----------------------- برگشت از صفحه اجاره کارگاه--------------------
def back_home_ejareh_karghah():
    ejareh_karghah.withdraw()
    root.deiconify()
    metraj_kargah_entry.delete(0,tk.END)
    loctaion_ejareh_kargah_entry.delete(0,tk.END)
    gheimat_har_metr_ejareh_kargah_entry.delete(0,tk.END)
    mablagh_pish_ejareh_kargah_entry.delete(0,tk.END) 
    delete_root()
#----------------------- برگشت از صفحه فروش کارگاه--------------------
def back_home_forosh_karghah():
    forosh_karghah.withdraw()
    root.deiconify()
    metraj_kargah_entry.delete(0,tk.END)
    loctaion_forosh_kargah_entry.delete(0,tk.END)
    mablagh_pish_forosh_kargah_entry.delete(0,tk.END)
    gheimat_har_metr_forosh_kargah_entry.delete(0,tk.END) 
    delete_root()
#----------------------------برگشت از صفحه اجاره کارگاه------------------
def back_to_ejareh_karghah():
    option_file_frame_ejareh_bagh_zamin.withdraw()
    ejareh_karghah.deiconify()
#-----------------------------برگشت از صفحه خرید باغ / زمین------------------
def back_home_kharid_bagh():
    kharid_bagh_zamin.withdraw()
    root.deiconify()    
    metraj_zamin_kharid_bagh_zamin_entry.delete(0,tk.END)
    bagh_loctaion_kharid_bagh_zamin_entry.delete(0,tk.END)
    mablagh_ejare_kharid_edari_tejari_entry.delete(0,tk.END)
    mablagh_ejare_kharid_edari_tejari_entry.delete(0,tk.END)
    metraj_derakht_kharid_bagh_zamin_entry.delete(0,tk.END)
    tedad_derakht_kharid_bagh_zamin_entry.delete(0,tk.END)
    metraj_vila_kharid_bagh_zamin_entry.delete(0,tk.END)
    sal_sakht_vila_kharid_bagh_zamin_entry.delete(0,tk.END)
    delete_root()
#-----------------------------برگشت از صفحه خرید کارگاه--------------------
def back_home_kharid_kargah():
    kharid_kargah.withdraw()   
    root.deiconify()
    metraj_kharid_kargah_entry.delete(0,tk.END)
    loctaion_kharid_kargah_entry.delete(0,tk.END)
    gheimat_har_metr_kharid_kargah_entry.delete(0,tk.END)
    mablagh_pish_kharid_kargah_entry.delete(0,tk.END)
    delete_root()
#----------------------------برگشت از صفحه خرید مسکونی-------------------
def back_home_kharid_maskoni():
    root.deiconify()
    kharid_maskoni_page.withdraw()
    sal_sakht_kharid_maskoni_entry.delete(0,tk.END)
    addrres_kharid_maskoni_entry.delete(0,tk.END)
    tabaghe_kharid_maskoni_entry.delete(0,tk.END)
    vahed_kharid_maskoni_entry.delete(0,tk.END)
    otagh_kharid_maskoni_entry.delete(0,tk.END)
    gheimat_kharid_maskoni_entry.delete(0,tk.END)
    delete_root()
#=========================================================
#--------برگشت از امکانات فایل ها به صفحه اصلی ثبتی-------
#-------برگشت اجاره مسکونی------------------
def back_to_ejareh_maskoni_page():
    option_file_frame_ejareh_maskoni.withdraw()
    ejareh_rehn_page.deiconify()
#-------برگشت فروش مسکونی------------------    
def back_to_forosh_maskoni_page():
    option_file_frame_forosh_maskoni.withdraw()
    forosh_rehn_page.deiconify()
#--------برگشت اجاره اداری/تجاری----------------- 
def back_to_ejareh_edari_tejari():
    option_file_frame_ejareh_edari_tajari.withdraw()
    ejareh_edari_tejari.deiconify()
#--------برگشت فروش اداری/تجاری----------------- 
def back_to_forosh_edari_tejari():
    option_file_frame_forosh_edari_tejari.withdraw()
    forosh_edari_tejari.deiconify()
#-------برگشت اجاره باغ و زمین------------------
def back_home_ejareh_bagh():
    ejareh_bagh_zamin.withdraw()
    root.deiconify()
#--------------------برگشت فروش باغ و زمین------------------------------------------------
def  back_to_forosh_bagh_zamin():
     option_file_frame_forosh_bagh_zamin.withdraw()
     forosh_bagh_zamin.deiconify()
#--------------------برگشت اجاره کارگاه------------------------------------------------
def  back_to_ejareh_karghah():
     option_file_frame_ejareh_kargah.withdraw()
     ejareh_karghah.deiconify()
#--------------------برگشت فروش کارگاه------------------------------------------------
def  back_to_forosh_karghah():
     option_file_frame_forosh_kargah.withdraw()
     forosh_karghah.deiconify()
#-----------------------------برگشت خرید مسکونی--------------------------
def back_to_kharid_maskoni_page():
    option_file_frame_kharid_maskoni.withdraw()
    kharid_maskoni_page.deiconify()
#--------برگشت خرید اداری/تجاری----------------- 
def back_to_kharid_edari_tejari():
    option_file_frame_kharid_edari_tejari.withdraw()
    kharid_edari_tejari.deiconify()
#--------------------برگشت خرید باغ و زمین------------------------------------------------
def  back_to_kharid_bagh_zamin():
     option_file_frame_kharid_bagh_zamin.withdraw()
     kharid_bagh_zamin.deiconify()
#-------------------برگشت خرید کارگاه---------------------------
def  back_to_kharid_kargah():
     option_file_frame_kharid_kargah.withdraw()
     kharid_kargah.deiconify()
#----------برگشت باکس ها(نوع ملک)-------------
def back_forosh_exit():
    box_forosh.withdraw()
    box_forosh.grab_release()

def back_rehn_ejareh_exit():
    box_rehn_ejareh.withdraw()
    box_rehn_ejareh.grab_release()

def back_kharid_exit():
    box_kharid.withdraw()
    box_kharid.grab_release()

def back_mosharekat_exit():
    box_mosharekat.withdraw()
    box_mosharekat.grab_release()

#============================================
#--------باز و بسته کردن بین باکس ها----------------
#-----بستن باکس و باز کردن صفحه اجاره مسکونی-----------
def ejareh_rehn_page():
    box_rehn_ejareh.withdraw()
    root.withdraw()
    ejareh_rehn_page.deiconify()
    box_rehn_ejareh.grab_release()
#-----بستن باکس و باز کردن صفحه اجاره اداری/تجاری-----------
def ejareh_edari_tejari():
    box_rehn_ejareh.withdraw()
    root.withdraw()
    ejareh_edari_tejari.deiconify() 
    box_rehn_ejareh.grab_release()
#-----بستن باکس و باز کردن صفحه اجاره باغ/زمین---------
def ejarebagh_zamin():
    box_rehn_ejareh.withdraw()
    root.withdraw()
    ejareh_bagh_zamin.deiconify()
    box_rehn_ejareh.grab_release()
#-----بستن باکس و باز کردن صفحه اجاره کارگاه---------
def ejareh_karghah():
    box_rehn_ejareh.withdraw()
    root.withdraw()
    ejareh_karghah.deiconify() 
    box_rehn_ejareh.grab_release()
#-----بستن باکس و باز کردن صفحه فروش مسکونی-----------
def forosh_rehn_page():
    box_forosh.withdraw()
    root.withdraw()
    forosh_rehn_page.deiconify() 
    box_forosh.grab_release()
#-----بستن باکس و باز کردن صفحه فروش اداری/تجاری-----------
def forosh_edari_tejari():
    box_forosh.withdraw()
    root.withdraw()
    forosh_edari_tejari.deiconify()
    box_forosh.grab_release()
#-----بستن باکس و باز کردن صفحه فروش باغ/زمین---------
def forosh_bagh_zamin():
    box_forosh.withdraw()
    root.withdraw()
    forosh_bagh_zamin.deiconify()
    box_forosh.grab_release()  
#-----بستن باکس و باز کردن صفحه فروش  کارگاه---------
def forosh_karghah():
    box_forosh.withdraw()
    root.withdraw()
    forosh_karghah.deiconify() 
    box_forosh.grab_release()
#--------بستن باکس و باز کردن صفحه خرید مسکونی--------
def kharid_maskoni_page():
    box_kharid.withdraw()
    root.withdraw()
    kharid_maskoni_page.deiconify() 
    box_kharid.grab_release()
#-----بستن باکس و باز کردن صفحه خرید اداری/تجاری-----------
def kharid_edari_tejari():
    box_kharid.withdraw()
    root.withdraw()
    kharid_edari_tejari.deiconify()
    box_kharid.grab_release()
#-----بستن باکس و باز کردن صفحه خرید باغ/زمین---------
def kharid_bagh_zamin():
    box_kharid.withdraw()
    root.withdraw()
    kharid_bagh_zamin.deiconify()
    box_kharid.grab_release()   
#------بستن باکس و باز کردن صفحه خرید کارگاه-----------
def kharid_kargah():
    box_kharid.withdraw()
    root.withdraw()
    kharid_kargah.deiconify()
    box_kharid.grab_release()   

#-------------رادیو باتن باکس-------------------
#تابع رادیو باتن باز و بسته کردن صفحات فروش
def sabt_radio_frosh():
    selected2 = forosh_radio_value.get()

    if selected2==0:
            box_forosh.withdraw()
            root.withdraw()
            forosh_rehn_page.deiconify() 
            box_forosh.grab_release()

    elif selected2==2:
            box_forosh.withdraw()
            root.withdraw()
            forosh_edari_tejari.deiconify()
            box_forosh.grab_release()
        
    elif selected2==4:
         box_forosh.withdraw()
         root.withdraw()
         forosh_bagh_zamin.deiconify()
         box_forosh.grab_release()
        
    elif selected2==6:
        box_forosh.withdraw()
        root.withdraw()
        forosh_karghah.deiconify()
        box_forosh.grab_release()

#تابع رادیو باتن باز و بسته کردن صفحات اجاره
def sabt_radio_rehn():
    selected = ejareh_radio_value.get()

    if selected==0:
            box_rehn_ejareh.withdraw()
            root.withdraw()
            ejareh_rehn_page.deiconify()
            box_rehn_ejareh.grab_release()
        
    elif selected==2:
        box_rehn_ejareh.withdraw()
        root.withdraw()
        ejareh_edari_tejari.deiconify() 
        box_rehn_ejareh.grab_release()

    elif selected==4:
            box_rehn_ejareh.withdraw()
            root.withdraw()
            ejareh_bagh_zamin.deiconify()
            box_rehn_ejareh.grab_release()

    elif selected==6:
            box_rehn_ejareh.withdraw()
            root.withdraw()
            ejareh_karghah.deiconify()
            box_rehn_ejareh.grab_release()

#تابع رادیو باتن باز و بسته کردن صفحات خرید
def sabt_radio_kharid():
    selected = kharid_radio_value.get()

    if selected==0:
            box_kharid.withdraw()
            root.withdraw()
            kharid_maskoni_page.deiconify()
            box_kharid.grab_release()
        
    elif selected==2:
        box_kharid.withdraw()
        root.withdraw()
        kharid_edari_tejari.deiconify()
        box_kharid.grab_release()

    elif selected==4:
        box_kharid.withdraw()
        root.withdraw()
        kharid_bagh_zamin.deiconify()
        box_kharid.grab_release()

    elif selected==6:
        box_kharid.withdraw()
        root.withdraw()
        kharid_kargah.deiconify()
        box_kharid.grab_release()

#تابع رادیو باتن باز و بسته کردن صفحات مشارکت
def sabt_radio_mosharekat():
    selected = mosharekat_radio_value.get()

    if selected==0:
        box_mosharekat.withdraw()
        root.withdraw()
        #mosharekat_sakht_page.deiconify()
        box_mosharekat.grab_release()
        
    elif selected==2:
        box_mosharekat.withdraw()
        root.withdraw()
        #pishforosh_page.deiconify()
        box_mosharekat.grab_release()
            
#=======================================================
#---------------/جابه جایی کاربری باغ و زمین در قسمت های فروش/خرید/اجاره-------------
def change_bagh_zamin1(event):
    co=karbari_zamin_combo.get()
    if co=="باغ":
        fram_option_zamin_ejareh_bagh_zamin.place_forget()
        option_frame_options_ejareh_bagh_zamin.place(x=60,y=60)
    else:
        option_frame_options_ejareh_bagh_zamin.place_forget()
        fram_option_zamin_ejareh_bagh_zamin.place(x=60,y=60)

def change_bagh_zamin_forosh_bagh(event):
    co=karbary_zamin_forosh_bagh_zamin_combo.get()
    if co=="باغ":
        option_frame_option2_forosh_bagh_zamin.place_forget()
        option_frame_forosh_bagh_zamin.place(x=60,y=60)#فریم باغ
    else:
        option_frame_forosh_bagh_zamin.place_forget()
        option_frame_option2_forosh_bagh_zamin.place(x=60,y=60)

def change_bagh_zamin_kharid_bagh(event):
    co=karbary_zamin_kharid_bagh_zamin_combo.get()
    if co=="باغ":
        option_frame_option2_kharid_bagh_zamin.place_forget()
        option_frame_kharid_bagh_zamin.place(x=60,y=60)
    else:
        option_frame_kharid_bagh_zamin.place_forget()
        option_frame_option2_kharid_bagh_zamin.place(x=60,y=60)

#=============================================================      
#---------------------قسمت اضافه کردن اپشن های تفریحی و درختان در قسمت باغ و زمین------------
selected_trees=[]
def add_tree():# برای اضافه کردن درخت به صورت دستی
    t=type_tree_combo.get()
    if t and t not in selected_trees:
        selected_trees.append(t)
        label_result_add.config(text=','.join(selected_trees))
selected_option=[]
def add_option():
    op=option_ejareh_bagh_zamin_combo.get()
    if op and op not in selected_option:
        selected_option.append(op)
        label_result2_add.config(text=','.join(selected_option))
selected_topo1=[]
def add_topo1():
    topo=zamin_shekl_ejareh_bagh_zamin_combo.get()
    if topo and topo not in selected_topo1:
        selected_topo1.append(topo)
        label_natige_topo_add_ejareh_bagh_zamin.config(text=','.join(selected_topo1))

selected_topo2=[]
def add_topo2():
    topo2=zamin_shekl_forosh_bagh_zamin_combo.get()
    if topo2 and topo2 not in selected_topo2:
        selected_topo2.append(topo2)
        lable_natige_add_forosh_bagh_zamin.config(text=','.join(selected_topo2))

selected_topo3=[]
def add_topo3():
    topo3=zamin_shekl_kharid_bagh_zamin_combo.get()
    if topo3 and topo3 not in selected_topo3:
        selected_topo3.append(topo3)
        lable_natige_add_kharid_bagh_zamin.config(text=','.join(selected_topo3))
def home_true_false1(): # برای فعال یا غیر فعال کردن ویجت های خونه باغ در اجاره
    if var0.get()==1:
        metraj_vila_bagh_entry.config(state="normal")
        sal_sakht_vila_bagh_entry.config(state="normal")
        type_vila_ejareh_bagh_zamin_combo.config(state="normal")
        toilet_bagh_combo.config(state="normal")
        hamam_bagh_combo.config(state="normal")
        sanad_bagh_combo.config(state="normal")
        option_ejareh_bagh_zamin_combo.config(state="normal")
        mojavez_sakht_ejareh_bagh_zamin.config(state="normal")
        mohavate_ejareh_bagh_zamin.config(state="normal")
    else:
        metraj_vila_bagh_entry.config(state="disabled")
        sal_sakht_vila_bagh_entry.config(state="disabled")
        type_vila_ejareh_bagh_zamin_combo.config(state="disabled")
        toilet_bagh_combo.config(state="disabled")
        hamam_bagh_combo.config(state="disabled")
        sanad_bagh_combo.config(state="disabled")
        option_ejareh_bagh_zamin_combo.config(state="disabled")
        mojavez_sakht_ejareh_bagh_zamin.config(state="disabled")
        mohavate_ejareh_bagh_zamin.config(state="disabled")
        
def home_true_false2(): #برای فعال یا غیر فعال کردن ویجت های خونه باغ در فروش
    if var0.get()==1:
        metraj_vila_forosh_bagh_zamin_entry.config(state="normal")
        sal_sakht_vila_forosh_bagh_zamin_entry.config(state="normal")
        type_vila_forosh_bagh_zamin_combo.config(state="normal")
        toilet_forosh_bagh_zamin_combo.config(state="normal")
        hamam_forosh_bagh_zamin_combo.config(state="normal")
        sanad_forosh_bagh_zamin_combo.config(state="normal")
        option_forosh_bagh_zamin_combo.config(state="normal")
        mojavez_sakht_check_btn_forosh_bagh_zamin.config(state="normal")
        mohavate_sazi_check_btn_forosh_bagh_zamin.config(state="normal")
    else:
        metraj_vila_forosh_bagh_zamin_entry.config(state="disabled")
        sal_sakht_vila_forosh_bagh_zamin_entry.config(state="disabled")
        type_vila_forosh_bagh_zamin_combo.config(state="disabled")
        toilet_forosh_bagh_zamin_combo.config(state="disabled")
        hamam_forosh_bagh_zamin_combo.config(state="disabled")
        sanad_forosh_bagh_zamin_combo.config(state="disabled")
        option_forosh_bagh_zamin_combo.config(state="disabled")
        mojavez_sakht_check_btn_forosh_bagh_zamin.config(state="disabled")
        mohavate_sazi_check_btn_forosh_bagh_zamin.config(state="disabled")
def choos_kesht(event):
    a=kesht_ejareh_bagh_zamin_combo.get()
    if a=="بدون کشت":
        kesht_ejareh_bagh_zamin_entry.config(state="disabled")
    else:
        kesht_ejareh_bagh_zamin_entry.config(state="normal")
def choos_kesht2(event):
    b=kesht_forosh_bagh_zamin_combo.get()
    if b=="بدون کشت":
        kesht_forosh_bagh_zamin_entry.config(state="disabled")
    else:
        kesht_forosh_bagh_zamin_entry.config(state="normal")
def choos_kesht3(event):
    c=kesht_kharid_bagh_zamin_combo.get()
    if c=="بدون کشت":
        kesht_kharid_bagh_zamin_entry.config(state="disabled")
    else:
        kesht_kharid_bagh_zamin_entry.config(state="normal")
selected_trees2=[]
def add_tree2():
    t3=type_tree_forosh_bagh_zamin_combo.get()
    if t3 and t3 not in selected_trees2:
        selected_trees2.append(t3)
        type_tree_forosh_btn.config(text=','.join(selected_trees2))
selected_option2=[]
def add_option2():
    op2=option_forosh_bagh_zamin_combo.get()
    if op2 and op2 not in selected_option2:
        selected_option2.append(op2)
        add_option_button_forosh_bagh_zamin.config(text=','.join(selected_option2))

selected_trees3=[]
def add_tree3():
    t4=type_tree_kharid_bagh_zamin_combo.get()
    if t4 and t4 not in selected_trees3:
        selected_trees3.append(t4)
        type_tree_kharid_btn.config(text=','.join(selected_trees3))
selected_option3=[]
def add_option3():
    op3=option_kharid_bagh_zamin_combo.get()
    if op3 and op3 not in selected_option3:
        selected_option3.append(op3)
        add_option_button_kharid_bagh_zamin.config(text=','.join(selected_option3))


#=======================================================

#---------------------قسمت اضافه کردن اپشن های تفریحی و درختان در قسمت باغ و زمین------------
selected_trees=[]
def add_tree():# برای اضافه کردن درخت به صورت دستی
    t=type_tree_combo.get()
    if t and t not in selected_trees:
        selected_trees.append(t)
        label_result_add.config(text=','.join(selected_trees))
selected_option=[]
def add_option():
    op=option_ejareh_bagh_zamin_combo.get()
    if op and op not in selected_option:
        selected_option.append(op)
        label_result2_add.config(text=','.join(selected_option))
selected_topo1=[]
def add_topo1():
    topo=zamin_shekl_ejareh_bagh_zamin_combo.get()
    if topo and topo not in selected_topo1:
        selected_topo1.append(topo)
        label_natige_topo_add_ejareh_bagh_zamin.config(text=','.join(selected_topo1))

selected_topo2=[]
def add_topo2():
    topo2=zamin_shekl_forosh_bagh_zamin_combo.get()
    if topo2 and topo2 not in selected_topo2:
        selected_topo2.append(topo2)
        add_topo2_button_forosh_bagh_zamin.config(text=','.join(selected_topo2))


def home_true_false1(): # برای فعال یا غیر فعال کردن ویجت های خونه باغ در اجاره
    if var0.get()==1:
        metraj_vila_bagh_entry.config(state="normal")
        sal_sakht_vila_bagh_entry.config(state="normal")
        type_vila_ejareh_bagh_zamin_combo.config(state="normal")
        toilet_bagh_combo.config(state="normal")
        hamam_bagh_combo.config(state="normal")
        sanad_bagh_combo.config(state="normal")
        option_forosh_bagh_zamin_combo.config(state="normal")
        mojavez_sakht_ejareh_bagh_zamin.config(state="normal")
        mohavate_ejareh_bagh_zamin.config(state="normal")
    else:
        metraj_vila_bagh_entry.config(state="disabled")
        sal_sakht_vila_bagh_entry.config(state="disabled")
        type_vila_ejareh_bagh_zamin_combo.config(state="disabled")
        toilet_bagh_combo.config(state="disabled")
        hamam_bagh_combo.config(state="disabled")
        sanad_bagh_combo.config(state="disabled")
        option_forosh_bagh_zamin_combo.config(state="disabled")
        mojavez_sakht_ejareh_bagh_zamin.config(state="disabled")
        mohavate_ejareh_bagh_zamin.config(state="disabled")

        
def home_true_false2(): #برای فعال یا غیر فعال کردن ویجت های خونه باغ در فروش
    if var0.get()==1:
        metraj_vila_forosh_bagh_zamin_entry.config(state="normal")
        sal_sakht_vila_forosh_bagh_zamin_entry.config(state="normal")
        type_vila_forosh_bagh_zamin_combo.config(state="normal")
        toilet_forosh_bagh_zamin_combo.config(state="normal")
        hamam_forosh_bagh_zamin_combo.config(state="normal")
        sanad_forosh_bagh_zamin_combo.config(state="normal")
        option_forosh_bagh_zamin_combo.config(state="normal")
        divar_forosh_bagh_zamin.config(state="normal")
        mojavez_sakht_check_btn_forosh_bagh_zamin.config(state="normal")
        mohavate_sazi_check_btn_forosh_bagh_zamin.config(state="normal")
    else:
        metraj_vila_forosh_bagh_zamin_entry.config(state="disabled")
        sal_sakht_vila_forosh_bagh_zamin_entry.config(state="disabled")
        type_vila_forosh_bagh_zamin_combo.config(state="disabled")
        toilet_forosh_bagh_zamin_combo.config(state="disabled")
        hamam_forosh_bagh_zamin_combo.config(state="disabled")
        sanad_forosh_bagh_zamin_combo.config(state="disabled")
        option_forosh_bagh_zamin_combo.config(state="disabled")
        mojavez_sakht_check_btn_forosh_bagh_zamin.config(state="disabled")
        mohavate_sazi_check_btn_forosh_bagh_zamin.config(state="disabled")
def home_true_false3(): #برای فعال یا غیر فعال کردن ویجت های خونه باغ در خرید
    if var0.get()==1:
        metraj_vila_kharid_bagh_zamin_entry.config(state="normal")
        sal_sakht_vila_kharid_bagh_zamin_entry.config(state="normal")
        type_vila_kharid_bagh_zamin_combo.config(state="normal")
        toilet_kharid_bagh_zamin_combo.config(state="normal")
        hamam_kharid_bagh_zamin_combo.config(state="normal")
        sanad_kharid_bagh_zamin_combo.config(state="normal")
        option_kharid_bagh_zamin_combo.config(state="normal")
        divar_kharid_bagh_zamin.config(state="normal")
        mojavez_sakht_check_btn_kharid_bagh_zamin.config(state="normal")
        mohavate_sazi_check_btn_kharid_bagh_zamin.config(state="normal")
    else:
        metraj_vila_kharid_bagh_zamin_entry.config(state="disabled")
        sal_sakht_vila_kharid_bagh_zamin_entry.config(state="disabled")
        type_vila_kharid_bagh_zamin_combo.config(state="disabled")
        toilet_kharid_bagh_zamin_combo.config(state="disabled")
        hamam_kharid_bagh_zamin_combo.config(state="disabled")
        sanad_kharid_bagh_zamin_combo.config(state="disabled")
        option_kharid_bagh_zamin_combo.config(state="disabled")
        mojavez_sakht_check_btn_kharid_bagh_zamin.config(state="disabled")
        mohavate_sazi_check_btn_kharid_bagh_zamin.config(state="disabled")
def choos_kesht(event):
    a=kesht_ejareh_bagh_zamin_combo.get()
    if a=="بدون کشت":
        kesht_ejareh_bagh_zamin_entry.config(state="disabled")
    else:
        kesht_ejareh_bagh_zamin_entry.config(state="normal")
def choos_kesht2(event):
    b=kesht_forosh_bagh_zamin_combo.get()
    if b=="بدون کشت":
        kesht_forosh_bagh_zamin_entry.config(state="disabled")
    else:
        kesht_forosh_bagh_zamin_entry.config(state="normal")
selected_trees2=[]
def add_tree2():
    t3=type_tree_forosh_bagh_zamin_combo.get()
    if t3 and t3 not in selected_trees2:
        selected_trees2.append(t3)
        type_tree_forosh_btn.config(text=','.join(selected_trees2))
selected_option2=[]
def add_option2():
    op2=option_forosh_bagh_zamin_combo.get()
    if op2 and op2 not in selected_option2:
        selected_option2.append(op2)
        add_option_button_forosh_bagh_zamin.config(text=','.join(selected_option2))



#---#----#----#----#----#----------  گرافیک   ----------#----#----#----#-----#-----------
# ---------دکمه فایل با منوی کشویی ------------------
#region 
menubar = tk.Menu(root, font=("Shabnam", 10))
# ایجاد منوی "ثبت فایل ها"
file_menu_sabt_file = tk.Menu(menubar, tearoff=0, font=("Shabnam", 10))
file_menu_sabt_file.add_command(label="خرید", command=kharid)
file_menu_sabt_file.add_command(label="فروش", command=forosh)
file_menu_sabt_file.add_command(label="رهن/اجاره", command=rahn)
file_menu_sabt_file.add_command(label="مشارکت", command=mosharecat)

# اضافه کردن منوی "ثبت فایل ها" به منوبار
menubar.add_cascade(label="ثبت فایل ها", menu=file_menu_sabt_file)

# اتصال منوبار به پنجره
root.config(menu=menubar)
#endregion
# ---------------اضافه کردن فیلد قرارداد ---------------
#region
file_menu_gharardad= tk.Menu(menubar, tearoff=0, font=("Shabnam", 10))
file_menu_gharardad.add_command(label="خرید", command=None)
file_menu_gharardad.add_command(label="فروش", command=None)
file_menu_gharardad.add_command(label="رهن/اجاره", command=None)
file_menu_gharardad.add_command(label="مشارکت", command=None)

# اضافه کردن منوی قرار دادها به منوبار
menubar.add_cascade(label="قراردادها", menu=file_menu_gharardad)
#endregion
#----------------دکمه گزارش ها با منوی کشویی ------------------------
# ----------لیست کشویی فیلد گزارش ها-----------------
file_menu_gozaresh = tk.Menu(menubar, tearoff=0, font=("Shabnam", 10))
file_menu_gozaresh.add_command(label="خروجی اکسل", command=None)
file_menu_gozaresh.add_command(label="قراردادها", command=None)

# اضافه کردن منوی گزارش ها به منوبار
menubar.add_cascade(label="گزارش ها", menu=file_menu_gozaresh)

#---------------------------تابع های خروجی اکسل و قرار دادها------------
def excel():
    pass
def gharardadeha():
    pass

# ----------------------اضافه کردن فیلد درخواست ها-------
#region
file_menu_darkhast= tk.Menu(menubar, tearoff=0, font=("Shabnam", 10))
file_menu_darkhast.add_command(label="", command=None)
file_menu_darkhast.add_command(label="", command=None)

# اضافه کردن منوی گزارش ها به منوبار
menubar.add_cascade(label="درخواست ها", menu=file_menu_darkhast)
#endregion
#-------------------------اضافه کردن فیلد کاربران---------
#region
file_menu_karbaran= tk.Menu(menubar, tearoff=0, font=("Shabnam", 10))
file_menu_karbaran.add_command(label="", command=None)
file_menu_karbaran.add_command(label="", command=None)

# اضافه کردن منوی گزارش ها به منوبار
menubar.add_cascade(label="کاربران", menu=file_menu_karbaran)
#endregion
#========================================================
# -----------باکس سمت چپ - جستجو در فایل های ملک----------
#region
frame_jostojo_melk_left= tk.LabelFrame(root, text="جستجوی ملک", width=200, bg="#575353",fg="#F8F7F7", font=("Shabnam", 16))
frame_jostojo_melk_left.pack(side="left", fill="y", padx=6, pady=15)

box_jostojo_malk1= tk.Frame(frame_jostojo_melk_left,bg="#0F6E6E")
box_jostojo_malk1.pack(padx=6, pady=15)

file_type = tk.Label(box_jostojo_malk1,text="نوع فایل",bg="#0F6E6E", fg="#FFFFFF",font=("Shabnam", 13))
file_type.pack(padx=15,pady=10, side="right")
combo_file_type= ttk.Combobox(box_jostojo_malk1)
combo_file_type["values"] = ("رهن/اجاره","خرید","فروش","مشارکت",)
combo_file_type.pack(padx=10, pady=10) 

box_jostojo_malk2= tk.Frame(frame_jostojo_melk_left,bg="#0F6E6E")
box_jostojo_malk2.pack(padx=6, pady=15)

melk_type_lable = tk.Label(box_jostojo_malk2,text="نوع ملک",bg="#0F6E6E", fg="#FFFFFF",font=("Shabnam", 13))
melk_type_lable.pack(padx=15,pady=10, side="right")
melk_type_combo= ttk.Combobox(box_jostojo_malk2)
melk_type_combo["values"] = ("مسکونی","مغازه/ تجاری"," باغ / زمین","کارگاه")
melk_type_combo.pack(padx=10, pady=10) 

box_jostojo_malk3 = tk.Frame(frame_jostojo_melk_left,bg="#0F6E6E")
box_jostojo_malk3.pack(padx=6, pady=5)

melk_mahdode_gheimat_lable = tk.Label(box_jostojo_malk3,text="محدوده قیمت",bg="#0F6E6E", fg="#FFFFFF",font=("Shabnam", 13))
melk_mahdode_gheimat_lable.pack(padx=5, pady=1)
melk_mahdode_gheimat_entry = tk.Entry(box_jostojo_malk3,bg="#C2C2C2", fg="#FFFFFF",font=("Shabnam", 13))
melk_mahdode_gheimat_entry.pack(padx=20,pady=10)

metraj_lable = tk.Label(box_jostojo_malk3,text=" متراژ",bg="#0F6E6E", fg="#FFFFFF",font=("Shabnam", 13))
metraj_lable.pack(padx=5, pady=1)
metraj_entry = tk.Entry(box_jostojo_malk3,bg="#C2C2C2", fg="#FFFFFF",font=("Shabnam", 13))
metraj_entry.pack(padx=20,pady=10)

address_lable = tk.Label(box_jostojo_malk3,text=" منطقه / آدرس",bg="#0F6E6E", fg="#FFFFFF",font=("Shabnam", 13))
address_lable.pack(padx=5, pady=1)
address_entry = tk.Entry(box_jostojo_malk3,bg="#C2C2C2", fg="#FFFFFF",font=("Shabnam", 13))
address_entry.pack(padx=20,pady=10)

# ---------------------دکمه جستجوی ملک-----------------
search_btn = tk.Button(frame_jostojo_melk_left, text="    جستجو    " , bg="#94c6dd", fg="#201F1F", font=("Shabnam", 13), command=open_file)
search_btn.pack(pady=10)
#=====================================================
#endregion
# ---------------------------باکس وسط - نمایش جستجوی --------------
#region
frame_list_amlack_centre = tk.LabelFrame(root, text="لیست املاک", bg="#ffffff", font=("Shabnam", 13))
frame_list_amlack_centre.pack(side="left", fill="both", expand=True, padx=4, pady=15)

columns = ["آدرس", "قیمت ", "نوع ملک ", "متراژ"]
tree = ttk.Treeview(frame_list_amlack_centre, columns=columns, show="headings")
for textt in columns:
    tree.heading(textt,text=textt)
    tree.column(textt, width=100)
tree.pack(fill="both", expand=True)
#===================================================
#endregion

# --------------------باکس سمت راست - نمایش جزئیات فایل های موجود املاک---------------
#region
frame_joziat_amlack = tk.LabelFrame(root, text="جزئیات ملک", width=200, bg="#ffffff", font=("Shabnam", 13))
frame_joziat_amlack.pack(side="right", fill="y", padx=6, pady=15)

photo_melk_lbl = tk.Label(frame_joziat_amlack, text="[تصویر ملک]", bg="gray", width=20, height=10)
photo_melk_lbl.pack(pady=10)

malek = tk.Label(frame_joziat_amlack,text="مالک ",bg="#272B61", fg="#F7F7FA",font=("Shabnam", 13))
malek.pack(padx=6,pady=4)

entry_malek = tk.Entry(frame_joziat_amlack,bg="#C2C2C2", fg="#FFFFFF",font=("Shabnam", 13))
entry_malek.pack(padx=20,pady=4)

malek_phone_number = tk.Label(frame_joziat_amlack,text="شماره تماس مالک ",bg="#272B61", fg="#F7F7FA",font=("Shabnam", 13))
malek_phone_number.pack(padx=6,pady=4)

entry_malek_phone_number = tk.Entry(frame_joziat_amlack,bg="#C2C2C2", fg="#FFFFFF",font=("Shabnam", 13))
entry_malek_phone_number.pack(padx=20,pady=4)

metraj_lable_right= tk.Label(frame_joziat_amlack,text="متراژ ",bg="#272B61", fg="#F7F7FA",font=("Shabnam", 13))
metraj_lable_right.pack(padx=6,pady=4)

metraj_lable_right_entry = tk.Entry(frame_joziat_amlack,bg="#C2C2C2", fg="#FFFFFF",font=("Shabnam", 13))
metraj_lable_right_entry.pack(padx=20,pady=4)

gheimat_melk_right_lable = tk.Label(frame_joziat_amlack,text="قیمت ",bg="#272B61", fg="#F7F7FA",font=("Shabnam", 13))
gheimat_melk_right_lable.pack(padx=6,pady=4)

gheimat_melk_right_entry= tk.Entry(frame_joziat_amlack,bg="#C2C2C2", fg="#FFFFFF",font=("Shabnam", 13))
gheimat_melk_right_entry.pack(padx=20,pady=4)

tozihat_right_lable = tk.Label(frame_joziat_amlack,text="توضیحات ",bg="#272B61", fg="#F7F7FA",font=("Shabnam", 13))
tozihat_right_lable.pack(padx=6,pady=4)

tozihat_right_entry = tk.Entry(frame_joziat_amlack,bg="#C2C2C2", fg="#FFFFFF",font=("Shabnam", 13))
tozihat_right_entry.pack(padx=20,pady=4)
#=======================================================
#endregion
#-------------------------باکس های نوع ثبتی فایل ها----------------------
#-------------------نوع انتخاب ثبتی فایل برای پنجره های رهن و اجاره--------------
#region
box_rehn_ejareh=tk.Toplevel(root)
box_rehn_ejareh.title("انتخاب نوع ملک رهن و اجاره")
box_rehn_ejareh.geometry("500x270")
box_rehn_ejareh.withdraw()
box_rehn_ejareh.configure(bg="#0F6E6E")

ejareh_radio_value = tk.IntVar(value=0)

ejareh_maskoni_radio = tk.Radiobutton(box_rehn_ejareh,text="ثبت فایل مسکونی",background="#0F6E6E",variable=ejareh_radio_value,value=0,font=("Shabnam", 11))
ejareh_maskoni_radio.place(x=330, y=50)

ejareh_edari_radio = tk.Radiobutton( box_rehn_ejareh,text="ثبت فایل اداری/تجاری",
    bg="#0F6E6E",
    variable=ejareh_radio_value,
    value=2,
    font=("Shabnam", 11))
ejareh_edari_radio.place(x=330, y=90)

ejareh_bagh_radio = tk.Radiobutton(box_rehn_ejareh,text="ثبت فایل باغ/زمین",bg="#0F6E6E",
    variable=ejareh_radio_value,
    value=4,
    font=("Shabnam", 11))
ejareh_bagh_radio.place(x=330, y=130)

ejareh_kargah_radio = tk.Radiobutton(box_rehn_ejareh,text="ثبت فایل کارگاه",bg="#0F6E6E",variable=ejareh_radio_value,value=6,
    font=("Shabnam", 11))
ejareh_kargah_radio.place(x=330, y=170)




back_to_home_box_ejareh=tk.Button(box_rehn_ejareh,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_rehn_ejareh_exit)
back_to_home_box_ejareh.place(x=140,y=210)


zakhire_radio_box_ejareh=tk.Button(box_rehn_ejareh,text="ادامه",bg="#13f",fg="white",width=12,height=2,command=sabt_radio_rehn)
zakhire_radio_box_ejareh.place(x=60,y=210)

box_rehn_ejareh.protocol("WM_DELETE_WINDOW", lambda: None)
box_rehn_ejareh.resizable(False, False) 

#=====================================================================
#endregion
#----------------------------------نوع انتخاب ثبتی فایل برای پنجره های فروش-----------------
#region
box_forosh=tk.Toplevel(root)
box_forosh.title("انتخاب نوع ملک فروش")
box_forosh.geometry("500x270")
box_forosh.withdraw()
box_forosh.configure(bg="#0F6E6E")

# یک متغیر مشترک برای همه رادیوباتن‌ها
forosh_radio_value = tk.IntVar(value=0)  # مقدار پیش‌فرض -1 یعنی هیچکدام انتخاب نشده

forosh_maskoni_radio = tk.Radiobutton(box_forosh, value=0, text="ثبت فایل مسکونی", background="#0F6E6E", variable=forosh_radio_value, font=("Shabnam",11))
forosh_maskoni_radio.place(x=330,y=50)

forosh_edari_radio = tk.Radiobutton(box_forosh, value=2, text="ثبت فایل اداری/تجاری",
bg="#0F6E6E", variable=forosh_radio_value, font=("Shabnam",11))
forosh_edari_radio.place(x=330,y=90)

forosh_bagh_radio = tk.Radiobutton(box_forosh, value=4, text="ثبت فایل باغ/زمین",bg="#0F6E6E", variable=forosh_radio_value, font=("Shabnam",11))
forosh_bagh_radio.place(x=330,y=130)

forosh_kargah_radio = tk.Radiobutton(box_forosh, value=6, text="ثبت فایل کارگاه",bg="#0F6E6E", variable=forosh_radio_value, font=("Shabnam",11))
forosh_kargah_radio.place(x=330,y=170)


back_to_home_box_forosh=tk.Button(box_forosh,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_forosh_exit)
back_to_home_box_forosh.place(x=140,y=210)

zakhire_radio_box_forosh=tk.Button(box_forosh,text="ادامه",bg="#13f",fg="white",width=12,height=2,command=sabt_radio_frosh)
zakhire_radio_box_forosh.place(x=60,y=210)

box_forosh.protocol("WM_DELETE_WINDOW", lambda: None)
box_forosh.resizable(False, False) 




#======================================================================
#endregion
#----------------------------------نوع انتخاب ثبتی فایل برای پنجره های خرید-----------------
#region
box_kharid=tk.Toplevel(root)
box_kharid.title("انتخاب نوع ملک خرید")
box_kharid.geometry("500x270")
box_kharid.withdraw()
box_kharid.configure(bg="#0F6E6E")

# یک متغیر مشترک برای همه رادیوباتن‌ها
kharid_radio_value = tk.IntVar(value=0)  # مقدار پیش‌فرض -1 یعنی هیچکدام انتخاب نشده

kharid_maskoni_radio = tk.Radiobutton(box_kharid, value=0, text="ثبت فایل مسکونی", background="#0F6E6E", variable=kharid_radio_value, font=("Shabnam",11))
kharid_maskoni_radio.place(x=330,y=50)

kharid_edari_radio = tk.Radiobutton(box_kharid, value=2, text="ثبت فایل اداری/تجاری",
bg="#0F6E6E", variable=kharid_radio_value, font=("Shabnam",11))
kharid_edari_radio.place(x=330,y=90)

kharid_bagh_radio = tk.Radiobutton(box_kharid, value=4, text="ثبت فایل باغ/زمین",bg="#0F6E6E", variable=kharid_radio_value, font=("Shabnam",11))
kharid_bagh_radio.place(x=330,y=130)

kharid_kargah_radio = tk.Radiobutton(box_kharid, value=6, text="ثبت فایل کارگاه",bg="#0F6E6E", variable=kharid_radio_value, font=("Shabnam",11))
kharid_kargah_radio.place(x=330,y=170)


back_to_home_box_kharid=tk.Button(box_kharid,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_kharid_exit)
back_to_home_box_kharid.place(x=140,y=210)

zakhire_radio_box_kharid=tk.Button(box_kharid,text="ادامه",bg="#13f",fg="white",width=12,height=2,command=sabt_radio_kharid)
zakhire_radio_box_kharid.place(x=60,y=210)

box_kharid.protocol("WM_DELETE_WINDOW", lambda: None)
box_kharid.resizable(False, False)
#endregion 
#----------------------------------نوع انتخاب ثبتی فایل برای پنجره های مشارکت-----------------
#region
box_mosharekat=tk.Toplevel(root)
box_mosharekat.title("انتخاب نوع ملک مشارکت")
box_mosharekat.geometry("350x300")
box_mosharekat.withdraw()
box_mosharekat.configure(bg="#0F6E6E")

# یک متغیر مشترک برای همه رادیوباتن‌ها
mosharekat_radio_value = tk.IntVar(value=0)  # مقدار پیش‌فرض -1 یعنی هیچکدام انتخاب نشده

mosharekat_sakht_radio = tk.Radiobutton(box_mosharekat, value=0, text="مشارکت در ساخت", background="#0F6E6E", variable=mosharekat_radio_value, font=("Shabnam",11))
mosharekat_sakht_radio.place(x=200,y=50)

mosharekat_pishforosh_radio = tk.Radiobutton(box_mosharekat, value=2, text="پیش فروش",
bg="#0F6E6E", variable=mosharekat_radio_value, font=("Shabnam",11))
mosharekat_pishforosh_radio.place(x=200,y=90)

back_to_home_box_mosharekat=tk.Button(box_mosharekat,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_mosharekat_exit)
back_to_home_box_mosharekat.place(x=140,y=210)

zakhire_radio_box_mosharekat=tk.Button(box_mosharekat,text="ادامه",bg="#13f",fg="white",width=12,height=2,command=sabt_radio_mosharekat)
zakhire_radio_box_mosharekat.place(x=60,y=210)

box_mosharekat.protocol("WM_DELETE_WINDOW", lambda: None)
box_mosharekat.resizable(False, False)
#endregion
#-----------------پنجره های ثبتی بخش رهن و اجاره----------------------------
#-------------------------------------------پنجره اجاره مسکونی----------------
#region
ejareh_rehn_page = tk.Toplevel(root)
ejareh_rehn_page.title("رهن و اجاره مسکونی")
ejareh_rehn_page.geometry("800x600")
ejareh_rehn_page.withdraw()
ejareh_rehn_page.configure(bg="#0F6E6E")
 
#----------------------پنجره امکانات اجاره مسکونی-----------------------------
option_file_frame_ejareh_maskoni=tk.Toplevel(ejareh_rehn_page,background="#bbfbd1" )
option_file_frame_ejareh_maskoni.title("امکانات اجاره مسکونی ")
option_file_frame_ejareh_maskoni.geometry("500x370")
option_file_frame_ejareh_maskoni.pack_propagate(False)
option_file_frame_ejareh_maskoni.withdraw()


rehn_page_frame_asli_ejareh_maskoni=tk.Frame(ejareh_rehn_page,width=490,height=800,bg="#5d6059",border=2)
rehn_page_frame_asli_ejareh_maskoni.place(x=450,y=40)

melk_type_ejareh_maskoni_lable=tk.Label(rehn_page_frame_asli_ejareh_maskoni,text="نوع ملک",bg="#0F6E6E",fg="#ffffff",width=10)
melk_type_ejareh_maskoni_lable.grid(padx=8,pady=15,sticky="e",row=0,column=1)

melk_type_ejareh_maskoni_entry=tk.Entry(rehn_page_frame_asli_ejareh_maskoni,text="اجاره مسکونی",bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
melk_type_ejareh_maskoni_entry.grid(padx=8, pady=15,row=0,column=0,sticky="w") 

sal_sakht_ejareh_maskoni_lable=tk.Label(rehn_page_frame_asli_ejareh_maskoni,text="سال ساخت",bg="#0F6E6E",fg="#ffffff",width=10)
sal_sakht_ejareh_maskoni_lable.grid(padx=8,pady=10,sticky="e",row=1,column=1)

sal_sakht_ejareh_maskoni_entry=tk.Entry(rehn_page_frame_asli_ejareh_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
sal_sakht_ejareh_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

addrres_ejareh_maskoni_lable=tk.Label(rehn_page_frame_asli_ejareh_maskoni,text="آدرس",bg="#0F6E6E",fg="#ffffff",width=10)
addrres_ejareh_maskoni_lable.grid(padx=8,pady=15,sticky="e",row=2,column=1)

addrres_ejare_maskoni_entry=tk.Entry(rehn_page_frame_asli_ejareh_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
addrres_ejare_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

tabaghe_ejare_maskoni_lable=tk.Label(rehn_page_frame_asli_ejareh_maskoni,text="طبقه",bg="#0F6E6E",fg="#ffffff",width=10)
tabaghe_ejare_maskoni_lable.grid(padx=8,pady=15,sticky="e",row=3,column=1)

tabaghe_ejare_maskoni_entry=tk.Entry(rehn_page_frame_asli_ejareh_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
tabaghe_ejare_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

vahed_ejare_maskoni_lable=tk.Label(rehn_page_frame_asli_ejareh_maskoni,text="واحد",bg="#0F6E6E",fg="#ffffff",width=10)
vahed_ejare_maskoni_lable.grid(padx=8,pady=15,sticky="e",row=4,column=1)

vahed_ejare_maskoni_entry=tk.Entry(rehn_page_frame_asli_ejareh_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
vahed_ejare_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

otagh_ejare_maskoni_lable=tk.Label(rehn_page_frame_asli_ejareh_maskoni,text="اتاق",bg="#0F6E6E",fg="#ffffff",width=10)
otagh_ejare_maskoni_lable.grid(padx=8,pady=15,sticky="e",row=5,column=1)

otagh_ejare_maskoni_entry=tk.Entry(rehn_page_frame_asli_ejareh_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
otagh_ejare_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=5,column=0)

gheimat_ejare_ejare_maskoni_lable=tk.Label(rehn_page_frame_asli_ejareh_maskoni,text="مبلغ اجاره",bg="#0F6E6E",fg="#ffffff",width=10)
gheimat_ejare_ejare_maskoni_lable.grid(padx=8,pady=15,sticky="e",row=7,column=0)

gheimat_pish_ejare_maskoni_lable=tk.Label(rehn_page_frame_asli_ejareh_maskoni,text="مبلغ پیش",bg="#0F6E6E",fg="#ffffff",width=10)
gheimat_pish_ejare_maskoni_lable.grid(padx=8,pady=15,sticky="e",row=7,column=1)

gheimat_ejare_ejare_maskoni_entry=tk.Entry(rehn_page_frame_asli_ejareh_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
gheimat_ejare_ejare_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=8,column=0)

gheimat_pish_ejare_maskoni_entry=tk.Entry(rehn_page_frame_asli_ejareh_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
gheimat_pish_ejare_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=8,column=1)

back_to_home_ejareh_maskoni=tk.Button(ejareh_rehn_page,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_ejare_maskoni)
back_to_home_ejareh_maskoni.place(x=320,y=520)

save_button_ejareh_maskooni=tk.Button(ejareh_rehn_page,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_rehn_maskkoni)
save_button_ejareh_maskooni.place(x=220,y=520)

photo_box_ejare_maskoni=tk.Frame(ejareh_rehn_page,width=410,height=450,background="#e4dde3")
photo_box_ejare_maskoni.place(x=30,y=40)
photo_lbl2_ejare_maskoni = tk.Label(photo_box_ejare_maskoni, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_ejare_maskoni.place(x=30,y=45)
add_img_btn_ejare_maskoni = tk.Button(photo_box_ejare_maskoni, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_ejare_maskoni.place(x=40,y=330)
#endregion
#------------------ساخت امکانات اجاره مسکونی------------------------
#region
option_frame_ejare_maskoni=tk.Frame(ejareh_rehn_page,width=300,height=30,background="#bbfbd1")
option_frame_ejare_maskoni.place(x=525,y=500)

add_option_frame_ejare_maskoni=tk.Label(option_frame_ejare_maskoni,text='افزودن امکانات فایل',font=("Shabnam",10,"bold"),background="#FFFFFF",fg="#000000")
add_option_frame_ejare_maskoni.pack(side="right",padx=1)

button_label_ejare_maskoni=tk.Label(option_frame_ejare_maskoni)
button_label_ejare_maskoni.pack(side="left",padx=1)

plus_button_ejare_maskoni=tk.Button(option_frame_ejare_maskoni,image=plus,command=open_option1,border=0)
plus_button_ejare_maskoni.pack()

option_frame_photos_ejareh_maskoni=tk.Frame(option_file_frame_ejareh_maskoni,width=400,height=100,background="#bbfbd1")
option_frame_photos_ejareh_maskoni.pack(padx=10,pady=15)

parking_checkbutton_btn_ejareh_maskoni=tk.Checkbutton(option_frame_photos_ejareh_maskoni,image=parking_pic,background="#022578")
parking_checkbutton_btn_ejareh_maskoni.pack(padx=15,side="left")

asansor_checkbutton_btn_ejareh_maskoni=tk.Checkbutton(option_frame_photos_ejareh_maskoni,image=elvator_pic,background="#022578")
asansor_checkbutton_btn_ejareh_maskoni.pack(padx=15,side="left")

anbari_checkbutton_btn_ejareh_maskoni=tk.Checkbutton(option_frame_photos_ejareh_maskoni,image=warehouse_pic,background="#022578")
anbari_checkbutton_btn_ejareh_maskoni.pack(padx=15,side="right")

option_frame_combos_ejareh_maskoni=tk.Frame(option_file_frame_ejareh_maskoni,width=400,height=400,background="#bbfbd1",border=1)
option_frame_combos_ejareh_maskoni.pack(padx=10,pady=15)

sarmaesh_ejare_maskoni=tk.Label(option_frame_combos_ejareh_maskoni,text="سرمایش",background="#025578",fg="#ffffff")
sarmaesh_ejare_maskoni.grid(row=0,column=1,padx=15,pady=5)
sarmaesh_ejare_maskoni_combo=ttk.Combobox(option_frame_combos_ejareh_maskoni)
sarmaesh_ejare_maskoni_combo["values"] = ("ندارد","پنکه سقفی","کولر ابی","کولر گازی ","ابی/گازی")
sarmaesh_ejare_maskoni_combo.grid(row=0,column=0,padx=15,pady=5)

garmaesh_ejare_maskoni=tk.Label(option_frame_combos_ejareh_maskoni,text="گرمایش",background="#025578",fg="#ffffff")
garmaesh_ejare_maskoni.grid(row=1,column=1,padx=15,pady=5)
garmaesh_ejare_maskoni_combo=ttk.Combobox(option_frame_combos_ejareh_maskoni)
garmaesh_ejare_maskoni_combo["values"] = ("ندارد","بخاری"," شوفاژ","گرمایش از کف ")
garmaesh_ejare_maskoni_combo.grid(row=1,column=0,padx=15,pady=5)

kaf_ejare_maskoni=tk.Label(option_frame_combos_ejareh_maskoni,text="کف",background="#025578",fg="#ffffff")
kaf_ejare_maskoni.grid(row=2,column=1,padx=15,pady=5)
kaf_ejare_maskoni_combo=ttk.Combobox(option_frame_combos_ejareh_maskoni)
kaf_ejare_maskoni_combo["values"] = ("سرامیک","موزاییک","پارکت")
kaf_ejare_maskoni_combo.grid(row=2,column=0,padx=15,pady=5)

toilet_ejare_maskoni=tk.Label(option_frame_combos_ejareh_maskoni,text="سرویس بهداشتی",background="#025578",fg="#ffffff")
toilet_ejare_maskoni.grid(row=3,column=1,padx=5,pady=5)
toilet_ejare_maskoni_combo=ttk.Combobox(option_frame_combos_ejareh_maskoni)
toilet_ejare_maskoni_combo["values"] = ("ایرانی","فرنگی","هردو")
toilet_ejare_maskoni_combo.grid(row=3,column=0,padx=15,pady=5)

save_optoin_ejareh_maskoni=tk.Button(option_file_frame_ejareh_maskoni,text="ذخیره",command=None,background="#079BDB",fg="#ffffff",width=8)
save_optoin_ejareh_maskoni.place(x=170,y=330)

back_to_ejare_maskoni=tk.Button(option_file_frame_ejareh_maskoni,text="بازگشت",command=back_to_ejareh_maskoni_page,background="#079BDB",fg="#ffffff",width=8)
back_to_ejare_maskoni.place(x=95,y=330)
#endregion
#------------------------پنجره اجاره اداری/تجاری--------------------
#region
ejareh_edari_tejari = tk.Toplevel(root)
ejareh_edari_tejari.title("رهن و اجاره اداری / تجاری")
ejareh_edari_tejari.geometry("800x600")
ejareh_edari_tejari.withdraw()
ejareh_edari_tejari.configure(bg="#0F6E6E")

#--------------------پنجره امکانات اجاره اداری/تجاری----------------------
option_file_frame_ejareh_edari_tajari=tk.Toplevel(ejareh_edari_tejari,background="#bbfbd1" )
option_file_frame_ejareh_edari_tajari.title("امکانات اجاره اداری/تجاری ")
option_file_frame_ejareh_edari_tajari.geometry("500x370")
option_file_frame_ejareh_edari_tajari.pack_propagate(False)
option_file_frame_ejareh_edari_tajari.withdraw()

rehn_page_frame_asli_ejareh_edari_tejari=tk.Frame(ejareh_edari_tejari,width=490,height=800,bg="#5d6059",border=2)
rehn_page_frame_asli_ejareh_edari_tejari.place(x=500,y=50)

melk_type_ejareh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_ejareh_edari_tejari,text="متراژ ملک ",bg="#0F6E6E",fg="#ffffff",width=10)
melk_type_ejareh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=0,column=1)

melk_type_ejareh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_ejareh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
melk_type_ejareh_edari_tejari_entry.grid(padx=8, pady=15,sticky="w",row=0,column=0) 

sal_sakht_ejareh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_ejareh_edari_tejari,text="سال ساخت",bg="#0F6E6E",fg="#ffffff",width=10)
sal_sakht_ejareh_edari_tejari_lable.grid(padx=8,pady=10,sticky="e",row=1,column=1)

sal_sakht_ejareh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_ejareh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
sal_sakht_ejareh_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

addrres_ejareh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_ejareh_edari_tejari,text="آدرس",bg="#0F6E6E",fg="#ffffff",width=10)
addrres_ejareh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=2,column=1)

addrres_ejareh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_ejareh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
addrres_ejareh_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

tabaghe_ejareh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_ejareh_edari_tejari,text="طبقه",bg="#0F6E6E",fg="#ffffff",width=10)
tabaghe_ejareh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=3,column=1)

tabaghe_ejareh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_ejareh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
tabaghe_ejareh_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

vahed_ejareh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_ejareh_edari_tejari,text="واحد",bg="#0F6E6E",fg="#ffffff",width=10)
vahed_ejareh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=4,column=1)

vahed_ejareh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_ejareh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
vahed_ejareh_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)


mablagh_pish_ejareh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_ejareh_edari_tejari,text="مبلغ ودیعه",bg="#0F6E6E",fg="#ffffff",width=10)
mablagh_pish_ejareh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=5,column=1)

mablagh_pish_ejareh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_ejareh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
mablagh_pish_ejareh_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=5,column=0)

mablagh_ejare_ejareh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_ejareh_edari_tejari,text=" مبلغ اجاره",bg="#0F6E6E",fg="#ffffff",width=10)
mablagh_ejare_ejareh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=6,column=1)

mablagh_ejare_ejareh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_ejareh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
mablagh_ejare_ejareh_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=6,column=0)

rahn_kamel_ejareh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_ejareh_edari_tejari,text=" رهن کامل؟ ",bg="#0F6E6E",fg="#ffffff",width=10)
rahn_kamel_ejareh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=7,column=1)

rahn_kamel_checkbutton_ejareh_edari_tejari=tk.Checkbutton(rehn_page_frame_asli_ejareh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
rahn_kamel_checkbutton_ejareh_edari_tejari.grid(padx=8,pady=15,sticky="w",row=7,column=0)

back_to_home_ejareh_edari_tejari=tk.Button(ejareh_edari_tejari,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_ejareh_edari_tejari)
back_to_home_ejareh_edari_tejari.place(x=650,y=535)

zakhire_ejareh_edari_tejari=tk.Button(ejareh_edari_tejari,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_rehn_edari)
zakhire_ejareh_edari_tejari.place(x=550,y=532)

photo_box_ejareh_edari_tejari=tk.Frame(ejareh_edari_tejari,width=410,height=450,background="#e4dde3")
photo_box_ejareh_edari_tejari.place(x=40,y=40)
photo_lbl2_ejareh_edari_tejari = tk.Label(photo_box_ejareh_edari_tejari, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_ejareh_edari_tejari.place(x=30,y=45)
add_img_btn_ejareh_edari_tejari = tk.Button(photo_box_ejareh_edari_tejari, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_ejareh_edari_tejari.place(x=40,y=330)
#endregion
#----------------------ساخت امکانات اجاره اداری/تجاری---------------------
#region
option_frame_ejareh_edari_tejari=tk.Frame(ejareh_edari_tejari,width=300,height=30,background="#bbfbd1")
option_frame_ejareh_edari_tejari.place(x=520,y=475)

option_label_ejareh_edari_tejari=tk.Label(option_frame_ejareh_edari_tejari,text='افزودن امکانات فایل',font=("Shabnam",10,"bold"),background="#FFFFFF",fg="#000000")
option_label_ejareh_edari_tejari.pack(side="right",padx=1)

button_label_ejareh_edari_tejari=tk.Label(option_frame_ejareh_edari_tejari)
button_label_ejareh_edari_tejari.pack(side="left",padx=1)
plus_button_ejareh_edari_tejari=tk.Button(option_frame_ejareh_edari_tejari,image=plus,command=open_option3,border=0)
plus_button_ejareh_edari_tejari.pack()

option_frame_photos_ejareh_edari_tejari=tk.Frame(option_file_frame_ejareh_edari_tajari,width=400,height=100,background="#bbfbd1")
option_frame_photos_ejareh_edari_tejari.pack(padx=10,pady=15)

parking_ch_btn_ejareh_edari_tejari=tk.Checkbutton(option_frame_photos_ejareh_edari_tejari,image=parking_pic,background="#022578")
parking_ch_btn_ejareh_edari_tejari.pack(padx=15,side="left")

elvator_ch_btn_ejareh_edari_tejari=tk.Checkbutton(option_frame_photos_ejareh_edari_tejari,image=elvator_pic,background="#022578")
elvator_ch_btn_ejareh_edari_tejari.pack(padx=15,side="left")

warehouse_ch_btn_ejareh_edari_tejari=tk.Checkbutton(option_frame_photos_ejareh_edari_tejari,image=warehouse_pic,background="#022578")
warehouse_ch_btn_ejareh_edari_tejari.pack(padx=15,side="right")

option_frame_combos_ejareh_edari_tejari=tk.Frame(option_file_frame_ejareh_edari_tajari,width=400,height=400,background="#bbfbd1",border=1)
option_frame_combos_ejareh_edari_tejari.pack(padx=10,pady=15)


ab_va_gaz_emkanat_ejareh_edari_tejari=tk.Label(option_frame_combos_ejareh_edari_tejari,text="وضعیت آب و گاز",background="#0F6E6E",fg="#ffffff",width=17)
ab_va_gaz_emkanat_ejareh_edari_tejari.grid(padx=8,pady=15,row=0,column=1)

ab_va_gaz_combo_emkanat_ejareh_edari_tejari=ttk.Combobox(option_frame_combos_ejareh_edari_tejari)
ab_va_gaz_combo_emkanat_ejareh_edari_tejari["values"] = ("فقط گاز دارد","فقط آب دارد","آب و گاز دارد")
ab_va_gaz_combo_emkanat_ejareh_edari_tejari.grid(padx=8,pady=15,row=0,column=0)

sarmayesh_emkanat_ejareh_edari_tejari=tk.Label(option_frame_combos_ejareh_edari_tejari,text="سیستم سرمایش",background="#0F6E6E",fg="#ffffff",width=17)
sarmayesh_emkanat_ejareh_edari_tejari.grid(padx=8,pady=15,row=4,column=1)

sarmayesh_combo_emkanat_ejareh_edari_tejari=ttk.Combobox(option_frame_combos_ejareh_edari_tejari)
sarmayesh_combo_emkanat_ejareh_edari_tejari["values"] = (" کولر گازی"," کولرآبی","پنکه سقفی","ندارد")
sarmayesh_combo_emkanat_ejareh_edari_tejari.grid(padx=8,pady=15,row=4,column=0)

garmayesh_emkanat_ejareh_edari_tejari=tk.Label(option_frame_combos_ejareh_edari_tejari,text="سیستم گرمایش",background="#0F6E6E",fg="#ffffff",width=17)
garmayesh_emkanat_ejareh_edari_tejari.grid(padx=8,pady=15,row=5,column=1)

garmayesh_combo_emkanat_ejareh_edari_tejari=ttk.Combobox(option_frame_combos_ejareh_edari_tejari)
garmayesh_combo_emkanat_ejareh_edari_tejari["values"] = (" شوفاژ"," بخاری","ندارد")
garmayesh_combo_emkanat_ejareh_edari_tejari.grid(padx=8,pady=15,row=5,column=0)

save_optoin_ejareh_maskoni=tk.Button(option_file_frame_ejareh_edari_tajari,text="ذخیره",command=None,background="#079BDB",fg="#ffffff",width=8)
save_optoin_ejareh_maskoni.place(x=170,y=330)

back_to_home_ejareh_edari_tejari=tk.Button(option_file_frame_ejareh_edari_tajari,text="بازگشت",command=back_to_ejareh_edari_tejari,background="#079BDB",fg="#ffffff",width=8)
back_to_home_ejareh_edari_tejari.place(x=95,y=330)
#endregion

#-------------------پنجره اجاره باغ/زمین------------------------
#region
ejareh_bagh_zamin = tk.Toplevel(root)
ejareh_bagh_zamin.title(" اجاره باغ و زمین")
ejareh_bagh_zamin.geometry("800x600")
ejareh_bagh_zamin.withdraw()
ejareh_bagh_zamin.configure(bg="#0F6E6E")

ejareh_bagh_zamin_frame=tk.Frame(ejareh_bagh_zamin,width=490,height=800,bg="#5d6059",border=2)
ejareh_bagh_zamin_frame.place(x=500,y=90)

metraj_zamin_ejareh_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin_frame,text="متراژ",bg="#0F6E6E",fg="#ffffff",width=10)
metraj_zamin_ejareh_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=0,column=1)

metraj_zamin_ejareh_bagh_zamin_entry=tk.Entry(ejareh_bagh_zamin_frame,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),textvariable="متر مربع")
metraj_zamin_ejareh_bagh_zamin_entry.grid(padx=8,pady=15,sticky="w",row=0,column=0)

bagh_type_lable=tk.Label(ejareh_bagh_zamin_frame,text="کاربری زمین",bg="#0F6E6E",fg="#ffffff",width=10)
bagh_type_lable.grid(padx=8,pady=15,sticky="e",row=1,column=1)

bagh_type_combo=ttk.Combobox(ejareh_bagh_zamin_frame,state="readonly")
bagh_type_combo["values"]=("باغ","زمین کشاورزی")
bagh_type_combo.set("باغ")
bagh_type_combo.grid(padx=8,pady=15,sticky="w",row=1,column=0)

bagh_loctaion_lable=tk.Label(ejareh_bagh_zamin_frame,text="منطقه و ادرس ",bg="#0F6E6E",fg="#ffffff",width=10)
bagh_loctaion_lable.grid(padx=8,pady=15,sticky="e",row=2,column=1)

bagh_loctaion_entry=tk.Entry(ejareh_bagh_zamin_frame,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
bagh_loctaion_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

bagh_gheimat_ejareh_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin_frame,text='ودیعه',bg="#0F6E6E",fg="#ffffff",width=10)
bagh_gheimat_ejareh_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=3,column=1)

bagh_gheimat_ejareh_bagh_zamin_entry=tk.Entry(ejareh_bagh_zamin_frame,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
bagh_gheimat_ejareh_bagh_zamin_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

bagh_gheimat_har_metr_ejareh_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin_frame,text='قیمت هر متر',bg="#0F6E6E",fg="#ffffff",width=10)
bagh_gheimat_har_metr_ejareh_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=4,column=1)

bagh_gheimat_ejareh_bagh_zamin_entry=tk.Entry(ejareh_bagh_zamin_frame,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
bagh_gheimat_ejareh_bagh_zamin_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

time_bagh_ejareh_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin_frame,text="مدت اجاره",bg="#0F6E6E",fg="#ffffff",width=10)
time_bagh_ejareh_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=5,column=1)

bagh_time_combo=ttk.Combobox(ejareh_bagh_zamin_frame,state="readonly")
bagh_time_combo["values"]=("بلندمدت","کوتاه مدت","فصلی","سالانه")
bagh_time_combo.set("فصلی")
bagh_time_combo.grid(padx=8,pady=15,sticky="w",row=5,column=0)

photo_box_ejareh_bagh_zamin=tk.Frame(ejareh_bagh_zamin,width=410,height=450,background="#e4dde3")
photo_box_ejareh_bagh_zamin.place(x=50,y=40)

photo_lbl2_ejareh_bagh_zamin = tk.Label(photo_box_ejareh_bagh_zamin, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_ejareh_bagh_zamin.place(x=30,y=45)
add_img_btn_ejareh_bagh_zamin = tk.Button(photo_box_ejareh_bagh_zamin, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_ejareh_bagh_zamin.place(x=40,y=330)

back_to_home_ejareh_bagh_zamin=tk.Button(ejareh_bagh_zamin,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_ejareh_bagh)
back_to_home_ejareh_bagh_zamin.place(x=320,y=520)

zakhire_ejareh_bagh_zamin=tk.Button(ejareh_bagh_zamin,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_rehn_bagh)
zakhire_ejareh_bagh_zamin.place(x=220,y=520)
#endregion
#---------------------امکانات اجاره باغ/زمین---------------------
#region
option_frame_ejareh_bagh_zamin=tk.Frame(ejareh_bagh_zamin,width=300,height=30,background="#bbfbd1")
option_frame_ejareh_bagh_zamin.place(x=550,y=450)

option_label_ejareh_bagh_zamin=tk.Label(option_frame_ejareh_bagh_zamin,text='افزودن امکانات فایل',font=("Shabnam",10,"bold"),background="#FFFFFF",fg="#000000")
option_label_ejareh_bagh_zamin.pack(side="right",padx=1)

button_label_ejareh_bagh_zamin=tk.Label(option_frame_ejareh_bagh_zamin)
button_label_ejareh_bagh_zamin.pack(side="left",padx=1)
plus_button_ejareh_bagh_zamin=tk.Button(option_frame_ejareh_bagh_zamin,image=plus,command=open_option5,border=0)
plus_button_ejareh_bagh_zamin.pack()

option_file_frame_ejareh_bagh_zamin=tk.Toplevel(ejareh_bagh_zamin,background="#bbfbd1")
option_file_frame_ejareh_bagh_zamin.title(" امکانات اجاره باغ/زمین")
option_file_frame_ejareh_bagh_zamin.geometry("690x630")
option_file_frame_ejareh_bagh_zamin.pack_propagate(False)
option_file_frame_ejareh_bagh_zamin.withdraw()
mini_frame_ejareh_bagh_zamin=tk.Frame(option_file_frame_ejareh_bagh_zamin)
mini_frame_ejareh_bagh_zamin.place(x=290,y=20)
karbari_zamin_ejareh_bagh_zamin_lable=tk.Label(mini_frame_ejareh_bagh_zamin,text="کاربری زمین",bg="#0F6E6E",fg="#ffffff",width=10)
karbari_zamin_ejareh_bagh_zamin_lable.pack(padx=5,pady=5,side="right")

karbari_zamin_combo=ttk.Combobox(mini_frame_ejareh_bagh_zamin,state="readonly")
karbari_zamin_combo["values"]=("باغ","زمین کشاورزی")
karbari_zamin_combo.set("باغ")
karbari_zamin_combo.pack(padx=5,pady=5,side="left")

karbari_zamin_combo.bind("<<ComboboxSelected>>",change_bagh_zamin1)

option_frame_options_ejareh_bagh_zamin=tk.Frame(option_file_frame_ejareh_bagh_zamin,width=430,height=290,background="#d1e0df")
option_frame_options_ejareh_bagh_zamin.place(x=60,y=60)

metraj_tree=tk.Label(option_frame_options_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="متراژ درخت کاری")
metraj_tree.grid(padx=10,pady=5,row=0,column=4)

metraj_tree_entry=tk.Entry(option_frame_options_ejareh_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff")
metraj_tree_entry.grid(padx=10,pady=5,row=0,column=3)

tree_count=tk.Label(option_frame_options_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="تعداد درخت")
tree_count.grid(padx=10,pady=5,row=1,column=4)

tree_count_entry=tk.Entry(option_frame_options_ejareh_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff")
tree_count_entry.grid(padx=10,pady=5,row=1,column=3)
abyari=tk.Label(option_frame_options_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع ابیاری")
abyari.grid(padx=10,pady=5,row=2,column=4)

abyari_combo=ttk.Combobox(option_frame_options_ejareh_bagh_zamin)
abyari_combo["values"]=("سطحی","بارانی","قطره ای","تحت فشار")
abyari_combo.set("سطحی")
abyari_combo.grid(padx=10,pady=5,row=2,column=3)

type_tree=tk.Label(option_frame_options_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع درخت")
type_tree.grid(padx=10,pady=5,row=3,column=4)

type_tree_combo=ttk.Combobox(option_frame_options_ejareh_bagh_zamin)
type_tree_combo["values"]=(" ","پسته","بادام","گردو","شلیل","هلو","سیب","انگور"
                           ,"انجیر","زردالو","گیلاس","البالو")
type_tree_combo.set("گردو")
type_tree_combo.grid(padx=10,pady=5,row=3,column=3)
add_tree_button=tk.Button(option_frame_options_ejareh_bagh_zamin,text="افزودن درخت",command=add_tree,bg="#007acc",width=10)
add_tree_button.grid(padx=10,pady=5,row=4,column=4)

label_result_add=tk.Label(option_frame_options_ejareh_bagh_zamin,text="")
label_result_add.grid(padx=10,pady=5,row=4,column=3)

chah_bagh=tk.Checkbutton(option_frame_options_ejareh_bagh_zamin,text="چاه",background="#d6d0d0")
chah_bagh.grid(padx=0,pady=5,row=5,column=0)

estakhr_bagh=tk.Checkbutton(option_frame_options_ejareh_bagh_zamin,text="استخر",background="#d6d0d0")
estakhr_bagh.grid(padx=0,pady=5,row=5,column=1)

loleh_bagh=tk.Checkbutton(option_frame_options_ejareh_bagh_zamin,text="اب لوله کشی",background="#d6d0d0")
loleh_bagh.grid(padx=0,pady=5,row=5,column=2)

bargh_bagh=tk.Checkbutton(option_frame_options_ejareh_bagh_zamin,text="برق کشی",background="#d6d0d0")
bargh_bagh.grid(padx=0,pady=5,row=5,column=3)

gas_bagh=tk.Checkbutton(option_frame_options_ejareh_bagh_zamin,text="گاز کشی",background="#d6d0d0")
gas_bagh.grid(padx=0,pady=5,row=5,column=4)

var0=tk.IntVar(value=0)#چک باتن پیش فرض تیک نخورده باشه

room_bagh_checkbutton=tk.Checkbutton(option_frame_options_ejareh_bagh_zamin,variable=var0,image=warehouse_pic,background="#022578",text="ساختمان",command=home_true_false1)
room_bagh_checkbutton.grid(padx=10,pady=5,row=6,column=4)

metraj_vila_bagh_lable=tk.Label(option_frame_options_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="متراژ سازه")
metraj_vila_bagh_lable.grid(padx=10,pady=5,row=7,column=4)

metraj_vila_bagh_entry=tk.Entry(option_frame_options_ejareh_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
metraj_vila_bagh_entry.grid(padx=10,pady=5,row=7,column=3)

sal_sakht_vila_bagh_lable=tk.Label(option_frame_options_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="سال ساخت")
sal_sakht_vila_bagh_lable.grid(padx=10,pady=5,row=8,column=4)

sal_sakht_vila_bagh_entry=tk.Entry(option_frame_options_ejareh_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
sal_sakht_vila_bagh_entry.grid(padx=10,pady=5,row=8,column=3)

type_vila_ejareh_bagh_zamin=tk.Label(option_frame_options_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="نوع سازه")
type_vila_ejareh_bagh_zamin.grid(padx=10,pady=5,row=9,column=4)

type_vila_ejareh_bagh_zamin_combo=ttk.Combobox(option_frame_options_ejareh_bagh_zamin,state="disabled")
type_vila_ejareh_bagh_zamin_combo["values"]=("آجری","بلوکی","کانکس","چوبی")
type_vila_ejareh_bagh_zamin_combo.set("آجری")
type_vila_ejareh_bagh_zamin_combo.grid(padx=10,pady=5,row=9,column=3)

toilet_bagh=tk.Label(option_frame_options_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="سرویس بهداشتی")
toilet_bagh.grid(padx=10,pady=5,row=10,column=4)

toilet_bagh_combo=ttk.Combobox(option_frame_options_ejareh_bagh_zamin,state="disabled")
toilet_bagh_combo["values"]=(" ","ندارد","فرنگی","ایرانی","هردو")
toilet_bagh_combo.set("")
toilet_bagh_combo.grid(padx=10,pady=5,row=10,column=3)

hamam_bagh=tk.Label(option_frame_options_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="حمام")
hamam_bagh.grid(padx=10,pady=5,row=11,column=4)

hamam_bagh_combo=ttk.Combobox(option_frame_options_ejareh_bagh_zamin,state="disabled")
hamam_bagh_combo["values"]=(" ","ندارد","دارد")
hamam_bagh_combo.set(" ")
hamam_bagh_combo.grid(padx=10,pady=5,row=11,column=3)

sanad_bagh=tk.Label(option_frame_options_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="سند")
sanad_bagh.grid(padx=10,pady=5,row=12,column=4)

sanad_bagh_combo=ttk.Combobox(option_frame_options_ejareh_bagh_zamin,state="disabled")
sanad_bagh_combo["values"]=(" ","ندارد","تک برگ","قولنامه ای","مشاع")
sanad_bagh_combo.set(" ")
sanad_bagh_combo.grid(padx=10,pady=5,row=12,column=3)

option_ejareh_bagh_zamin=tk.Label(option_frame_options_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="امکانات تفریحی")
option_ejareh_bagh_zamin.grid(padx=10,pady=5,row=13,column=4)

option_ejareh_bagh_zamin_combo=ttk.Combobox(option_frame_options_ejareh_bagh_zamin,state="disabled")
option_ejareh_bagh_zamin_combo["values"]=(" ","استخر","جکوزی","باربیکیو")
option_ejareh_bagh_zamin_combo.set(" ")
option_ejareh_bagh_zamin_combo.grid(padx=10,pady=5,row=13,column=3)

add_option_button=tk.Button(option_frame_options_ejareh_bagh_zamin,text="افزودن امکانات",command=add_option,bg="#007acc",width=10)
add_option_button.grid(padx=10,pady=5,row=13,column=2)
label_result2_add=tk.Label(option_frame_options_ejareh_bagh_zamin,text="")
label_result2_add.grid(padx=10,pady=5,row=13,column=1)

mojavez_sakht_ejareh_bagh_zamin=tk.Checkbutton(option_frame_options_ejareh_bagh_zamin,text="مجوز ساختن",background="#d6d0d0",state="disabled")
mojavez_sakht_ejareh_bagh_zamin.grid(padx=10,pady=5,row=14,column=4)

mohavate_ejareh_bagh_zamin=tk.Checkbutton(option_frame_options_ejareh_bagh_zamin,text="محوطه سازی",background="#d6d0d0",state="disabled")
mohavate_ejareh_bagh_zamin.grid(padx=10,pady=5,row=14,column=3)

divar_ejareh_bagh_zamin=tk.Checkbutton(option_frame_options_ejareh_bagh_zamin,text="دیوار کشی",background="#d6d0d0")
divar_ejareh_bagh_zamin.grid(padx=10,pady=5,row=14,column=2)

zakhire_option_ejareh_bagh_zamin=tk.Button(option_file_frame_ejareh_bagh_zamin,text="ذخیره",background="#079BDB",fg="#ffffff",width=8)
zakhire_option_ejareh_bagh_zamin.place(x=170,y=580)

back_to_ejareh_bagh_zamin=tk.Button(option_file_frame_ejareh_bagh_zamin,text="بازگشت",command=back_to_ejareh_bagh_zamin,background="#079BDB",fg="#ffffff",width=8)
back_to_ejareh_bagh_zamin.place(x=95,y=580)
#endregion
#-------------------تعویض کاربری به زمین در قسمت اجاره باغ/زمین--------------
#region
fram_option_zamin_ejareh_bagh_zamin=tk.Frame(option_file_frame_ejareh_bagh_zamin,width=445,height=290,background="#d1e0df")
fram_option_zamin_ejareh_bagh_zamin.place_forget()

metraj_zamin_ejareh_bagh_zamin2=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="متراژ زمین")
metraj_zamin_ejareh_bagh_zamin2.grid(padx=10,pady=5,row=0,column=4)

metraj_zamin_ejareh_bagh_zamin_entry2=tk.Entry(fram_option_zamin_ejareh_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff")
metraj_zamin_ejareh_bagh_zamin_entry2.grid(padx=10,pady=5,row=0,column=3)

karbari_ejareh_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع کاربری")
karbari_ejareh_ejareh_bagh_zamin.grid(padx=10,pady=5,row=1,column=4)

karbari_ejareh_ejareh_bagh_zamin_combo=ttk.Combobox(fram_option_zamin_ejareh_bagh_zamin)
karbari_ejareh_ejareh_bagh_zamin_combo["values"]=(" ","زراعی","باغی","گلخانه ای","دامداری ","مرغداری",
                               "دامداری و مرغداری","آیش")                             
karbari_ejareh_ejareh_bagh_zamin_combo.set(" ")
karbari_ejareh_ejareh_bagh_zamin_combo.grid(padx=10,pady=5,row=1,column=3)

khak_ejareh_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع خاک")
khak_ejareh_ejareh_bagh_zamin.grid(padx=10,pady=5,row=2,column=4)

khak_ejareh_ejareh_bagh_zamin_combo=ttk.Combobox(fram_option_zamin_ejareh_bagh_zamin)
khak_ejareh_ejareh_bagh_zamin_combo["values"]=(" ","رسی","شنی","لومی","رسی_شنی","شنی_لومی",
                               "رسی_لومی")                             
khak_ejareh_ejareh_bagh_zamin_combo.set(" ")
khak_ejareh_ejareh_bagh_zamin_combo.grid(padx=10,pady=5,row=2,column=3)

ab_ejareh_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="منبع اب")
ab_ejareh_ejareh_bagh_zamin.grid(padx=10,pady=5,row=3,column=4)

ab_ejareh_ejareh_bagh_zamin_combo=ttk.Combobox(fram_option_zamin_ejareh_bagh_zamin)
ab_ejareh_ejareh_bagh_zamin_combo["values"]=(" ","چاه","قنات","رودخانه","کانال ابیاری","چشمه",
                               "آب لوله کشی کشاورزی","تانکر","استخر")                             
ab_ejareh_ejareh_bagh_zamin_combo.set(" ")
ab_ejareh_ejareh_bagh_zamin_combo.grid(padx=10,pady=5,row=3,column=3)

zamin_shekl_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="توپوگرافی")
zamin_shekl_ejareh_bagh_zamin.grid(padx=10,pady=5,row=4,column=4)

zamin_shekl_ejareh_bagh_zamin_combo=ttk.Combobox(fram_option_zamin_ejareh_bagh_zamin)
zamin_shekl_ejareh_bagh_zamin_combo["values"]=(" "," صاف و یکدست"," شیب دار"," باتلاقی","سنگی ")                             
zamin_shekl_ejareh_bagh_zamin_combo.set(" ")
zamin_shekl_ejareh_bagh_zamin_combo.grid(padx=10,pady=5,row=4,column=3)

add_topo_button=tk.Button(fram_option_zamin_ejareh_bagh_zamin,text=" مورد دلخواه",command=add_topo1,bg="#007acc",width=10)
add_topo_button.grid(padx=10,pady=5,row=4,column=2)
label_natige_topo_add_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,text="")
label_natige_topo_add_ejareh_bagh_zamin.grid(padx=10,pady=5,row=4,column=1)

kesht_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="سطح زیر کشت")
kesht_ejareh_bagh_zamin.grid(padx=10,pady=5,row=5,column=4)

kesht_ejareh_bagh_zamin_combo=ttk.Combobox(fram_option_zamin_ejareh_bagh_zamin)
kesht_ejareh_bagh_zamin_combo["values"]=("بدون کشت"," زیر کشت")                             
kesht_ejareh_bagh_zamin_combo.set("بدون کشت ")
kesht_ejareh_bagh_zamin_combo.grid(padx=10,pady=5,row=5,column=3)
kesht_ejareh_bagh_zamin_combo.bind("<<ComboboxSelected>>",choos_kesht)

kesht_ejareh_bagh_zamin_label=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="محصول زیرکشت")
kesht_ejareh_bagh_zamin_label.grid(padx=10,pady=5,row=5,column=2)

kesht_ejareh_bagh_zamin_entry=tk.Entry(fram_option_zamin_ejareh_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
kesht_ejareh_bagh_zamin_entry.grid(padx=10,pady=5,row=5,column=1)

security_room_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="اتاق نگهبان",background="#d6d0d0")
security_room_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=6,column=0)

bargh_tak_faz_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="برق تک فاز",background="#d6d0d0")
bargh_tak_faz_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=6,column=1)

bargh_se_faz_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="برق سه فاز",background="#d6d0d0")
bargh_se_faz_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=6,column=2)

anbar_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="انبار/سوله",background="#d6d0d0")
anbar_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=6,column=3)

fans_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="فنس/دیوار",background="#d6d0d0")
fans_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=6,column=4)

mojavez_golkhane_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="اجازه ساخت گلخانه",background="#d6d0d0")
mojavez_golkhane_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=7,column=0)

mojavaz_chah_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="اجازه حفر چاه",background="#d6d0d0")
mojavaz_chah_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=7,column=1)

bardasht_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="حق برداشت ",background="#d6d0d0")
bardasht_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=7,column=2)

dam_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="اجازه ورود دام",background="#d6d0d0")
dam_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=7,column=3)

#=======================================================================
#endregion
#---------------------------پنجره های ثبتی بخش فروش--------------------
#-------------------پنجره فروش مسکونی----------------------
#region
forosh_rehn_page = tk.Toplevel(root)
forosh_rehn_page.title("فروش مسکونی")
forosh_rehn_page.geometry("800x600")
forosh_rehn_page.withdraw()
forosh_rehn_page.configure(bg="#0F6E6E")

#---------------------پنجره امکانات فروش مسکونی----------------------
option_file_frame_forosh_maskoni=tk.Toplevel(forosh_rehn_page,background="#bbfbd1" )
option_file_frame_forosh_maskoni.title(" امکانات فروش مسکونی")
option_file_frame_forosh_maskoni.geometry("500x370")
option_file_frame_forosh_maskoni.pack_propagate(False)
option_file_frame_forosh_maskoni.withdraw()

rehn_page_frame_forosh_maskoni=tk.Frame(forosh_rehn_page,width=490,height=800,bg="#5d6059",border=2)
rehn_page_frame_forosh_maskoni.place(x=500,y=50)

melk_type_forosh_maskoni=tk.Label(rehn_page_frame_forosh_maskoni,text="نوع ملک",bg="#0F6E6E",fg="#ffffff",width=10)
melk_type_forosh_maskoni.grid(padx=8,pady=15,sticky="e",row=0,column=1)

melk_type_forosh_maskoni_entry=tk.Entry(rehn_page_frame_forosh_maskoni,text="فروش مسکونی",bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
melk_type_forosh_maskoni_entry.grid(padx=8, pady=15,row=0,column=0,sticky="w") 

sal_sakht_forosh_maskoni=tk.Label(rehn_page_frame_forosh_maskoni,text="سال ساخت",bg="#0F6E6E",fg="#ffffff",width=10)
sal_sakht_forosh_maskoni.grid(padx=8,pady=10,sticky="e",row=1,column=1)

sal_sakht_forosh_maskoni_entry=tk.Entry(rehn_page_frame_forosh_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
sal_sakht_forosh_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

addrres_forosh_maskoni=tk.Label(rehn_page_frame_forosh_maskoni,text="آدرس",bg="#0F6E6E",fg="#ffffff",width=10)
addrres_forosh_maskoni.grid(padx=8,pady=15,sticky="e",row=2,column=1)

addrres_forosh_maskoni_entry=tk.Entry(rehn_page_frame_forosh_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
addrres_forosh_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

tabaghe_forosh_maskoni=tk.Label(rehn_page_frame_forosh_maskoni,text="طبقه",bg="#0F6E6E",fg="#ffffff",width=10)
tabaghe_forosh_maskoni.grid(padx=8,pady=15,sticky="e",row=3,column=1)

tabaghe_forosh_maskoni_entry=tk.Entry(rehn_page_frame_forosh_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
tabaghe_forosh_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

vahed_forosh_maskoni=tk.Label(rehn_page_frame_forosh_maskoni,text="واحد",bg="#0F6E6E",fg="#ffffff",width=10)
vahed_forosh_maskoni.grid(padx=8,pady=15,sticky="e",row=4,column=1)

vahed_forosh_maskoni_entry=tk.Entry(rehn_page_frame_forosh_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
vahed_forosh_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

otagh_forosh_maskoni=tk.Label(rehn_page_frame_forosh_maskoni,text="اتاق",bg="#0F6E6E",fg="#ffffff",width=10)
otagh_forosh_maskoni.grid(padx=8,pady=15,sticky="e",row=5,column=1)

otagh_forosh_maskoni_entry=tk.Entry(rehn_page_frame_forosh_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
otagh_forosh_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=5,column=0)

gheimat_forosh_maskoni=tk.Label(rehn_page_frame_forosh_maskoni,text="قیمت",bg="#0F6E6E",fg="#ffffff",width=10)
gheimat_forosh_maskoni.grid(padx=8,pady=15,sticky="e",row=6,column=1)

gheimat_forosh_maskoni_entry=tk.Entry(rehn_page_frame_forosh_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
gheimat_forosh_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=6,column=0)

back_to_home_forosh_maskoni=tk.Button(forosh_rehn_page,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_forosh_maskoni)
back_to_home_forosh_maskoni.place(x=650,y=535)

zakhire_forosh_maskoni=tk.Button(forosh_rehn_page,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_forosh_maskkoni)
zakhire_forosh_maskoni.place(x=550,y=535)

photo_box_forosh_maskoni=tk.Frame(forosh_rehn_page,width=410,height=450,background="#e4dde3")
photo_box_forosh_maskoni.place(x=40,y=40)
photo_lbl2_forosh_maskoni = tk.Label(photo_box_forosh_maskoni, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_forosh_maskoni.place(x=30,y=45)
add_img_btn_forosh_maskoni = tk.Button(photo_box_forosh_maskoni, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_forosh_maskoni.place(x=40,y=330)
#endregion
#------------------------امکانات فروش مسکونی--------------------
#region
option_frame_options_forosh_maskoni=tk.Frame(forosh_rehn_page,width=300,height=30,background="#bbfbd1")
option_frame_options_forosh_maskoni.place(x=520,y=460)

option_label_forosh_maskoni=tk.Label(option_frame_options_forosh_maskoni,text='افزودن امکانات فایل',font=("Shabnam",10,"bold"),background="#FFFFFF",fg="#000000")
option_label_forosh_maskoni.pack(side="right",padx=1)

button_label_forosh_maskoni=tk.Label(option_frame_options_forosh_maskoni)
button_label_forosh_maskoni.pack(side="left",padx=1)
plus_button_forosh_maskoni=tk.Button(option_frame_options_forosh_maskoni,image=plus,command=open_option2,border=0)
plus_button_forosh_maskoni.pack()

option_lable_forosh_maskoni=tk.Frame(option_file_frame_forosh_maskoni,width=400,height=100,background="#bbfbd1")
option_lable_forosh_maskoni.pack(padx=10,pady=15)

parking_ch_btn_forosh_maskoni=tk.Checkbutton(option_lable_forosh_maskoni,image=parking_pic,background="#022578")
parking_ch_btn_forosh_maskoni.pack(padx=15,side="left")

asansor_ch_btn_forosh_maskoni=tk.Checkbutton(option_lable_forosh_maskoni,image=elvator_pic,background="#022578")
asansor_ch_btn_forosh_maskoni.pack(padx=15,side="left")

anbari_checkbuton_forosh_maskoni=tk.Checkbutton(option_lable_forosh_maskoni,image=warehouse_pic,background="#022578")
anbari_checkbuton_forosh_maskoni.pack(padx=15,side="right")

option_frame_options_forosh_maskoni2=tk.Frame(option_file_frame_forosh_maskoni,width=400,height=400,background="#bbfbd1",border=1)
option_frame_options_forosh_maskoni2.pack(padx=10,pady=15)

sarmaesh_forosh_maskoni=tk.Label(option_frame_options_forosh_maskoni2,text="سرمایش",background="#025578",fg="#ffffff")
sarmaesh_forosh_maskoni.grid(row=0,column=1,padx=15,pady=5)
sarmaesh_combo_forosh_maskoni=ttk.Combobox(option_frame_options_forosh_maskoni2)
sarmaesh_combo_forosh_maskoni["values"] = ("ندارد","پنکه سقفی","کولر ابی","کولر گازی ","ابی/گازی")
sarmaesh_combo_forosh_maskoni.grid(row=0,column=0,padx=15,pady=5)

garmaesh_forosh_maskoni=tk.Label(option_frame_options_forosh_maskoni2,text="گرمایش",background="#025578",fg="#ffffff")
garmaesh_forosh_maskoni.grid(row=1,column=1,padx=15,pady=5)
garmaesh_combo_forosh_maskoni=ttk.Combobox(option_frame_options_forosh_maskoni2)
garmaesh_combo_forosh_maskoni["values"] = ("ندارد","بخاری"," شوفاژ","گرمایش از کف ")
garmaesh_combo_forosh_maskoni.grid(row=1,column=0,padx=15,pady=5)

kaf_forosh_maskoni=tk.Label(option_frame_options_forosh_maskoni2,text="کف",background="#025578",fg="#ffffff")
kaf_forosh_maskoni.grid(row=2,column=1,padx=15,pady=5)
kaf_combo_forosh_maskoni=ttk.Combobox(option_frame_options_forosh_maskoni2)
kaf_combo_forosh_maskoni["values"] = ("سرامیک","موزاییک","پارکت")
kaf_combo_forosh_maskoni.grid(row=2,column=0,padx=15,pady=5)

toilet_forosh_maskoni=tk.Label(option_frame_options_forosh_maskoni2,text="سرویس بهداشتی",background="#025578",fg="#ffffff")
toilet_forosh_maskoni.grid(row=3,column=1,padx=5,pady=5)
toilet_combo_forosh_maskoni=ttk.Combobox(option_frame_options_forosh_maskoni2)
toilet_combo_forosh_maskoni["values"] = ("ایرانی","فرنگی","هردو")
toilet_combo_forosh_maskoni.grid(row=3,column=0,padx=15,pady=5)

zakhire_options_forosh_maskini=tk.Button(option_file_frame_forosh_maskoni,text="ذخیره",command=None,background="#079BDB",fg="#ffffff",width=8)
zakhire_options_forosh_maskini.place(x=170,y=330)

back_to_home_forosh_maskoni=tk.Button(option_file_frame_forosh_maskoni,text="بازگشت",command=back_to_forosh_maskoni_page,background="#079BDB",fg="#ffffff",width=8)
back_to_home_forosh_maskoni.place(x=95,y=330)
#endregion
#-----------------پنجره فروش اداری/تجاری-------------------
#region
forosh_edari_tejari = tk.Toplevel(root)
forosh_edari_tejari.title(" فروش اداری / تجاری")
forosh_edari_tejari.geometry("800x600")
forosh_edari_tejari.withdraw()
forosh_edari_tejari.configure(bg="#0F6E6E")

#---------------پنجره امکانات فروش اداری/تجاری----------------

option_file_frame_forosh_edari_tejari=tk.Toplevel(forosh_edari_tejari,background="#bbfbd1" )
option_file_frame_forosh_edari_tejari.title(" امکانات فروش اداری/تجاری")
option_file_frame_forosh_edari_tejari.geometry("500x370")
option_file_frame_forosh_edari_tejari.pack_propagate(False)
option_file_frame_forosh_edari_tejari.withdraw()

rehn_page_frame_asli_forosh_edari_tejari=tk.Frame(forosh_edari_tejari,width=490,height=800,bg="#5d6059",border=2)
rehn_page_frame_asli_forosh_edari_tejari.place(x=500,y=50)

melk_type_forosh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_forosh_edari_tejari,text="متراژ ملک ",bg="#0F6E6E",fg="#ffffff",width=10)
melk_type_forosh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=0,column=1)

melk_type_forosh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_forosh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
melk_type_forosh_edari_tejari_entry.grid(padx=8, pady=15,sticky="w",row=0,column=0) 

sal_sakht_forosh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_forosh_edari_tejari,text="سال ساخت",bg="#0F6E6E",fg="#ffffff",width=10)
sal_sakht_forosh_edari_tejari_lable.grid(padx=8,pady=10,sticky="e",row=1,column=1)

sal_sakht_forosh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_forosh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
sal_sakht_forosh_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

addrres_forosh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_forosh_edari_tejari,text="آدرس",bg="#0F6E6E",fg="#ffffff",width=10)
addrres_forosh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=2,column=1)

addrres_forosh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_forosh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
addrres_forosh_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

tabaghe_forosh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_forosh_edari_tejari,text="طبقه",bg="#0F6E6E",fg="#ffffff",width=10)
tabaghe_forosh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=3,column=1)

tabaghe_forosh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_forosh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
tabaghe_forosh_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

vahed_forosh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_forosh_edari_tejari,text="واحد",bg="#0F6E6E",fg="#ffffff",width=10)
vahed_forosh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=4,column=1)

vahed_forosh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_forosh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
vahed_forosh_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)


mablagh_pish_forosh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_forosh_edari_tejari,text="مبلغ ودیعه",bg="#0F6E6E",fg="#ffffff",width=10)
mablagh_pish_forosh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=5,column=1)

mablagh_pish_forosh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_forosh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
mablagh_pish_forosh_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=5,column=0)

mablagh_ejare_forosh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_forosh_edari_tejari,text=" مبلغ اجاره",bg="#0F6E6E",fg="#ffffff",width=10)
mablagh_ejare_forosh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=6,column=1)

mablagh_ejare_forosh_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_forosh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
mablagh_ejare_forosh_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=6,column=0)

rahn_kamel_forosh_edari_tejari_lable=tk.Label(rehn_page_frame_asli_forosh_edari_tejari,text=" رهن کامل؟ ",bg="#0F6E6E",fg="#ffffff",width=10)
rahn_kamel_forosh_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=7,column=1)

rahn_kamel_check_btn_forosh_edari_tejari=tk.Checkbutton(rehn_page_frame_asli_forosh_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
rahn_kamel_check_btn_forosh_edari_tejari.grid(padx=8,pady=15,sticky="w",row=7,column=0)

back_to_home_forosh_edari_tejari=tk.Button(forosh_edari_tejari,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_forosh_edari_tejari)
back_to_home_forosh_edari_tejari.place(x=650,y=535)

zakhire_forosh_edari_tejari=tk.Button(forosh_edari_tejari,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_forosh_edari)
zakhire_forosh_edari_tejari.place(x=550,y=535)

photo_box_forosh_edari_tejari=tk.Frame(forosh_edari_tejari,width=410,height=450,background="#e4dde3")
photo_box_forosh_edari_tejari.place(x=40,y=40)
photo_lbl2_forosh_edari_tejari = tk.Label(photo_box_forosh_edari_tejari, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_forosh_edari_tejari.place(x=30,y=45)
add_img_btn_forosh_edari_tejari = tk.Button(photo_box_forosh_edari_tejari, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_forosh_edari_tejari.place(x=40,y=330)
#endregion
#---------------امکانات فروش اداری/تجاری-------------------
#region
option_frame_options_forosh_edari_tejari=tk.Frame(forosh_edari_tejari,width=300,height=30,background="#bbfbd1")
option_frame_options_forosh_edari_tejari.place(x=520,y=475)

option_label_forosh_edari_tejari=tk.Label(option_frame_options_forosh_edari_tejari,text='افزودن امکانات فایل',font=("Shabnam",10,"bold"),background="#FFFFFF",fg="#000000")
option_label_forosh_edari_tejari.pack(side="right",padx=1)

button_label_forosh_eedari_tejari=tk.Label(option_frame_options_forosh_edari_tejari)
button_label_forosh_eedari_tejari.pack(side="left",padx=1)
plus_button_forosh_eedari_tejari=tk.Button(option_frame_options_forosh_edari_tejari,image=plus,command=open_option4,border=0)
plus_button_forosh_eedari_tejari.pack()

option_frame_photosh_options_forosh_edari_tejari=tk.Frame(option_file_frame_forosh_edari_tejari,width=400,height=100,background="#bbfbd1")
option_frame_photosh_options_forosh_edari_tejari.pack(padx=10,pady=15)

parking_check_btn_forosh_edari_tejari=tk.Checkbutton(option_frame_photosh_options_forosh_edari_tejari,image=parking_pic,background="#022578")
parking_check_btn_forosh_edari_tejari.pack(padx=15,side="left")

asansor_check_btn_forosh_edari_tejari=tk.Checkbutton(option_frame_photosh_options_forosh_edari_tejari,image=elvator_pic,background="#022578")
asansor_check_btn_forosh_edari_tejari.pack(padx=15,side="left")

anbari_check_btn_forosh_edari_tejari=tk.Checkbutton(option_frame_photosh_options_forosh_edari_tejari,image=warehouse_pic,background="#022578")
anbari_check_btn_forosh_edari_tejari.pack(padx=15,side="right")

option_frame_combos_forosh_edari_tejari=tk.Frame(option_file_frame_forosh_edari_tejari,width=400,height=400,background="#bbfbd1",border=1)
option_frame_combos_forosh_edari_tejari.pack(padx=10,pady=15)


aab_va_gaz_emkanat_forosh_edari_tejari=tk.Label(option_frame_combos_forosh_edari_tejari,text="وضعیت آب و گاز",background="#0F6E6E",fg="#ffffff",width=17)
aab_va_gaz_emkanat_forosh_edari_tejari.grid(padx=8,pady=15,row=0,column=1)

aab_va_gaz_combo_emkanat_forosh_edari_tejari=ttk.Combobox(option_frame_combos_forosh_edari_tejari)
aab_va_gaz_combo_emkanat_forosh_edari_tejari["values"] = ("فقط گاز دارد","فقط آب دارد","آب و گاز دارد")
aab_va_gaz_combo_emkanat_forosh_edari_tejari.grid(padx=8,pady=15,row=0,column=0)

sarmayesh_emkanat_forosh_edari_tejari=tk.Label(option_frame_combos_forosh_edari_tejari,text="سیستم سرمایش",background="#0F6E6E",fg="#ffffff",width=17)
sarmayesh_emkanat_forosh_edari_tejari.grid(padx=8,pady=15,row=4,column=1)

sarmayesh_combo_emkanat_forosh_edari_tejari=ttk.Combobox(option_frame_combos_forosh_edari_tejari)
sarmayesh_combo_emkanat_forosh_edari_tejari["values"] = (" کولر گازی"," کولرآبی","پنکه سقفی","ندارد")
sarmayesh_combo_emkanat_forosh_edari_tejari.grid(padx=8,pady=15,row=4,column=0)

garmayesh_emkanat_forosh_edari_tejari=tk.Label(option_frame_combos_forosh_edari_tejari,text="سیستم گرمایش",background="#0F6E6E",fg="#ffffff",width=17)
garmayesh_emkanat_forosh_edari_tejari.grid(padx=8,pady=15,row=5,column=1)

garmayesh_combo_emkanat_forosh_edari_tejari=ttk.Combobox(option_frame_combos_forosh_edari_tejari)
garmayesh_combo_emkanat_forosh_edari_tejari["values"] = (" شوفاژ"," بخاری","ندارد")
garmayesh_combo_emkanat_forosh_edari_tejari.grid(padx=8,pady=15,row=5,column=0)

zakhire_options_forosh_edari_tejari=tk.Button(option_file_frame_forosh_edari_tejari,text="ذخیره",command=None,background="#079BDB",fg="#ffffff",width=8)
zakhire_options_forosh_edari_tejari.place(x=170,y=330)

back_to_home_forosh_edari_tejari=tk.Button(option_file_frame_forosh_edari_tejari,text="بازگشت",command=back_to_forosh_edari_tejari,background="#079BDB",fg="#ffffff",width=8)
back_to_home_forosh_edari_tejari.place(x=95,y=330)
#endregion
#--------------------پنجره فروش باغ/زمین-----------------------
#region
forosh_bagh_zamin = tk.Toplevel(root)
forosh_bagh_zamin.title("فروش باغ و زمین")
forosh_bagh_zamin.geometry("800x600")
forosh_bagh_zamin.withdraw()
forosh_bagh_zamin.configure(bg="#0F6E6E")

frame_asli_forosh_bagh_zamin=tk.Frame(forosh_bagh_zamin,width=490,height=800,bg="#5d6059",border=2)
frame_asli_forosh_bagh_zamin.place(x=500,y=90)

metraj_zamin_forosh_bagh_zamin_lable=tk.Label(frame_asli_forosh_bagh_zamin,text="متراژ",bg="#0F6E6E",fg="#ffffff",width=10)
metraj_zamin_forosh_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=0,column=1)

metraj_zamin_forosh_bagh_zamin_entry=tk.Entry(frame_asli_forosh_bagh_zamin,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),textvariable="متر مربع")
metraj_zamin_forosh_bagh_zamin_entry.grid(padx=8,pady=15,sticky="w",row=0,column=0)

bagh_type_forosh_bagh_zamin_lable=tk.Label(frame_asli_forosh_bagh_zamin,text="کاربری زمین",bg="#0F6E6E",fg="#ffffff",width=10)
bagh_type_forosh_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=1,column=1)

bagh_type_forosh_bagh_zamin_combo=ttk.Combobox(frame_asli_forosh_bagh_zamin,state="readonly")
bagh_type_forosh_bagh_zamin_combo["values"]=("باغ","زمین کشاورزی")
bagh_type_forosh_bagh_zamin_combo.set("باغ")
bagh_type_forosh_bagh_zamin_combo.grid(padx=8,pady=15,sticky="w",row=1,column=0)

bagh_loctaion_forosh_bagh_zamin_lable=tk.Label(frame_asli_forosh_bagh_zamin,text="منطقه و ادرس ",bg="#0F6E6E",fg="#ffffff",width=10)
bagh_loctaion_forosh_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=2,column=1)

bagh_loctaion_forosh_bagh_zamin_entry=tk.Entry(frame_asli_forosh_bagh_zamin,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
bagh_loctaion_forosh_bagh_zamin_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

gheimat_bagh_forosh_bagh_zamin_lable=tk.Label(frame_asli_forosh_bagh_zamin,text='ودیعه',bg="#0F6E6E",fg="#ffffff",width=10)
gheimat_bagh_forosh_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=3,column=1)

gheimat_bagh_forosh_bagh_zamin_entry=tk.Entry(frame_asli_forosh_bagh_zamin,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
gheimat_bagh_forosh_bagh_zamin_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

gheimat_har_matr_babagh_zamin_forosh_bagh_zamin_lable=tk.Label(frame_asli_forosh_bagh_zamin,text='قیمت هر متر',bg="#0F6E6E",fg="#ffffff",width=10)
gheimat_har_matr_babagh_zamin_forosh_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=4,column=1)

gheimat_har_metr_babagh_zamin_forosh_bagh_zamin_entry=tk.Entry(frame_asli_forosh_bagh_zamin,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
gheimat_har_metr_babagh_zamin_forosh_bagh_zamin_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

#time_bagh_forosh_bagh_zamin=tk.Label(frame_asli_forosh_bagh_zamin,text="مدت اجاره",bg="#0F6E6E",fg="#ffffff",width=10)
#time_bagh_forosh_bagh.grid(padx=8,pady=15,sticky="e",row=5,column=1)

#bagh_time_forosh_bagh_combo=ttk.Combobox(frame_asli_forosh_bagh_zamin,state="readonly")
#bagh_time_forosh_bagh_zamin_combo["values"]=("بلندمدت","کوتاه مدت","فصلی","سالانه")
#.set("فصلی")
#bagh_time_forosh_bagh_zamin_combo.grid(padx=8,pady=15,sticky="w",row=5,column=0)

photo_box_forosh_bagh_zamin=tk.Frame(forosh_bagh_zamin,width=410,height=450,background="#e4dde3")
photo_box_forosh_bagh_zamin.place(x=50,y=40)

photo_forosh_bagh_zamin_lable= tk.Label(photo_box_forosh_bagh_zamin, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_forosh_bagh_zamin_lable.place(x=30,y=45)
add_img_btn_forosh_bagh_zamin = tk.Button(photo_box_forosh_bagh_zamin, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_forosh_bagh_zamin.place(x=40,y=330)

back_to_home_forosh_bagh_zamin=tk.Button(forosh_bagh_zamin,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_forosh_bagh)
back_to_home_forosh_bagh_zamin.place(x=320,y=520)

zakhire_forosh_bagh_zamin=tk.Button(forosh_bagh_zamin,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_forosh_bagh)
zakhire_forosh_bagh_zamin.place(x=220,y=520)
#endregion
#-----------------------پنجره امکانات فروش باغ/زمین-------------------
#region
option_frame_options_forosh_bagh_zamin=tk.Frame(forosh_bagh_zamin,width=300,height=30,background="#bbfbd1")
option_frame_options_forosh_bagh_zamin.place(x=550,y=450)

option_label_forosh_bagh_zamin=tk.Label(option_frame_options_forosh_bagh_zamin,text='افزودن امکانات فایل',font=("Shabnam",10,"bold"),background="#FFFFFF",fg="#000000")
option_label_forosh_bagh_zamin.pack(side="right",padx=1)

button_label_forosh_bagh_zamin=tk.Label(option_frame_options_forosh_bagh_zamin)
button_label_forosh_bagh_zamin.pack(side="left",padx=1)
plus_button_forosh_bagh_zamin=tk.Button(option_frame_options_forosh_bagh_zamin,image=plus,command=open_option6,border=0)
plus_button_forosh_bagh_zamin.pack()

option_file_frame_forosh_bagh_zamin=tk.Toplevel(forosh_bagh_zamin,background="#bbfbd1")
option_file_frame_forosh_bagh_zamin.title(" امکانات فروش باغ/زمین")
option_file_frame_forosh_bagh_zamin.geometry("690x630")
option_file_frame_forosh_bagh_zamin.pack_propagate(False)
option_file_frame_forosh_bagh_zamin.withdraw()

mini_frame_forosh_bagh_zamin=tk.Frame(option_file_frame_forosh_bagh_zamin)
mini_frame_forosh_bagh_zamin.place(x=290,y=20)
karbary_zamin_forosh_bagh_zamin=tk.Label(mini_frame_forosh_bagh_zamin,text="کاربری زمین",bg="#0F6E6E",fg="#ffffff",width=10)
karbary_zamin_forosh_bagh_zamin.pack(padx=5,pady=5,side="right")

karbary_zamin_forosh_bagh_zamin_combo=ttk.Combobox(mini_frame_forosh_bagh_zamin,state="readonly")
karbary_zamin_forosh_bagh_zamin_combo["values"]=("باغ","زمین کشاورزی")
karbary_zamin_forosh_bagh_zamin_combo.set("باغ")
karbary_zamin_forosh_bagh_zamin_combo.pack(padx=5,pady=5,side="left")

karbary_zamin_forosh_bagh_zamin_combo.bind("<<ComboboxSelected>>",change_bagh_zamin_forosh_bagh)

option_frame_forosh_bagh_zamin=tk.Frame(option_file_frame_forosh_bagh_zamin,width=430,height=290,background="#d1e0df")
option_frame_forosh_bagh_zamin.place(x=60,y=60)

metraj_derakht_forosh_bagh_zamin_lable=tk.Label(option_frame_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="متراژ درخت کاری")
metraj_derakht_forosh_bagh_zamin_lable.grid(padx=10,pady=5,row=0,column=4)

metraj_derakht_forosh_bagh_zamin_entry=tk.Entry(option_frame_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff")
metraj_derakht_forosh_bagh_zamin_entry.grid(padx=10,pady=5,row=0,column=3)

tedad_derakht_forosh_bagh_zamin_lable=tk.Label(option_frame_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="تعداد درخت")
tedad_derakht_forosh_bagh_zamin_lable.grid(padx=10,pady=5,row=1,column=4)

tedad_derakht_forosh_bagh_zamin_entry=tk.Entry(option_frame_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff")
tedad_derakht_forosh_bagh_zamin_entry.grid(padx=10,pady=5,row=1,column=3)

abyari_forosh_bagh_zamin_lable=tk.Label(option_frame_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع ابیاری")
abyari_forosh_bagh_zamin_lable.grid(padx=10,pady=5,row=2,column=4)

abyari_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_forosh_bagh_zamin)
abyari_forosh_bagh_zamin_combo["values"]=("سطحی","بارانی","قطره ای","تحت فشار")
abyari_forosh_bagh_zamin_combo.set("سطحی")
abyari_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=2,column=3)

type_tree_forosh_bagh_zamin_lable=tk.Label(option_frame_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع درخت")
type_tree_forosh_bagh_zamin_lable.grid(padx=10,pady=5,row=3,column=4)

type_tree_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_forosh_bagh_zamin)
type_tree_forosh_bagh_zamin_combo["values"]=(" ","پسته","بادام","گردو","شلیل","هلو","سیب","انگور"
                           ,"انجیر","زردالو","گیلاس","البالو")
type_tree_forosh_bagh_zamin_combo.set("گردو")
type_tree_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=3,column=3)
type_tree_forosh_btn=tk.Button(option_frame_forosh_bagh_zamin,text="افزودن درخت",command=add_tree2,bg="#007acc",width=10)
type_tree_forosh_btn.grid(padx=10,pady=5,row=4,column=4)

label_natige_forosh_bagh_zamin=tk.Label(option_frame_forosh_bagh_zamin,text="")
label_natige_forosh_bagh_zamin.grid(padx=10,pady=5,row=4,column=3)

chah_forosh_bagh_zamin=tk.Checkbutton(option_frame_forosh_bagh_zamin,text="چاه",background="#d6d0d0")
chah_forosh_bagh_zamin.grid(padx=0,pady=5,row=5,column=0)

estakhr_forosh_bagh_zamin=tk.Checkbutton(option_frame_forosh_bagh_zamin,text="استخر",background="#d6d0d0")
estakhr_forosh_bagh_zamin.grid(padx=0,pady=5,row=5,column=1)

loleh_keshi_ab_forosh_bagh_zamin=tk.Checkbutton(option_frame_forosh_bagh_zamin,text="اب لوله کشی",background="#d6d0d0")
loleh_keshi_ab_forosh_bagh_zamin.grid(padx=0,pady=5,row=5,column=2)

bargh_keshi_forosh_bagh_zamin=tk.Checkbutton(option_frame_forosh_bagh_zamin,text="برق کشی",background="#d6d0d0")
bargh_keshi_forosh_bagh_zamin.grid(padx=0,pady=5,row=5,column=3)

gas_keshi_forosh_bagh_zamin=tk.Checkbutton(option_frame_forosh_bagh_zamin,text="گاز کشی",background="#d6d0d0")
gas_keshi_forosh_bagh_zamin.grid(padx=0,pady=5,row=5,column=4)

var0_forosh_bagh_zamin=tk.IntVar(value=0)#چک باتن پیش فرض تیک نخورده باشه

otagh_check_btn_forosh_bagh_zamin=tk.Checkbutton(option_frame_forosh_bagh_zamin,variable=var0,image=warehouse_pic,background="#022578",text="ساختمان",command=home_true_false2)
otagh_check_btn_forosh_bagh_zamin.grid(padx=10,pady=5,row=6,column=4)

metraj_vila_forosh_bagh_zamin=tk.Label(option_frame_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="متراژ سازه")
metraj_vila_forosh_bagh_zamin.grid(padx=10,pady=5,row=7,column=4)

metraj_vila_forosh_bagh_zamin_entry=tk.Entry(option_frame_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
metraj_vila_forosh_bagh_zamin_entry.grid(padx=10,pady=5,row=7,column=3)

sal_sakht_vila_forosh_bagh_zamin_lable=tk.Label(option_frame_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="سال ساخت")
sal_sakht_vila_forosh_bagh_zamin_lable.grid(padx=10,pady=5,row=8,column=4)

sal_sakht_vila_forosh_bagh_zamin_entry=tk.Entry(option_frame_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
sal_sakht_vila_forosh_bagh_zamin_entry.grid(padx=10,pady=5,row=8,column=3)

type_vila_forosh_bagh_zamin=tk.Label(option_frame_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="نوع سازه")
type_vila_forosh_bagh_zamin.grid(padx=10,pady=5,row=9,column=4)

type_vila_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_forosh_bagh_zamin,state="disabled")
type_vila_forosh_bagh_zamin_combo["values"]=("آجری","بلوکی","کانکس","چوبی")
type_vila_forosh_bagh_zamin_combo.set("آجری")
type_vila_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=9,column=3)

toilet_forosh_bagh_zamin_lable=tk.Label(option_frame_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="سرویس بهداشتی")
toilet_forosh_bagh_zamin_lable.grid(padx=10,pady=5,row=10,column=4)

toilet_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_forosh_bagh_zamin,state="disabled")
toilet_forosh_bagh_zamin_combo["values"]=(" ","ندارد","فرنگی","ایرانی","هردو")
toilet_forosh_bagh_zamin_combo.set("")
toilet_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=10,column=3)

hamam_forosh_bagh_zamin=tk.Label(option_frame_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="حمام")
hamam_forosh_bagh_zamin.grid(padx=10,pady=5,row=11,column=4)

hamam_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_forosh_bagh_zamin,state="disabled")
hamam_forosh_bagh_zamin_combo["values"]=(" ","ندارد","دارد")
hamam_forosh_bagh_zamin_combo.set(" ")
hamam_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=11,column=3)

sanad_forosh_bagh_zamin_lable=tk.Label(option_frame_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="سند")
sanad_forosh_bagh_zamin_lable.grid(padx=10,pady=5,row=12,column=4)

sanad_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_forosh_bagh_zamin,state="disabled")
sanad_forosh_bagh_zamin_combo["values"]=(" ","ندارد","تک برگ","قولنامه ای","مشاع")
sanad_forosh_bagh_zamin_combo.set(" ")
sanad_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=12,column=3)

option_forosh_bagh_zamin=tk.Label(option_frame_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="امکانات تفریحی")
option_forosh_bagh_zamin.grid(padx=10,pady=5,row=13,column=4)

option_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_forosh_bagh_zamin,state="disabled")
option_forosh_bagh_zamin_combo["values"]=(" ","استخر","جکوزی","باربیکیو")
option_forosh_bagh_zamin_combo.set(" ")
option_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=13,column=3)
add_option_button_forosh_bagh_zamin=tk.Button(option_frame_forosh_bagh_zamin,text="افزودن امکانات",command=add_option2,bg="#007acc",width=10)
add_option_button_forosh_bagh_zamin.grid(padx=10,pady=5,row=13,column=2)
lable_natige_add_forosh_bagh_zamin=tk.Label(option_frame_forosh_bagh_zamin,text="")
lable_natige_add_forosh_bagh_zamin.grid(padx=10,pady=5,row=13,column=1)

mojavez_sakht_check_btn_forosh_bagh_zamin=tk.Checkbutton(option_frame_forosh_bagh_zamin,text="مجوز ساختن",background="#d6d0d0",state="disabled")
mojavez_sakht_check_btn_forosh_bagh_zamin.grid(padx=10,pady=5,row=14,column=4)

mohavate_sazi_check_btn_forosh_bagh_zamin=tk.Checkbutton(option_frame_forosh_bagh_zamin,text="محوطه سازی",background="#d6d0d0",state="disabled")
mohavate_sazi_check_btn_forosh_bagh_zamin.grid(padx=10,pady=5,row=14,column=3)

divar_forosh_bagh_zamin=tk.Checkbutton(option_frame_forosh_bagh_zamin,text="دیوار کشی",background="#d6d0d0")
divar_forosh_bagh_zamin.grid(padx=10,pady=5,row=14,column=2)

zakhire_options_forosh_bagh_zamin=tk.Button(option_file_frame_forosh_bagh_zamin,text="ذخیره",background="#079BDB",fg="#ffffff",width=8)
zakhire_options_forosh_bagh_zamin.place(x=170,y=580)

back_to_forosh_bagh_zamin=tk.Button(option_file_frame_forosh_bagh_zamin,text="بازگشت",command=back_to_forosh_bagh_zamin,background="#079BDB",fg="#ffffff",width=8)
back_to_forosh_bagh_zamin.place(x=95,y=580)
#endregion
#-------------------------تعویض کاربری به زمین در قسمت فروش باغ/زمین-------------
#region
option_frame_option2_forosh_bagh_zamin=tk.Frame(option_file_frame_forosh_bagh_zamin,width=445,height=290,background="#d1e0df")
option_frame_option2_forosh_bagh_zamin.place_forget()

metraj_zamin2_forosh_bagh_zamin_lable=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="متراژ زمین")
metraj_zamin2_forosh_bagh_zamin_lable.grid(padx=10,pady=5,row=0,column=4)

metraj_zamin2_forosh_bagh_zamin_entry=tk.Entry(option_frame_option2_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff")
metraj_zamin2_forosh_bagh_zamin_entry.grid(padx=10,pady=5,row=0,column=3)

karbari_forosh_bagh_zamin_lable=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع کاربری")
karbari_forosh_bagh_zamin_lable.grid(padx=10,pady=5,row=1,column=4)

karbari_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_option2_forosh_bagh_zamin)
karbari_forosh_bagh_zamin_combo["values"]=(" ","زراعی","باغی","گلخانه ای","دامداری ","مرغداری",
                               "دامداری و مرغداری","آیش")                             
karbari_forosh_bagh_zamin_combo.set(" ")
karbari_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=1,column=3)

khak_forosh_bagh_zamin=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع خاک")
khak_forosh_bagh_zamin.grid(padx=10,pady=5,row=2,column=4)

khak_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_option2_forosh_bagh_zamin)
khak_forosh_bagh_zamin_combo["values"]=(" ","رسی","شنی","لومی","رسی_شنی","شنی_لومی",
                               "رسی_لومی")                             
khak_forosh_bagh_zamin_combo.set(" ")
khak_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=2,column=3)

ab_forosh_bagh_zamin=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="منبع اب")
ab_forosh_bagh_zamin.grid(padx=10,pady=5,row=3,column=4)

ab_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_option2_forosh_bagh_zamin)
ab_forosh_bagh_zamin_combo["values"]=(" ","چاه","قنات","رودخانه","کانال ابیاری","چشمه",
                               "آب لوله کشی کشاورزی","تانکر","استخر")                             
ab_forosh_bagh_zamin_combo.set(" ")
ab_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=3,column=3)

zamin_shekl_forosh_bagh_zamin_forosh_lable=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="توپوگرافی")
zamin_shekl_forosh_bagh_zamin_forosh_lable.grid(padx=10,pady=5,row=4,column=4)

zamin_shekl_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_option2_forosh_bagh_zamin)
zamin_shekl_forosh_bagh_zamin_combo["values"]=(" "," صاف و یکدست"," شیب دار"," باتلاقی","سنگی ")                             
zamin_shekl_forosh_bagh_zamin_combo.set(" ")
zamin_shekl_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=4,column=3)

add_topo2_button_forosh_bagh_zamin=tk.Button(option_frame_option2_forosh_bagh_zamin,text=" مورد دلخواه",command=add_topo2,bg="#007acc",width=10)
add_topo2_button_forosh_bagh_zamin.grid(padx=10,pady=5,row=4,column=2)
label_natige_topo_add_forosh_bagh_zamin=tk.Label(option_frame_option2_forosh_bagh_zamin,text="")
label_natige_topo_add_forosh_bagh_zamin.grid(padx=10,pady=5,row=4,column=1)

kesht_forosh_bagh_zamin=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="سطح زیر کشت")
kesht_forosh_bagh_zamin.grid(padx=10,pady=5,row=5,column=4)

kesht_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_option2_forosh_bagh_zamin)
kesht_forosh_bagh_zamin_combo["values"]=("بدون کشت"," زیر کشت")                             
kesht_forosh_bagh_zamin_combo.set("بدون کشت ")
kesht_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=5,column=3)
kesht_forosh_bagh_zamin_combo.bind("<<ComboboxSelected>>",choos_kesht2)

kesht_forosh_bagh_zamin_label=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="محصول زیرکشت")
kesht_forosh_bagh_zamin_label.grid(padx=10,pady=5,row=5,column=2)

kesht_forosh_bagh_zamin_entry=tk.Entry(option_frame_option2_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
kesht_forosh_bagh_zamin_entry.grid(padx=10,pady=5,row=5,column=1)

security_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="اتاق نگهبان",background="#d6d0d0")
security_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=6,column=0)

bargh_kesi_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="برق تک فاز",background="#d6d0d0")
bargh_kesi_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=6,column=1)

bargh_keshi_zamin_forosh_bagh_zamin2=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="برق سه فاز",background="#d6d0d0")
bargh_keshi_zamin_forosh_bagh_zamin2.grid(padx=10,pady=6,row=6,column=2)

anbar_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="انبار/سوله",background="#d6d0d0")
anbar_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=6,column=3)

fans_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="فنس/دیوار",background="#d6d0d0")
fans_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=6,column=4)

mojavez_golkhane_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="اجازه ساخت گلخانه",background="#d6d0d0")
mojavez_golkhane_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=7,column=0)

mojavez_chah_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="اجازه حفر چاه",background="#d6d0d0")
mojavez_chah_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=7,column=1)

bardasht_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="حق برداشت ",background="#d6d0d0")
bardasht_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=7,column=2)

dam_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="اجازه ورود دام",background="#d6d0d0")
dam_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=7,column=3)
#endregion
#############################################################################
#-------------------پنجره اجاره کارگاه------------------------
#region
ejareh_karghah = tk.Toplevel(root)
ejareh_karghah.title(" اجاره کارگاه")
ejareh_karghah.geometry("800x600")
ejareh_karghah.withdraw()
ejareh_karghah.configure(bg="#0F6E6E")

ejareh_kargah_frame=tk.Frame(ejareh_karghah,width=490,height=800,bg="#5d6059",border=2)
ejareh_kargah_frame.place(x=500,y=90)

karbari_zamin_ejareh_kargah=tk.Label(ejareh_kargah_frame,text="کاربری زمین",bg="#0F6E6E",fg="#ffffff",width=10)
karbari_zamin_ejareh_kargah.grid(padx=8,pady=15,sticky="e",row=0,column=1)

ejareh_kargah_lable=tk.Label(ejareh_kargah_frame,text=" کارگاه ",bg="#C2C2C2",fg="#313131",width=20)
ejareh_kargah_lable.grid(padx=8,pady=15,sticky="e",row=0,column=0)

metraj_kargah_lable=tk.Label(ejareh_kargah_frame,text="متراژ",bg="#0F6E6E",fg="#ffffff",width=10)
metraj_kargah_lable.grid(padx=8,pady=15,sticky="e",row=1,column=1)

metraj_kargah_entry=tk.Entry(ejareh_kargah_frame,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),textvariable="متر مربع")
metraj_kargah_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

loctaion_ejareh_kargah_lable=tk.Label(ejareh_kargah_frame,text="منطقه و ادرس ",bg="#0F6E6E",fg="#ffffff",width=10)
loctaion_ejareh_kargah_lable.grid(padx=8,pady=15,sticky="e",row=2,column=1)

loctaion_ejareh_kargah_entry=tk.Entry(ejareh_kargah_frame,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
loctaion_ejareh_kargah_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

mablagh_pish_ejareh_kargah_lable=tk.Label(ejareh_kargah_frame,text='ودیعه',bg="#0F6E6E",fg="#ffffff",width=10)
mablagh_pish_ejareh_kargah_lable.grid(padx=8,pady=15,sticky="e",row=3,column=1)

mablagh_pish_ejareh_kargah_entry=tk.Entry(ejareh_kargah_frame,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
mablagh_pish_ejareh_kargah_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

gheimat_har_metr_ejareh_kargah_lable=tk.Label(ejareh_kargah_frame,text='قیمت هر متر',bg="#0F6E6E",fg="#ffffff",width=10)
gheimat_har_metr_ejareh_kargah_lable.grid(padx=8,pady=15,sticky="e",row=4,column=1)

gheimat_har_metr_ejareh_kargah_entry=tk.Entry(ejareh_kargah_frame,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
gheimat_har_metr_ejareh_kargah_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

time_ejate_ejareh_kargah_lable=tk.Label(ejareh_kargah_frame,text="مدت اجاره",bg="#0F6E6E",fg="#ffffff",width=10)
time_ejate_ejareh_kargah_lable.grid(padx=8,pady=15,sticky="e",row=5,column=1)

time_ejare_ejareh_kargah_combo=ttk.Combobox(ejareh_kargah_frame,state="readonly")
time_ejare_ejareh_kargah_combo["values"]=("بلندمدت","کوتاه مدت","فصلی","سالانه")
time_ejare_ejareh_kargah_combo.set("فصلی")
time_ejare_ejareh_kargah_combo.grid(padx=8,pady=15,sticky="w",row=5,column=0)

photo_box_ejareh_kargah=tk.Frame(ejareh_karghah,width=410,height=450,background="#e4dde3")
photo_box_ejareh_kargah.place(x=50,y=40)

photo_lbl2_ejareh_kargah = tk.Label(photo_box_ejareh_kargah, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_ejareh_kargah.place(x=30,y=45)
add_img_btn_ejareh_kargah = tk.Button(photo_box_ejareh_kargah, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_ejareh_kargah.place(x=40,y=330)

back_to_home_ejareh_kargah=tk.Button(ejareh_karghah,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_ejareh_karghah)
back_to_home_ejareh_kargah.place(x=320,y=520)

zakhire_ejareh_kargah=tk.Button(ejareh_karghah,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_ejareh_karghah)
zakhire_ejareh_kargah.place(x=220,y=520)
#endregion
#---------------------پنجره امکانات اجاره کارگاه---------------------
#region
option_frame_ejareh_kargah=tk.Frame(ejareh_karghah,width=300,height=30,background="#bbfbd1")
option_frame_ejareh_kargah.place(x=550,y=450)

option_frame_ejareh_kargah_lable=tk.Label(option_frame_ejareh_kargah,text='افزودن امکانات فایل',font=("Shabnam",10,"bold"),background="#FFFFFF",fg="#000000")
option_frame_ejareh_kargah_lable.pack(side="right",padx=1)

button_lable_ejareh_kargah=tk.Label(option_frame_ejareh_kargah)
button_lable_ejareh_kargah.pack(side="left",padx=1)
plus_button_ejareh_kargah=tk.Button(option_frame_ejareh_kargah,image=plus,command=open_option7,border=0)
plus_button_ejareh_kargah.pack()

option_file_frame_ejareh_kargah=tk.Toplevel(ejareh_karghah,background="#bbfbd1")
option_file_frame_ejareh_kargah.title(" امکانات اجاره کارگاه")
option_file_frame_ejareh_kargah.geometry("500x450")
option_file_frame_ejareh_kargah.pack_propagate(False)
option_file_frame_ejareh_kargah.withdraw()
mini_frame_ejareh_kargah=tk.Frame(option_file_frame_ejareh_kargah)
mini_frame_ejareh_kargah.place(x=290,y=20)

option_frame_asli_ejareh_kargah=tk.Frame(option_file_frame_ejareh_kargah,width=400,height=400,background="#bbfbd1")
option_frame_asli_ejareh_kargah.place(x=60,y=60)

sal_sakht_ejareh_kargah_lable=tk.Label(option_frame_asli_ejareh_kargah,bg="#0F6E6E",fg="#ffffff",width=13,text="سال ساخت")
sal_sakht_ejareh_kargah_lable.grid(padx=10,pady=5,row=0,column=1)

sal_sakht_ejareh_kargah_entry=tk.Entry(option_frame_asli_ejareh_kargah,width=10,bg="#ffffff",fg="#000000")
sal_sakht_ejareh_kargah_entry.grid(padx=10,pady=5,row=0,column=0)

vaziat_bagh_ejareh_kargah=tk.Label(option_frame_asli_ejareh_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text="وضعیت برق")
vaziat_bagh_ejareh_kargah.grid(padx=10,pady=5,row=1,column=1)

vaziat_bargh_ejareh_kargah_combo=ttk.Combobox(option_frame_asli_ejareh_kargah)
vaziat_bargh_ejareh_kargah_combo["values"]=("برق شهری","سه فاز","تک فاز")
vaziat_bargh_ejareh_kargah_combo.set("برق شهری")
vaziat_bargh_ejareh_kargah_combo.grid(padx=10,pady=5,row=1,column=0)

garmayesh_ejareh_kargah=tk.Label(option_frame_asli_ejareh_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text="سیستم گرمایش")
garmayesh_ejareh_kargah.grid(padx=10,pady=5,row=2,column=1)

garmayesh_type_ejareh_kargah_combo=ttk.Combobox(option_frame_asli_ejareh_kargah)
garmayesh_type_ejareh_kargah_combo["values"]=("بخاری ","شوفاژ ","فن کوئل(گرما) ")
garmayesh_type_ejareh_kargah_combo.set(" بخاری")
garmayesh_type_ejareh_kargah_combo.grid(padx=10,pady=3,row=2,column=0)

sarmayesh_ejareh_kargah=tk.Label(option_frame_asli_ejareh_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text="سیستم سرمایش ")
sarmayesh_ejareh_kargah.grid(padx=10,pady=5,row=3,column=1)

sarmayesh_fan_ejareh_kargah=tk.Checkbutton(option_frame_asli_ejareh_kargah,text="تهویه(فن)",background="#d6d0d0")
sarmayesh_fan_ejareh_kargah.grid(padx=0,pady=5,row=4,column=0)

sarmayesh_panke_ejareh_kargah=tk.Checkbutton(option_frame_asli_ejareh_kargah,text="پنکه سقفی",background="#d6d0d0")
sarmayesh_panke_ejareh_kargah.grid(padx=0,pady=5,row=4,column=1)

sarmayesh_kooler_abi_ejareh_kargah=tk.Checkbutton(option_frame_asli_ejareh_kargah,text="کولر آبی",background="#d6d0d0")
sarmayesh_kooler_abi_ejareh_kargah.grid(padx=0,pady=5,row=5,column=0)

sarmayesh_kooler_gazi_ejareh_kargah=tk.Checkbutton(option_frame_asli_ejareh_kargah,text="کولر گازی",background="#d6d0d0")
sarmayesh_kooler_gazi_ejareh_kargah.grid(padx=0,pady=5,row=5,column=1)

vaziat_ab_ejareh_kargah=tk.Label(option_frame_asli_ejareh_kargah,bg="#0F6E6E",fg="#ffffff",width=13,text=" وضعیت آب")
vaziat_ab_ejareh_kargah.grid(padx=10,pady=5,row=6,column=1)

vaziat_ab_ejareh_kargah_combo=ttk.Combobox(option_frame_asli_ejareh_kargah,width=35)
vaziat_ab_ejareh_kargah_combo["values"]=(" آب مستقیم لوله کشی (بدون فشار) " ," آب مستقیم لوله کشی (همراه موتور فشار) ","دارای منبع(همراه موتور فشار)","دارای منبع(بدون فشار)")
vaziat_ab_ejareh_kargah_combo.set(" آب مستقیم لوله کشی (بدون فشار) ")
vaziat_ab_ejareh_kargah_combo.grid(padx=10,pady=5,row=6,column=0)

abzar_ejareh_kargah=tk.Label(option_frame_asli_ejareh_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text=" ابزار صنعتی ")
abzar_ejareh_kargah.grid(padx=10,pady=5,row=7,column=1)

abzaar_ejareh_kargah_combo=ttk.Combobox(option_frame_asli_ejareh_kargah,width=23)
abzaar_ejareh_kargah_combo["values"]=("(کارگاه خالی) بدون دستگاه ","دارای دستگاه های تولیدی")
abzaar_ejareh_kargah_combo.set("(کارگاه خالی) بدون دستگاه ")
abzaar_ejareh_kargah_combo.grid(padx=10,pady=5,row=7,column=0)

toilet_ejareh_kargah=tk.Label(option_frame_asli_ejareh_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text="سرویس بهداشتی")
toilet_ejareh_kargah.grid(padx=10,pady=5,row=8,column=1)

toilet_ejareh_kargah_combo=ttk.Combobox(option_frame_asli_ejareh_kargah)
toilet_ejareh_kargah_combo["values"]=("دارد","ندارد")
toilet_ejareh_kargah_combo.set("دارد")
toilet_ejareh_kargah_combo.grid(padx=10,pady=5,row=8,column=0)

hamam_ejareh_kargah=tk.Label(option_frame_asli_ejareh_kargah,bg="#0F6E6E",fg="#ffffff",width=13,text="حمام")
hamam_ejareh_kargah.grid(padx=10,pady=5,row=9,column=1)

hamam_ejareh_kargah__combo=ttk.Combobox(option_frame_asli_ejareh_kargah)
hamam_ejareh_kargah__combo["values"]=("ندارد","دارد")
hamam_ejareh_kargah__combo.set("ندارد")
hamam_ejareh_kargah__combo.grid(padx=10,pady=5,row=9,column=0)

otagh_ejareh_kargah=tk.Label(option_frame_asli_ejareh_kargah,bg="#0F6E6E",fg="#ffffff",width=17,text="اتاق رخت کن و استراحت")
otagh_ejareh_kargah.grid(padx=10,pady=5,row=10,column=1)

otagh_ejareh_kargah_combo=ttk.Combobox(option_frame_asli_ejareh_kargah)
otagh_ejareh_kargah_combo["values"]=("ندارد","دارد")
otagh_ejareh_kargah_combo.set("ندارد")
otagh_ejareh_kargah_combo.grid(padx=10,pady=5,row=10,column=0)

zakhire_options_ejareh_kargah=tk.Button(option_file_frame_ejareh_kargah,text="ذخیره",background="#079BDB",fg="#ffffff",width=8)
zakhire_options_ejareh_kargah.place(x=170,y=420)

back_to_ejareh_kargah=tk.Button(option_file_frame_ejareh_kargah,text="بازگشت",command=back_to_ejareh_karghah,background="#079BDB",fg="#ffffff",width=8)
back_to_ejareh_kargah.place(x=95,y=420)
#endregion
#EMAD
#-------------------پنجره فروش کارگاه------------------------
#region
forosh_karghah = tk.Toplevel(root)
forosh_karghah.title(" فروش کارگاه")
forosh_karghah.geometry("800x600")
forosh_karghah.withdraw()
forosh_karghah.configure(bg="#0F6E6E")

frame_forosh_kargah=tk.Frame(forosh_karghah,width=490,height=800,bg="#5d6059",border=2)
frame_forosh_kargah.place(x=500,y=90)

karbari_forosh_kargah=tk.Label(frame_forosh_kargah,text="کاربری زمین",bg="#0F6E6E",fg="#ffffff",width=10)
karbari_forosh_kargah.grid(padx=8,pady=15,sticky="e",row=0,column=1)

lable_forosh_kargah=tk.Label(frame_forosh_kargah,text=" کارگاه ",bg="#C2C2C2",fg="#313131",width=20)
lable_forosh_kargah.grid(padx=8,pady=15,sticky="e",row=0,column=0)

metraj_forosh_kargah=tk.Label(frame_forosh_kargah,text="متراژ",bg="#0F6E6E",fg="#ffffff",width=10)
metraj_forosh_kargah.grid(padx=8,pady=15,sticky="e",row=1,column=1)

metraj_forosh_kargah_entry=tk.Entry(frame_forosh_kargah,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),textvariable="متر مربع")
metraj_forosh_kargah_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

loctaion_forosh_kargah=tk.Label(frame_forosh_kargah,text="منطقه و ادرس ",bg="#0F6E6E",fg="#ffffff",width=10)
loctaion_forosh_kargah.grid(padx=8,pady=15,sticky="e",row=2,column=1)

loctaion_forosh_kargah_entry=tk.Entry(frame_forosh_kargah,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
loctaion_forosh_kargah_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

mablagh_pish_forosh_kargah=tk.Label(frame_forosh_kargah,text='ودیعه',bg="#0F6E6E",fg="#ffffff",width=10)
mablagh_pish_forosh_kargah.grid(padx=8,pady=15,sticky="e",row=3,column=1)

mablagh_pish_forosh_kargah_entry=tk.Entry(frame_forosh_kargah,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
mablagh_pish_forosh_kargah_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

gheimat_har_metr_forosh_kargah=tk.Label(frame_forosh_kargah,text='قیمت هر متر',bg="#0F6E6E",fg="#ffffff",width=10)
gheimat_har_metr_forosh_kargah.grid(padx=8,pady=15,sticky="e",row=4,column=1)

gheimat_har_metr_forosh_kargah_entry=tk.Entry(frame_forosh_kargah,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
gheimat_har_metr_forosh_kargah_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

time_ejare_forosh_kargah=tk.Label(frame_forosh_kargah,text="مدت اجاره",bg="#0F6E6E",fg="#ffffff",width=10)
time_ejare_forosh_kargah.grid(padx=8,pady=15,sticky="e",row=5,column=1)

time_ejare_forosh_kargah_combo=ttk.Combobox(frame_forosh_kargah,state="readonly")
time_ejare_forosh_kargah_combo["values"]=("بلندمدت","کوتاه مدت","فصلی","سالانه")
time_ejare_forosh_kargah_combo.set("فصلی")
time_ejare_forosh_kargah_combo.grid(padx=8,pady=15,sticky="w",row=5,column=0)

photo_box_forosh_kargah=tk.Frame(forosh_karghah,width=410,height=450,background="#e4dde3")
photo_box_forosh_kargah.place(x=50,y=40)

photo_lbl2_forosh_kargah = tk.Label(photo_box_forosh_kargah, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_forosh_kargah.place(x=30,y=45)
add_img_btn_forosh_kargah = tk.Button(photo_box_forosh_kargah, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_forosh_kargah.place(x=40,y=330)

back_to_home_forosh_kargah=tk.Button(forosh_karghah,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_forosh_karghah)
back_to_home_forosh_kargah.place(x=320,y=520)

zakhire_forosh_kargah=tk.Button(forosh_karghah,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_forosh_karghah)
zakhire_forosh_kargah.place(x=220,y=520)
#endregion
#---------------------پنجره امکانات فروش کارگاه---------------------
#region
option_frame_forosh_kargah=tk.Frame(forosh_karghah,width=300,height=30,background="#bbfbd1")
option_frame_forosh_kargah.place(x=550,y=450)

option_frame_lable_forosh_kargah=tk.Label(option_frame_forosh_kargah,text='افزودن امکانات فایل',font=("Shabnam",10,"bold"),background="#FFFFFF",fg="#000000")
option_frame_lable_forosh_kargah.pack(side="right",padx=1)

button_label_forosh_kargah=tk.Label(option_frame_forosh_kargah)
button_label_forosh_kargah.pack(side="left",padx=1)
plus_button_forosh_kargah=tk.Button(option_frame_forosh_kargah,image=plus,command=open_option8,border=0)
plus_button_forosh_kargah.pack()

option_file_frame_forosh_kargah=tk.Toplevel(forosh_karghah,background="#bbfbd1")
option_file_frame_forosh_kargah.title(" امکانات فروش کارگاه")
option_file_frame_forosh_kargah.geometry("500x450")
option_file_frame_forosh_kargah.pack_propagate(False)
option_file_frame_forosh_kargah.withdraw()
mini_frame_forosh_kargah=tk.Frame(option_file_frame_forosh_kargah)
mini_frame_forosh_kargah.place(x=290,y=20)

option_frame_asli_forosh_kargah=tk.Frame(option_file_frame_forosh_kargah,width=400,height=400,background="#bbfbd1")
option_frame_asli_forosh_kargah.place(x=60,y=60)

sal_sakht_forosh_kargah=tk.Label(option_frame_asli_forosh_kargah,bg="#0F6E6E",fg="#ffffff",width=13,text="سال ساخت")
sal_sakht_forosh_kargah.grid(padx=10,pady=5,row=0,column=1)

sal_sakht_forosh_kargah_entry=tk.Entry(option_frame_asli_forosh_kargah,width=10,bg="#ffffff",fg="#000000")
sal_sakht_forosh_kargah_entry.grid(padx=10,pady=5,row=0,column=0)

vaziat_bargh_forosh_kargah=tk.Label(option_frame_asli_forosh_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text="وضعیت برق")
vaziat_bargh_forosh_kargah.grid(padx=10,pady=5,row=1,column=1)

vaziat_bargh_forosh_kargah_combo=ttk.Combobox(option_frame_asli_forosh_kargah)
vaziat_bargh_forosh_kargah_combo["values"]=("برق شهری","سه فاز","تک فاز")
vaziat_bargh_forosh_kargah_combo.set("برق شهری")
vaziat_bargh_forosh_kargah_combo.grid(padx=10,pady=5,row=1,column=0)

garmayesh_forosh_kargah=tk.Label(option_frame_asli_forosh_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text="سیستم گرمایش")
garmayesh_forosh_kargah.grid(padx=10,pady=5,row=2,column=1)

garmayesh_type_forosh_kargah_combo=ttk.Combobox(option_frame_asli_forosh_kargah)
garmayesh_type_forosh_kargah_combo["values"]=("بخاری ","شوفاژ ","فن کوئل(گرما) ")
garmayesh_type_forosh_kargah_combo.set(" بخاری")
garmayesh_type_forosh_kargah_combo.grid(padx=10,pady=3,row=2,column=0)

sarmayesh_forosh_kargah=tk.Label(option_frame_asli_forosh_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text="سیستم سرمایش ")
sarmayesh_forosh_kargah.grid(padx=10,pady=5,row=3,column=1)

sarmayesh_fan_forosh_kargah=tk.Checkbutton(option_frame_asli_forosh_kargah,text="تهویه(فن)",background="#d6d0d0")
sarmayesh_fan_forosh_kargah.grid(padx=0,pady=5,row=4,column=0)

sarmayesh_panke_forosh_kargah=tk.Checkbutton(option_frame_asli_forosh_kargah,text="پنکه سقفی",background="#d6d0d0")
sarmayesh_panke_forosh_kargah.grid(padx=0,pady=5,row=4,column=1)

sarmayesh_kooler_abi_forosh_kargah=tk.Checkbutton(option_frame_asli_forosh_kargah,text="کولر آبی",background="#d6d0d0")
sarmayesh_kooler_abi_forosh_kargah.grid(padx=0,pady=5,row=5,column=0)

sarmayesh_kooler_gazi_forosh_kargah=tk.Checkbutton(option_frame_asli_forosh_kargah,text="کولر گازی",background="#d6d0d0")
sarmayesh_kooler_gazi_forosh_kargah.grid(padx=0,pady=5,row=5,column=1)

vaziat_ab_forosh_kargah=tk.Label(option_frame_asli_forosh_kargah,bg="#0F6E6E",fg="#ffffff",width=13,text=" وضعیت آب")
vaziat_ab_forosh_kargah.grid(padx=10,pady=5,row=6,column=1)

vaziat_ab_forosh_kargah_combo=ttk.Combobox(option_frame_asli_forosh_kargah,width=35)
vaziat_ab_forosh_kargah_combo["values"]=(" آب مستقیم لوله کشی (بدون فشار) " ," آب مستقیم لوله کشی (همراه موتور فشار) ","دارای منبع(همراه موتور فشار)","دارای منبع(بدون فشار)")
vaziat_ab_forosh_kargah_combo.set(" آب مستقیم لوله کشی (بدون فشار) ")
vaziat_ab_forosh_kargah_combo.grid(padx=10,pady=5,row=6,column=0)

abzar_forosh_kargah=tk.Label(option_frame_asli_forosh_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text=" ابزار صنعتی ")
abzar_forosh_kargah.grid(padx=10,pady=5,row=7,column=1)

abzarforosh_kargah_combo=ttk.Combobox(option_frame_asli_forosh_kargah,width=23)
abzarforosh_kargah_combo["values"]=("(کارگاه خالی) بدون دستگاه ","دارای دستگاه های تولیدی")
abzarforosh_kargah_combo.set("(کارگاه خالی) بدون دستگاه ")
abzarforosh_kargah_combo.grid(padx=10,pady=5,row=7,column=0)

toilet_forosh_kargah=tk.Label(option_frame_asli_forosh_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text="سرویس بهداشتی")
toilet_forosh_kargah.grid(padx=10,pady=5,row=8,column=1)

toilet_forosh_kargah_combo=ttk.Combobox(option_frame_asli_forosh_kargah)
toilet_forosh_kargah_combo["values"]=("دارد","ندارد")
toilet_forosh_kargah_combo.set("دارد")
toilet_forosh_kargah_combo.grid(padx=10,pady=5,row=8,column=0)

hamam_forosh_kargah=tk.Label(option_frame_asli_forosh_kargah,bg="#0F6E6E",fg="#ffffff",width=13,text="حمام")
hamam_forosh_kargah.grid(padx=10,pady=5,row=9,column=1)

hamam_forosh_kargah_combo=ttk.Combobox(option_frame_asli_forosh_kargah)
hamam_forosh_kargah_combo["values"]=("ندارد","دارد")
hamam_forosh_kargah_combo.set("ندارد")
hamam_forosh_kargah_combo.grid(padx=10,pady=5,row=9,column=0)

otagh_forosh_kargah=tk.Label(option_frame_asli_forosh_kargah,bg="#0F6E6E",fg="#ffffff",width=17,text="اتاق رخت کن و استراحت")
otagh_forosh_kargah.grid(padx=10,pady=5,row=10,column=1)

otagh_forosh_kargah_combo=ttk.Combobox(option_frame_asli_forosh_kargah)
otagh_forosh_kargah_combo["values"]=("ندارد","دارد")
otagh_forosh_kargah_combo.set("ندارد")
otagh_forosh_kargah_combo.grid(padx=10,pady=5,row=10,column=0)

zakhire_options_forosh_kargah=tk.Button(option_file_frame_forosh_kargah,text="ذخیره",background="#079BDB",fg="#ffffff",width=8)
zakhire_options_forosh_kargah.place(x=170,y=420)

back_to_forosh_kargah=tk.Button(option_file_frame_forosh_kargah,text="بازگشت",command=back_to_forosh_karghah,background="#079BDB",fg="#ffffff",width=8)
back_to_forosh_kargah.place(x=95,y=420)
#endregion
#--------------------پنجره های ثبتی بخش خرید-----------------------
#----------------------پنجره خرید مسکونی--------------------------
#region
kharid_maskoni_page = tk.Toplevel(root)
kharid_maskoni_page.title("خرید مسکونی")
kharid_maskoni_page.geometry("800x600")
kharid_maskoni_page.withdraw()
kharid_maskoni_page.configure(bg="#0F6E6E")

#---------------------پنجره امکانات خرید مسکونی----------------------
option_file_frame_kharid_maskoni=tk.Toplevel(kharid_maskoni_page,background="#bbfbd1" )
option_file_frame_kharid_maskoni.title(" امکانات خرید مسکونی")
option_file_frame_kharid_maskoni.geometry("500x370")
option_file_frame_kharid_maskoni.pack_propagate(False)
option_file_frame_kharid_maskoni.withdraw()

rehn_page_frame_kharid_maskoni=tk.Frame(kharid_maskoni_page,width=490,height=800,bg="#5d6059",border=2)
rehn_page_frame_kharid_maskoni.place(x=500,y=50)

melk_type_kharid_maskoni=tk.Label(rehn_page_frame_kharid_maskoni,text="نوع ملک",bg="#0F6E6E",fg="#ffffff",width=10)
melk_type_kharid_maskoni.grid(padx=8,pady=15,sticky="e",row=0,column=1)

melk_type_kharid_maskoni_entry=tk.Entry(rehn_page_frame_kharid_maskoni,text="فروش مسکونی",bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
melk_type_kharid_maskoni_entry.grid(padx=8, pady=15,row=0,column=0,sticky="w") 

sal_sakht_kharid_maskoni=tk.Label(rehn_page_frame_kharid_maskoni,text="سال ساخت",bg="#0F6E6E",fg="#ffffff",width=10)
sal_sakht_kharid_maskoni.grid(padx=8,pady=10,sticky="e",row=1,column=1)

sal_sakht_kharid_maskoni_entry=tk.Entry(rehn_page_frame_kharid_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
sal_sakht_kharid_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

addrres_kharid_maskoni=tk.Label(rehn_page_frame_kharid_maskoni,text="آدرس",bg="#0F6E6E",fg="#ffffff",width=10)
addrres_kharid_maskoni.grid(padx=8,pady=15,sticky="e",row=2,column=1)

addrres_kharid_maskoni_entry=tk.Entry(rehn_page_frame_kharid_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
addrres_kharid_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

tabaghe_kharid_maskoni=tk.Label(rehn_page_frame_kharid_maskoni,text="طبقه",bg="#0F6E6E",fg="#ffffff",width=10)
tabaghe_kharid_maskoni.grid(padx=8,pady=15,sticky="e",row=3,column=1)

tabaghe_kharid_maskoni_entry=tk.Entry(rehn_page_frame_kharid_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
tabaghe_kharid_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

vahed_kharid_maskoni=tk.Label(rehn_page_frame_kharid_maskoni,text="واحد",bg="#0F6E6E",fg="#ffffff",width=10)
vahed_kharid_maskoni.grid(padx=8,pady=15,sticky="e",row=4,column=1)

vahed_kharid_maskoni_entry=tk.Entry(rehn_page_frame_kharid_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
vahed_kharid_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

otagh_kharid_maskoni=tk.Label(rehn_page_frame_kharid_maskoni,text="اتاق",bg="#0F6E6E",fg="#ffffff",width=10)
otagh_kharid_maskoni.grid(padx=8,pady=15,sticky="e",row=5,column=1)

otagh_kharid_maskoni_entry=tk.Entry(rehn_page_frame_kharid_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
otagh_kharid_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=5,column=0)

gheimat_kharid_maskoni=tk.Label(rehn_page_frame_kharid_maskoni,text="قیمت",bg="#0F6E6E",fg="#ffffff",width=10)
gheimat_kharid_maskoni.grid(padx=8,pady=15,sticky="e",row=6,column=1)

gheimat_kharid_maskoni_entry=tk.Entry(rehn_page_frame_kharid_maskoni,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
gheimat_kharid_maskoni_entry.grid(padx=8,pady=15,sticky="w",row=6,column=0)

back_to_home_kharid_maskoni=tk.Button(kharid_maskoni_page,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_kharid_maskoni)
back_to_home_kharid_maskoni.place(x=650,y=535)

zakhire_kharid_maskoni=tk.Button(kharid_maskoni_page,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_forosh_maskkoni)
zakhire_kharid_maskoni.place(x=550,y=535)

photo_box_kharid_maskoni=tk.Frame(kharid_maskoni_page,width=410,height=450,background="#e4dde3")
photo_box_kharid_maskoni.place(x=40,y=40)
photo_lbl2_kharid_maskoni = tk.Label(photo_box_kharid_maskoni, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_kharid_maskoni.place(x=30,y=45)
add_img_btn_kharid_maskoni = tk.Button(photo_box_kharid_maskoni, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_kharid_maskoni.place(x=40,y=330)
#endregion
#------------------------امکانات خرید مسکونی--------------------
#region
option_frame_options_kharid_maskoni=tk.Frame(kharid_maskoni_page,width=300,height=30,background="#bbfbd1")
option_frame_options_kharid_maskoni.place(x=520,y=460)

option_label_kharid_maskoni=tk.Label(option_frame_options_kharid_maskoni,text='افزودن امکانات فایل',font=("Shabnam",10,"bold"),background="#FFFFFF",fg="#000000")
option_label_kharid_maskoni.pack(side="right",padx=1)

button_label_kharid_maskoni=tk.Label(option_frame_options_kharid_maskoni)
button_label_kharid_maskoni.pack(side="left",padx=1)
plus_button_kharid_maskoni=tk.Button(option_frame_options_kharid_maskoni,image=plus,command=open_option9,border=0)
plus_button_kharid_maskoni.pack()

option_lable_kharid_maskoni=tk.Frame(option_file_frame_kharid_maskoni,width=400,height=100,background="#bbfbd1")
option_lable_kharid_maskoni.pack(padx=10,pady=15)

parking_ch_btn_kharid_maskoni=tk.Checkbutton(option_lable_kharid_maskoni,image=parking_pic,background="#022578")
parking_ch_btn_kharid_maskoni.pack(padx=15,side="left")

asansor_ch_btn_kharid_maskoni=tk.Checkbutton(option_lable_kharid_maskoni,image=elvator_pic,background="#022578")
asansor_ch_btn_kharid_maskoni.pack(padx=15,side="left")

anbari_checkbuton_kharid_maskoni=tk.Checkbutton(option_lable_kharid_maskoni,image=warehouse_pic,background="#022578")
anbari_checkbuton_kharid_maskoni.pack(padx=15,side="right")

option_frame_options_kharid_maskoni2=tk.Frame(option_file_frame_kharid_maskoni,width=400,height=400,background="#bbfbd1",border=1)
option_frame_options_kharid_maskoni2.pack(padx=10,pady=15)

sarmaesh_kharid_maskoni=tk.Label(option_frame_options_kharid_maskoni2,text="سرمایش",background="#025578",fg="#ffffff")
sarmaesh_kharid_maskoni.grid(row=0,column=1,padx=15,pady=5)
sarmaesh_combo_kharid_maskoni=ttk.Combobox(option_frame_options_kharid_maskoni2)
sarmaesh_combo_kharid_maskoni["values"] = ("ندارد","پنکه سقفی","کولر ابی","کولر گازی ","ابی/گازی")
sarmaesh_combo_kharid_maskoni.grid(row=0,column=0,padx=15,pady=5)

garmaesh_kharid_maskoni=tk.Label(option_frame_options_kharid_maskoni2,text="گرمایش",background="#025578",fg="#ffffff")
garmaesh_kharid_maskoni.grid(row=1,column=1,padx=15,pady=5)
garmaesh_combo_kharid_maskoni=ttk.Combobox(option_frame_options_kharid_maskoni2)
garmaesh_combo_kharid_maskoni["values"] = ("ندارد","بخاری"," شوفاژ","گرمایش از کف ")
garmaesh_combo_kharid_maskoni.grid(row=1,column=0,padx=15,pady=5)

kaf_kharid_maskoni=tk.Label(option_frame_options_kharid_maskoni2,text="کف",background="#025578",fg="#ffffff")
kaf_kharid_maskoni.grid(row=2,column=1,padx=15,pady=5)
kaf_combo_kharid_maskoni=ttk.Combobox(option_frame_options_kharid_maskoni2)
kaf_combo_kharid_maskoni["values"] = ("سرامیک","موزاییک","پارکت")
kaf_combo_kharid_maskoni.grid(row=2,column=0,padx=15,pady=5)

toilet_kharid_maskoni=tk.Label(option_frame_options_kharid_maskoni2,text="سرویس بهداشتی",background="#025578",fg="#ffffff")
toilet_kharid_maskoni.grid(row=3,column=1,padx=5,pady=5)
toilet_combo_kharid_maskoni=ttk.Combobox(option_frame_options_kharid_maskoni2)
toilet_combo_kharid_maskoni["values"] = ("ایرانی","فرنگی","هردو")
toilet_combo_kharid_maskoni.grid(row=3,column=0,padx=15,pady=5)

zakhire_options_kharid_maskini=tk.Button(option_file_frame_kharid_maskoni,text="ذخیره",command=None,background="#079BDB",fg="#ffffff",width=8)
zakhire_options_kharid_maskini.place(x=170,y=330)

back_to_home_kharid_maskoni=tk.Button(option_file_frame_kharid_maskoni,text="بازگشت",command=back_to_kharid_maskoni_page,background="#079BDB",fg="#ffffff",width=8)
back_to_home_kharid_maskoni.place(x=95,y=330)
#endregion
#-----------------پنجره خرید اداری/تجاری-------------------
#region
kharid_edari_tejari = tk.Toplevel(root)
kharid_edari_tejari.title(" خرید اداری / تجاری")
kharid_edari_tejari.geometry("800x600")
kharid_edari_tejari.withdraw()
kharid_edari_tejari.configure(bg="#0F6E6E")

#---------------پنجره امکانات خرید اداری/تجاری----------------

option_file_frame_kharid_edari_tejari=tk.Toplevel(kharid_edari_tejari,background="#bbfbd1" )
option_file_frame_kharid_edari_tejari.title(" امکانات خرید اداری/تجاری")
option_file_frame_kharid_edari_tejari.geometry("500x370")
option_file_frame_kharid_edari_tejari.pack_propagate(False)
option_file_frame_kharid_edari_tejari.withdraw()

rehn_page_frame_asli_kharid_edari_tejari=tk.Frame(kharid_edari_tejari,width=490,height=800,bg="#5d6059",border=2)
rehn_page_frame_asli_kharid_edari_tejari.place(x=500,y=50)

melk_type_kharid_edari_tejari_lable=tk.Label(rehn_page_frame_asli_kharid_edari_tejari,text="متراژ ملک ",bg="#0F6E6E",fg="#ffffff",width=10)
melk_type_kharid_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=0,column=1)

melk_type_kharid_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_kharid_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
melk_type_kharid_edari_tejari_entry.grid(padx=8, pady=15,sticky="w",row=0,column=0) 

sal_sakht_kharid_edari_tejari_lable=tk.Label(rehn_page_frame_asli_kharid_edari_tejari,text="سال ساخت",bg="#0F6E6E",fg="#ffffff",width=10)
sal_sakht_kharid_edari_tejari_lable.grid(padx=8,pady=10,sticky="e",row=1,column=1)

sal_sakht_kharid_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_kharid_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
sal_sakht_kharid_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

addrres_kharid_edari_tejari_lable=tk.Label(rehn_page_frame_asli_kharid_edari_tejari,text="آدرس",bg="#0F6E6E",fg="#ffffff",width=10)
addrres_kharid_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=2,column=1)

addrres_kharid_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_kharid_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
addrres_kharid_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

tabaghe_kharid_edari_tejari_lable=tk.Label(rehn_page_frame_asli_kharid_edari_tejari,text="طبقه",bg="#0F6E6E",fg="#ffffff",width=10)
tabaghe_kharid_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=3,column=1)

tabaghe_kharid_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_kharid_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
tabaghe_kharid_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

vahed_kharid_edari_tejari_lable=tk.Label(rehn_page_frame_asli_kharid_edari_tejari,text="واحد",bg="#0F6E6E",fg="#ffffff",width=10)
vahed_kharid_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=4,column=1)

vahed_kharid_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_kharid_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
vahed_kharid_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)


mablagh_pish_kharid_edari_tejari_lable=tk.Label(rehn_page_frame_asli_kharid_edari_tejari,text="مبلغ ودیعه",bg="#0F6E6E",fg="#ffffff",width=10)
mablagh_pish_kharid_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=5,column=1)

mablagh_pish_kharid_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_kharid_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
mablagh_pish_kharid_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=5,column=0)

mablagh_ejare_kharid_edari_tejari_lable=tk.Label(rehn_page_frame_asli_kharid_edari_tejari,text=" مبلغ اجاره",bg="#0F6E6E",fg="#ffffff",width=10)
mablagh_ejare_kharid_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=6,column=1)

mablagh_ejare_kharid_edari_tejari_entry=tk.Entry(rehn_page_frame_asli_kharid_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),)
mablagh_ejare_kharid_edari_tejari_entry.grid(padx=8,pady=15,sticky="w",row=6,column=0)

rahn_kamel_kharid_edari_tejari_lable=tk.Label(rehn_page_frame_asli_kharid_edari_tejari,text=" رهن کامل؟ ",bg="#0F6E6E",fg="#ffffff",width=10)
rahn_kamel_kharid_edari_tejari_lable.grid(padx=8,pady=15,sticky="e",row=7,column=1)

rahn_kamel_check_btn_kharid_edari_tejari=tk.Checkbutton(rehn_page_frame_asli_kharid_edari_tejari,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
rahn_kamel_check_btn_kharid_edari_tejari.grid(padx=8,pady=15,sticky="w",row=7,column=0)

back_to_home_kharid_edari_tejari=tk.Button(kharid_edari_tejari,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_kharid_edari_tejari)
back_to_home_kharid_edari_tejari.place(x=650,y=535)

zakhire_kharid_edari_tejari=tk.Button(kharid_edari_tejari,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=None)
zakhire_kharid_edari_tejari.place(x=550,y=535)

photo_box_kharid_edari_tejari=tk.Frame(kharid_edari_tejari,width=410,height=450,background="#e4dde3")
photo_box_kharid_edari_tejari.place(x=40,y=40)
photo_lbl2_kharid_edari_tejari = tk.Label(photo_box_kharid_edari_tejari, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_kharid_edari_tejari.place(x=30,y=45)
add_img_btn_kharid_edari_tejari = tk.Button(photo_box_kharid_edari_tejari, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_kharid_edari_tejari.place(x=40,y=330)
#endregion
#---------------امکانات خرید اداری/تجاری-------------------
#region
option_frame_options_kharid_edari_tejari=tk.Frame(kharid_edari_tejari,width=300,height=30,background="#bbfbd1")
option_frame_options_kharid_edari_tejari.place(x=520,y=475)

option_label_kharid_edari_tejari=tk.Label(option_frame_options_kharid_edari_tejari,text='افزودن امکانات فایل',font=("Shabnam",10,"bold"),background="#FFFFFF",fg="#000000")
option_label_kharid_edari_tejari.pack(side="right",padx=1)

button_label_kharid_eedari_tejari=tk.Label(option_frame_options_kharid_edari_tejari)
button_label_kharid_eedari_tejari.pack(side="left",padx=1)
plus_button_kharid_eedari_tejari=tk.Button(option_frame_options_kharid_edari_tejari,image=plus,command=open_option10,border=0)
plus_button_kharid_eedari_tejari.pack()

option_frame_photosh_options_kharid_edari_tejari=tk.Frame(option_file_frame_kharid_edari_tejari,width=400,height=100,background="#bbfbd1")
option_frame_photosh_options_kharid_edari_tejari.pack(padx=10,pady=15)

parking_check_btn_kharid_edari_tejari=tk.Checkbutton(option_frame_photosh_options_kharid_edari_tejari,image=parking_pic,background="#022578")
parking_check_btn_kharid_edari_tejari.pack(padx=15,side="left")

asansor_check_btn_kharid_edari_tejari=tk.Checkbutton(option_frame_photosh_options_kharid_edari_tejari,image=elvator_pic,background="#022578")
asansor_check_btn_kharid_edari_tejari.pack(padx=15,side="left")

anbari_check_btn_kharid_edari_tejari=tk.Checkbutton(option_frame_photosh_options_kharid_edari_tejari,image=warehouse_pic,background="#022578")
anbari_check_btn_kharid_edari_tejari.pack(padx=15,side="right")

option_frame_combos_kharid_edari_tejari=tk.Frame(option_file_frame_kharid_edari_tejari,width=400,height=400,background="#bbfbd1",border=1)
option_frame_combos_kharid_edari_tejari.pack(padx=10,pady=15)


aab_va_gaz_emkanat_kharid_edari_tejari=tk.Label(option_frame_combos_kharid_edari_tejari,text="وضعیت آب و گاز",background="#0F6E6E",fg="#ffffff",width=17)
aab_va_gaz_emkanat_kharid_edari_tejari.grid(padx=8,pady=15,row=0,column=1)

aab_va_gaz_combo_emkanat_kharid_edari_tejari=ttk.Combobox(option_frame_combos_kharid_edari_tejari)
aab_va_gaz_combo_emkanat_kharid_edari_tejari["values"] = ("فقط گاز دارد","فقط آب دارد","آب و گاز دارد")
aab_va_gaz_combo_emkanat_kharid_edari_tejari.grid(padx=8,pady=15,row=0,column=0)

sarmayesh_emkanat_kharid_edari_tejari=tk.Label(option_frame_combos_kharid_edari_tejari,text="سیستم سرمایش",background="#0F6E6E",fg="#ffffff",width=17)
sarmayesh_emkanat_kharid_edari_tejari.grid(padx=8,pady=15,row=4,column=1)

sarmayesh_combo_emkanat_kharid_edari_tejari=ttk.Combobox(option_frame_combos_kharid_edari_tejari)
sarmayesh_combo_emkanat_kharid_edari_tejari["values"] = (" کولر گازی"," کولرآبی","پنکه سقفی","ندارد")
sarmayesh_combo_emkanat_kharid_edari_tejari.grid(padx=8,pady=15,row=4,column=0)

garmayesh_emkanat_kharid_edari_tejari=tk.Label(option_frame_combos_kharid_edari_tejari,text="سیستم گرمایش",background="#0F6E6E",fg="#ffffff",width=17)
garmayesh_emkanat_kharid_edari_tejari.grid(padx=8,pady=15,row=5,column=1)

garmayesh_combo_emkanat_kharid_edari_tejari=ttk.Combobox(option_frame_combos_kharid_edari_tejari)
garmayesh_combo_emkanat_kharid_edari_tejari["values"] = (" شوفاژ"," بخاری","ندارد")
garmayesh_combo_emkanat_kharid_edari_tejari.grid(padx=8,pady=15,row=5,column=0)

zakhire_options_kharid_edari_tejari=tk.Button(option_file_frame_kharid_edari_tejari,text="ذخیره",command=None,background="#079BDB",fg="#ffffff",width=8)
zakhire_options_kharid_edari_tejari.place(x=170,y=330)

back_to_home_kharid_edari_tejari=tk.Button(option_file_frame_kharid_edari_tejari,text="بازگشت",command=back_to_kharid_edari_tejari,background="#079BDB",fg="#ffffff",width=8)
back_to_home_kharid_edari_tejari.place(x=95,y=330)
#endregion
#--------------------پنجره خرید باغ/زمین-----------------------
#region
kharid_bagh_zamin = tk.Toplevel(root)
kharid_bagh_zamin.title("خرید باغ و زمین")
kharid_bagh_zamin.geometry("800x600")
kharid_bagh_zamin.withdraw()
kharid_bagh_zamin.configure(bg="#0F6E6E")

frame_asli_kharid_bagh_zamin=tk.Frame(kharid_bagh_zamin,width=490,height=800,bg="#5d6059",border=2)
frame_asli_kharid_bagh_zamin.place(x=500,y=90)

metraj_zamin_kharid_bagh_zamin_lable=tk.Label(frame_asli_kharid_bagh_zamin,text="متراژ",bg="#0F6E6E",fg="#ffffff",width=10)
metraj_zamin_kharid_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=0,column=1)

metraj_zamin_kharid_bagh_zamin_entry=tk.Entry(frame_asli_kharid_bagh_zamin,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),textvariable="متر مربع")
metraj_zamin_kharid_bagh_zamin_entry.grid(padx=8,pady=15,sticky="w",row=0,column=0)

bagh_type_kharid_bagh_zamin_lable=tk.Label(frame_asli_kharid_bagh_zamin,text="کاربری زمین",bg="#0F6E6E",fg="#ffffff",width=10)
bagh_type_kharid_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=1,column=1)

bagh_type_kharid_bagh_zamin_combo=ttk.Combobox(frame_asli_kharid_bagh_zamin,state="readonly")
bagh_type_kharid_bagh_zamin_combo["values"]=("باغ","زمین کشاورزی")
bagh_type_kharid_bagh_zamin_combo.set("باغ")
bagh_type_kharid_bagh_zamin_combo.grid(padx=8,pady=15,sticky="w",row=1,column=0)

bagh_loctaion_kharid_bagh_zamin_lable=tk.Label(frame_asli_kharid_bagh_zamin,text="منطقه و ادرس ",bg="#0F6E6E",fg="#ffffff",width=10)
bagh_loctaion_kharid_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=2,column=1)

bagh_loctaion_kharid_bagh_zamin_entry=tk.Entry(frame_asli_kharid_bagh_zamin,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
bagh_loctaion_kharid_bagh_zamin_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

gheimat_bagh_kharid_bagh_zamin_lable=tk.Label(frame_asli_kharid_bagh_zamin,text='قیمت کل',bg="#0F6E6E",fg="#ffffff",width=10)
gheimat_bagh_kharid_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=3,column=1)

gheimat_bagh_kharid_bagh_zamin_entry=tk.Entry(frame_asli_kharid_bagh_zamin,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
gheimat_bagh_kharid_bagh_zamin_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

gheimat_har_matr_babagh_zamin_kharid_bagh_zamin_lable=tk.Label(frame_asli_kharid_bagh_zamin,text='قیمت هر متر',bg="#0F6E6E",fg="#ffffff",width=10)
gheimat_har_matr_babagh_zamin_kharid_bagh_zamin_lable.grid(padx=8,pady=15,sticky="e",row=4,column=1)

gheimat_har_metr_babagh_zamin_kharid_bagh_zamin_entry=tk.Entry(frame_asli_kharid_bagh_zamin,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
gheimat_har_metr_babagh_zamin_kharid_bagh_zamin_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

photo_box_kharid_bagh_zamin=tk.Frame(kharid_bagh_zamin,width=410,height=450,background="#e4dde3")
photo_box_kharid_bagh_zamin.place(x=50,y=40)

photo_kharid_bagh_zamin_lable= tk.Label(photo_box_kharid_bagh_zamin, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_kharid_bagh_zamin_lable.place(x=30,y=45)
add_img_btn_kharid_bagh_zamin = tk.Button(photo_box_kharid_bagh_zamin, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_kharid_bagh_zamin.place(x=40,y=330)

back_to_home_kharid_bagh_zamin=tk.Button(kharid_bagh_zamin,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_kharid_bagh)
back_to_home_kharid_bagh_zamin.place(x=320,y=520)

zakhire_kharid_bagh_zamin=tk.Button(kharid_bagh_zamin,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=None)
zakhire_kharid_bagh_zamin.place(x=220,y=520)
#endregion
#-----------------------پنجره امکانات خرید باغ/زمین-------------------
#region
option_frame_options_kharid_bagh_zamin=tk.Frame(kharid_bagh_zamin,width=300,height=30,background="#bbfbd1")
option_frame_options_kharid_bagh_zamin.place(x=550,y=450)

option_label_kharid_bagh_zamin=tk.Label(option_frame_options_kharid_bagh_zamin,text='افزودن امکانات فایل',font=("Shabnam",10,"bold"),background="#FFFFFF",fg="#000000")
option_label_kharid_bagh_zamin.pack(side="right",padx=1)

button_label_kharid_bagh_zamin=tk.Label(option_frame_options_kharid_bagh_zamin)
button_label_kharid_bagh_zamin.pack(side="left",padx=1)
plus_button_kharid_bagh_zamin=tk.Button(option_frame_options_kharid_bagh_zamin,image=plus,command=open_option11,border=0)
plus_button_kharid_bagh_zamin.pack()

option_file_frame_kharid_bagh_zamin=tk.Toplevel(kharid_bagh_zamin,background="#bbfbd1")
option_file_frame_kharid_bagh_zamin.title(" امکانات خرید باغ/زمین")
option_file_frame_kharid_bagh_zamin.geometry("690x630")
option_file_frame_kharid_bagh_zamin.pack_propagate(False)
option_file_frame_kharid_bagh_zamin.withdraw()

mini_frame_kharid_bagh_zamin=tk.Frame(option_file_frame_kharid_bagh_zamin)
mini_frame_kharid_bagh_zamin.place(x=290,y=20)
karbary_zamin_kharid_bagh_zamin=tk.Label(mini_frame_kharid_bagh_zamin,text="کاربری زمین",bg="#0F6E6E",fg="#ffffff",width=10)
karbary_zamin_kharid_bagh_zamin.pack(padx=5,pady=5,side="right")

karbary_zamin_kharid_bagh_zamin_combo=ttk.Combobox(mini_frame_kharid_bagh_zamin,state="readonly")
karbary_zamin_kharid_bagh_zamin_combo["values"]=("باغ","زمین کشاورزی")
karbary_zamin_kharid_bagh_zamin_combo.set("باغ")
karbary_zamin_kharid_bagh_zamin_combo.pack(padx=5,pady=5,side="left")

karbary_zamin_kharid_bagh_zamin_combo.bind("<<ComboboxSelected>>",change_bagh_zamin_kharid_bagh)

option_frame_kharid_bagh_zamin=tk.Frame(option_file_frame_kharid_bagh_zamin,width=430,height=290,background="#d1e0df")
option_frame_kharid_bagh_zamin.place(x=60,y=60)

metraj_derakht_kharid_bagh_zamin_lable=tk.Label(option_frame_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="متراژ درخت کاری")
metraj_derakht_kharid_bagh_zamin_lable.grid(padx=10,pady=5,row=0,column=4)

metraj_derakht_kharid_bagh_zamin_entry=tk.Entry(option_frame_kharid_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff")
metraj_derakht_kharid_bagh_zamin_entry.grid(padx=10,pady=5,row=0,column=3)

tedad_derakht_kharid_bagh_zamin_lable=tk.Label(option_frame_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="تعداد درخت")
tedad_derakht_kharid_bagh_zamin_lable.grid(padx=10,pady=5,row=1,column=4)

tedad_derakht_kharid_bagh_zamin_entry=tk.Entry(option_frame_kharid_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff")
tedad_derakht_kharid_bagh_zamin_entry.grid(padx=10,pady=5,row=1,column=3)

abyari_kharid_bagh_zamin_lable=tk.Label(option_frame_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع ابیاری")
abyari_kharid_bagh_zamin_lable.grid(padx=10,pady=5,row=2,column=4)

abyari_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_kharid_bagh_zamin)
abyari_kharid_bagh_zamin_combo["values"]=("سطحی","بارانی","قطره ای","تحت فشار")
abyari_kharid_bagh_zamin_combo.set("سطحی")
abyari_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=2,column=3)

type_tree_kharid_bagh_zamin_lable=tk.Label(option_frame_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع درخت")
type_tree_kharid_bagh_zamin_lable.grid(padx=10,pady=5,row=3,column=4)

type_tree_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_kharid_bagh_zamin)
type_tree_kharid_bagh_zamin_combo["values"]=(" ","پسته","بادام","گردو","شلیل","هلو","سیب","انگور"
                           ,"انجیر","زردالو","گیلاس","البالو")
type_tree_kharid_bagh_zamin_combo.set("گردو")
type_tree_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=3,column=3)
type_tree_kharid_btn=tk.Button(option_frame_kharid_bagh_zamin,text="افزودن درخت",command=add_tree3,bg="#007acc",width=10)
type_tree_kharid_btn.grid(padx=10,pady=5,row=4,column=4)

label_natige_kharid_bagh_zamin=tk.Label(option_frame_forosh_bagh_zamin,text="")
label_natige_kharid_bagh_zamin.grid(padx=10,pady=5,row=4,column=3)

chah_kharid_bagh_zamin=tk.Checkbutton(option_frame_kharid_bagh_zamin,text="چاه",background="#d6d0d0")
chah_kharid_bagh_zamin.grid(padx=0,pady=5,row=5,column=0)

estakhr_kharid_bagh_zamin=tk.Checkbutton(option_frame_kharid_bagh_zamin,text="استخر",background="#d6d0d0")
estakhr_kharid_bagh_zamin.grid(padx=0,pady=5,row=5,column=1)

loleh_keshi_ab_kharid_bagh_zamin=tk.Checkbutton(option_frame_kharid_bagh_zamin,text="اب لوله کشی",background="#d6d0d0")
loleh_keshi_ab_kharid_bagh_zamin.grid(padx=0,pady=5,row=5,column=2)

bargh_keshi_kharid_bagh_zamin=tk.Checkbutton(option_frame_kharid_bagh_zamin,text="برق کشی",background="#d6d0d0")
bargh_keshi_kharid_bagh_zamin.grid(padx=0,pady=5,row=5,column=3)

gas_keshi_kharid_bagh_zamin=tk.Checkbutton(option_frame_kharid_bagh_zamin,text="گاز کشی",background="#d6d0d0")
gas_keshi_kharid_bagh_zamin.grid(padx=0,pady=5,row=5,column=4)

var0_kharid_bagh_zamin=tk.IntVar(value=0)#چک باتن پیش فرض تیک نخورده باشه

otagh_check_btn_kharid_bagh_zamin=tk.Checkbutton(option_frame_kharid_bagh_zamin,variable=var0,image=warehouse_pic,background="#022578",text="ساختمان",command=home_true_false3)
otagh_check_btn_kharid_bagh_zamin.grid(padx=10,pady=5,row=6,column=4)

metraj_vila_kharid_bagh_zamin=tk.Label(option_frame_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="متراژ سازه")
metraj_vila_kharid_bagh_zamin.grid(padx=10,pady=5,row=7,column=4)

metraj_vila_kharid_bagh_zamin_entry=tk.Entry(option_frame_kharid_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
metraj_vila_kharid_bagh_zamin_entry.grid(padx=10,pady=5,row=7,column=3)

sal_sakht_vila_kharid_bagh_zamin_lable=tk.Label(option_frame_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="سال ساخت")
sal_sakht_vila_kharid_bagh_zamin_lable.grid(padx=10,pady=5,row=8,column=4)

sal_sakht_vila_kharid_bagh_zamin_entry=tk.Entry(option_frame_kharid_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
sal_sakht_vila_kharid_bagh_zamin_entry.grid(padx=10,pady=5,row=8,column=3)

type_vila_kharid_bagh_zamin=tk.Label(option_frame_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="نوع سازه")
type_vila_kharid_bagh_zamin.grid(padx=10,pady=5,row=9,column=4)

type_vila_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_kharid_bagh_zamin,state="disabled")
type_vila_kharid_bagh_zamin_combo["values"]=("آجری","بلوکی","کانکس","چوبی")
type_vila_kharid_bagh_zamin_combo.set("آجری")
type_vila_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=9,column=3)

toilet_kharid_bagh_zamin_lable=tk.Label(option_frame_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="سرویس بهداشتی")
toilet_kharid_bagh_zamin_lable.grid(padx=10,pady=5,row=10,column=4)

toilet_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_kharid_bagh_zamin,state="disabled")
toilet_kharid_bagh_zamin_combo["values"]=(" ","ندارد","فرنگی","ایرانی","هردو")
toilet_kharid_bagh_zamin_combo.set("")
toilet_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=10,column=3)

hamam_kharid_bagh_zamin=tk.Label(option_frame_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="حمام")
hamam_kharid_bagh_zamin.grid(padx=10,pady=5,row=11,column=4)

hamam_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_kharid_bagh_zamin,state="disabled")
hamam_kharid_bagh_zamin_combo["values"]=(" ","ندارد","دارد")
hamam_kharid_bagh_zamin_combo.set(" ")
hamam_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=11,column=3)

sanad_kharid_bagh_zamin_lable=tk.Label(option_frame_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="سند")
sanad_kharid_bagh_zamin_lable.grid(padx=10,pady=5,row=12,column=4)

sanad_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_kharid_bagh_zamin,state="disabled")
sanad_kharid_bagh_zamin_combo["values"]=(" ","ندارد","تک برگ","قولنامه ای","مشاع")
sanad_kharid_bagh_zamin_combo.set(" ")
sanad_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=12,column=3)

option_kharid_bagh_zamin=tk.Label(option_frame_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="امکانات تفریحی")
option_kharid_bagh_zamin.grid(padx=10,pady=5,row=13,column=4)

option_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_kharid_bagh_zamin,state="disabled")
option_kharid_bagh_zamin_combo["values"]=(" ","استخر","جکوزی","باربیکیو")
option_kharid_bagh_zamin_combo.set(" ")
option_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=13,column=3)
add_option_button_kharid_bagh_zamin=tk.Button(option_frame_kharid_bagh_zamin,text="افزودن امکانات",command=add_option3,bg="#007acc",width=10)
add_option_button_kharid_bagh_zamin.grid(padx=10,pady=5,row=13,column=2)
lable_natige_add_kharid_bagh_zamin=tk.Label(option_frame_kharid_bagh_zamin,text="")
lable_natige_add_kharid_bagh_zamin.grid(padx=10,pady=5,row=13,column=1)

mojavez_sakht_check_btn_kharid_bagh_zamin=tk.Checkbutton(option_frame_kharid_bagh_zamin,text="مجوز ساختن",background="#d6d0d0",state="disabled")
mojavez_sakht_check_btn_kharid_bagh_zamin.grid(padx=10,pady=5,row=14,column=4)

mohavate_sazi_check_btn_kharid_bagh_zamin=tk.Checkbutton(option_frame_kharid_bagh_zamin,text="محوطه سازی",background="#d6d0d0",state="disabled")
mohavate_sazi_check_btn_kharid_bagh_zamin.grid(padx=10,pady=5,row=14,column=3)

divar_kharid_bagh_zamin=tk.Checkbutton(option_frame_kharid_bagh_zamin,text="دیوار کشی",background="#d6d0d0")
divar_kharid_bagh_zamin.grid(padx=10,pady=5,row=14,column=2)

zakhire_options_kharid_bagh_zamin=tk.Button(option_file_frame_kharid_bagh_zamin,command=None,text="ذخیره",background="#079BDB",fg="#ffffff",width=8)
zakhire_options_kharid_bagh_zamin.place(x=170,y=580)

back_to_kharid_bagh_zamin=tk.Button(option_file_frame_kharid_bagh_zamin,text="بازگشت",command=back_to_kharid_bagh_zamin,background="#079BDB",fg="#ffffff",width=8)
back_to_kharid_bagh_zamin.place(x=95,y=580)
#endregion
#-------------------------تعویض کاربری به زمین در قسمت خرید باغ/زمین-------------
#region
option_frame_option2_kharid_bagh_zamin=tk.Frame(option_file_frame_kharid_bagh_zamin,width=445,height=290,background="#d1e0df")
option_frame_option2_kharid_bagh_zamin.place_forget()

metraj_zamin2_kharid_bagh_zamin_lable=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=13,text="متراژ زمین")
metraj_zamin2_kharid_bagh_zamin_lable.grid(padx=10,pady=5,row=0,column=4)

metraj_zamin2_kharid_bagh_zamin_entry=tk.Entry(option_frame_option2_kharid_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff")
metraj_zamin2_kharid_bagh_zamin_entry.grid(padx=10,pady=5,row=0,column=3)

karbari_kharid_bagh_zamin_lable=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع کاربری")
karbari_kharid_bagh_zamin_lable.grid(padx=10,pady=5,row=1,column=4)

karbari_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_option2_kharid_bagh_zamin)
karbari_kharid_bagh_zamin_combo["values"]=(" ","زراعی","باغی","گلخانه ای","دامداری ","مرغداری",
                               "دامداری و مرغداری","آیش")                             
karbari_kharid_bagh_zamin_combo.set(" ")
karbari_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=1,column=3)

khak_kharid_bagh_zamin=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="نوع خاک")
khak_kharid_bagh_zamin.grid(padx=10,pady=5,row=2,column=4)

khak_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_option2_kharid_bagh_zamin)
khak_kharid_bagh_zamin_combo["values"]=(" ","رسی","شنی","لومی","رسی_شنی","شنی_لومی",
                               "رسی_لومی")                             
khak_kharid_bagh_zamin_combo.set(" ")
khak_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=2,column=3)

ab_kharid_bagh_zamin=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="منبع اب")
ab_kharid_bagh_zamin.grid(padx=10,pady=5,row=3,column=4)

ab_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_option2_kharid_bagh_zamin)
ab_kharid_bagh_zamin_combo["values"]=(" ","چاه","قنات","رودخانه","کانال ابیاری","چشمه",
                               "آب لوله کشی کشاورزی","تانکر","استخر")                             
ab_kharid_bagh_zamin_combo.set(" ")
ab_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=3,column=3)

zamin_shekl_kharid_bagh_zamin_kharid_lable=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="توپوگرافی")
zamin_shekl_kharid_bagh_zamin_kharid_lable.grid(padx=10,pady=5,row=4,column=4)

zamin_shekl_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_option2_kharid_bagh_zamin)
zamin_shekl_kharid_bagh_zamin_combo["values"]=(" "," صاف و یکدست"," شیب دار"," باتلاقی","سنگی ")                             
zamin_shekl_kharid_bagh_zamin_combo.set(" ")
zamin_shekl_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=4,column=3)

add_topo2_button_kharid_bagh_zamin=tk.Button(option_frame_option2_kharid_bagh_zamin,text=" مورد دلخواه",command=add_topo3,bg="#007acc",width=10)
add_topo2_button_kharid_bagh_zamin.grid(padx=10,pady=5,row=4,column=2)
label_natige_topo_add_kharid_bagh_zamin=tk.Label(option_frame_option2_kharid_bagh_zamin,text="")
label_natige_topo_add_kharid_bagh_zamin.grid(padx=10,pady=5,row=4,column=1)

kesht_kharid_bagh_zamin=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="سطح زیر کشت")
kesht_kharid_bagh_zamin.grid(padx=10,pady=5,row=5,column=4)

kesht_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_option2_kharid_bagh_zamin)
kesht_kharid_bagh_zamin_combo["values"]=("بدون کشت"," زیر کشت")                             
kesht_kharid_bagh_zamin_combo.set("بدون کشت ")
kesht_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=5,column=3)
kesht_kharid_bagh_zamin_combo.bind("<<ComboboxSelected>>",choos_kesht3)

kesht_kharid_bagh_zamin_label=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#0F6E6E",fg="#ffffff",width=10,text="محصول زیرکشت")
kesht_kharid_bagh_zamin_label.grid(padx=10,pady=5,row=5,column=2)

kesht_kharid_bagh_zamin_entry=tk.Entry(option_frame_option2_kharid_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
kesht_kharid_bagh_zamin_entry.grid(padx=10,pady=5,row=5,column=1)

security_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="اتاق نگهبان",background="#d6d0d0")
security_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=6,column=0)

bargh_kesi_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="برق تک فاز",background="#d6d0d0")
bargh_kesi_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=6,column=1)

bargh_keshi_zamin_kharid_bagh_zamin2=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="برق سه فاز",background="#d6d0d0")
bargh_keshi_zamin_kharid_bagh_zamin2.grid(padx=10,pady=6,row=6,column=2)

anbar_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="انبار/سوله",background="#d6d0d0")
anbar_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=6,column=3)

fans_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="فنس/دیوار",background="#d6d0d0")
fans_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=6,column=4)

mojavez_golkhane_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="اجازه ساخت گلخانه",background="#d6d0d0")
mojavez_golkhane_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=7,column=0)

mojavez_chah_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="اجازه حفر چاه",background="#d6d0d0")
mojavez_chah_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=7,column=1)

bardasht_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="حق برداشت ",background="#d6d0d0")
bardasht_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=7,column=2)

dam_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="اجازه ورود دام",background="#d6d0d0")
dam_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=7,column=3)
#endregion
#-------------------پنجره خرید کارگاه------------------------
#region
kharid_kargah= tk.Toplevel(root)
kharid_kargah.title("خرید کارگاه")
kharid_kargah.geometry("800x600")
kharid_kargah.withdraw()
kharid_kargah.configure(bg="#0F6E6E")

kharid_kargah_frame=tk.Frame(kharid_kargah,width=490,height=800,bg="#5d6059",border=2)
kharid_kargah_frame.place(x=500,y=90)

karbari_zamin_kharid_kargah=tk.Label(kharid_kargah_frame,text="کاربری زمین",bg="#0F6E6E",fg="#ffffff",width=10)
karbari_zamin_kharid_kargah.grid(padx=8,pady=15,sticky="e",row=0,column=1)

kharid_kargah_lable=tk.Label(kharid_kargah_frame,text=" کارگاه ",bg="#C2C2C2",fg="#313131",width=20)
kharid_kargah_lable.grid(padx=8,pady=15,sticky="e",row=0,column=0)

kharid_kargah_lable=tk.Label(kharid_kargah_frame,text="متراژ",bg="#0F6E6E",fg="#ffffff",width=10)
kharid_kargah_lable.grid(padx=8,pady=15,sticky="e",row=1,column=1)

metraj_kharid_kargah_entry=tk.Entry(kharid_kargah_frame,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),textvariable="متر مربع")
metraj_kharid_kargah_entry.grid(padx=8,pady=15,sticky="w",row=1,column=0)

loctaion_kharid_kargah_lable=tk.Label(kharid_kargah_frame,text="منطقه و ادرس ",bg="#0F6E6E",fg="#ffffff",width=10)
loctaion_kharid_kargah_lable.grid(padx=8,pady=15,sticky="e",row=2,column=1)

loctaion_kharid_kargah_entry=tk.Entry(kharid_kargah_frame,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
loctaion_kharid_kargah_entry.grid(padx=8,pady=15,sticky="w",row=2,column=0)

mablagh_pish_kharid_kargah_lable=tk.Label(kharid_kargah_frame,text='ودیعه',bg="#0F6E6E",fg="#ffffff",width=10)
mablagh_pish_kharid_kargah_lable.grid(padx=8,pady=15,sticky="e",row=3,column=1)

mablagh_pish_kharid_kargah_entry=tk.Entry(kharid_kargah_frame,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
mablagh_pish_kharid_kargah_entry.grid(padx=8,pady=15,sticky="w",row=3,column=0)

gheimat_har_metr_kharid_kargah_lable=tk.Label(kharid_kargah_frame,text='قیمت هر متر',bg="#0F6E6E",fg="#ffffff",width=10)
gheimat_har_metr_kharid_kargah_lable.grid(padx=8,pady=15,sticky="e",row=4,column=1)

gheimat_har_metr_kharid_kargah_entry=tk.Entry(kharid_kargah_frame,bg="#C2C2C2", fg="#180202",font=("Shabnam", 10))
gheimat_har_metr_kharid_kargah_entry.grid(padx=8,pady=15,sticky="w",row=4,column=0)

photo_box_kharid_kargah=tk.Frame(kharid_kargah,width=410,height=450,background="#e4dde3")
photo_box_kharid_kargah.place(x=50,y=40)

photo_lbl2_kharid_kargah = tk.Label(photo_box_kharid_kargah, text="[تصویر ملک]", bg="gray", width=50, height=15)
photo_lbl2_kharid_kargah.place(x=30,y=45)
add_img_btn_kharid_kargah = tk.Button(photo_box_kharid_kargah, text="افزودن تصویر", bg="#007acc", fg="white",command=open_file,height=3,width=13)
add_img_btn_kharid_kargah.place(x=40,y=330)

back_to_home_kharid_kargah=tk.Button(kharid_kargah,text="بازگشت",bg="#13f",fg="white",width=12,height=2,command=back_home_kharid_kargah)
back_to_home_kharid_kargah.place(x=320,y=520)

zakhire_kharid_kargah=tk.Button(kharid_kargah,text="ذخیره",bg="#13f",fg="white",width=12,height=2,command=save_kharid_karghah)
zakhire_kharid_kargah.place(x=220,y=520)
#endregion
#---------------------پنجره امکانات اجاره کارگاه---------------------
#region
option_frame_kharid_kargah=tk.Frame(kharid_kargah,width=300,height=30,background="#bbfbd1")
option_frame_kharid_kargah.place(x=550,y=450)

option_frame_kharid_kargah_lable=tk.Label(option_frame_kharid_kargah,text='افزودن امکانات فایل',font=("Shabnam",10,"bold"),background="#FFFFFF",fg="#000000")
option_frame_kharid_kargah_lable.pack(side="right",padx=1)

button_lable_kharid_kargah=tk.Label(option_frame_kharid_kargah)
button_lable_kharid_kargah.pack(side="left",padx=1)
plus_button_kharid_kargah=tk.Button(option_frame_kharid_kargah,image=plus,command=open_option12,border=0)
plus_button_kharid_kargah.pack()

option_file_frame_kharid_kargah=tk.Toplevel(kharid_kargah,background="#bbfbd1")
option_file_frame_kharid_kargah.title(" امکانات خرید کارگاه")
option_file_frame_kharid_kargah.geometry("500x450")
option_file_frame_kharid_kargah.pack_propagate(False)
option_file_frame_kharid_kargah.withdraw()
mini_frame_kharid_kargah=tk.Frame(option_file_frame_kharid_kargah)
mini_frame_kharid_kargah.place(x=290,y=20)


option_frame_asli_kharid_kargah=tk.Frame(option_file_frame_kharid_kargah,width=400,height=400,background="#bbfbd1")
option_frame_asli_kharid_kargah.place(x=60,y=60)

sal_sakht_kharid_kargah_lable=tk.Label(option_frame_asli_kharid_kargah,bg="#0F6E6E",fg="#ffffff",width=13,text="سال ساخت")
sal_sakht_kharid_kargah_lable.grid(padx=10,pady=5,row=0,column=1)

sal_sakht_kharid_kargah_entry=tk.Entry(option_frame_asli_kharid_kargah,width=10,bg="#ffffff",fg="#000000")
sal_sakht_kharid_kargah_entry.grid(padx=10,pady=5,row=0,column=0)

vaziat_bagh_kharid_kargah=tk.Label(option_frame_asli_kharid_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text="وضعیت برق")
vaziat_bagh_kharid_kargah.grid(padx=10,pady=5,row=1,column=1)

vaziat_bargh_kharid_kargah_combo=ttk.Combobox(option_frame_asli_kharid_kargah)
vaziat_bargh_kharid_kargah_combo["values"]=("برق شهری","سه فاز","تک فاز")
vaziat_bargh_kharid_kargah_combo.set("برق شهری")
vaziat_bargh_kharid_kargah_combo.grid(padx=10,pady=5,row=1,column=0)

garmayesh_kharid_kargah=tk.Label(option_frame_asli_kharid_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text="سیستم گرمایش")
garmayesh_kharid_kargah.grid(padx=10,pady=5,row=2,column=1)

garmayesh_type_kharid_kargah_combo=ttk.Combobox(option_frame_asli_kharid_kargah)
garmayesh_type_kharid_kargah_combo["values"]=("بخاری ","شوفاژ ","فن کوئل(گرما) ")
garmayesh_type_kharid_kargah_combo.set(" بخاری")
garmayesh_type_kharid_kargah_combo.grid(padx=10,pady=3,row=2,column=0)

sarmayesh_kharid_kargah=tk.Label(option_frame_asli_kharid_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text="سیستم سرمایش ")
sarmayesh_kharid_kargah.grid(padx=10,pady=5,row=3,column=1)

sarmayesh_fan_kharid_kargah=tk.Checkbutton(option_frame_asli_kharid_kargah,text="تهویه(فن)",background="#d6d0d0")
sarmayesh_fan_kharid_kargah.grid(padx=0,pady=5,row=4,column=0)

sarmayesh_panke_kharid_kargah=tk.Checkbutton(option_frame_asli_kharid_kargah,text="پنکه سقفی",background="#d6d0d0")
sarmayesh_panke_kharid_kargah.grid(padx=0,pady=5,row=4,column=1)

sarmayesh_kooler_abi_kharid_kargah=tk.Checkbutton(option_frame_asli_kharid_kargah,text="کولر آبی",background="#d6d0d0")
sarmayesh_kooler_abi_kharid_kargah.grid(padx=0,pady=5,row=5,column=0)

sarmayesh_kooler_gazi_kharid_kargah=tk.Checkbutton(option_frame_asli_kharid_kargah,text="کولر گازی",background="#d6d0d0")
sarmayesh_kooler_gazi_kharid_kargah.grid(padx=0,pady=5,row=5,column=1)

vaziat_ab_kharid_kargah=tk.Label(option_frame_asli_kharid_kargah,bg="#0F6E6E",fg="#ffffff",width=13,text=" وضعیت آب")
vaziat_ab_kharid_kargah.grid(padx=10,pady=5,row=6,column=1)

vaziat_ab_kharid_kargah_combo=ttk.Combobox(option_frame_asli_kharid_kargah,width=35)
vaziat_ab_kharid_kargah_combo["values"]=(" آب مستقیم لوله کشی (بدون فشار) " ," آب مستقیم لوله کشی (همراه موتور فشار) ","دارای منبع(همراه موتور فشار)","دارای منبع(بدون فشار)")
vaziat_ab_kharid_kargah_combo.set(" آب مستقیم لوله کشی (بدون فشار) ")
vaziat_ab_kharid_kargah_combo.grid(padx=10,pady=5,row=6,column=0)

abzar_kharid_kargah=tk.Label(option_frame_asli_kharid_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text=" ابزار صنعتی ")
abzar_kharid_kargah.grid(padx=10,pady=5,row=7,column=1)

abzaar_kharid_kargah_combo=ttk.Combobox(option_frame_asli_kharid_kargah,width=23)
abzaar_kharid_kargah_combo["values"]=("(کارگاه خالی) بدون دستگاه ","دارای دستگاه های تولیدی")
abzaar_kharid_kargah_combo.set("(کارگاه خالی) بدون دستگاه ")
abzaar_kharid_kargah_combo.grid(padx=10,pady=5,row=7,column=0)

toilet_kharid_kargah=tk.Label(option_frame_asli_kharid_kargah,bg="#0F6E6E",fg="#ffffff",width=15,text="سرویس بهداشتی")
toilet_kharid_kargah.grid(padx=10,pady=5,row=8,column=1)

toilet_kharid_kargah_combo=ttk.Combobox(option_frame_asli_kharid_kargah)
toilet_kharid_kargah_combo["values"]=("دارد","ندارد")
toilet_kharid_kargah_combo.set("دارد")
toilet_kharid_kargah_combo.grid(padx=10,pady=5,row=8,column=0)

hamam_kharid_kargah=tk.Label(option_frame_asli_kharid_kargah,bg="#0F6E6E",fg="#ffffff",width=13,text="حمام")
hamam_kharid_kargah.grid(padx=10,pady=5,row=9,column=1)

hamam_kharid_kargah__combo=ttk.Combobox(option_frame_asli_kharid_kargah)
hamam_kharid_kargah__combo["values"]=("ندارد","دارد")
hamam_kharid_kargah__combo.set("ندارد")
hamam_kharid_kargah__combo.grid(padx=10,pady=5,row=9,column=0)

otagh_kharid_kargah=tk.Label(option_frame_asli_kharid_kargah,bg="#0F6E6E",fg="#ffffff",width=17,text="اتاق رخت کن و استراحت")
otagh_kharid_kargah.grid(padx=10,pady=5,row=10,column=1)

otagh_kharid_kargah_combo=ttk.Combobox(option_frame_asli_kharid_kargah)
otagh_kharid_kargah_combo["values"]=("ندارد","دارد")
otagh_kharid_kargah_combo.set("ندارد")
otagh_kharid_kargah_combo.grid(padx=10,pady=5,row=10,column=0)

zakhire_options_kharid_kargah=tk.Button(option_file_frame_kharid_kargah,text="ذخیره",background="#079BDB",fg="#ffffff",width=8)
zakhire_options_kharid_kargah.place(x=170,y=420)

back_to_kharid_kargah=tk.Button(option_file_frame_kharid_kargah,text="بازگشت",command=back_to_kharid_kargah,background="#079BDB",fg="#ffffff",width=8)
back_to_kharid_kargah.place(x=95,y=420)
#endregion
#پنجره مشارکت در ساخت و ساز
#---------------------------------------------------------------
#region
mosharecat_window=tk.Toplevel(root,background="#adf6ed")
mosharecat_window.geometry("800x600")
mosharecat_window.title("پنجره مشارکت در ساخت و ساز")
mosharecat_window.pack_propagate(False)
mosharecat_window.rowconfigure(0, weight=1)
mosharecat_window.columnconfigure(0, weight=1)


#فریم اول مشخصات ملک

melk_mosharecat_data=tk.Frame(mosharecat_window,bg="#b2c4ff",height=600,width=1000)
melk_mosharecat_data.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# ستون‌ها برای گسترش Entry/Combobox
melk_mosharecat_data.columnconfigure(0, weight=1)
melk_mosharecat_data.columnconfigure(1, weight=0)

melk_mosharecat_data.pack_propagate(False)

type_melk_mosharecat=tk.Label(melk_mosharecat_data,text="نوع ملک",bg="#efefef" ,fg="black",width=10)
type_melk_mosharecat.grid(padx=5,pady=10,row=0,column=1)

type_melk_mosharecat_combo=ttk.Combobox(melk_mosharecat_data)
type_melk_mosharecat_combo["values"]=(' ',"کلنگی","زمین","ویلایی","آپارتمان")
type_melk_mosharecat_combo.set(' ')
type_melk_mosharecat_combo.grid(padx=5,pady=10,row=0,column=0)

address_melk_moshrecat=tk.Label(melk_mosharecat_data,text="آدرس دقیق",bg="#e5e5e5",fg="black",width=10)
address_melk_moshrecat.grid(padx=5,pady=10,row=1,column=1)

address_melk_moshrecat_entry=scrolledtext.ScrolledText(melk_mosharecat_data,width=30,height=8)
address_melk_moshrecat_entry.grid(padx=5,pady=2,row=1,column=0)

metraj_melk_moshrecat=tk.Label(melk_mosharecat_data,text="متراژ",bg="#e5e5e5",fg="black",width=10)
metraj_melk_moshrecat.grid(padx=5,pady=10,row=2,column=1)

metraj_melk_moshrecat_entry=tk.Entry(melk_mosharecat_data,bg="#e5e5e5",fg="black")
metraj_melk_moshrecat_entry.grid(padx=5,pady=10,row=2,column=0)

arzzamin_melk_moshrecat=tk.Label(melk_mosharecat_data,text="عرض زمین",bg="#e5e5e5",fg="black",width=10)
arzzamin_melk_moshrecat.grid(padx=5,pady=10,row=3,column=1)

arzzamin_melk_moshrecat_entry=tk.Entry(melk_mosharecat_data,bg="#e5e5e5",fg="black")
arzzamin_melk_moshrecat_entry.grid(padx=5,pady=10,row=3,column=0)

located_melk_mosharecat=tk.Label(melk_mosharecat_data,text="موقعیت ملک",bg="#e5e5e5",fg="black",width=10)
located_melk_mosharecat.grid(padx=5,pady=10,row=4,column=1)

located_melk_mosharecat_combo=ttk.Combobox(melk_mosharecat_data)
located_melk_mosharecat_combo["values"]=(' شمالی',"جنوبی","دونبش","سرنبش")
located_melk_mosharecat_combo.set( "شمالی")
located_melk_mosharecat_combo.grid(padx=5,pady=10,row=4,column=0)

karbary_melk_mosharecat=tk.Label(melk_mosharecat_data,text="کاربری",bg="#e5e5e5",fg="black",width=10)
karbary_melk_mosharecat.grid(padx=5,pady=10,row=5,column=1)

karbary_melk_mosharecat_combo=ttk.Combobox(melk_mosharecat_data)
karbary_melk_mosharecat_combo["values"]=("مسکونی","تجاری","هردو")
karbary_melk_mosharecat_combo.set( "مسکونی")
karbary_melk_mosharecat_combo.grid(padx=5,pady=10,row=5,column=0)

sanad_melk_mosharecat=tk.Label(melk_mosharecat_data,text="وضعیت سند",bg="#e5e5e5",fg="black",width=10)
sanad_melk_mosharecat.grid(padx=5,pady=10,row=6,column=1)

sanad_melk_mosharecat_combo=ttk.Combobox(melk_mosharecat_data)
sanad_melk_mosharecat_combo["values"]=("تک برگ","قول نامه","ثبتی","نامشخص")
sanad_melk_mosharecat_combo.set( "تک برگ")
sanad_melk_mosharecat_combo.grid(padx=5,pady=10,row=6,column=0)

edame_moshrecat_melk1=tk.Button(melk_mosharecat_data,text="ذخیره",background="#079BDB",fg="#ffffff",width=8,command=None)
edame_moshrecat_melk1.place(x=200,y=500)

back_to_root=tk.Button(melk_mosharecat_data,text="برگشت به صفحه اصلی",command=None,background="#079BDB",fg="#ffffff",width=17)
back_to_root.place(x=50,y=500)

#---------------------------------------------------------------------------
#---------------------------- و سازنده فریم دوم مشخصات مالک--------------------------------------
malek_mosharecat_frame=tk.Frame(mosharecat_window,bg="#b2c4ff",height=600,width=1000)
malek_mosharecat_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

malek_mosharecat_frame.columnconfigure(0, weight=1)
malek_mosharecat_frame.columnconfigure(1, weight=0)

malek_mosharecat_frame.pack_propagate(False)

name_malek_mosharecat=tk.Label(malek_mosharecat_frame,text="نام مالک/مالکان",bg="#efefef" ,fg="black",width=13)
name_malek_mosharecat.grid(padx=5,pady=10,row=0,column=1)

name_malek_mosharecat_entry=scrolledtext.ScrolledText(malek_mosharecat_frame,width=30,height=5)
name_malek_mosharecat_entry.grid(padx=5,pady=10,row=0,column=0)

number_malek_mosharecat=tk.Label(malek_mosharecat_frame,text="شماره تماس مالک/نماینده ",bg="#efefef" ,fg="black",width=18)
number_malek_mosharecat.grid(padx=5,pady=10,row=1,column=1)

number_malek_mosharecat_entry=tk.Entry(malek_mosharecat_frame,bg="#e5e5e5",fg="black")
number_malek_mosharecat_entry.grid(padx=5,pady=10,row=1,column=0)

tedad_malek_mosharecat=tk.Label(malek_mosharecat_frame,text="تعداد مالک",bg="#efefef" ,fg="black",width=13)
tedad_malek_mosharecat.grid(padx=5,pady=10,row=2,column=1)

tedad_malek_mosharecat_entry=tk.Entry(malek_mosharecat_frame,bg="#e5e5e5",fg="black")
tedad_malek_mosharecat_entry.grid(padx=5,pady=10,row=2,column=0)

type_malekiyat_mosharecat=tk.Label(malek_mosharecat_frame,text="نوع مالکیت",bg="#efefef" ,fg="black",width=13)
type_malekiyat_mosharecat.grid(padx=5,pady=10,row=3,column=1)

type_malekiyat_mosharecat_combo=ttk.Combobox(malek_mosharecat_frame)
type_malekiyat_mosharecat_combo["values"]=("شش دانگ","مشاع")
type_malekiyat_mosharecat_combo.set( "شش دانگ")
type_malekiyat_mosharecat_combo.grid(padx=5,pady=10,row=3,column=0)

#بعد میتوان درصد مشارکت هم اضافه کرد ولی باید به تایید جمع برسه
#-------------قسمت مشخصات سازنده-----------------------
#این فیلدها اجباری نیست چراکه ممکنه هن.ز سازنده تعیین نشده باشه
name_sazandeh_moshrecat=tk.Label(malek_mosharecat_frame,text="نام سازنده/شرکت",bg="#efefef" ,fg="black",width=13)
name_sazandeh_moshrecat.grid(padx=5,pady=10,row=4,column=1)

name_sazandeh_moshrecat_entry=tk.Entry(malek_mosharecat_frame,bg="#e5e5e5",fg="black")
name_sazandeh_moshrecat_entry.grid(padx=5,pady=10,row=4,column=0)

number_sazandeh_moshrecat=tk.Label(malek_mosharecat_frame,text="شماره تماس",bg="#efefef" ,fg="black",width=13)
number_sazandeh_moshrecat.grid(padx=5,pady=10,row=5,column=1)

number_sazandeh_moshrecat_entry=tk.Entry(malek_mosharecat_frame,bg="#e5e5e5",fg="black")
number_sazandeh_moshrecat_entry.grid(padx=5,pady=10,row=5,column=0)

sazandeh_info_moshrecat=tk.Label(malek_mosharecat_frame,text="سابقه کوتاه سازنده",bg="#efefef" ,fg="black",width=15)
sazandeh_info_moshrecat.grid(padx=5,pady=10,row=6,column=1)

sazandeh_info_mosharecat_entry=scrolledtext.ScrolledText(malek_mosharecat_frame,width=30,height=8)
sazandeh_info_mosharecat_entry.grid(padx=5,pady=10,row=6,column=0)

edame_moshrecat_malek=tk.Button(malek_mosharecat_frame,text="ادامه",background="#079BDB",fg="#ffffff",width=8,command=None)
edame_moshrecat_malek.place(x=200,y=500)

back_to_melk_mosharecat=tk.Button(malek_mosharecat_frame,text="برگشت ",command=None,background="#079BDB",fg="#ffffff",width=17)
back_to_melk_mosharecat.place(x=50,y=500)







#endregion

#############################################################################
# ----------------------اجرای برنامه-------------------
#region
root.protocol("WM_DELETE_WINDOW",close_window)
root.mainloop()
#endregion