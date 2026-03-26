a = (1, 7, 2)
print("Tuple:", a)

try:
    a[0] = 10  # trying to change
except TypeError as e:
    print("Error:", e)
    print("Proved: Tuple cannot be changed in Python!")
