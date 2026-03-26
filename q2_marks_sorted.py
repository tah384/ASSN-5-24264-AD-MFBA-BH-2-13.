marks = []
for i in range(6):
    m = int(input("Enter marks of student " + str(i+1) + ": "))
    marks.append(m)
marks.sort()
print("Sorted marks:", marks)
