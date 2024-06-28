import re

with open("text.txt") as f:
    list = f.read().splitlines()

elems_to_str = ''
only_letters_str = ''
list_with_words = []

for elem in list:
    elems_to_str = elems_to_str + " " + elem + " "

for elem in elems_to_str:
    # left the space chars, as they'll be useful to split the words apart afterwards
    if re.search("[^a-z]", elem) and re.search("[^A-Z]", elem) and elem != " ":
        continue
    else:
        only_letters_str = only_letters_str + elem

list_with_words = only_letters_str.split()
set1 = set(list_with_words)

print("All the unique words used in the book are: {}\n".format(set1))

print("Nr. of words used is: {}".format(len(list_with_words)))
print("Nr. of unique words used is: {}".format(len(set1)))
