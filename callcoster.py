day = input("Enter the day the call started at: ")
time = int(input("Enter the time the call started at (hhmm): "))
duration = int(input("Enter the duration of the call (in minutes): "))

if(day == "Sat" or day == "Sun"):
    price = 0.15
else:
    if(800<=time<=1800):
        price = 0.4
    else:
        price = 0.25
        
cost = '%2.2f' % (price * duration)
               
print("This call will cost $", cost, sep="")