parrot = "Norwegian Blue"

# In the slicing the last character you specify isnt' incldued.
print(parrot[0:6]) #Norweg
print(parrot[3:5]) #we
print(parrot[0:9]) 
print(parrot[:9]) 

#Slice with negative number
print(parrot[-1]) # Print out last word `e`
print(parrot[-4])
print(parrot[-4:-2]) 
print(parrot[-4:12]) # From index -4, up to but not including index position 12


#Using a step in slice
print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nr

number = "3,123,456,789,999"
seperators = number[1::4]
print(seperators)
values = "".join(char if char not in seperators else " "for char in number).split()
print(values)

#Slice Back
letters = "abcedfg"
backwords = letters[6:0:-1] # does not include `a` 
print(backwords)
backwordsCorrect = letters[6::-1]
print(backwordsCorrect)
backwordsCorrect2 = letters[::-1]
print(backwordsCorrect2)

          #012345678910  
alphabet ="abcdefghijzlmnopqrstuvwxyz"
print(alphabet[16:13:-1]) # Standing position 16 extended backwards up to, but not including the charater at position 13.

print(alphabet[4::-1]) # Standing position 4 extended backwards up to end

print(alphabet[:-9:-1]) # last 8 characters, in reverse order 

print(alphabet[-4:]) # - means from the last index, count 4 and that point start slicing.
print(alphabet[:1]) 