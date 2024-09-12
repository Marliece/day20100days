print("List Generator")
print()
print()
starting_num = int(input("Start at: "))
ending_num = int(input("End before: "))
increment = int(input("Increment between values: "))
print()

for i in range(starting_num, ending_num, increment):
  print(i)