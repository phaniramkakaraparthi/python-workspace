# Iterate Lists
my_list = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in my_list:
    list_sum = list_sum + num
    if num % 2 == 0:
        print(f'{num} is Even')
    else:
        print('{} is Odd'.format(num))

print(f'List sum: {list_sum}')

# Iterate Strings
for letter in 'Hello World':
    print(letter)

# Iterate tuple
tup = (1,2,3)
for num in tup:
    print(num)

tup_list = [(1,2),(3,4),(5,6),(7,8)]
# Tuple unpacking from list
for (a,b) in tup_list:
    print(a)
    print(b)

# Iterate Dictionary

dict_val = {'k1':1,'k2':2,'k3':3}

for item in dict_val.items():
    print(item)

# Use tuple unpacking to print key:value as above statement returns tuple pairs

for key,value in dict_val.items():
    print(f'{key} : {value}')

# Keywords pass,break,continue usage
for item in my_list:
    # pass indicate to do nothing at all
    pass
print('End of my script')

# Continue keywords usage
mystring = 'sammy'
for char in mystring:
    if char == 'm':
        continue
    print(char)

# Break keywords usage
for char in mystring:
    if char == 'y':
        break
    print(char)