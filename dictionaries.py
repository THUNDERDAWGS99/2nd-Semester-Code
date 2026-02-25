from datetime import datetime

#checks if the user put the birthday in USA format like 12/25/25
def is_valid_date(date_str):
    """check if date valid (MM/DD/YYYY)."""
    try:
        datetime.strptime(date_str, "%m/%d/%Y")
        return True
    except ValueError:
        return False

#home screen
def main():
    birthdays = {}

    while True:
        print("\n   Birthdate Manager    ")
        print(" ")
        print("1. Add a new birthday")
        print("2. List all the people in the list")
        print("3. List all birthdays in the list")
        print("4. Empty the list of people and birthdays")
        print(" ")
        
        #add new birthday 
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter the person's name: ")
            date = input("Enter their birthday (MM/DD/YYYY): ")

            if is_valid_date(date):
                birthdays[name] = date
                print(f"Birthdate for {name} has been added!")
            else:
                print("please only use MM/DD/YYYY format!")

        # List all people
        elif choice == "2":
            if birthdays:
                print("\nPeople stored in list:")
                for person in birthdays.keys():
                    print("-", person)
            else:
                print("No people are stored")

        # List all unique birthdays
        elif choice == "3":
            if birthdays:
                unique_birthdays = set(birthdays.values())
                print("\nUnique birthdates:")
                for bday in unique_birthdays:
                    print("-", bday)
            else:
                print("No birthdates are stored.")

        # Empty the list
        elif choice == "4":
            birthdays.clear()
            print("All birthdays have been removed from the list")

        

        else:
            print("please only choose 1 through 5 ")
            

if __name__ == "__main__":
    main()
