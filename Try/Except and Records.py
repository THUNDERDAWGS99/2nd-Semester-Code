# Anthony Woods
# Period 7
# 
# Time Spent: 4 Weeks


import time
import sys

#Add function
def add(x, y):
    return x + y
    
#Subtract function
def subtract(x, y):
    return x - y
    
#Multiply Function  
def multiply(x, y):
    return x * y
    
#Divide Function
def divide(x, y):
    if y == 0:
        return "You cant divide by zero."
    return x / y
    
    
#Title
print("="*40)
print("             Calculator")
print("="*40)
print(" ")
print("          Pick an Operation")
print(" ")

#Shows each operation every second for 4 seconds
time.sleep(.5)
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print(" ")


#tells user to select a operation and the 2 numbers needed. Then checks if the number/letter that is chosen isnt or is in the list, if not, it reminds the user and sends them back to the selection
while True:
    try:
        choice = input("Enter Your Selected Operation Here (1/2/3/4): ")

        if choice not in ('1', "2", "3", "4"):
            raise ValueError
            
        #asks for users 1st number
        while True:
            try:
                num1 = float(input("Enter your first number: "))
                break
            except ValueError:
                print("thats not an number try again")
                time.sleep(1)
                sys.stdout.write("\033[F") #moves cursor up 1 line
                sys.stdout.write("\033[K") #clears line
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")  
                
                
                
                
                    
                
        #asks for users 2nd number        
        while True:
            try:
                num2 = float(input("Now, enter your second number: "))
                break
            except ValueError:    
                print("thats not an number try again")
                time.sleep(1)
                sys.stdout.write("\033[F")  #moves cursor up 1 line
                sys.stdout.write("\033[K")  #clears line
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")    
                
            
                continue
        
        sys.stdout.write("\033[F")  
        sys.stdout.write("\033[K")  
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        
        #format for the answer the calculator gives
        if choice == "1":
            result = add(num1, num2)
            print(num1, "+", num2, "=", result)
            
        elif choice == "2":
            result = subtract(num1, num2)
            print(num1, "-", num2, "=", result)
            
        elif choice == "3":
            result = multiply(num1, num2)
            print(num1, "x", num2, "=", result)
            
        elif choice == "4":
            result = divide(num1, num2)
            print(num1, "/", num2, "=", result)
            
        with open("calculatorrecord.txt", "a") as file:
            file.write(f"{choice}, {num1}, {num2}, {result}\n")
            
        #asks user if they want to do another calculation and checks if the answer is only yes or no
        print(' ')
        while True:
            time.sleep(1)    
            continue_calculating = input("you completed your calculation! Would you like to do another calculation? (yes/no)")
            if continue_calculating == "no":
                sys.exit()
            elif continue_calculating == 'yes':
                time.sleep(1)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print(' ')
                break
            else:
                print('yes / no only')
                time.sleep(1)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print(' ')
                
    #reminds user to use only 1 thru 4 of the operations only
    except ValueError:
        print("please choose only between 1/2/3/4.")
        time.sleep(1)
        sys.stdout.write("\033[F") 
        sys.stdout.write("\033[K")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
