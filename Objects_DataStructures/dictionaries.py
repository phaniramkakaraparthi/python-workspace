# Dictionary declaration
my_dict = {'key1':'value1','key2':'value2'}

# Retrieving value from dict
print('Value from key1: ' + my_dict['key1'])

list_mix = {'key1':'val1','key2':[0,1,2],'key3':{'key4':'val4'}}

print(list_mix['key2'][0])
print(list_mix['key3']['key4'])

# Add new key:value to dictionary
my_dict['key3'] = 'value3'
print(my_dict)

# Print keys & values in a dictionary seperately
print(my_dict.keys())
print(my_dict.values())

# Print list of items in a dictionary
print(my_dict.items())