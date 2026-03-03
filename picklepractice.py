import pickle

#ask users for their inputs
set1_input = input("Enter details of the first set separated with spaces: ")
set2_input = input("now enter details of the second set separated with spaces: ")

#turns the imput into sets and unions them
set1 = set(set1_input.split())
set2 = set(set2_input.split())
union_set = set1.union(set2)

#serialize the set into practice.dat
with open("practice.dat", "wb") as file:
    pickle.dump(union_set, file)

#tells the user its been saved to practice.dat
print("Union was saved to practice.dat file")
