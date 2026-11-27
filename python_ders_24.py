#String method and formatting types

text = "The temperature is between {: } and {: } degress celsius"
text1 = "The universe is {:,} years old"
text2 = "The universe is {:_} years old"
text3 = "The binary version of {0} is {0:b}"
text4 = "The unicode version of {0} is {0:c}"
text5 = "We have {:d} lesson"
text6 = "We have {:e} lesson"
text7 = "We have {:E} lesson"



print(text.format(-4,5))
print(text1.format(1390000000))
print(text2.format(1390000000))
print(text3.format(6))
print(text4.format(199))
print(text5.format(0b101))
print(text6.format(7))
print(text7.format(7))

