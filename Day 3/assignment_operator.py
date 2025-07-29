#Assignment Operator(=, +=, -=, *=, /=, //=, %=, **=)
a = 10
b = 20

a += b
print("After += operation, a =", a) #a = 30
b -= a
print("After -= operation, b =", b) #b = -10
a *= b
print("After *= operation, a =", a) #a = -300
b /= 10
print("After /= operation, b =", b) #b = -1.0
a //= 3
print("After //= operation, a =", a) #a = -100
b %= 3
print("After %= operation, b =", b) #b = 2.0
a **= 2
print("After **= operation, a =", a) #a = 10000
b = 2
print("Final value of b =", b) #b = 2

