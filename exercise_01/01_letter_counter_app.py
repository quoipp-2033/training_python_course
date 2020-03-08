# 1. Letter Counter App
# Write a console programme that
# (1) Allows users to enter a string
# (2) Then allows users to enter a character or a string
# (3) Prints the number of occurrences of the character or string in (2) in the string in (1)
print("Exercise 01_01: Letter Counter App")
original_string = input("Please input the original string: ")
search_string = input("Please input the search string: ")
occurrences_count = original_string.count(search_string)
print ("The number of occurrences of '{}' in '{}' is: {}".format(search_string, original_string, occurrences_count))
