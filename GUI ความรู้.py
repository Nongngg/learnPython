from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()   #นี้คือจอหลัก
GUI.title('โปรเเกรมบันทึกข้อมูล')#ชื้อ
GUI.geometry('500x400')#ขนาด

B1 = ttk.Button(GUI,text='จงเเสดงเงิน')#ปุ่ม
B1.pack(ipadx=20,ipady=20)

def Button2():
    text ='ตอนนี้มีเงินอยู่ 300 บาท'
    messagebox.showerror('เงินในบัญชี',text)
    
FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text='จงเเสดงเงิน',command=Button2)
B2.pack(ipadx=20,ipady=20)




GUI.mainloop()
