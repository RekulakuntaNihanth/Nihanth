#Simple programs
x=5
y="ram"
print(x)
print(y)
#Assign values to the multiple variables
x,y,z="orange","banana","cherry"
print(x)
print(y)
print(z)
#Assign the same values to the multiple variables in one line
x=y=z="orange"
print(x)
print(y)
print(z)
#To combine both text and a variable we use '+'.
x="python is "
y="programming language"
print(x+y)
# split() method
text = 'Python is fun'
print(text.split())
#seperator parameter
#Concatenating strings with a custom separator:
print('Hello', 'world', sep=', ')
#Printing numbers with a specific separator
print(1, 2, 3, sep=' - ')
#Combining different data types with a separator:
print('apple', 10, True, sep=' | ')
#Printing a list with a custom separator
my_list = ['apple', 'banana', 'orange']
print(*my_list, sep=', ')
#end parameter
print('Hello', end=' ')
print('world')
#end parameter
print('Counting:', end=' ')
for i in range(1, 6):
    print(i,end='')
#end parameter
print('1', end='')
print('2', end='')
print('3')


