#Anthony Woods
#Period 7
#Creating and Editing Lists 
#Time took: 2 hours


#ask the user for elements
listsize = int(input("How many elements would you like in your list? "))

elementlist = []

# asks for value of the element
for i in range(listsize):
    value = input(f"enter value for the element {i}: ")
    elementlist.append(value)

print("\nYour list is:", elementlist)

#lets the user edit an elemet
while True:
    print(" ")
    choice = input("Would you like to edit an element? (yes/no): ")

    if choice == "no":
        print("Final list:", elementlist)
        break

    if choice == "yes":
        try:
            index = int(input("Enter the index of the element you want to change: "))
            newvalue = input("Enter your new value: ")
            elementlist[index] = newvalue
            print("The updated list:", elementlist)
            
#prevents code from crashing and also gives a message
        except IndexError:
            print("That index is out of range, try putting an index thats in range.")

        except ValueError:
            print("Please enter a valid number for the index.")

    else:
        print("Please answer 'yes' or 'no' in lowercase form.")
