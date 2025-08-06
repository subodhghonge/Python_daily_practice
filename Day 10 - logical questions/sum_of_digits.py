#Sum of digits
n = int(input("Enter numbers: "))
sum = 0

length = len(str(n))

for i in range(length):
    a = n % 10
    sum = sum + a
    n = n // 10
print(sum)