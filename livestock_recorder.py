num_livestock = int(input('how much livestock would you like to add? ')) 
with open('livestockcount.txt','w') as livestock_file: 
  for count in range(1, num_livestock + 1):
    print(f'Enter data for livestock count #{count}')
    # get fields for a record
    field_1 = input('Animal Type: ')
    field_2 = input('Number of Animal Type: ')
    field_3 = input('How many Children of the animal type: ')
    # write record to file
    livestock_file.write(f'{field_1}\n')
    livestock_file.write(f'{field_2}\n')
    livestock_file.write(f'{field_3}\n')
print() # prints a blank line
print('data have been written to livestockcount.txt')

marker = 'y'
with open('livestockcount.txt','a') as livestock_file:
  while marker == 'y' or marker == 'Y':
  # get fields for a record
    field_1 = input('Animal Type: ')
    field_2 = input('Number of Animal Type: ')
    field_3 = input('How many Children of the animal type: ')
    # write record to file
    livestock_file.write(f'{field_1}\n')
    livestock_file.write(f'{field_2}\n')
    livestock_file.write(f'{field_3}\n')
    
    marker = input('Y = continue, anything else will end the loop')
