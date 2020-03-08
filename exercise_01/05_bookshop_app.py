# 5. Bookshop App
# (1) Allows clerks to enter a list of books (including titles and quantities – using a
# dictionary) that are available in his/her shop
# (2) Allows customers to check whether an item is in stock or not by inputting a title:
# just show “N items available” or “Out of stock!” on screen

from helper.numeric_helper import NumericChecker

numeric_checker = NumericChecker()
book_list = {}
def InputBook():
  input_book_title = "a"
  input_book_quantity = "a"
  input_book_title = input("Enter your book title: ")
  while not(numeric_checker.quantityCheck(input_book_quantity)):
    input_book_quantity = input("Enter your book quantity: ")
  book_list[input_book_title] = input_book_quantity

def SearchBook():
  search_book_title = input("Enter your searching book title: ")
  if (book_list[search_book_title] > 0):
    print("Available")
  else:
    print("Out of stock!")

print("Exercise 01_05: Book shop App")
option = 0
while (option not in (1, 2, 3)):
  option = input ("Please choose an option (1.Input new book    2.Search book): ")
if (option == 1):
  InputBook()
elif (option == 2):
  SearchBook()


