import sys
import alpha.mathlib.geometry as geometry  #  load geometry.py and run the code

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)
print()
# 1. current folder
# 2. folders in PYTHONPATH
# 3. folders in sys.prefix/lib

for path in sys.path:
    print(path)