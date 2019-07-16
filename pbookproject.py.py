import tkinter
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
from tkinter.filedialog import askopenfilename


def quitt():
    p.destroy()


def sign():    # yaha se hum signup start karte h or jo bhi user apni details enter karte h use file me store karate h
    def quit2():
        win.destroy()
    
    def signup():#from here we take the input from user
        u=e3.get()
        p=e4.get()
        rp=e5.get()
        e=e6.get()
        ep=e7.get()
        if p==rp:
            password=p
            file=open("int.txt",'a')
            file.write(u)
            file.write(',')
            file.write(p)
            file.write(',')
            file.write(e)
            file.write(',')
            file.write(ep)
            file.write("\n")
            file.close()
            signupwin=Tk()
            signupwin.title('signupwin')
            l10=Label(signupwin,text='thankyou {} for register \nsignup complete'.format(e3.get()))
            l10.place(x=5,y=10)

        else:
            signupwin=Tk()
            signupwin.title('signupwin')
            l11=Label(signupwin,text='Retype password do not match')
            l11.place(x=5,y=10)
    



    #create a gui window to ask a user to enter the details 
    win=Toplevel()
    win.geometry('500x500')
    photo1 = PhotoImage(file=pt)
    w1 = Label(win, image=photo1)
    w1.pack()
    l4=Label(win,text='New User signup ',bg='yellow',fg='blue',font=('Edwardian Script ITC',25,'underline'))
    l4.place(x=80,y=10)
    l5=Label(win,text='Username : ',font=('Lucida Calligraphy',8,'bold'))
    l5.place(x=2,y=80)
    e3=Entry(win)
    e3.place(x=110,y=80)
    l6=Label(win,text='password : ',font=('Lucida Calligraphy',8,'bold'))
    l6.place(x=2,y=120)
    e4=Entry(win,show='•')  
    e4.place(x=110,y=120)
    l7=Label(win,text='Re-password : ',font=('Lucida Calligraphy',8,'bold'))
    l7.place(x=2,y=160) 
    e5=Entry(win,show='•')
    e5.place(x=110,y=160)
    l8=Label(win,text='E-mail : ',font=('Lucida Calligraphy',8,'bold'))
    l8.place(x=2,y=200)
    e6=Entry(win)
    e6.place(x=110,y=200)
    l9=Label(win,text='E-mailpss: ',font=('Lucida Calligraphy',8,'bold'))
    l9.place(x=2,y=240)
    e7=Entry(win)
    e7.place(x=110,y=240)
    b2=Button(win,text='signup',font=('Lucida Calligraphy',10,'bold'),fg='White',bg='Blue',command=signup)
    b2.place(x=95,y=280)
    b3=Button(win,text='Back',font=('Lucida Calligraphy',10,'bold'),fg='White',bg='Red',command=win.destroy)
    b3.place(x=170,y=280)
    win.mainloop()




