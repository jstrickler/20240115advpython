s1 = "spam\n"  #  \n is newline   \t is tab  
print(len(s1))
print(s1)
s2 = 'spam\n'  # same as ""
s3 = """spam\n"""
s4 = '''spam\n'''

print("Guido's the ex-BDFL")
print('Guido is the ex-"BDFL"')
print("""Guido's the ex-"BDFL" of Python""")

query = """
select first_name, last_name, birth_state
from presidents
where party == "Whig"
"""

s5 = r"spam\n"
print(s5)

folder = r"my\new\terrific\folder\myfile.txt"  # bad
folder = "my\\new\\terrific\\folder\\myfile.txt"  # so-so
folder = "my/new/terrific/folder/myfile.txt"  #  good

#  \uXXXX     \UXXXXXXXX

state = "North Carolina"
print("North" in state)

x = "geo"
y = "duck"
m = x + y
print(m)
print(len(m))
print()

actor = "Chris Hemsworth"
print(actor)
print(actor.upper())
x = actor.upper()
#  .upper() .lower()  .title()  .capitalize()
print(actor.count('h'))
print(actor.count('z'))
print(actor.count('H'))
print(actor.lower().count('h'))

file_path = "bullwinkle.moose"
print(file_path.startswith('bull'))
print(file_path.startswith('cow'))

print(file_path.removesuffix('.moose'))
print(file_path.replace('winkle', ''))
print(file_path.replace('winkle', 'hockey'))

name = "          Chris Hemsworth         "
print("|" + name + "|")
print("|" + name.lstrip() + "|")
print("|" + name.rstrip() + "|")
print("|" + name.strip() + "|")
print()

value = "$100,123.98"
value = value.replace(',', '')
value = value.lstrip("$")
print(value)

ip_address = "47.9.238.113"

bytes = ip_address.split('.')
print(bytes)

record = "John Q. Public"
parts = record.split()
print(parts)






