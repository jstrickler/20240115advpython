value = 56

if value > 75:
    print("wombat")
    print("wallaby")
elif value > 50:  # else-if
    print("koala")
    print("kookaburra")
    print("kangaroo")
else:
    print("platypus")

print("ALL DONE")

# false values
# None 
# False
# X, if X is numeric and equal to 0
# X, if X has a length and len(X) is equal to 0

# everything else is True (......mostly)

DEBUG = True

color = "red" if DEBUG else "green"

#  color = DEBUG?"red":"green"   ternary operator

print(f"{color = }")

# relational
#  == != > < >= <=

# boolean
#  not and or

a = 23
b = 47

if (a < 30) and (b > 42):
    print('whoo-hooo')
else:
    print("boo-hoo")


















