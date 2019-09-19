<<<<<<< HEAD
# PATH sbox/lpthw/mystuff/ex15.py

from sys import argv

=======
# PATH ~/sbox/lpthw/mystuff/ex15.py

from sys import argv


>>>>>>> 1ef4f8e46798b447163f96007c042158c6c65f39
script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

<<<<<<< HEAD
print(txt_again.read())
=======
print(txt_again.read())
>>>>>>> 1ef4f8e46798b447163f96007c042158c6c65f39
