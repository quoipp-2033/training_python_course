# 4. Grocery App
# Write a programme that
# (1) Allows warehouse employees to enter a list of goods (including names only - using
# a string separated by commas) that are available in his/her shop
# (2) Allows customers to check whether an item is in stock or not by inputting a name:
# just show “Available” or “Out of stock!” on screen

print("Exercise 01_04: Grocery App")
input_list = input("Enter your good list, seperating by comma: ")
book_list = input_list.split(",")
i = 0
while i < len(book_list):
  x = book_list[i].strip()
  book_list[i] = x
  i = i + 1

search_title = input("Check status of: ")
if search_title in book_list:
    print("Available")
else:
    print("Out of stock!")