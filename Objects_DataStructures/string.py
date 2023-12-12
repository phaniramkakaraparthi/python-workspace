# String
name = "phani is a nice guy"
print('Hello', name)

# Length of string
print('Length of Name ', len(name))

# Reverse Indexing
print(name[-3])

# Slicing
alphabets = 'abcdefghijk'

# Print from c i.e. skip a,b
print(alphabets[2:])

# Print only 'abc', note that end index in slicing excludes that character
print(alphabets[:3])

# Print only 'def' characters
print(alphabets[3:6])

# Print only fghi
print(alphabets[5:9])

# Entire string represented as below too
print(alphabets[::])

# Steps of 2 for entire string starting from beginning till end
print(alphabets[::2])

# Combine begin,end and step in one statement
print(alphabets[0:10:2])

# Reverse string using step size
print(alphabets[::-1])

# Strings are immutable in Python, i.e. name[0] = N will throw an error.
last_letters = name[1:]
print('S' + last_letters)

# Print a letter 10 times using '*'
letter_z = 'z'
print(letter_z * 10)

print(name.capitalize())
print(name.upper())
print(name.lower())

# Split string based on white spaces as default or we can give the character to split and convert to list.
print(name.split())

# format() method usage
print("Hello {}".format("Phani"))

# format() method argument usage
print("The {2} {1} {0}".format('fox','brown','quick'))

# format() variable keyword assignment
print("The {q} {b} {f}".format(f='fox',b='brown',q='quick'))

# Float formatting follows "{value:width.precision f}"
value = 100/7
print(value)

print('Value of Division is {r:1.5f}'.format(r=value))

# formatted String or fstring usage from python 3.6
print(f'Value of division is {value:1.5f}')
name = 'Phani'
age = 34
print(f'{name} is of {age} years age')