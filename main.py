import mysql.connector as db
import re
import os
import time

mydb=db.connect(host='localhost',user='******',password='********',database='*******')
cur=mydb.cursor()
#cur.execute("create table directory (mob varchar(10) primary key,name varchar(30),email varchar(20),address varchar(75))")

regex=r'\b[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[A-Z|a-z]{2,3}\b'

def check_cont(con):
    if (len(con)==10 and con.isdigit()):
        return con
    else:
        print("invalid phone number...\nPlease enter again\n")
        con=input("Enter Contact Number:")
        return check_cont(con)

def check_email(em):
    if(re.fullmatch(regex,em)):
        return em
    else:
        print("Invalid Email address...\nEnter again\n")
        em=input("Enter email address:")
        return check_email(em)

def create_contact():
    name=input("Enter Name:")

    contact=input("Enter Contact Number:")
    contact=check_cont(contact)
   
    email=input("Enter email id:")
    email=check_email(email)

    address=input("Enter Address:")
    w=('insert into directory values(%s,%s,%s,%s)')
    val=[contact,name,email,address]
    cur.execute(w,val)
    mydb.commit()    
    print("Record Inserted")    
    time.sleep(1)

def delete_contact():
    del_val=input("Enter the Contact number/name to be deleted:")
    if(del_val.isdigit()):
        nam=('delete from directory where mob=%s')
        cur.execute(nam,(del_val,))
        mydb.commit()
        print("Contact deleted...\n")
        time.sleep(1)

    else:
        nam=('delete from directory where name=%s')
        cur.execute(nam,(del_val,))
        mydb.commit()
        print("Contact deleted...\n")
        time.sleep(1)


def search_contact():
    ch1=input("Enter the Contact number/name to search:\n")
    if(ch1.isdigit()):
        ac1='select *from directory where mob=%s'
        cur.execute(ac1,(ch1,))
        res=cur.fetchall()
    else:
        ac1='select *from directory where name=%s'
        cur.execute(ac1,(ch1,))
        res=cur.fetchall()
    
    if(len(res)==0):
        print("NO Record Found\n")
    else:
        os.system('cls')
        print("The following are the Records Found")
        j=1
        for i in res:
            print('\nSl no.:',j,'\nName:',i[1],'\nContact Number:',i[0],'\nEmail id:',i[2],'\nAddress:',i[3],'\n\n')
            j+=1


def show_all():
    ch2='select *from directory'
    cur.execute(ch2)
    re=cur.fetchall()
    j=1
    for i in re:
        print('\nSl no.:',j,'\nName:',i[1],'\nContact Number:',i[0],'\nEmail id:',i[2],'\nAddress:',i[3],'\n\n')
        j+=1
    b=input('\n\n\n\npress any key to return to home page:')


choice=1
while(choice==1):
    os.system('cls')
    print("Welcome to Phonebook Directory")
    print("Enter 1 to Create a contact")
    print("Enter 2 to Search a contact")
    print("Enter 3 to Delete a contact")
    print("Enter 4 to Displat All Contacts")
    print("Enter 5 to Exit")
    a=input()
    if(a=='1'):
        os.system('cls')
        create_contact()
        pass
    elif a=='2':
        os.system('cls')
        search_contact()
        b=input('\n\n\n\npress any key to return to home page:')
        pass
    elif a=='3':
        os.system('cls')
        delete_contact()
    elif a=='4':
        os.system('cls')
        show_all()
    elif a=='5':
        choice=0
    else:
        print("Invalid Input...")
        time.sleep(2)
        


