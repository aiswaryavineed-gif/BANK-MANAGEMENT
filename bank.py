
import mysql.connector
from mysql.connector import cursor


class Bank:
     def __init__(self):
         try:
             self.con=mysql.connector.connect(
                  user='root',
                  password='aiswarya',
                  host='localhost',
                  database='bank_management'
             )
         except Exception:
             self.con=None
             print('Database connection failed')

     def create (self,customer_name,account_type,phone,balance):
         try:
             cursor=self.con.cursor()
             query='insert into accounts (customer_name,account_type,phone,balance) values(%s,%s,%s,%s)'
             data=(customer_name,account_type,phone,balance)
             cursor.execute(query,data)
             if balance>0:
                 self.con.commit()
             else:
                 print('rejected')
         except Exception:
             print('connection failed')
         finally:
             cursor.close()

     def  view(self,balance):
         try:
             cursor=self.con.cursor()
             query='select * from accounts where balance >= %s order by balance desc '
             cursor.execute(query,(balance,))
             records=cursor.fetchall()
             if records:
                    for rows in records:
                         print(rows)
             else:
                     print('no records')
         except Exception:
             print('failed')
         finally:
             cursor.close()

     def search(self,customer_name):
         try:
             cursor=self.con.cursor()
             query='select * from accounts where account_id =%s or  customer_name like %s'
             cursor.execute(query,( customer_name,'%'+customer_name+'%'))
             records= cursor.fetchall()
             if records:
                 for rows in records:
                     print(rows)
             else:
                 print('no records')
         except Exception:
             print('failed ')
         finally:
             cursor.close()


     def deposit(self,account_id,a):
         try:
             cursor=self.con.cursor()
             query='update accounts set balance=%s where account_id=%s '
             data=(account_id,a)
             cursor.execute(query,data)
             self.con.commit()
             if cursor.rowcount>0:
                 print('updated ')
             else:
                 print('no records')
         except Exception:
             print('failed')
         finally:
             cursor.close()

     def withdraw(self,account_id,balance):
         try:
             cursor=self.con.cursor()
             query='update accounts set balance>=%s where account_id=%s'
             data=(account_id,)
             cursor.execute(query,data)
             if cursor.rowcount>0:
                     print('updated balance')
             else:
                     print('no records')
         except Exception:
             print('failed')
         finally:
             cursor.close()

     def delete(self,account_id):
         try:
             cursor=self.con.cursor()
             query='delete from accounts where account_id= %s '
             data=(account_id,)
             cursor.execute(query,data)
             self.con.commit()
             if cursor.rowcount>0:
                 print('deleted')
             else:
                 print('no records')
         except Exception:
             print('failed')
         finally:
             cursor.close()

     def summary(self):
         try:
             cursor=self.con.cursor()
             query='select account_type, count(*) , avg(balance) from accounts group by account_type '
             cursor.execute(query)
             records = cursor.fetchall()
             if records:
                for rows in records:
                 print(rows)
             else:
               print('no records')

         except Exception:
                 print('failed ')
         finally:
                cursor.close()

b=Bank()
while True:
    print('BANK ACCOUNT MANAGEMENT')
    print('1.create account')
    print('2.view account')
    print('3.search account')
    print('4.deposit account')
    print('5. withdraw account')
    print('6.delete account')
    print('7. account summary')
    print('8. exit')

    ch=int(input('enter choices:'))
    if ch==1:
        customer_name=input('enter customer name')
        account_type=input('enter account type')
        phone=int(input('enter phone'))
        balance=int(input('enter balance'))
        b.create(customer_name,account_type,phone,balance)

    elif ch==2:
        balance=int(input('enter balance'))
        b.view(balance)

    elif ch==3:
        customer_name=input('enter name')
        b.search(customer_name)

    elif ch==4:
        account_id=int(input('enter id'))
        a=int(input('enter amount'))
        b.deposit(account_id,a)

    elif ch==5:
        account_id=int(input('enter id'))
        b.withdraw(account_id,balance)

    elif ch==6:
        account_id=int(input('enter id'))
        b.delete(account_id)

    elif ch==7:
        b.summary()

    elif ch==8:
        print('exit')
        break

    else:
        print('invalid')













