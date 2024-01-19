fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f1 = [f.title() for f in fruits]
print(f"{f1 = }\n")

f2 = [f.upper() for f in fruits if f.endswith('y')]
print(f"{f2 = }\n")

f3 = {f:(f[:3], len(f)) for f in fruits}
print(f"{f3 = }\n")

fgen = (f.title() for f in fruits)
print(f"{fgen = }")
for fruit in fgen:
    print(fruit)
print()

