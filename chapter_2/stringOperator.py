string1 = "he's "
string2 = "probably "
stirng3 = "pining "
string4 = "for the "
string5 = "her"

# Concatenating string literls 
print(string1 + string2 + stirng3 + string4 + string5)

print("he's " "probably " "pining " "for the " "her")

# Multiplied string
print("Hello " * 5)

# Check charater in strings
today = "friday"
print("day" in today) # true
print("fri" in today) # true
print("thur" in today) # false

#String Replacement Fields
age = 30
print("My age is " +str(age) + " years")
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))

print("Jan: {2}, Feb: {0}, Mar:{2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}".format(28,30,31))

print("\n")
print("""
Jan: {2}
Feb: {0}
Mar:{2} 
Apr: {1} 
May: {2} 
Jun: {1} 
Jul: {2} 
Sep: {1} 
Oct: {2} 
Nov: {1} 
Dec: {2}
""".format(28,30,31))