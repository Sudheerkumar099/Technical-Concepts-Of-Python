for num in range(1,10,1): # 1 is the starting point , 10 is ending point , 1 is step value
    print ("sending a message for",num," time", " *"*num)

success= False
for number in range(3):
    print("Attempt", number)
    if success:
        print("Successful") #executes when condition is met
        break
else:
    print("Failed all 3 attempts") #executes when the loop is exhausted without break


# Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x} , {y})")
    
    