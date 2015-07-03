# sum_dollars_in_text.py
# sums all US dollar amounts (in the form $xxxx.xx) in a text file 

import re

# open a file containing text and create a single string (big_string) of it's contents
big_string = ""
f = open("Book1.txt", "r")
for line in f:
    big_string += line
f.close()

# build list of strings matching regex for US money amounts in big_string
list_of_payments = re.findall('\$.+\.\d{2}', big_string)

# rebuild the list, removing all "$" and "," characters
list_of_payments_cleaned = []
for i in list_of_payments:
    string_builder = ""
    for char in i:
        if char not in "$,":
            string_builder += char
    list_of_payments_cleaned.append(string_builder)

# convert the list of strings to a list of floats to allow use of sum()
list_of_payments_cleaned = [float(x) for x in list_of_payments_cleaned]

print("The sum of all dollar amounts in the data file is $" + str(sum(list_of_payments_cleaned)))