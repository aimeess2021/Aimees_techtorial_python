
# Ask iser to enter a string and find out last 2 letters of the string using negative indexing

from platform import python_branch


print("Enter a text")
s = input()
# if you want slicing to continue till the end of string using negativee indexing 
# you should leave the ending part empty.
print(s[-2:])