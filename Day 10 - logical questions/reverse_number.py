n = int(input("Enter numbers: "))

temp = n
reverse = 0

length = len(str(n))

for i in range(length):
    length = n % 10
    reverse = reverse * 10 + length
    n //= 10
print(reverse)

#or

n = 1234
r = 0

while n > 0:
    a = n%10
    r = r % 10 + a
    n = n // 10

print(r)