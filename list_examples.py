list1 = list()   # empty list
print(f"{list1 = }")

colors = ['red', 'blue', 'purple']
print(f"{colors = }")

things = []  # empty list

# x = list(any-iterable-type)

cities = list()
cities.append("New York")
print(f"{cities = }\n")
cities.append("Trenton")
cities.append("Nyack")
cities.append("Parsippany")
print(f"{cities = }\n")
cities.insert(0, "Morristown")
cities.insert(3, "West Orange")
cities.insert(1, "Beach Haven")
print(f"{cities = }\n")

nc_cities = ['Durham', 'Charlotte', 'Asheville']
cities.extend(nc_cities)
print(f"{cities = }\n")

# LIST.append(obj)  LIST.insert(pos, obj)   LIST.extend(iterable)

del cities[1]
print(f"{cities = }\n")
cities.remove('Nyack') 
print(f"{cities = }\n")

city = cities.pop()   # remove last element
print(f"{city = }")
print(f"{cities = }\n")

city = cities.pop(3)
print(f"{city = }")
print(f"{cities = }\n")

#   del LIST[pos]   LIST.remove(value)    value = LIST.pop(pos)
print(f"{len(cities) = }\n")

print(f"{cities[0] = }")
print(f"{cities[5] = }")
print(f"{cities[len(cities)-1] = }")
print(f"{cities[-1] = }")
print()

# print(f"{cities[22] = }")   INDEX ERROR

print(f"{cities[0:4] = }")
#   [start:stop]

print(f"{cities[1:4] = }")

print(f"{cities[:3] = }")
print(f"{cities[2:] = }")

print(f"{cities[-3:] = }")
print('-' * 60)

# for VAR in ITERABLE: ...
for city in cities:
    print(city)


















