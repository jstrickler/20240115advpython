
"""Basic sorting example"""

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
         "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
         "grape"]

sorted_fruit = sorted(fruits)  # sorted() returns a list

print(sorted_fruit)
print()

f1 = sorted(fruits, key=str.lower)
print(f"{f1 = }\n")

f2 = sorted(fruits, key=len)
print(f"{f2 = }\n")

def mysort(item):
    comparison_value = len(item), item.lower()
    print(f"Comparing {item} as {comparison_value}")
    return comparison_value

f3 = sorted(fruits, key=mysort)
print(f"{f3 = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def ln_fn_sort(person):
    return person[1], person[0]

for person in sorted(people, key=ln_fn_sort):
    print(person)
print('-' * 60)

for person in sorted(people, key=lambda p: (p[1], p[0])):
    print(person)
print('-' * 60)

# lambda parameters...: return-value


