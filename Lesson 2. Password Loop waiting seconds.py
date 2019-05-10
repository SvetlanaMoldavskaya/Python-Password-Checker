import time
choice = int(input("How many seconds should I wait?: "))
number_of_seconds = 1
for number_of_seconds in range (1, choice): 
    print (".")  
    number_of_seconds += 1 
    time.sleep (1)

password = int (input("Enter password: "))
while password == 6:
    print("Correct password! ")
    time.sleep (2)
    break
else:
    print ("Incorrect password! ")
    time.sleep (2)