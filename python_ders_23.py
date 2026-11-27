#String method and formatting types

text = "The price is only {price:.2f} turkish lira!"
text1 = "My name is {fname}, I'm {age} years old".format(fname = "Mehemmed",age =24 )#Formati bele de isledile biler
text2 = "My name is {0}, I'm {1} years old".format("Mehemmed",24 )#indeksleri verib yerlesdirir
text3 = "My name is {}, I'm {} years old".format("Mehemmed",24 )#indeksleri ardicil elave olunur
print(text1)
print(text2)
print(text3)
print(text.format(price = 70)) #verilen hisseye burdan melumat elave etmek ucun istifade edilir

text4 = "We do not have {:<10} children"
text5 = "We do not have {:>10} children"
text6 = "We do not have {:^10} children"
text7 = "We do not have {:=10} children"
text8 = "We do not have {:+10} children"
text9 = "We do not have {:-10} children"
text10= "The price is only {:f} turkish lira!"
x = float('inf')
text11= "The price is only {:F} turkish lira!"
text12= "The price is only {:g} turkish lira!"
text13= "The octal version is {:o}"#8 lik say sistemi
text14= "The hexadecimal version is {0:x} and {0:X}"#16 liq say sistemi
text15= "The price is only {:n} turkish lira!"
text16= "The price is only {:.0%} turkish lira!"


print(text4.format(7))
print(text5.format(7))
print(text6.format(7))
print(text7.format(-7))
print(text8.format(+7))
print(text9.format(-7))
print(text10.format(719.23233232))
print(text11.format(x))
print(text12.format(7))
print(text13.format(10))
print(text14.format(250))
print(text15.format(350))
print(text16.format(0.55))