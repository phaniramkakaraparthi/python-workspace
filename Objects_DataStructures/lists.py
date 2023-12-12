list_a = ['one','two','three']
list_b = ['four','five']

list_b.append('six')
print(list_b)

list_a[0] = 'ONE'
print(list_a)

list_c = list_a + list_b
print(list_c)

list_c.pop()
print(list_c)

list_c.pop(0)
print(list_c)

alph_list = ['a', 'z', 'f', 'x']
alph_list.sort()
print(alph_list)

# value x in range values to create a list.
mylist = [x for x in range(1,10)]

print(mylist)


