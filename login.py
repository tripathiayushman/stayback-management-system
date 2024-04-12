from tkinter import *
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="stayback")
cur=conn.cursor()
user=""
pswd=""
Type=""
a=""
f3=""
adm=""
stu=""
par=""
con=""
rou=""
cla=""
tid=""
date=""
dura=""

reas=""
def asearch(f):
    global Type,a,data
    global user,pswd
    username=user.get()
    password=pswd.get()
    q="select password from login where username='{}' and type='{}'".format(username,Type)
    cur.execute(q)
    w=cur.fetchone()
    x="('"+password+"',)"
    if str(w)==str(x):
        L5=Label(f,text="Login Successful")
        L5.place(x=100,y=200)
        f1=Frame(a,height=700,width=700)
        f1.place(x=0,y=0)
        f2=Frame(a,height=700,width=200,bg="sky blue")
        f2.place(x=550,y=0)
        header=Label(f1,text=("Welcome Admin"+username),font=("Arial",15,"bold"))
        header.place(x=150,y=30)
        btn=Button(f1,text="Insert Records",height=2,width=20,command=ins)
        btn.place(x=200,y=150)
        btn1=Button(f1,text="Delete Records",height=2,width=20,command=Del)
        btn1.place(x=200,y=250)
    else:
        L5=Label(f,text="Login Failed")
        L5.place(x=100,y=200)
def tsearch(f):
    global Type,a,data
    global user,pswd
    import mysql.connector
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="ayushman#18082004",
        database="stayback")
    cur=conn.cursor()
    username=user.get()
    password=pswd.get()
    q="select password from login where username='{}' and type='{}'".format(username,Type)
    cur.execute(q)
    w=cur.fetchone()
    x="('"+password+"',)"
    if str(w)==str(x):
        L5=Label(f,text="Login Successful")
        L5.place(x=100,y=200)
        f2=Frame(a,height=600,width=700)
        f2.place(x=0,y=0)
        f3=Frame(f2,height=700,width=100,bg="sky blue")
        f3.place(x=0,y=0)
        header=Label(f2,text=("Welcome Teacher "+username),
        font=("Arial",15,"bold"))
        header.place(x=200,y=40)
        ttinsert=Button(f2,text='Add Student',
        width=20,font=('Helvetica',10,'bold'),height=4,command=tins)
        ttinsert.place(x=250,y=200)
        ttdelete=Button(f2,text='Delete Student',
        width=20,font=('Helvetica',10,'bold'),height=4,command=tDel)
        ttdelete.place(x=250,y=300)
    else:
        L5=Label(f,text="Login Failed")
        L5.place(x=100,y=200)
def alogin():
    global Type,a
    Type="Admin"

    global user,pswd
    a=Tk()
    a.geometry("680x500")
    a.title("Admin")
    f=Frame(a,bg="sky blue",height=400,width=600)
    f.place(x=40,y=70)
    L1=Label(a,text="LOGIN",font=("Cambria",20,"bold"))
    L1.place(x=300,y=30)
    L2=Label(f,text="Enter your username:")
    L2.place(x=100,y=100)
    user=Entry(f,width=20)
    user.place(x=250,y=100)
    L3=Label(f,text="Enter your password:")
    L3.place(x=100,y=150)
    pswd=Entry(f,width=20)
    pswd.place(x=250,y=150)
    L4=Label(f,text="Enter your login credentials",font=("Arial",12,"bold"),bg="sky blue")
    L4.place(x=200,y=30)
    B=Button(f,text="Submit",command=lambda:asearch(f))
    B.place(x=300,y=200)
def tlogin():
    global Type,a
    Type="Teacher"
    global user,pswd
    a=Tk()
    a.geometry("680x500")
    a.title("Teacher")
    f=Frame(a,bg="sky blue",height=400,width=600)
    f.place(x=40,y=70)
    L1=Label(a,text="LOGIN",font=("Cambria",20,"bold"))
    L1.place(x=300,y=30)
    L2=Label(f,text="Enter your username:")
    L2.place(x=100,y=100)
    user=Entry(f,width=20)
    user.place(x=250,y=100)
    L3=Label(f,text="Enter your password:")
    L3.place(x=100,y=150)
    pswd=Entry(f,width=20)
    pswd.place(x=250,y=150)
    L4=Label(f,text="Enter your login credentials",font=("Arial",12,"bold"),bg="sky blue")
    L4.place(x=200,y=30)
    B=Button(f,text="Submit",command=lambda:tsearch(f))
    B.place(x=300,y=200)
def plogin():
    global Type,a
    Type="Parent"
    global user,pswd
    t=Tk()
    t.geometry("680x500")
    t.title("Parent")
    f=Frame(t,bg="sky blue",height=400,width=600)
    f.place(x=40,y=70)
    L1=Label(t,text="LOGIN",font=("Cambria",20,"bold"))
    L1.place(x=300,y=30)
    L2=Label(f,text="Enter your username:")
    L2.place(x=50,y=100)
    user=Entry(f,width=20)
    user.place(x=200,y=100)
    L3=Label(f,text="Enter your password:")
    L3.place(x=50,y=150)
    pswd=Entry(f,width=20)
    pswd.place(x=200,y=150)
    L4=Label(f,text="Enter your login credentials",font=("Arial",12),bg="sky blue")
    L4.place(x=200,y=30)
    B=Button(f,text="Submit",command=lambda:asearch(f))
    B.place(x=300,y=200)
