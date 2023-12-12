myfile = open('file.txt')

# Print content from file
print(myfile.read())

# Read each line i.e convert it into a list
myfile.seek(0) # Reset cursor to Beginning of file
myfile_list = myfile.readlines();
print(myfile_list[1]) # Print specific index from list

# Manually closing the file
myfile.close()

# Writing content to file
with open('file.txt',mode='a') as my_file:
    my_file.write('\nThis is another line in file')

# Alternatively we can open the file like below so that explicit closing is not needed.
with open('file.txt',mode='r') as my_file:
    contents = my_file.read()
    print(contents)

# Create new file when writing content to file using mode='w'
with open('new_file.txt', mode='w') as new_file:
    new_file.write('This is a new file')
