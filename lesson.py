import sys  
#Burda esasen bosluqlara baxdiq yeni ki python iceri girintilere gore isleyir 
if 7>3: 
    print('7 is greater then 3')
    print("None of your business")

#Commentler "#" isaresi ile qoyulur



#-------------------------------Variable 


#Burda variablelara baxdiq.Pythonda variable yazanda onun tipini vermeye ehtiyac yoxdur ozu arxada tamamlayir
x=7
y="python"

m ='12'
print(x)
print(y)
print(m)

#Variable casting
#Variable castinge baxdiq 
a = str(7)
b = int(7)
c= float(7)


print(a)
print(b)
print(c)

#variable get the type
#type() methodu ile deyiskenin tipini almaq olur ona baxdiq 
d = 7
e = "mehemmed"
f= 'cls'
m = 5.7

print(type(d))
print(type(e))
print(type(f))
print(type(m))

#Variable case sensitive 
#Burda variable namelerin case sensitive oldugunu gorduk yeni ki eger ki ferqli formatda yazsaq ayri ayri deyisken sayilir.
name = "Mehemmed";

NaMe = "Baloglanov"


# Her ikisi ferqli variabledir 
print(name)
print(NaMe)

#variable names
xt=7
age=23
toplam_hacim = 100

#name ya '_' ya da herifle baslaya bilir. Ummen adlandirma reqem herif ve "_" bundan ibaret ola biler
_name  = "Mehemmed"
#2name = "Mehemmed" reqem ile baslaya bilmez

myFullName = "mehemmed Baloglanov" #CamelCase

MyFullName = "Mehemmed Baloglanov" #PaskalCase

my_full_name = "Mehemmed Baloglanov" # SnakeCase

o,p,w  = 'o',9,'w' #toplu sekilde variablea deyer menimsetmek ucundur 

k=pd=l="mehemmed1"

print(k)
print(pd)
print(l)

print(o)
print(p)
print(w)

print(myFullName)
print(MyFullName)
print(my_full_name)
print(_name)
print(name)


#variable unpacking

colors  = ["red","black","blue"]

red,black,blue = colors #colors da olan rengleri ardicil olaraq variablelara assign edir

print(red)
print(black)
print(blue)


#output variables

text1 = "Python "
text2 ="is wonderful"

kj = 4
kl = "python"
print(text1,text2)
print(text1+text2)
#print(kj+kl) #burda error atacaq int ve str ni yaza bilmessen
print(kj,kl) # bu isleyir yan yana yazir

#global variables- bir funksiyanin xaricinde yaradilan variable -a deyilir. Hem funtion icin de hemde xaricinde istifade edile biler

global_variables = "marvellous" #Global variable 

def myFunction():
    global_variables = "local" #Local variable 
    local_variable  = "local variable"
    global local_variable2 #global keyword ile local variable-i globala cevirmek mumkundur
    local_variable2 = "global local variable"
    print("Python is " + global_variables) #output---->Python is local

myFunction()
print("Python is " + global_variables) #output--->Python is marvellous
#print("Local variable calling " + local_variable) burda xeta atir cunki funksiyanin icinde olan deyeri funksiyanin xaricinden cagirmaga calisiriq
print("Calling global local variables " + local_variable2)


#why variables

number  = 7
print(number)
number = 19
print(number)

number = number +2
print(number)

#Data types
#Text type--> str 
#Numeric type --> int,float,complex  
#Sequence type --> list, tuple, range
#Mapping type --> dict
#Set type --> set, frozenset
#Boolean type --> bool
#Binary type --> bytes, bytearray, memoryview
#None type --> NoneType

text_type = "Mehemmed"
int_type = 12
float_type = 12.6
complex_type = 5j
list_type = ["mehemmed","seid","sahib","elvin"]
tuple_type = ("mehemmed","seid","sahib","elvin") #List ile arasindaki ferq deyisdirilenmir. Deyisdirmek ucun liste cevirmek lazimdir
list(tuple_type) 
range_type = range(7) # 0,1,2,3,4,5,6 deyerleri olan bir list yaradir
print(*range_type)
dict_type = {"key":"value", "name":"Mehemmed"} #map kimi key value ile isleyir
set_type = {"Mehemmed","Mehemmed","Baloglanov"} #Her deyerden 1 dene saxlayir
print(set_type)
frozenset_type = frozenset({"Mehemmed","Mehemmed","Baloglanov"})
print(frozenset_type)
print(type(frozenset_type))
bool_type = True
noneType = None # null menasini verir
print(sys.getsizeof(int_type))
bytes_type = b"python" #bu ASCII kod cedvelindeki herifleri destekleyir yeni ş ç ı ğ  kimi herifleri desteklemir
print(bytes_type)
bytes_type_az_herif = bytes("Ə","utf-8")
print(bytes_type_az_herif)
bytearray_type = bytearray([65]) #ASCII cedveldeki qarsiligini qaytarir
memoryview_type = memoryview(bytes(5))
print(memoryview_type)

#bir deyeri basqa bir data type cevirmek 
int_type1 = 12
text3 = str(int_type1)
print(type(text3)) #output str

#Yaratdigimiz deyerin istediyimiz data type olmasi
str_type = str(True)

complex_type1 = complex(6+5j)
print(complex_type1)

ustlu_int_deyer = 19E5
print(ustlu_int_deyer)

#-------------------------

PI= 3.15
#radius = float(input("Radius: "))
#sahe = PI*radius*radius
#print("SAHE: " , sahe)

#uzunluq = 2* PI * radius
#print("UZUNLUQ:",uzunluq)


#Random numbur
import random

#random.seed(7)
print(random.random())

state = random.getstate()

print(random.random())

random.setstate(state)

print(int(random.random()*100))

print(random.getrandbits(8))

print("=======================================================")

print(random.randrange(1,11,3))

print(random.randint(1,10))

my_List = ["Red","Blue","Orange"]

print(random.choice(my_List))

print(random.choices(my_List,weights=[4,1,1],k=10))

random.shuffle(my_List)
print(my_List)

print(random.sample(my_List,k=2))

print(random.uniform(20,40))

print(random.triangular(20,40,21))

print(random.betavariate(1,8))

print(random.expovariate(0.5))

print(random.gammavariate(1,8))

print(random.gauss(100,50))

print(random.lognormvariate(0,0.25))

print(random.normalvariate(100,50))

print(random.vonmisesvariate(0,5))

print(random.paretovariate(3))

print(random.weibullvariate(1,1.5))


#String class

print("String class")

print('String class')

#\ escape character
print('He is called \'big boy\'')

text = """ This is so good
           life is good
           I'm a variable
           multiline strings
"""

print(text)


cars = ["BMW","Volvo","Skoda","Nissan"]
print(cars[2])

#String is array
string_arr = "Hello, Python!"
print(string_arr[2])

string_loop = "Python is weird"
for x in string_loop:
    print(x)

length = len(string_loop)
print(length)

#in and not in command
in_command = "The best languages in life are free!"
search = "ede"
print(search in in_command)

if(search in in_command):
    print("in_command contains " + search)

if(search not in in_command):
    print("in_command not contains " + search)


#python dilimleme ve birlesdirme
string_dilimleme = "python is weird"
print(string_dilimleme[1:5])

print(string_dilimleme[:5])

print(string_dilimleme[5:])

print(string_dilimleme[-5:-1])

#String concatenation
string_1 = "Python"
string_2 = "is weird"

concat = string_1 + " " + string_2
print(concat)