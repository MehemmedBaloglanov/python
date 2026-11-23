#String functions

text = "Welcome to my world. How is it going?"

print(text.upper())#Hamisi boyuk
print(text.lower())#Hamisi kicik
print(text.capitalize())#Ancaq cumlenin 1 ci herifi boyuk
print(text.casefold())#Hamisi kicik edir. lowerle ferqi daha cox simvolu cevire bilir. Ikinci ferqi ise casefold daha yavas isleyir 
print(text.title())#Her sozun birinci heriflerini boyuk edir
print(text.swapcase())# Kicik herifleri boyuk, Boyuk herifleri kicik herife cevirir
print(text.islower()) #Butun herifler kicikdirse onda True qaytarir
print(text.isupper()) #Butun herifler boyukdurse onda True qaytarir
print(text.center(100,"*")) #Verilen stringi ortada saxlayir