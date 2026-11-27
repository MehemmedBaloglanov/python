#Character encoding and unicode code table

result = 'ç'.encode("utf-8")
#print(result)
#print(type(result))

text = "\x50\x79\x74\x6F\x6E" #Pyton sozunun ASCII kod ile yazilisidir
encode_text = text.encode("ascii")
decode_text = encode_text.decode()
print(encode_text)
print(decode_text)
print(type(encode_text))
print(type(decode_text))


text1 = "Şükrü"
#result1 = text1.encode(encoding="ascii",errors="strict")
result2 = text1.encode(encoding="ascii",errors="backslashreplace")
result3 = text1.encode(encoding="ascii",errors="ignore")
result4 = text1.encode(encoding="ascii",errors="namereplace")
result5 = text1.encode(encoding="ascii",errors="replace")
result6 = text1.encode(encoding="ascii",errors="xmlcharrefreplace")
result7 = text1.encode(encoding="utf-8")

#print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)