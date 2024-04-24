# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements of a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing tuple
print("Sliced tuple:", my_tuple[2:4])

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked elements:", a, b, c, d, e)

# Length of a tuple
print("Length of tuple:", len(my_tuple))

# Concatenating tuples
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated tuple:", concatenated_tuple)

# Checking membership in a tuple
print("Is 3 in the tuple?", 3 in my_tuple)