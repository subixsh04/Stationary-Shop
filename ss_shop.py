
import mysql.connector as mys
con=mys.connect (host='localhost', user = 'root', password = '2004',charset = 'utf8')
cur= con.cursor()
cur.execute("create database if not exists stationary_shop")
cur.execute("use stationary_shop")
cur.execute("create table if not exists ss_basic (itemcode varchar(10) primary key, item_name varchar(20) not null, price float(10) not null)")
#print("table1 created")
cur.execute("insert ignore into ss_basic values('B01', 'PEN', 10.00)")
cur.execute("insert ignore into ss_basic values('B02', 'PENCIL', 5.00)")
cur.execute("insert ignore into ss_basic values('B03', 'ERASER', 5.00)")
cur.execute("insert ignore into ss_basic values('B04', 'SCALE', 10.00)")
cur.execute("insert ignore into ss_basic values('B05', 'SHARPNER', 5.00)")
cur.execute("insert ignore into ss_basic values('B06', 'INK BOTTLE', 35.00)")
cur.execute("insert ignore into ss_basic values('B07', 'GUM', 15.0000)")
cur.execute("insert ignore into ss_basic values('B08', 'GLUE STICK', 25.00)")
con.commit()
#print("records inserted")
#-----------------------------------displaying table1-------------------------------------------------------
def basic():
    print()
    print("\t\tBASIC\n")
    print("SNO.\tITEM_NAME\t  PRICE")
    i=1
    cur.execute("select * from ss_basic")
    rec=cur.fetchall()
    for a,b,c in rec:
        if len(b)<9 and len(b)<=5:
            print('',i,"\t",b,"\t\t",'Rs.',c)
        else:
            print('',i,"\t",b,"\t",'Rs.',c)
        i+=1
   
#------------------------------------TABLE1 COMPLETED------------------------------------------------------
#----------------------------------------creating table2---------------------------------------------------
cur.execute("create table if not exists ss_art_supplies (itemcode varchar(10) primary key, item_name varchar(20) not null, price float(10) not null)")
#print("table2 created")
cur.execute("insert ignore into ss_art_supplies values('A01', 'BRUSH PAINT', 45.00)")
cur.execute("insert ignore into ss_art_supplies values('A02', 'A4/A3 PAPER', 2.00)")
cur.execute("insert ignore into ss_art_supplies values('A03', 'SKETCH PEN', 25.00)")
cur.execute("insert ignore into ss_art_supplies values('A04', 'COLOR PENCIL', 35.00)")
cur.execute("insert ignore into ss_art_supplies values('A05', 'CRAYONS', 40.00)")
cur.execute("insert ignore into ss_art_supplies values('A06', 'CHART PAPER', 10.00)")
cur.execute("insert ignore into ss_art_supplies values('A07', 'WATER COLOR', 50.00)")
cur.execute("insert ignore into ss_art_supplies values('A08', 'RULED/UNRULED PAPER', 3.00)")
#print("records inserted")
#---------------------------------------------displaying table2-------------------------------
def artsupplies():
    print()
    print("\t\tART SUPPLIES\n")
    print("SNO.\t ITEM_NAME\t\t PRICE")
    i=1
    cur.execute("select * from ss_art_supplies")
    rec=cur.fetchall()
    for a,b,c in rec:
        if len(b)<=12:
            print('',i,"\t",b,"\t\t",'Rs.',c)
        else:
            print('',i,"\t",b,"\t",'Rs.',c)
        i+=1
#-------------------------------------------table2 completed----------------------------------------
#--------------------------------------------CRAETING TABLE3---------------------------------------
cur.execute("create table if not exists ss_general (itemcode varchar(10) primary key, item_name varchar(20) not null, price float(10) not null)")
#print("table3 created")
cur.execute("insert ignore into ss_general values('G01', 'STAPLER', 25.00)")
cur.execute("insert ignore into ss_general values('G02', 'SCISSIOR', 20.00)")
cur.execute("insert ignore into ss_general values('G03', 'CALCULATOR', 50.00)")
cur.execute("insert ignore into ss_general values('G04', 'BEL CLIPS', 10.00)")
cur.execute("insert ignore into ss_general values('G05', 'SCOTH TAPE', 15.00)")
cur.execute("insert ignore into ss_general values('G06', 'NOTEBOOKS', 30.00)")
cur.execute("insert ignore into ss_general values('G07', 'WRITING PAD', 70.00)")
cur.execute("insert ignore into ss_general values('G08', 'ENVELOPE', 15.00)")
#print("records inserted")
#---------------------------------------------displaying table3-------------------------------
def general():
    print()
    print("\t\tGENERAL\n")
    print("SNO.\tITEM_NAME\t\t  PRICE")
    i=1
    cur.execute("select * from ss_general")
    rec=cur.fetchall()
    for a,b,c in rec:
        if len(b)<=12:
            print('', i,"\t",b,"\t\t",'Rs.',c)
        else:
            print('',i,"\t",b,"\t",'Rs.',c)
        i+=1
