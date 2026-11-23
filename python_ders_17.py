#Escape characters

text = "  Python is \"doing\" well" #Eger ki "" ile yaratdigimiz stringde "" istifade etmek isteyirikse \ isaresinden istifade edilmelidir eynisi '' ucunde kecerlidir
print(text)

#  \' -> Single Quote
#  \\ -> Backslash
#  \n -> New Line
#  \r -> Carriage Return
#  \t -> Tab
#  \b -> Backspace
#  \ooo -> Octal value (8-lik say sistemi)
#  \xhh -> Hex value (16-liq say sistemi)

text1 = "Hello\rPy" # \r imleci en basa cekir. H->P e->y qalanlar yerinde qalir
print(text1) 

text2 = "Hello\bPy" # \b imleci bir character sola cekir. o->P qalanlar yerinde qalir.
print(text2)

text3 = "\120\171\164\150\157\156"; # Octal ededle
print(text3)

text4 = "\x50\x79\x74\x68\x6F\x6E"
print(text4)