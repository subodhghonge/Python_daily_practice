cp = eval(input("Enter cost price: "))
sp = eval(input("Enter selling price: "))

if sp > cp:
    print("Profit:", sp-cp)
else:
    print("Loss:", cp-sp)