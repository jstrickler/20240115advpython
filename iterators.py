fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

for i, fruit in enumerate(fruits):
    print(i, fruit)
print('-' * 60)
print(f"{list(enumerate(fruits)) = }")
print()

ef = enumerate(fruits)
print(f"{ef = }")
for i, fruit in ef:
    print(i, fruit)
    if i == 5:
        break
print('-' * 60)

rf = reversed(fruits)
print(f"{rf = }")
for fruit in rf:
    print(fruit)
print()
print('-' * 60)

states = ['NC', 'TX', 'CA', 'VA']
capitals = ['Raleigh', 'Austin', 'Sacramento']

st_caps = zip(states, capitals)
print(f"{st_caps = }")
for state, cap in st_caps:
    print(state, cap)

#  range(stop)  range(start, stop)
for i in range(5):
    print("nana")
print()



