#addition

def sum(x, y):
    return x + y

# subtraction

def subtract(x, y):
    return x - y

# multipication

def multiply(x, y):
    return x * y

#division

def divide(x, y):
    return x / y

#distance

def distance(time,s):
	return time * s
#speed

def speed(time,d):
        return d / time

#simple interest

def interest(P,T,R):
	SI=(P * T * R)/100
	return SI
    
print("Select operation.")
print("1.Addition")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.distance")
print("6.speed")
print("7.interest")
while True:
    choice=input("Enter choice(MAKE YOUR SELECTION):")
    if choice == "1":
        x=int(input("x = "))
        y=int(input("y = "))
        print("sum","=",sum(x,y))
    elif choice == "2":
        x=int(input("x = "))
        y=int(input("y = "))
        print("subtract","=",subtract(x,y))
    elif choice == "3":
        x=int(input("x = "))
        y=int(input("y = "))
        print("multiply","=",multiply(x,y))
    elif choice == "4":
        x=int(input("x = "))
        y=int(input("y = "))
        print("divide","=",divide(x,y))
    elif choice =="5":
        time=int(input("Enter time(hr) :"))
        s=int(input("Enter speed(km/hr) :"))
        print("Distance is :",dis(time,s),"km")
    elif choice =="6":
        time=int(input("Enter time(hr) :"))
        d=int(input("Enter Distance(km) :"))
        print("Speed is :",speed(time,d),"km/hr")
    elif choice =="7":
        p=int(input("Enter Principal :"))
        t=int(input("Enter Time :"))
        r=int(input("Enter Rate :"))
        print("Interest",interest(p,t,r))
