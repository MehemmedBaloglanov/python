#String formatlama

age = 24
name = "Mehemmed"
price1 = 100

def get_VAT(price):
    return price*0.18;

text = "My name is {}, I am {}".format(name,age) #Index yazilmasa onda ardiciliqla elave edir
print(text)

text2 = "My name is {1}, I am {0}".format(name,age) #Index yazildigi ucun 1 yazilana age, 0 yazilana ise name yazir
print(text2)

text3 = f"My name is {name}, I am {age}" #f yazaraq birbasa variable oture bilerik
print(text3)

text4 = f"My name is {name}, I am {age}, I have {get_VAT(100)} $ VAT" #f yazaraq scoplarin icersisine funksiyalar da yaza bilerik
print(text4)


#-----------------------------------------------------------------------------------------------------
midterm_exam_score = input("Enter the midterm exam score:")
final_exam_score = input("Enter the final exam score:")
average_score = (float(midterm_exam_score)  + float(final_exam_score))/2
result = f"Your midterm exam score is {midterm_exam_score}\nYour final exam score is {final_exam_score}\nYour average score is {average_score}"
print(result)