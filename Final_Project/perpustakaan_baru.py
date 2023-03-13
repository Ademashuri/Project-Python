import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['idbuku'])
    e2.insert(0,select['judul'])
    e3.insert(0,select['pengarang'])
    e4.insert(0,select['penerbit'])
    e5.insert(0,select['tahun_terbit'])
    e6.insert(0,select['jumlah_halaman'])
    
def Add():
    bookid = e1.get()
    bookname = e2.get()
    publishname = e3.get()
    authorname = e4.get()
    year = e5.get()
    hal = e6.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="latihan")
    mycursor=mysqldb.cursor()

    try:
       sql = "INSERT INTO  perpustakaan (idbuku,judul,pengarang,penerbit,tahun_terbit,jumlah_halaman) VALUES (%s, %s, %s, %s, %s, %s)"
       val = (bookid,bookname,publishname,authorname,year,hal)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Book inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e1.focus_set()
       show()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()

def update():
    bookid = e1.get()
    bookname = e2.get()
    publishname = e3.get()
    authorname = e4.get()
    year = e5.get()
    hal = e6.get()
    
    
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="latihan")
    mycursor=mysqldb.cursor()

    try:
       sql = "Update  perpustakaan set judul= %s,pengarang= %s,penerbit=%s,tahun_terbit=%s,jumlah_halaman= %s where idbuku= %s"
       val = (bookname,authorname,publishname,year,hal,bookid)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updateddddd successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e1.focus_set()
       show()
    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def delete():
    bookid = e1.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="latihan")
    mycursor=mysqldb.cursor()

    try:
       sql = "delete from perpustakaan where idbuku = %s"
       val = (bookid,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleteeeee successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e1.focus_set()
       show()
    except mysql.connector.Error as error:
        print("Failed to delete record from database: {}".format(error))
        mysqldb.rollback()
        mysqldb.close()


        
def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="latihan")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT idbuku,judul,pengarang,penerbit,tahun_terbit,jumlah_halaman FROM perpustakaan")
    records = mycursor.fetchall()
    listBox.delete(*listBox.get_children()) 
    for i, (bookid,bookname,publishname,authorname,year,hal) in enumerate(records, start=1):
        listBox.insert("", "end", values=(bookid,bookname,publishname,authorname,year,hal))

    mysqldb.close()  
        
            
root = Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4
global e5
global e6

tk.Label(root, text="Contoh Database", fg="black", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="idbuku").place(x=10, y=10)
Label(root, text="judul").place(x=10, y=40)
Label(root, text="pengarang").place(x=10, y=70)
Label(root, text="penerbit").place(x=10, y=95)     
Label(root, text="tahun_terbit").place(x=10, y=120) 
Label(root, text="jumlah_halaman").place(x=10, y=145) 

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=35)

e3 = Entry(root)
e3.place(x=140, y=60)

e4 = Entry(root)
e4.place(x=140, y=90)

e5 = Entry(root)
e5.place(x=140, y=120)

e6 = Entry(root)
e6.place(x=140, y=150)

Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=180)
Button(root, text="update",command = update,height=3, width= 13).place(x=140, y=180)
Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=180)

#Button(root, text="Show",command = show,height=3, width= 13).place(x=380, y=160)

cols = ('idbuku', 'judul', 'pengarang','penerbit','tahun_terbit','jumlah_halaman')
listBox = ttk.Treeview(root, columns=cols, show='headings' )
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=5, y=250)

show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()