def Del():
    global adm,f3
    f3=Frame(a,height=500,width=500)
    f3.place(x=40,y=70)
    adm=Entry(f3,width=20)
    adm.place(x=200,y=200)
    label=Label(f3,text="Enter the Admission No.",font=("Arial",22))
    label.place(x=100,y=100)
    btn=Button(f3,text="Submit",width=15,command=delete)
    btn.place(x=200,y=300)
def delete():
    global adm,f3
    admno=adm.get()
    query="delete from admin where admno={}".format(admno)
    cur.execute(query)
    cur.execute("commit")
    msg=Label(f3,text="Record deleted successfully",font=("Arial",10,"bold"))
    msg.place(x=180,y=350)
def ins():
    global adm,stu,par,rou,con,cla,f3
    f3=Frame(a,height=500,width=500,bg="sky blue")
    f3.place(x=40,y=70)
    adm=Entry(f3,width=20)
    adm.place(x=190,y=100)
    stu=Entry(f3,width=20)
    stu.place(x=190,y=130)
    par=Entry(f3,width=20)
    par.place(x=190,y=160)
    cla=Entry(f3,width=20)
    cla.place(x=190,y=190)
    rou=Entry(f3,width=20)
    rou.place(x=190,y=220)
    con=Entry(f3,width=20)
    con.place(x=190,y=250)
    btn=Button(f3,text="Submit",width=12,command=insert)
    btn.place(x=210,y=300)
    L1=Label(f3,text="Enter Admission No.",width=15)
    L1.place(x=70,y=100)
    L2=Label(f3,text="Enter Student Name",width=15)
    L2.place(x=70,y=130)
    L3=Label(f3,text="Enter Parent Name",width=15)
    L3.place(x=70,y=160)
    L4=Label(f3,text="Enter Class",width=15)
    L4.place(x=70,y=190)
    L5=Label(f3,text="Enter Route",width=15)
    L5.place(x=70,y=220)
    L6=Label(f3,text="Enter Contact",width=15)
    L6.place(x=70,y=250)
def insert():
    global adm,stu,par,rou,con,cla,f3
    admno=adm.get()
    sname=stu.get()
    pname=par.get()
    clas=cla.get()
    route=rou.get()
    cont=con.get()
    query="insert into admin values ({},'{}','{}','{}',{},{})".format(admno,sname,pname,clas,route,cont)
    cur.execute(query)
    cur.execute("commit")
    msg=Label(f3,text="Record added successfully",font=("Arial",10,"bold"))
    msg.place(x=100,y=400)
def tDel():
    global adm,f3
    f3=Frame(a,height=500,width=500)
    f3.place(x=100,y=70)
    adm=Entry(f3,width=20)
    adm.place(x=190,y=200)
    label=Label(f3,text="Enter the Admission No.",font=("Arial",22))
    label.place(x=100,y=100)
    btn=Button(f3,text="Submit",width=15,command=tdelete)
    btn.place(x=200,y=300)
def tdelete():
    global adm,f3
    admno=adm.get()
    query="delete from teacher where admno={}".format(admno)
    cur.execute(query)
    cur.execute("commit")
    msg=Label(f3,text="Record deleted successfully",font=("Arial",10,"bold"))
    msg.place(x=180,y=350)
def tins():
    global tid,adm,date,dura,reas,f3
    f3=Frame(a,height=500,width=500,bg="sky blue")
    f3.place(x=130,y=70)
    tid=Entry(f3,width=20)
    tid.place(x=240,y=100)
    adm=Entry(f3,width=20)
    adm.place(x=240,y=130)
    date=Entry(f3,width=20)
    date.place(x=240,y=160)
    dura=Entry(f3,width=20)
    dura.place(x=240,y=190)
    reas=Entry(f3,width=20)
    reas.place(x=240,y=220)
    btn=Button(f3,text="Submit",width=12,command=tinsert)
    btn.place(x=210,y=250)
    L1=Label(f3,text="Enter Teacher ID",width=20)
    L1.place(x=70,y=100)
    L2=Label(f3,text="Enter Admission No.",width=20)
    L2.place(x=70,y=130)
    L3=Label(f3,text="Enter Stayback Date",width=20)
    L3.place(x=70,y=160)
    L4=Label(f3,text="Enter Duration (hrs)",width=20)
    L4.place(x=70,y=190)
    L1=Label(f3,text="Enter Reason",width=20)
    L1.place(x=70,y=220)
def tinsert():
    global tid,adm,date,dura,reas,f3
    t_id=tid.get()
    admno=adm.get()
    dat=date.get()
    dur=dura.get()
    r=reas.get()
    query="insert into teacher values ('{}',{},'{}','{}','{}')".format(t_id,admno,dat,dur,r)
    cur.execute(query)
    cur.execute("commit")
    msg=Label(f3,text="Record added successfully")
    msg.place(x=150,y=400)
