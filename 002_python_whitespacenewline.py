# Add tabs - each print will automatically start on a new line
print("Left aligned")
print("\tTabbed Once")
print("\t\tTabbed Twice") 

# Add new line
print("I will start a new line \nhere and \nhere and \nhere and \n\there with a tab")

# strip whitespace at the end of a string when printing
message="there are spaces at the end of this string   "
print("\n",message.rstrip())

# strip whitespace at the end of a string
message2="there are not spaces at the end of this string   "
message2=message2.rstrip()
print("\n",message2.rstrip(),"\n")

# Also lstrip() to strip whitespace to left of string

# Also strip() to strip whitespace from right and left of string