#-------------------------------------------table3 completed----------------------------------------
#---------------------------------------------main display-------------------------------------------
print("\t\t\t....................................................................\t\t")
print("\n\t\t\t\t    **  Welcome to DST STATIONARY SHOP  **\n")
print("\t\t\t....................................................................\t\t")
print("\n\t\t\t\t       ***Chettinad Vidyashram***  \t\t\t\t\n")
cs_name=input("Enter coustmer name  ")
cs_ph= int(input("Enter your phone number  "))
def proceed():
    ch1=input("Do you want to buy any products from our shop(Y/N)  ")
    return ch1
ch2= proceed()    
def menu():
    print("\t\t\t-----------------------------------------")
    print("\n\t\t\t\t\t  MENU\n\n\t\t\t\t\t1.BASIC\n\n\t\t\t\t\t2.ART SUPPLIES\n\n\t\t\t\t\t3.GENERAL")
    print("\t\t\t-----------------------------------------")
if ch2=='Y' or ch2=='y':
    menu()   
else:
    print("press y to proceed")
    proceed()
    menu()
basic()
artsupplies()
general()
#----------------------------------------menu created----------------------------------------------------
#---------------------------------------accepting values-------------------------------------------------

print()
purchase=()
n=int(input("Enter no.of items to be purchased  "))
#menu()
print()
def cs_products():
    for i in range(n):
    ch3=int(input("enter the category in which you want to buy  "))
    t=()
    if ch3==1:
        for i in range(1):
            name=input("Enter item name  ")
            qty=int(input("Enter quantity  "))
            p="select price from ss_basic where item_name= '"+name+"'"
            cur.execute(p)
            pr=cur.fetchall()
            for i in pr:
                for j in i:
                    price=j
            t+=(name,qty,price,ch3)
        purchase+=(t),
    elif ch3==2:
        for i in range(1):
            name=input("Enter item name  ")
            qty=int(input("Enter quantity  "))
            p="select price from ss_art_supplies where item_name= '"+name+"'"
            cur.execute(p)
            pr=cur.fetchall()
            for i in pr:
                for j in i:
                    price=j
            t+=(name,qty,price,ch3)
        purchase+=(t),
    elif ch3==3:
        for i in range(1):
            name=input("Enter item name  ")
            qty=int(input("Enter quantity  "))
            p="select price from ss_general where item_name= '"+name+"'"
            cur.execute(p)
            pr=cur.fetchall()
            for i in pr:
                for j in i:
                    price=j
            t+=(name,qty,price,ch3)
        purchase+=(t),
    else:
        print("Invalid choice")
if n<25:
    cs_products()
else:
    print("Maximum number of items to be purchased can only be 24")
    
#-----------------------------------------------------------BILLING---------------------------------------------------
#print(purchase)
print("\t\t\t\t**********************************")
print("\t\t\t\t\tDST STATIONARY SHOP")
print("\t\t\t\t**********************************")
print("\n")
print("  CUSTOMER NAME : ",cs_name,"\t\tCUSTOMER PHONE NUMBER : ",cs_ph)
print()
print("------------------------------------------------------------------------------------------------------------")
print("S.NO  ITEM NAME\t\t\tQUANTITY\t\tPRICE\t\t\tAMOUNT")
print("------------------------------------------------------------------------------------------------------------")
k=1
amt=0
for i in purchase:
    if i[-1]==1:
        if len(i[0])<9 and len(i[0])<=8:
            if k<10:
                print('',k,'  ',i[0],'\t\t\t',i[1],'\t\t\t',i[2],'\t\t\t',i[1]*i[2])
            else:
                print('',k,' ',i[0],'\t\t\t',i[1],'\t\t\t',i[2],'\t\t\t',i[1]*i[2])     
        else:
            if k<10:
                print('',k,'  ',i[0],'\t\t',i[1],'\t\t\t',i[2],'\t\t\t',i[1]*i[2])
            else:
                print('',k,' ',i[0],'\t\t',i[1],'\t\t\t',i[2],'\t\t\t',i[1]*i[2])
    elif i[-1]==2:
        if len(i[0])<=10:
            if k<10:
                print('',k,'  ',i[0],"\t\t\t",i[1],'\t\t\t',i[2],'\t\t\t',i[1]*i[2])
            else:
                print('',k,' ',i[0],"\t\t\t",i[1],'\t\t\t',i[2],'\t\t\t',i[1]*i[2])
        elif len(i[0])>10 and len(i[0])<=16:
            if k<10:
                print('',k,'  ',i[0],'\t\t',i[1],'\t\t\t',i[2],'\t\t\t',i[1]*i[2])
            else:
                print('',k,' ',i[0],'\t\t',i[1],'\t\t\t',i[2],'\t\t\t',i[1]*i[2])
        else:
            if k<10:
                print('',k,'  ',i[0],"\t",i[1],'\t\t\t',i[2],'\t\t\t',i[1]*i[2])
            else:
                print('',k,' ',i[0],"\t",i[1],'\t\t\t',i[2],'\t\t\t',i[1]*i[2])
    k+=1
    amt+=i[1]*i[2]
print("------------------------------------------------------------------------------------------------------------")
print("\n\t\t\t\tTOTAL AMOUNT :",amt)
print("\n------------------------------------------------------------------------------------------------------------")
print()
print()

     
    


            














    


