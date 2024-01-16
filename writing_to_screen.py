person = "Beyonce"
city = "Los Angeles"
value = 4344.542898


# print(str(person) + " " + str(city) + " " + str(value) + "\n")


print(person)
print(person, city, value)
print(person, city, value, sep="/")
print(person, city, value, sep="#")
print(person, city, value, sep=", ")
print(person, city, value, sep="")

print(person)
print(city)
print('----')
print(person, end="XX")
print(city)

#  end=" "    end=""

#  city: person

print(f"{city}: {person}")  #  f-string
print(f"2 + 2 = {2 + 2}")

print(f"value is {value}")
print(f"value is {value:.3f}")  #     <total-width>.<decimal-places>f
print(f"value is {value:.2f}")
print(f"value is {value:.1f}")
print(f"value is {value:.0f}")

m = 19
print(f"Value is :{m:4d}:")
print(f"Value is :{m:04d}:")





