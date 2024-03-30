# Slicing = create a substring by extracting elements from another string
#                   indexing[ ] or slices( )
#                   [start:stop:step]

name = "Jhon Doe"

first_name = name[:4]
last_name = name[5:]
funky_name = name[ : : 3]
reversed_name = name[ : : -1]

website1 = "http://google.com"

website2 = "http://wikipedia.com"
slice = slice(7,-4)

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

print(website1[slice])
print(website2[slice])