def login():
    def attachm():
        global fname
        fname=askopenfilename()
        line=fname
        value=line.split('/')
        global filename
        filename=value[-1]
        lnm6=Label(nmsg,text=filename,font=('Lucida Calligraphy',8,'bold'))
        lnm6.place(x=60,y=350)
    
    def nmssg():
        global lnme3
        mssg=MIMEMultipart()
        to=lnme3.get()
        mssg['From']=e
        mssg['To']=lnme3.get()
        mssg['Subject']=lnme4.get()
        body=lnmt5.get('1.0',END)
        mssg.attach(MIMEText(body,'plain'))
        attachment=open(fname,"rb")
        p=MIMEBase('application','octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition',"attachment; filename= %s" % filename)
        mssg.attach(p)
        text = mssg.as_string()
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com',587)
        # start TLS for security : it encrypt all the smtp  command so that it will not save our details
        s.starttls()
        # Authentication
        sub=lnme4.get()
        mssg=lnmt5.get('1.0',END)
        message = 'Subject:{}\n\n{}'.format(sub,mssg)
        to=lnme3.get()
        s.login(e,ep1)
        # sending the mail
        s.sendmail(e,to,text)
        #terminating the session
        s.quit()
        print('message send')
    

  

        
    def newmssg():
        global to
        global lnme3
        global sub
        global mssg
        global message
        global lnme4
        global lnmt5
        global nmsg
        nmsg=Toplevel()
        nmsg.geometry('500x500')
        photo1 = PhotoImage(file=pt)
        w1 = Label(nmsg, image=photo1)
        w1.pack()
        lnm1=Label(nmsg,text='New message',bg='yellow',fg='blue',font=('Edwardian Script ITC',25,'underline'))
        lnm1.place(x=120,y=5)
        lnm3=Label(nmsg,text='From : ',font=('Lucida Calligraphy',8,'bold'))
        lnm3.place(x=2,y=70)
        lnme1=Entry(nmsg,width=40)
        lnme1.place(x=80,y=70)
        lnme1.insert('1',e)
        lnm3=Label(nmsg,text='To : ',font=('Lucida Calligraphy',8,'bold'))
        lnm3.place(x=2,y=110)
        lnme3=Entry(nmsg,width=40)
        lnme3.place(x=80,y=110)
        lnm4=Label(nmsg,text='Sub : ',font=('Lucida Calligraphy',8,'bold'))
        lnm4.place(x=2,y=140)
        lnme4=Entry(nmsg,width=40)
        lnme4.place(x=80,y=140)
        lnm5=Label(nmsg,text='message : ',font=('Lucida Calligraphy',8,'bold'))
        lnm5.place(x=2,y=170)
        lnmt5=Text(nmsg,width=40,height=10)
        lnmt5.place(x=80,y=170)
        blnm1=Button(nmsg,text='Attach',font=('Lucida Calligraphy',10,'bold'),fg='White',bg='Blue',command=attachm)
        blnm1.place(x=60,y=390)
        blnm2=Button(nmsg,text='Send',font=('Lucida Calligraphy',10,'bold'),fg='White',bg='Blue',command=nmssg)
        blnm2.place(x=150,y=390)
        blnm3=Button(nmsg,text='Back',font=('Lucida Calligraphy',10,'bold'),fg='White',bg='Red',command=nmsg.destroy)
        blnm3.place(x=230,y=390)
        nmsg.mainloop()


    
    def read():
        u=e1.get()
        p=e2.get()
        file=open('int.txt','r')
        for line in file:
            val=line.split(',')
            un=val[0]
            ps=val[1]
            global e
            e=val[2]
            ep=val[3]
            lc=len(ep)-1
            global ep1
            ep1=ep[0:lc]
            
            if u==un and p==ps:
                loginwin=Toplevel()
                loginwin.geometry('500x500')
                photo1 = PhotoImage(file=pt)
                w1 = Label(loginwin, image=photo1)
                w1.pack()
                loginwin.title('loginwindow')
                llogin=Label(loginwin,text='•••')
                llogin.place(x=2,y=5)
                l8=Label(loginwin,text='{}'.format(u),font=('Lucida Calligraphy',14,'bold','underline'),fg='green')
                l8.place(x=21,y=5)
                butlogin1=Button(loginwin,text='New message',font=('Lucida Calligraphy',10,'bold'),fg='White',bg='Blue',command=newmssg)
                butlogin1.place(x=2,y=65)
                butlogin2=Button(loginwin,text='Inbox',font=('Lucida Calligraphy',10,'bold'),fg='White',bg='Blue')
                butlogin2.place(x=2,y=95)
                butlogin3=Button(loginwin,text='Logout',font=('Lucida Calligraphy',10,'bold'),fg='White',bg='Red',command=loginwin.destroy)
                butlogin3.place(x=2,y=125)
                loginwin.mainloop()
                break
        else:
            loginwin=Toplevel()
            photo1 = PhotoImage(file=pt)
            w1 = Label(loginwin, image=photo1)
            w1.pack()
            loginwin.title('loginwindow')
            l9=Label(loginwin,text=('login failed'))
            l9.place(x=5,y=10)
            loginwin.mainloop()


    readdata=Toplevel()
    readdata.geometry('500x500')
    photo1 = PhotoImage(file=pt)
    w1 = Label(readdata, image=photo1)
    w1.pack()
    ll=Label(readdata,text='Login',bg='yellow',fg='blue',font=('Edwardian Script ITC',25,'underline'))
    ll.place(x=120,y=5)
    l2=Label(readdata,text='Username',font=('Lucida Calligraphy',8,'bold'))
    l2.place(x=2,y=80)
    l3=Label(readdata,text='password',font=('Lucida Calligraphy',10,'bold'))
    l3.place(x=2,y=120)
    e1=Entry(readdata)
    e1.place(x=90,y=80)
    e2=Entry(readdata,show='•')
    e2.place(x=90,y=120)
    b1=Button(readdata,text='login',font=('Lucida Calligraphy',10,'bold'),fg='White',bg='Blue',command=read)
    b1.place(x=90,y=160)
    b2=Button(readdata,text='Back',font=('Lucida Calligraphy',10,'bold'),fg='White',bg='Red',command=readdata.destroy)
    b2.place(x=160,y=160)
    readdata.mainloop()

from tkinter import *
p=Tk()
p.geometry('500x500')
global pt
pt='C:\desktop\IMG-20190715-WA0021 (1).png'
photo = PhotoImage(file=pt)
imagee = Label(p, image=photo)
imagee.pack()
l1=Label(p,text='welcome to python book',bg='yellow',fg='blue',font=('Edwardian Script ITC',25,'underline'))
l1.place(x=5,y=10)
but1=Button(p,text='Already user ',font=('Lucida Calligraphy',10,'bold'),fg='White',bg='Blue',command=login)
but1.place(x=4,y=80)
but2=Button(p,text='sign up',font=('Lucida Calligraphy',10,'bold'),fg='White',bg='Blue',command=sign)
but2.place(x=4,y=110)
but3=Button(p,text='quit',bg='Red',fg='White',font=('Lucida Calligraphy',10,'bold'),command=quitt)
but3.place(x=4,y=140)
p.mainloop()

