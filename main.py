#Module Importing
import os
import mysql.connector as m
import random
ex='n'
#Database connection
con=m.connect(host='localhost',user='root',password='Di@090103',database='pro')
c=con.cursor()

#Function defining
#1.New Account
def new_acc():
                c=con.cursor()
                name=input('Enter your name : ')
                acc_type=input("\nEnter type of the account (C/S): ")
                c.execute('select acc_no from bank')
                d=c.fetchall()
                def ap():               #Account No. Generator
                        acc=random.randint(10000,999999)
                        for i in range(len(d)):
                                if acc==d[i][0]:
                                                acc=ap()
                        return acc

                acc_no=ap()
                c.execute('select acc_no from bank')
                d=c.fetchall()
                deposit=int(input('Enter initial amount\n(>=500 for Saving and >=1000 for Current) : '))
                amount=deposit
                c.execute('insert into bank values(%s,"%s","%s",%s)'%(acc_no,name,acc_type,amount))
                con.commit()
                print ('Account created successfully !')
                print ('And the account no. is : ',acc_no)
#2.Deposit Amount
def dep():
                c=con.cursor()
                ac=int(input(('Enter account no. : ')))
                c.execute('select amount from bank where acc_no=%s'%(ac))
                d=c.fetchall()
                x=d[0][0]
                dp=int(input('Enter depositing amount : '))
                c.execute('update bank set amount=%s where acc_no=%s'%(x+dp,ac))
                con.commit()
                print ('The account balance is ',x+dp,'Rupees')
                

#3.Withdraw Amount
def withdraw():
                c=con.cursor()
                ac=int(input('Enter account no. : '))
                c.execute('select acc_type,amount from bank where acc_no=%s'%(ac))
                d=c.fetchall()
                acc_type=d[0][0]
                x=d[0][1]
                w=int(input('Enter withdrawing amount : '))
                if acc_type=='C':
                        if x-w>=1000:
                                c.execute('update bank set amount=%s where acc_no=%s'%(x-w,ac))
                                con.commit()
                                print ('The account balance is ',x-w,'Rupees')
                        else :
                                print ('After withdrawl remaining balance will be less than 1000')
                else:
                        if x-w>=500:
                                c.execute('update bank set amount=%s where acc_no=%s'%(x-w,ac))
                                con.commit()
                                print ('The account balance is ',x-w,'Rupees')
                        else:
                                print ('After withdrawl remaining balance will be less than 500')

#4.Balance Enquiry
def enq():
                c=con.cursor()
                ac=int(input('Enter account no. : '))
                c.execute('select * from bank where acc_no=%s'%(ac))
                d=c.fetchall()
                for i in range(len(d[0])):
                        if i==0:
                                print ('Account no. : ',d[0][i])
                        elif i==1:
                                print ('Name : ',d[0][i])
                        elif i==2:
                                if d[0][i]=='C' or d[0][i]=='c':
                                        print ('Account type : Current Account')
                                else :
                                        print ('Account type : Saving Account')
                        else :
                                print ('Account Balance : ',d[0][i])

#5.All account holders list
def all_acc():
                c=con.cursor()
                c.execute('select * from bank')
                d=c.fetchall()
                if len(d)==0:
                        print ('\nNO RECORDS FOUND !\n')
                else :
                        for I in d:
                                print (I)

#6.Close an account
def del_():
                ac=int(input('Enter account no. : '))
                c.execute('delete from bank where acc_no=%s'%(ac))
                con.commit()
                print ('\nAccount deleted successfully !\n')
        

while ex=='n' or ex=='N':
        os.system('clear')
        print ("""\n\n                * * * * * * * * * * * * * * * * * *
                *            MAIN MENU            *
                * * * * * * * * * * * * * * * * * *
                * 1. * New Account                *
                * 2. * Deposit Amount             *
                * 3. * Withdraw Amount            *
                * 4. * Balance Enquiry            *
                * 5. * All Account Holder List    *
                * 6. * Close An Account           *
                * 7. * Exit                       *
                * * * * * * * * * * * * * * * * * *
                    """)
        def inp():
                        ch=input("Enter Your Choice(1~7):")
                        return ch
        r=inp()
        if r.isnumeric():
                r = int(r)

        if r==1:
                        new_acc()
        elif r==2:
                        dep()
        elif r==3:
                        withdraw()
        elif r==4:
                        enq()
        elif r==5:
                        all_acc()
        elif r==6:
                        del_()
        elif r==7:
                        exit()
        else :
                        print ('Try again ! ')
        ex=input('Exit?(y/n) ')
