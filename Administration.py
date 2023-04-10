
#program to access the reports and other observatory options.
#requires the administrative access using an ID and a password.
import mysql.connector
from tabulate import tabulate
db=mysql.connector.connect(user="root",password="admin",host="localhost",database="parking")
mycursordb=db.cursor()
initial_count = 1
chances = 5
print("Welcome to Rajiv Chowk Parking Administrative system")
input_id = str(input("Enter the login id here: "))
password=input("Enter the Password")
mycursordb.execute("select ID from login where ID = '%s'" %(input_id))
idcheck=mycursordb.fetchall()
for i in idcheck:
    c=i[0]
mycursordb.execute("select Password from login where ID = '%s'" % (input_id))
passcheck=mycursordb.fetchall()
for a in passcheck:
    d=a[0]
if input_id==c and password==d:
    Options=int(input("""
Enter 1:For Tabular Report
Enter 2:For Revenue collected
Enter 3:  No. of cars
Enter 4:  Get Log Files of Specified Date
Enter 5: Current status of Pillars
Enter 6: Cars Present Inside Currently
Enter 7:Frequency Of a Car"""))
    if Options==1:
        mycursordb.execute("select VehicleNum,Floor,Pillar,EntryTime,ExitTime,code,AmountPaid from logfiles")
        result=mycursordb.fetchall()
        print(tabulate(result,headers=["VehicleNum","Floor","Pillar","EntryTime","ExitTime","Code","Amount"],tablefmt="psql"))
    if Options==2:
        mycursordb.execute("select SUM(AmountPaid)from logfiles")
        total=mycursordb.fetchall()
        for q in total:
            print("Total Revenue collected:",q[0])
    if Options==3:
        mycursordb.execute("select COUNT(VehicleNum)from logfiles")
        count=mycursordb.fetchall()
        for w in count:
            print("Total Number of Cars:",w[0])
    if Options==4:
        date=input("Enter the Date(YYYY/MM/DD)")
        mycursordb.execute("select VehicleNum,Floor,Pillar,EntryTime,ExitTime,code,AmountPaid from logfiles where cast(EntryTime as date)= '%s'"%(date))
        res=mycursordb.fetchall()
        print(tabulate(res,headers=["VehicleNum","Floor","Pillar","EntryTime","ExitTime","Code","Amount"],tablefmt="psql"))
        
    if Options==5:
        floor=int(input("Enter Floor Number"))
        if floor==1:
            mycursordb.execute("select *from floor_1")
            floor_1=mycursordb.fetchall()
            print(tabulate(floor_1,headers=["Floor","Pillars"],tablefmt="psql"))
                  
        if floor==2:
            mycursordb.execute("select *from floor_2")
            floor_2=mycursordb.fetchall()
            print(tabulate(floor_2,headers=["Floor","Pillars"],tablefmt="psql"))
                  
        if floor==3:
            mycursordb.execute("select *from floor_3")
            floor_3=mycursordb.fetchall()
            print(tabulate(floor_3,headers=["Floor","Pillars"],tablefmt="psql"))
        if floor>3:
            print("Invalid Input")
            
    if Options==6:
        mycursordb.execute("select COUNT(VehicleNum) from logfiles where AmountPaid=0")
        count1=mycursordb.fetchall()
        for z in count1:
            print("Total Number of Cars in Parking are:",z[0])
            
    if Options==7:
        Car=input("Enter Vehicle Registration Number")
        mycursordb.execute("select COUNT(VehicleNum) from logfiles where VehicleNum= '%s'" % (Car))
        count2=mycursordb.fetchall()
        for xz in count2:
            print("Frequency Of Car is :",xz[0])
      
else:
    print("Incorrect UserID or Password")
if input_id in idcheck :
    input_pass = input("Enter the password here: ")

db.close()




       
