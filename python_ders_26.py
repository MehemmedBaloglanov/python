text = "   BMW     "

text2 = "Hello, Python"
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text2.translate(str.maketrans("P","T","o")))
print(text2.partition(","))

