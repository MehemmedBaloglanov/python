#String method

text = "Welcome to my world. My world is python"

print(text.count("world",11,22))#istifade edilen sozun sayini qaytarir, 11 ci indexsden basliyib 22 ye qeder axtarir. Eger onlari yazmasaq butun metnde axtarir
print(text.endswith("ond",8,15))#gosterilen ifade ile bitirmi onu axtarir. 8 ci indexsden 15 ci indexse qederki ifadeye baxir eger o gosterilen ifade ile baslayib ya da bitirse onda true qaytarir
print(text.startswith("Wel"))#gosterilen ifade ile baslayirmi onu axtarir
print(text.expandtabs())#tablerin olcusunu ayarlamaq ucundur
print(text.find("rl"))# axtarilan deyerin indexsini qaytarir
print(text.index("e"))#1 ci tapdigi indexsi qaytarir
print(text.isalnum())#alfanumerik sadece reqem ve heriflerden ibaret olmalidir. Bosluq ve ya diger karakterler olmali deyil
print(text.isalpha())#yalniz heriflerden ibaret olmalidir
print(text.isascii())#hamisi asciide varmi onu yoxlayir
print(text.isdecimal())#yalniz reqemlerden ibaret olarsa true olur

