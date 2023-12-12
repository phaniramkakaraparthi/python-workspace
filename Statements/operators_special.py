
# range functions : Get the range from:to:step similar to slice functions
for num in range(0,10,2):
    print(num)
print('\n')

# enumeration functions : used as counter function needed in loops
word = 'Sammy'
for char in enumerate(word):
    print(char)
print('\n')

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# zip operator to zip together 2 lists
list_1 = [1,2,3]
list_2 = ['a','b','c']
list_3 = [100,200,300,400,500] # zip function zips to the shortest list in the arguments list
for item in zip(list_1, list_2,list_3):
    print(item)

# in operator to check if an element is in a list
print('\n')
list_alpha = ['x','y','z']
print('x' in list_alpha)
print('a' in 'is a in list of alphabets')

dictionary = {'mykey' : 345}
print('mykey' in dictionary)
print(123 in dictionary.values())

# min and max functions to get min and max values in a list
list_num = [1, 2, 3, 4, 5, 6]
print(min(list_num))
print(max(list_num))

from random import shuffle

mylist_shuffle = [1,2,3,4,5,6,5]
shuffle(mylist_shuffle)
print(mylist_shuffle)

# random integers
from random import randint
rand = randint(0,100)
print(rand)

# User inputs using input() function
num = int(input('Enter a number: '))
print(f'Input number: {num}')