# To split the line in python we use `\n` 
splitString = "This string has been \nsplit over \nserveral \nlines"
print(splitString)

# When we want to use `tab` use `\t`
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# Using a 's in a sentence
print('The pet shop owner said "No, no, \'e\'s uh,... he\'s resting".')

# Doudble quotes inside the string must be escaped
print("The pet shop owner said \"No, no, 'e's uh,... he's resting\".")

# Three quotes
print("""The pet shop owner said "No, no, 'e's uh,... he's resting" """)

anotherSplitString = """This string has been 
split over
serveral
lines"""
print(anotherSplitString)

#use backslash to escape the end of line.
anotherSplitString_2 = """This string has been \
split over \
serveral \
lines"""
print(anotherSplitString_2)

# To print this sentence "C:\Users\timbuchlka\notes.txt"(which includes \t and \n in a sentence)
print("C:\\Users\\timbuchlka\\notes.txt") #use escape backslash character
print(r"C:\Users\timbuchlka\notes.txt") #inlcude character 'r'