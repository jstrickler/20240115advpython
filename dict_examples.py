d1 = dict()  # empty dict
d2 = {'NY': 'Albany', 'NJ': 'Trenton'}
d3 = {}   # empty dict
d3['red'] = 5
d3['purple'] = 19
d3['blue'] = 8
d3['red'] = 35
print(f"{'blue' in d3 = }")
print(f"{'orange' in d3 = }")
print(f"{len(d3) = }")
del d3['red']
print(f"{len(d3) = }")

print(f"{d3['blue'] = }")
print(f"{d3.get('black') = }")
print(f"{d3.get('black', 100) = }")

print(f"{d3.setdefault('black', 44) = }")
print(f"{d3 = }")
print()

print(f"{d3.keys() = }")
print(f"{d3.values() = }")
print()

for color, value in d3.items():
    print(color, value)
print()

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

for code, city in airports.items():  #  [(code, city), (code, city), ...]
    print(code, city)




