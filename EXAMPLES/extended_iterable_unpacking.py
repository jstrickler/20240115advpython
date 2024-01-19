
values = ['a', 'b', 'c', 'd', 'e']  # values has 6 elements

x, y, *z = values  # {splat} takes all extra elements from iterable
print(f"x: {x}    y: {y}    z: {z}\n")

x, *y, z = values  # {splat} takes all extra elements from iterable
print(f"x: {x}    y: {y}    z: {z}\n")

*x, y, z = values  # {splat} takes all extra elements from iterable
print(f"x: {x}    y: {y}    z: {z}\n")

people = [
    ('Bill', 'Gates', 'Microsoft'),
    ('Steve', 'Jobs', 'Apple', 'NeXT'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Mark', 'Zuckerberg', 'Facebook', 'Thing1', 'Thing2'),
    ('Sergey', 'Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linux', 'Torvalds', 'Linux', 'Git'),
]

for first_name, last_name, *_ in people:  # name gets all but the last field
    print(first_name, last_name)
print()
