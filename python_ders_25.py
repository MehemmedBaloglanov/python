text = "l70234024wew_sx"

x = "\u0031"
y= "\u00B2"

print(x.isdigit())
print(y.isdigit())
print(text.isdigit())
print(text.isidentifier())# reqem herif ve "_" den ibaretdirse onda true olmalidir 
print(text.isnumeric())
print(text.isprintable())
print(text.isspace())# eger ancaq bosluqdan ibaretdirse onda true olur
print(text.istitle())#eger ki butun sozlerin 1 ci herifi boyukdurse onda true qayidir
Names = ("Mehemmed","Baloglanov","24","yas")
Names2 = {"surname":"Baloglanov","name":"Mehemmed"}
result = ",".join(Names)
seperator = ","
result2 = seperator.join(Names2["name"])
print(result)
print(result2)

cilek = "strawberry"
result3 = cilek.ljust(19)
result4 = cilek.rjust(19)
print(result3,"is my favorite fruit")


