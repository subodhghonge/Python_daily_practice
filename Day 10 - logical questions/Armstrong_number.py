n = int(input("Enter numbers: "))
temp = n
sum = 0
power = len(str(n))

for i in range(n):
    a = n % 10
    sum = sum + (a**power)
    n = n // 10
print(sum)

if (temp == sum):
    print("Armstrong")
else:
    print("Not Armstrong")