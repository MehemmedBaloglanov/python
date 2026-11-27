#Boolean data type

print(7>4)
print(7==5)
print(1>7)

x = 18
y = 19
if x>y:
    print(x,"is greater than",y)
else:
    print(x,"is less than",y)


value1 = bool("python")
value2 = bool(7)
value3 =bool(["Lemon","Apple"])
value4 =bool(0)
value5 =bool("")
value6 =bool(None)
value7 =bool(())
value8 =bool([])
value9 =bool({})

print("bool('python')",value1 )
print("bool(7)",value2)
print("['Lemon','Apple')",value3)
print("bool(0)",value4)
print("bool("")",value5)
print("bool(None)",value6)
print("bool(())",value7)
print("bool([])",value8)
print("bool({})",value9)

def myFunction():
    return True

if myFunction():
    print("Yes")
else:
    print("No")