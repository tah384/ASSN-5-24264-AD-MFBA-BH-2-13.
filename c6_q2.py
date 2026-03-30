# Q2
m1 = float(input("Marks in subject 1: "))
m2 = float(input("Marks in subject 2: "))
m3 = float(input("Marks in subject 3: "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

if percentage >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33:
    print("Pass")
else:
    print("Fail")
