
G=1
list=[]

class movies():
    def movie (self,name):
        while True:
            print("Available Movies")
            print("1>>Mangatha\n2>>Leo\n3>>Garudan\n4>>Vikram")
            name=int(input("enter the movie name:"))
            if name<5:
                if(name==1):
                    print("You Should Choose Mangatha")
                elif(name==2):
                    print("You Should Choose Leo")
                elif(name==3):
                    print("You Should Choose Garudan")
                elif(name==4):
                    print("You Should Choose Vikram")
                return 
            else:
                print("please enter Available Movies")
class time ():
    def timing (t,self):
        while True:
            print("=========================================")
            print("1>>10:30AM \n2>>12:00PM \n3>>3:00PM \n4>>6:30PM \n5>>9:45PM")
            t=int(input("entre the time:"))
            if t<=5:
                if(t==1):
                    print("ur time is 10:30AM \nSelect ur seat range")
                elif(t==2):
                    print("ur time is 12:00PM \nSelect ur seat range")
                elif(t==3):
                    print("ur time is 3:00PM \nSelect ur seat range")
                elif(t==4):
                    print("ur time is 6:30PM \nSelect ur seat range")
                elif(t==5):
                    print("ur time is 9:45PM \nSelect ur seat range")
                return
            else:
                print("Enter the available timing")
class ticket():
    def tick(h,g,self):
        print("=========================================")
        h=int(input("how many tickets:"))
        print("===========Seat Numbers============")
        for i in range(1,60+1):
            list.append(i)
        print(list)
        print("=========================================")    
        a=int(input("enter the start:"))
        b=int(input("enter the end:"))
        for i in range(a,b+1): 
            print("ur seat number=",i)
        print("=========================================")
        G=h*200
        print("ur Ticket amounti is:",G)
    
class payment(movies,ticket,time):
    def pay(self,p,UPI,d,c):
        print("1>>UPI \n2>>Debit Card \n3>>Credit card ")
        p=int(input("enter ur payment option:"))
        while True:
            if p<=3:
                if p==1:
                    UPI=input("enter ur UPI Number")
                    if len(UPI) == 4 or len(UPI) == 6:
                        print("Your tickets are booking successfully")
                        return
                    else:
                        print("Invalid UPI number. Please enter a valid 4 or 6-digit UPI.")
                        break
                if p==2:
                    num = input("Enter your Card number:")
                    d = input("Enter Expiry date:")
                    c = int(input("Enter CVV (3 digits): "))
                    name = int(input("Enter OTP: "))
                    print("Your tickets are booking successfully")
                if p==3:
                    num = input("Enter your Card number:")
                    d = input("Enter Expiry date:")
                    c = int(input("Enter CVV (3 digits): "))
                    name = int(input("Enter OTP: "))
                    print("Your tickets are booking successfully")
                return
            else:
                print("Enter ur correct payment Option")

print("************WELCOME TO PVR CENIMAS****************")            
pvr=payment()
pvr.movie(1)
pvr.timing(1)
pvr.tick(1,1)
print("=========================================")
pvr.pay(1,1,1,1)
print("--------Payment Successful--------")
print("--------Collect ur Ticket--------")




   
            
