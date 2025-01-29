# Create a tuple
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

# Accessing elements using index
print("tup1[0] ", tup1[0])
print("tup2[1:5] ", tup2[1:5])

# Update command (concatenate two tuples)
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print(tup3)

# Delete command
tup1 = ('annu', 'mac', 1997, 2000)
print(tup1)
del tup1

# Convert the tuple to a list
GFG_tuple = (1, 2, 3)
GFG_list = list(GFG_tuple)
print(GFG_list)

# Using for loop: Using a for loop that iterates through each element in our tuple
GFG_tuple = (1, 2, 3)
GFG_list = []
for i in GFG_tuple:  # Correct indentation
    GFG_list.append(i)
print(GFG_list)

#Using List Comprehension:

GFG_tuple = (1, 2, 3)
GFG_list = [i for i in GFG_tuple]
print(GFG_list)

# Using map function:
