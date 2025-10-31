import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="vr1#%!)%(!!!!$",database="job")
mycursor = mydb.cursor()

from tkinter import*
from tkinter import messagebox as MessageBox
from tkinter import ttk
import webbrowser

top=Tk()
top.title("ONLINE JOB PORTAL")
top.geometry("1250x600")
top.configure(bg="white")
ent=Entry(top)


#signup
def signup_display():
    addun_screen=Toplevel(top)
    addun_screen.title("Signup")
    addun_screen.geometry("450x375")
    addun_screen.configure(bg="white")

    global first_name
    global last_name
    global user_id
    global pswd
    Label(addun_screen,text='Please Enter your Account Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",bg="blue",width=300).pack()
    first_name=StringVar()
    last_name=StringVar()
    user_id=StringVar()
    pswd=StringVar()
    Label(addun_screen, text="",bg="white").pack()
    Label(addun_screen, text="First Name:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(addun_screen, textvariable=first_name).pack()
    Label(addun_screen, text="",bg="white").pack()
    Label(addun_screen, text="Last Name:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(addun_screen, textvariable=last_name).pack()
    Label(addun_screen, text="",bg="white").pack()
    Label(addun_screen, text="User-ID:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(addun_screen, textvariable=user_id).pack()
    Label(addun_screen, text="",bg="white").pack()
    Label(addun_screen, text="Password:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(addun_screen, textvariable=pswd,show="*").pack()
    Label(addun_screen, text="",bg="white").pack()
    Button(addun_screen, text="Signup", bg="blue", fg='white', relief="groove", font=('calibri', 14, 'bold'),command=usinfo).pack()
    Label(addun_screen, text="",bg="white")
    
def usinfo():
    fname=first_name.get()
    lname=last_name.get()
    ui=user_id.get()
    pw=pswd.get()
    if(fname=="" or lname=="" or ui=="" or pw==""):
        MessageBox.showerror("Profile","All fields are required")
    else:
        try:
            sql="insert into signup(firstname,lastname,userid,passwd) values('{}','{}','{}','{}')".format(fname,lname,ui,pw)
            mycursor.execute(sql)
            mydb.commit()        
            
        
            MessageBox.showinfo("Showinfo","Successfully signed up")
            per_info()
      
            
        except mysql.connector.errors.IntegrityError:
            MessageBox.showinfo("Showinfo","Userid or Password already in use!")

def Exit():
    wayOut = MessageBox.askyesno("Signup System", "Do you want to exit the system?")
    if wayOut > 0:
        root.destroy()
        return

#login
def login_screen():
    login_screen=Toplevel(top)
    login_screen.title("Login")
    login_screen.geometry("450x375")
    login_screen.configure(bg="white")

    global userid
    global ps_wd
    Label(login_screen,text='Please Enter your Account Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",bg="blue",width=300).pack()
    userid=StringVar()
    ps_wd=StringVar()
    Label(login_screen, text="",bg="white").pack()
    Label(login_screen, text="User-ID:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(login_screen, textvariable=userid).pack()
    Label(login_screen, text="",bg="white").pack()
    Label(login_screen, text="Password:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(login_screen, textvariable=ps_wd,show="*").pack()
    Button(login_screen, text="Submit", bg="blue", fg='white', relief="groove", font=('calibri', 14, 'bold'),command=log).pack()
    Label(login_screen, text="",bg="white")

def log():
    usi=userid.get()
    pd=ps_wd.get()
    if(usi=="" or pd==""):
        MessageBox.showerror("Profile","All fields are required")
    else:
        sql3="insert into login(userid,passwd) values('{}','{}')".format(usi,pd)  
        mycursor.execute(sql3)
        mydb.commit()
        login()
        
               
def login():
    usi=userid.get()
    pd=ps_wd.get()
    sql4='select userid,passwd from signup'
    mycursor.execute(sql4)
    data=mycursor.fetchall()
    mydb.commit()
    for row in data:
        if(row[0]==usi) and (row[1]==pd):
            MessageBox.showinfo("showinfo","Successfully Logged In")
            fields2()
            break
        
    else:
         MessageBox.showinfo("showinfo","Profile Not Found")
              
            
def Exit2():
    wayOut = MessageBox.askyesno("Login System", "Do you want to exit the system?")
    if wayOut > 0:
        root.destroy()
        return 

#personal info
def per_info():
    per_screen=Toplevel(top)
    per_screen.title("Info")
    per_screen.geometry("450x375")
    per_screen.configure(bg="white")

    
    global degree
    global email
    global mobile_no
    Label(per_screen,text='Please Enter your Account Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",bg="blue",width=300).pack()
    degree=StringVar()
    email=StringVar()
    mobile_no=StringVar()
    Label(per_screen, text="",bg="white").pack()
    Label(per_screen, text="Field of Choice:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(per_screen, textvariable=degree).pack()
    Label(per_screen, text="",bg="white").pack()
    Label(per_screen, text="Email:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(per_screen, textvariable=email).pack()
    Label(per_screen, text="",bg="white").pack()
    Label(per_screen, text="Contact No:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(per_screen, textvariable=mobile_no,show="*").pack()
    Label(per_screen, text="",bg="white").pack()
    Button(per_screen, text="Submit", bg="blue", fg='white', relief="groove", font=('calibri', 14, 'bold'),command=personal).pack()
    Label(per_screen, text="",bg="white")

def personal():
    deg=degree.get()
    e=email.get()
    no=mobile_no.get()
    if(deg=="" or e=="" or no==""):
        MessageBox.showerror("Profile","All fields are required")
    else:
        sql2="insert into personal(degree,email,contact_no) values('{}','{}','{}')".format(deg,e,no)
        mycursor.execute(sql2)
        mydb.commit()        
        
    
        MessageBox.showinfo("showinfo","Updated Profile")
        fields()

def Exit3():
    wayOut = MessageBox.askyesno("Personal Info", "Do you want to exit the system?")
    if wayOut > 0:
        root.destroy()
        return 

#delete profile        
def rem_pro():
    global temp_userid
    global temp_pswd
    rempro_screen=Toplevel(top)
    rempro_screen.title("Remove Profile")
    rempro_screen.config(bg="white")
    rempro_screen.geometry("500x500")

    
    Label(rempro_screen,text="User-ID:",font=('calibri',14,"bold"),width=20,fg="black").grid(row=2,sticky=W,pady=10)
    Label(rempro_screen,text="Password:",font=('calibri',14,"bold"),width=20,fg="black").grid(row=3,sticky=W,pady=10)

    
    Button(rempro_screen,text="SUBMIT",font=("calibri",14,"bold"),fg="white",bg="blue",width=10,command=rempro).grid(row=5,sticky=E,pady=10)

    
    temp_userid=Entry(rempro_screen)
    temp_userid.grid(row=2,column=10,sticky=E,pady=10)
    temp_pswd=Entry(rempro_screen,show='*')
    temp_pswd.grid(row=3,column=10,sticky=E,pady=10)

def rempro():
    c=temp_userid.get()
    r=temp_pswd.get()
    if(c=="" or r==""):
        MessageBox.showerror("Removing profile","All fields are required")
    else:
        data=(c,r)
        sql='delete from signup where userid=%s and passwd=%s'
        mycursor.execute(sql,data)
        mydb.commit()
        

        MessageBox.showinfo("Showinfo","Profile deleted")

def Exit4():
    wayOut = MessageBox.askyesno("Remove Profile", "Do you want to exit the system?")
    if wayOut > 0:
        root.destroy()
        return 

frame= Frame(top)
def fields():
    field_screen=Toplevel(top)
    field_screen.title("Employee fields")
    field_screen.config(bg="white")
    field_screen.geometry("700x200")
    
    
    d=degree.get()
    em=email.get()
    ph=mobile_no.get()
    if (d=='BCOM') or (d=='bcom') or (d=='Bcom') or (d=='accountant') or (d=='Accountant') or (d=='banking') or (d=='Banking') or (d=='finance') or (d=='Finance') or (d=='accounts') or (d=='Accounts'):
        Button(field_screen,text="Accountancy,Banking and Finance",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=finance).grid(row=0,column=1,sticky=W,pady=10)
    elif (d=='business') or (d=='Business') or (d=='MBA') or (d=='mba') or  (d=='Management') or (d=='management'):
        Button(field_screen,text="Business,Consulting and Management",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=business).grid(row=1,column=1,sticky=W,pady=10)
    elif (d=='arts') or (d=='Arts'):
        Button(field_screen,text="Creative Artist",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=arts).grid(row=2,column=1,sticky=W,pady=10)
    elif (d=='Engineering') or (d=='engineering') or (d=='software engineering') or (d=='Software engineering') or (d=='civil engineering') or (d=='Civil engineering'):
        Button(field_screen,text="Engineering and Manufacturing",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=engineering).grid(row=3,column=1,sticky=W,pady=10)
    elif (d=='agriculture') or (d=='Agriculture') or (d=='Environment') or (d=='environment'):
        Button(field_screen,text="Environment and Agriculture",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=agri).grid(row=4,column=1,sticky=W,pady=10)
    elif (d=='MBBS') or (d=='mbbs') or (d=='medicine') or (d=='Medicine') or (d=='Doctor') or (d=='doctor'):
        Button(field_screen,text="Medicine",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=med).grid(row=5,column=1,sticky=W,pady=10)
    elif (d=='IT') or (d=='BCA') or (d=='bca') or (d=='Btech') or (d=='btech') or (d=='mtech') or (d=='Mtech'):
        Button(field_screen,text="Information Technology",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=IT).grid(row=6,column=1,sticky=W,pady=10)
    elif (d=='Law') or (d=='law') or (d=='LLM'):
        Button(field_screen,text="Law",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=law).grid(row=0,column=3,sticky=W,pady=10)
    elif (d=='civil service') or (d=='Civil service'):
        Button(field_screen,text="Public services and Administration",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=admin).grid(row=1,column=3,sticky=W,pady=10)
    elif (d=='marketing') or (d=='Marketing') or (d=='sales') or (d=='Sales'):
        Button(field_screen,text="Marketing,Advertising and PR",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=mark).grid(row=2,column=3,sticky=W,pady=10)
    elif (d=='Media') or (d=='media'):
        Button(field_screen,text="Media",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=media).grid(row=3,column=3,sticky=W,pady=10)
    elif (d=='pharmacy') or (d=='Pharmacy'):
        Button(field_screen,text="Science and Pharmaceuticals",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=pharm).grid(row=4,column=3,sticky=W,pady=10)
    elif (d=='Teacher') or (d=='teacher') or (d=='education') or (d=='Education') or (d=='BEd') or (d=='bed'):
        Button(field_screen,text="Teacher training and Education",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=educ).grid(row=5,column=3,sticky=W,pady=10)
    elif (d=='transport') or (d=='Transport') or (d=='logistics') or (d=='Logistics'):
        Button(field_screen,text="Transport and Logistics",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=trans).grid(row=6,column=3,sticky=W,pady=10)
    else:
        MessageBox.showerror("Fields","Field not found")

def finance():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+accounting+and+finance&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htiq=job+for+accounting+and+finance&htidocid=GBVOoNF1EW0AAAAAAAAAAA%3D%3D")

def business():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+business+and+management&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=tcayou3zUocAAAAAAAAAAA%3D%3D")

def arts():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+arts+and+design&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=sW2isdalxLMAAAAAAAAAAA%3D%3D")

def engineering():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+engineering+and+manufacturing&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=cdf3lnGpvsYAAAAAAAAAAA%3D%3D")

def agri():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+environment+and+agriculture&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=bHcWHa3UQ2YAAAAAAAAAAA%3D%3D")

def med():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+healthcare+and+medicine&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=H-Ov90aEs3sAAAAAAAAAAA%3D%3D")

def IT():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+information+technology+&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=_OktzZqAe5cAAAAAAAAAAA%3D%3D")

def law():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+law&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=5QKhw4ps93EAAAAAAAAAAA%3D%3D")

def admin():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+administration&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=p-ect1FzTHYAAAAAAAAAAA%3D%3D")

def mark():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+Marketing,Advertising+and+PR&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=bpbf5hvReVoAAAAAAAAAAA%3D%3D")

def media():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+media&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=gnguNdPDKxkAAAAAAAAAAA%3D%3D")

def pharm():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+Science+and+Pharmaceuticals&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=3wiGs7l62fIAAAAAAAAAAA%3D%3D")

def educ():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+Teacher+training+and+Education&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=llA9tfLenB8AAAAAAAAAAA%3D%3D")

def trans():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+Transport+and+Logistics&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=hipojKRtM0QAAAAAAAAAAA%3D%3D")
    

frame=Frame(top)
def fields2():
    field2_screen=Toplevel(top)
    field2_screen.title("Employee fields")
    field2_screen.config(bg="white")
    field2_screen.geometry("2000x2750")
    
    
    Button(field2_screen,text="Accountancy,Banking and Finance",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=finance).grid(row=0,column=1,sticky=W,pady=10)
    Button(field2_screen,text="Business,Consulting and Management",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=business).grid(row=1,column=1,sticky=W,pady=10)
    Button(field2_screen,text="Creative Arts and design",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=arts).grid(row=2,column=1,sticky=W,pady=10)
    Button(field2_screen,text="Engineering and Manufacturing",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=engineering).grid(row=3,column=1,sticky=W,pady=10)
    Button(field2_screen,text="Environment and Agriculture",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=agri).grid(row=4,column=1,sticky=W,pady=10)
    Button(field2_screen,text="Medicine",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=med).grid(row=5,column=1,sticky=W,pady=10)
    Button(field2_screen,text="Information Technology",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=IT).grid(row=6,column=1,sticky=W,pady=10)
    Button(field2_screen,text="Law",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=law).grid(row=0,column=3,sticky=W,pady=10)
    Button(field2_screen,text="Public services and Administration",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=admin).grid(row=1,column=3,sticky=W,pady=10)
    Button(field2_screen,text="Marketing,Advertising and PR",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=mark).grid(row=2,column=3,sticky=W,pady=10)
    Button(field2_screen,text="Media",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=media).grid(row=3,column=3,sticky=W,pady=10)
    Button(field2_screen,text="Science and Pharmaceuticals",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=pharm).grid(row=4,column=3,sticky=W,pady=10)
    Button(field2_screen,text="Teacher training and Education",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=educ).grid(row=5,column=3,sticky=W,pady=10)
    Button(field2_screen,text="Transport and Logistics",bd=10,font=('calibri',20,"bold"),relief="groove",width=45,bg="blue",fg="white",command=trans).grid(row=6,column=3,sticky=W,pady=10)

def finance():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+accounting+and+finance&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htiq=job+for+accounting+and+finance&htidocid=GBVOoNF1EW0AAAAAAAAAAA%3D%3D")

def business():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+business+and+management&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=tcayou3zUocAAAAAAAAAAA%3D%3D")

def arts():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+arts+and+design&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=sW2isdalxLMAAAAAAAAAAA%3D%3D")

def engineering():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+engineering+and+manufacturing&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=cdf3lnGpvsYAAAAAAAAAAA%3D%3D")

def agri():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+environment+and+agriculture&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=bHcWHa3UQ2YAAAAAAAAAAA%3D%3D")

def med():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+healthcare+and+medicine&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=H-Ov90aEs3sAAAAAAAAAAA%3D%3D")

def IT():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+information+technology+&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=_OktzZqAe5cAAAAAAAAAAA%3D%3D")

def law():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+law&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=5QKhw4ps93EAAAAAAAAAAA%3D%3D")

def admin():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+administration&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=p-ect1FzTHYAAAAAAAAAAA%3D%3D")

def mark():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+Marketing,Advertising+and+PR&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=bpbf5hvReVoAAAAAAAAAAA%3D%3D")

def media():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+media&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=gnguNdPDKxkAAAAAAAAAAA%3D%3D")

def pharm():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+Science+and+Pharmaceuticals&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=3wiGs7l62fIAAAAAAAAAAA%3D%3D")

def educ():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+Teacher+training+and+Education&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=llA9tfLenB8AAAAAAAAAAA%3D%3D")

def trans():
    webbrowser.open_new_tab("https://www.google.com/search?q=job+for+Transport+and+Logistics&sxsrf=ALiCzsZSPBOGpr7-wi0ImPOhy5MGc0aiNg:1665595025739&source=hp&ei=kfZGY-njKsTgseMPoPKwgAM&iflsig=AJiK0e8AAAAAY0cEoT7igHmFUzlGws5E1ymIqjnMXiid&oq=job+for+accountancy&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIICAAQBRAeEAoyCggAEAUQHhAPEAo6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgsILhCABBCxAxCDAToFCC4QgAQ6CwguEIAEELEDENQCOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6CwgAEIAEELEDEMkDOggIABCABBDJAzoHCAAQgAQQDToKCAAQgAQQyQMQDToJCAAQgAQQDRAKOggIABAeEA0QCjoKCAAQHhAPEA0QCjoKCAAQBRAeEA0QCjoMCAAQBRAeEA8QDRAKOgoIABAIEB4QDRAKOggIABAIEB4QDToMCAAQCBAeEA8QDRAKUABY_mxgmnxoAHAAeACAAf4BiAG7I5IBBjAuOS4xM5gBAKABAQ&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwi_uKiHmdv6AhX0cGwGHZ4gC9MQkd0GegQICRAB#fpstate=tldetail&htivrt=jobs&htidocid=hipojKRtM0QAAAAAAAAAAA%3D%3D")
    
    
#main display
Label(top,text="ONLINE JOB PORTAL",bd=20,font=('calibri',25,"bold"),relief="raised",width=30,fg="blue").grid(row=0,sticky=N,pady=10)


Button(top,text="SIGNUP",bd=10,font=('calibri',20,"bold"),relief="groove",width=20,bg="blue",fg="white",command=signup_display).grid(row=2,sticky=W,pady=10)
Button(top,text="LOGIN",bd=10,font=('calibri',20,"bold"),relief="groove",width=20,bg="blue",fg="white",command=login_screen).grid(row=3,sticky=W,pady=10)
Button(top,text="REMOVE PROFILE",bd=10,font=('calibri',20,"bold"),relief="groove",width=20,bg="blue",fg="white",command=rem_pro).grid(row=4,sticky=W,pady=10)

top.mainloop()

