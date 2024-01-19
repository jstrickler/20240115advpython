from pprint import pprint

knight_data = {}

file_path = "DATA/knights.txt"

with open(file_path) as file_in:
    for raw_line in file_in:
        line = raw_line.rstrip()  #  remove \n
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment 

pprint(knight_data)
print()

for name, data in knight_data.items():  #  [(name,data), (name,data), ...]
    print("key:", name, "  data:", data)
#    print(data[0], name, data[2])
print()

print(knight_data['Bedevere'])
print(knight_data['Bedevere'][1])