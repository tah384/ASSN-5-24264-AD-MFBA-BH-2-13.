# Q1
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
n3 = float(input("Enter number 3: "))
n4 = float(input("Enter number 4: "))

greatest = n1
if n2 > greatest:
    greatest = n2
if n3 > greatest:
    greatest = n3
if n4 > greatest:
    greatest = n4

print("Greatest:", greatest)
