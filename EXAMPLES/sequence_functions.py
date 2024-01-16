
colors = ["red", "blue", "green", "yellow", "brown", "black"]
months = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
)

nums = [800, 80, 1000, 32, -4, 255, -8, 400, 5, 5000]


print(f"colors: len is {len(colors)}; min is {min(colors)}; max is {max(colors)}")
print(f"months: len is {len(months)}; min is {min(months)}; max is {max(months)}")
print(f"nums: len is {len(nums)}; min is {min(nums)}; max is {max(nums)}")
print(f"{sum(nums) = }")

print()

print("sorted:", end=' ')
for m in sorted(colors):   # sorted() returns a sorted list
    print(m, end=' ')
print()

sorted_colors = sorted(colors)
print(f"{sorted_colors = }")


