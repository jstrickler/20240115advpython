from collections import Counter


with open('DATA/breakfast.txt') as file_in:
    all_foods = file_in.read().splitlines()   # split file on \n into lines
    food_count = Counter(all_foods)

print(f"{food_count = }")
print()

print(f"{food_count.most_common(4) = }")




