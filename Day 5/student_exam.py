#A student will not be allowed to sit in exam if his/her attendance is less than 75%
#Take the input from user

total_classes = int(input("Enter number of classes held: "))
attended_classes = int(input("Enter number of classes attended: "))

attendance = (attended_classes / total_classes) * 100

print("Total attendance percentage :", attendance)

if attendance >= 75:
    print("You are eligible to sit for exams")
else:
    print("not eligible to sit for exams")