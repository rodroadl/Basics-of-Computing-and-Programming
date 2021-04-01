last_step = int(input("Please enter a positive integer greater than 1: "))
first = 1 
step = 1
first = 1
second = 1
print(first)
print(second)
while(step < last_step - 1  ):    
    step += 1
    third = first + second
    first = second
    second = third
    print(third)