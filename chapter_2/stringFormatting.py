for i in range(1,13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
print("\n")

# Specify a field width 
for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))


# left align the values `<`
for i in range(1,13):
    print("No. {0} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

# center align the values '^'
for i in range(1,13):
    print("No. {0} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12}".format(22.0 / 7))
print("Pi is approximately {0:12f}".format(22.0 / 7))
print("Pi is approximately {0:12.50f}".format(22.0 / 7))
print("Pi is approximately {0:52.50f}".format(22.0 / 7))
print("Pi is approximately {0:62.50f}".format(22.0 / 7))


# No specify field
for i in range(1,13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))