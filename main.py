from tkinter import *
from tkinter import ttk
from login import *
adm=""
stu=""
par=""
cla=""
route=""
cont=""
a=""
Sdat=""
def stu_search():
    global adm,a
    data=adm.get()
    q=("select student_name, dur, reason from teacher natural join admin where admno={} and date=date(now())").format(data)
    cur.execute(q)
    d=cur.fetchone()
    if d==None:
        x=Label(a,text="There is no stayback for Admission No." +data ,
        font=("Arial",13,"bold"),height=4)
        x.place(x=120,y=250)
    else:
        for i in d:
            for i in d:
                y = Label(a, text=('''{} has stayback \n for {} hours because \nof {}''').format(d[0], d[1], d[2]), font=("Arial", 15, "bold"), width=30)
                y.place(x=120, y=250)
def astudent():
    global adm,sname,pname,cla,route,cont
    admno=adm.get()
    sname=stu.get()
    pname=par.get()
    Class=cla.get()
    data=route.get()
    contact=cont.get()
    q="insert into admin values ({},'{}','{}','{}','{}',{})".format(admno,sname,pname,Class,data,contact)
    cur.execute(q)
    cur.execute("commit")
def bus(f1):
    global route,a
    data=route.get()
    q='''select student_name, class from teacher natural join admin where route ={}'''.format(data)
    cur.execute(q)
    d=cur.fetchall()
    tv=ttk.Treeview(f1,columns=(1,2),show="headings",height=10)
    tv.place(x=100,y=200)
    tv.heading(1,text="Student Name")
    tv.heading(2,text="Class")
    for i in d:
        tv.insert("","end",values=i)


def aop():
    a=Tk()
    a.title("Log-in to Admin")
    a.geometry("500x500")
    ainsert=Button(a,text='Insert Records',width=20,font=('Helvetica',10,'bold'))
    ainsert.place(x=150,y=170)
    adelete=Button(a,text='Delete Records'
    ,width=20,font=('Helvetica',10,'bold'))
    adelete.place(x=150,y=300)
def top():
    tinsert=Button(m,text='Add Student',width=20,font=('Helvetica',10,'bold'))
    tinsert.place(x=350,y=270)
    tdelete=Button(m,text='Delete Student',width=20,font=('Helvetica',10,'bold'))
    tdelete.place(x=350,y=400)
    tdisp=Button(m,text='Display Names of students',
    width=20,bg='#268010',font=('Helvetica',10,'bold'))
    tdisp.place(x=350,y=530)
def pop():
    global adm,a
    a=Tk()
    a.geometry("500x500")
    a.title("Parent")
    f=Frame(a,height=500,width=100,bg="sky blue")
    f.place(x=0,y=0)
    w7=Label(a,text='Enter the Admission No.',
    width=25,height=3,font=('Helvetica',14,'bold'))

    w7.place(x=150,y=10)
    adm=Entry(a,width=25,bg='white',font=( 'Helvetica',15,'bold'))
    adm.place(x=150,y=100)
    pdisp=Button(a,text='SEARCH',width=15,
    font=('Helvetica',13,'bold'),command=stu_search)
    pdisp.place(x=200,y=150)
def dop():
    a=Tk()
    a.title("Driver")
    a.geometry("500x500")
    f1=Frame(a,height=500,width=500)
    f1.place(x=0,y=0)
    f2=Frame(a,height=500,width=100,bg="sky blue")
    f2.place(x=0,y=0)
    rou=Label(f1,text='Enter your Route Number',width=25,
    font=( 'Helvetica',15,'bold'))
    rou.place(x=120,y=10)
    global route
    route=Entry(f1,width=20,font=( 'Helvetica',10,'bold'))
    route.place(x=200,y=100)
    data = route.get()
    bdisp=Button(f1,text='SEARCH',
    width=15,font=('Helvetica',10,'bold'),command=lambda:bus(f1))
    bdisp.place(x=200,y=150)

import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="stayback")
cur=conn.cursor()
m=Tk()
m.geometry("1080x720")
m.title("Stay-Back Management")
f=Frame(m,height=1000,width=250,bg="sky blue")
f.place(x=0,y=0)
header=Label(m,text="DELHI PUBLIC SCHOOL",font=('arial',20,'bold'))
header.place(x=450,y=15)
h2=Label(m,text="Stay-Back Management",font=('arial',15,'bold'))
h2.place(x=530,y=50)
w1=Button(f,text='Login as Admin',width=15,font=('Cambria',15,'bold'),command=alogin)
w1.place(x=30,y=170)
w2=Button(f,text='Login as Teacher',width=15,font=('Cambria',15,'bold'),command=tlogin)
w2.place(x=30,y=300)
w3=Button(f,text='Parent Login',width=15,font=('Cambria',15,'bold'),command=pop)
w3.place(x=30,y=430)
w4=Button(f,text='Driver Login',width=15,font=('Cambria',15,'bold'),command=dop)
w4.place(x=30,y=560)
i=PhotoImage(file="school logo.png")
img=Label(f,image=i)
img.place(x=60,y=1)
sch=PhotoImage(file="scho.png")

bvm=Label(m,image=sch)
bvm.place(x=300,y=140)
sch2=PhotoImage(file="scho2.png")
cov=Label(m,image=sch2)
cov.place(x=500,y=400)
sch3=PhotoImage(file="scho3.png")
cov1=Label(m,image=sch3)
cov1.place(x=700,y=140)
m.mainloop()

