# Declaration of set
myset = set()

myset.add(1)

print(myset)

myset.add('2')

print(myset)

myset.add(1)

# Note that value 1 is not added to set as set already contain item available and it won't add duplicate entries.
print(myset)

my_list = [1,1,1,1,2,2,3,4,5,3,4,5,3,5,1]

# Get unique values only from list and delete duplicates.
print(set(my_list))

print(set('Mississippi'))