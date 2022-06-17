from tkinter import*
import sqlite3
from tkinter import messagebox

root=Tk()
root.title("FACEBOOK")

conn=sqlite3.connect("Facebook.db")
c=conn.cursor()

def delete():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    c.execute("DELETE from addresses WHERE oid ="+ delete_box.get())
    print("Delete Successfully")

    delete_box.get(0,END)
    conn.commit()
    conn.close()


# c.execute("""CREATE TABLE address (
#     first_name text,
#     last_name text,
#     address text,
#     age text,
#     password text,
#     fathername text,
#     city text,
#     zipcode integer
#     )""")
# print("Table created successfully")

def submit():
    conn=sqlite3.connect("Facebook.db")
    c=conn.cursor()
    
    c.execute("INSERT INTO USER VALUES (:f_name,:l_name,:address,:age,:password,:fathername,:city,:zipcode)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'age':age.get(),
        'password':password.get(),
        'fathername':fathername.get(),
        'city':city.get(),
        'zipcode':zipcode.get()
        })
    messagebox.showinfo("Addresses","Inserted Successfully")
    conn.commit()
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    age.delete(0,END)
    password.delete(0,END)
    fathername.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

address=Entry(root,width=30)
address.grid(row=2,column=1)

age=Entry(root,width=30)
age.grid(row=3,column=1)

password=Entry(root,width=30)
password.grid(row=4,column=1)

fathername=Entry(root,width=30)
fathername.grid(row=5,column=1)

city=Entry(root,width=30)
city.grid(row=6,column=1)

zipcode=Entry(root,width=30)
zipcode.grid(row=7,column=1)

delete_box=Entry(root,width=30)
delete_box.grid(row=14,column=1)

f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0)

l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text="Address")
address_label.grid(row=2,column=0) 

age_label=Label(root,text="Age")
age_label.grid(row=3,column=0) 

password_label=Label(root,text="Password")
password_label.grid(row=4,column=0) 

fathername_label=Label(root,text="Fathername")
fathername_label.grid(row=5,column=0) 

city_label=Label(root,text="City")
city_label.grid(row=6,column=0)

zipcode_label=Label(root,text="Zipcode")
zipcode_label.grid(row=7,column=0)

submit_btn=Button(root,text="Add Records",command=submit) 
submit_btn.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

delete_btn=Button(root,text="Delete",command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=120)

conn.commit()
conn.close()
root.mainloop()
