num_entries = int(input('How many entries do you want to enter? '))

with open('steps_count.txt','w') as file_variable, open('steps_count.txt','r') as entry_list:
  for num in range(1, num_entries + 1):
    steps = input(f'#{num} How many steps would you like to add to the file? ')
    file_variable.write(f'{steps}\n')

  file_variable.flush()
  entry_list.seek(0)
  
  line = entry_list.readline()
  total_steps = 0

  while line != '': 
    total_steps += int(line)
    line = entry_list.readline()

print(f'The total steps of the numbers in the list is {total_steps}')
