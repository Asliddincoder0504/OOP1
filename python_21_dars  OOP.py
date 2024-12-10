#1-MASALA
# Oson1. "Oson1" nomli klass elon qiling. Bu klassda "a" integer o'zgaruvchi bor.
# output_a() - bu funksiya klassdagi "a" ni qiymatini print qilsin.


# class Oson1:
#     a=4
#     def output(cls):
#         print(cls.a)
# Oson1.output(Oson1)


#2-MASALA.Oson2. "Oson2" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchilari bor.
# summa() - bu funksiya klassdagi "a" va "b" ni yig'indisini print qilsin.


# class Oson2:
#     a=5
#     b=6
#     def summa(cls):
#         print(cls.a+cls.b)
# Oson2.summa(Oson2)


#3-MASALA.Oson3. "Oson3" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchisi bor.
# plus_minus() - bu funksiya klassdagi "a" ni musbat yoki manfiy ekanligini print qilsin.

# class Oson3:
#     a=-3
#     def plus_minus(self):
#         if self.a>0:
#             print(f"{self.a}  Musbat son")
#         elif self.a<0:
#             print(f"{self.a}  Manfiy son")
#         else:
#             print("Son nolga teng")
# Oson3.plus_minus(Oson3)


#4-MASALA.Oson4. "Oson4" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchi bor.
# odd_even() - bu funksiya klassdagi "a" ni to'g yoki juft ekanligini print qilib bersin.
# class Oson4:
#     a=7
#     def odd_even(self):
#         if self.a%2==0:
#             print(f" {self.a}  Juft son")
#         elif self.a%2!=0:
#             print(f" {self.a}  toq son")
# Oson4.odd_even(Oson4)


#5-MASALA.Oson5. "Oson5" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchisi bor.
# daraja() - bu funksiya klassdagi "a" ni "b" chi darajasini print qilsin.
# class Oson5:
#     a=7
#     b=5
#     def daraja(self):
#         natija=self.a**self.b
#         print(f"{self.a} ning darajasi {self.b}  {natija}")
# Oson5.daraja(Oson5)


#6-MASALA."MyClass6" nomli klass elon qililar. Bu klassda "words" list bo'sh o'zgaruvchisi bor.
# add_word(word) - bu funksiya "words" ga element qo'shib qo'ysin.
# remove(word) = bu funksiya "words" da "word" ni o'chirib tashlasin.

# class Myclass6:
#     def __init__(self):
#         self.words=[]
#
#     def add_word(self,word):
#         self.words.append(word)
#         print(f" {word }  so'zlar  ro'yxatiga  qo'shildi.Hozirgi  ro'yxat  {self.words}")
#
#     def remove_word(self,word):
#         self.words.remove(word)
#         print(f"{word}  so'zlar ro'yxaridan  o'chirildi  {self.words}")
# sozlar=Myclass6()
# sozlar.add_word("salom")
# sozlar.add_word(5)
#
# sozlar.remove_word(5)


#7-MASALA."MyClass7" nomli klass elon qiling. Bu klassda bo'sh "myDict" dictionary o'zgaruvchisi bor.
# add_elem(key, val) - bu funksiya "myDict" "key" ni qiymatiga teng bo'lgan key bo'lmasa "val" ni add qilsin,
# bor bolsa xech narsa qilmasin.
# update_elem(key, val) - bu funksiya "myDict" shu "key" ni qiymatiga teng bolgan key bo'lsa "val" ni update qilsin,
# yoq bolsa xech narsa qilmasin.

#
# class Myclass7:
#     def __init__(self):
#         self.myDict={}

#     def add_elem(self,key,val):
#         if key not in self.myDict:
#             self.myDict[key]=val
#             print(f"{key} qo'shildi : {val}")
#         else:
#             print(f"{key} oldindan mavjud")
#     def update_elem(self,key,val):
#         if key in self.myDict:
#             self.myDict[key]=val
#             print(f"{key } yangilandi: {val}")
#         else:
#             print(f"{key }  o'zgarmaydi")
#
# lugat=Myclass7()
# lugat.add_elem(5,"salom")
# lugat.add_elem(5,"alik")
#
# lugat.update_elem(5,"nima gaplar")


#8-MASALA."MyClass8" nomli klass elon qililar. Bu klassdan "numbers" list o'zgaruvchisi bor.
# compare_lists(new_list) - bu funksiya klassdagi "numbers" ni elementlar yig'indisi
# "new_list" ni elementlar yig'indisidan kattaligini aniqlab katta listni print qilsin.
#
# class MyClass8:
#     numbers = []
#
#     def compare_lists(self, new_list):
#         if sum(self.numbers) < sum(new_list):
#             print(new_list)
#         else:
#             print(self.numbers)
#
# lst = [7, 2, 3, 4]
# MyClass8.compare_lists(MyClass8,lst)


#9-MASALA. "MyClass9" nomli klass elon qililar. Bu klassdan "list1" va "list2" list o'zgaruvchilari bor.
# list1_max() - bu funksiya klassdagi "list1" dan maximumni topib return qilsin.
# list2_max() - bu funksiya klassdagi "list2" dan maximumni topib return qilsin.
# sum_of_two_max() - bu funksiya klassdagi list1_max() va list2_max() foydalanib ikkita maximumni topib yig'indisini print qilsin.


#
# class Myclass9:
#         list1=[2,5,6,5,3]
#         list2=[5,4,7,8,4]
#
#         def list1_max(self):
#             max_elem1=max(self.list1)
#             return max_elem1
#
#         def list2_max(self):
#             max_elem2=max(self.list2)
#             return max_elem2
#
#         def sum_of_two_max(self):
#             yigindi=self.list1_max(Myclass9)+self.list2_max(Myclass9)
#             print(f"list1_max va list2_max  yig'indisi   {yigindi}")
# Myclass9.sum_of_two_max(Myclass9)




#10-MASALA."MyClass10" nomli klass elon qililar. Bu klass "numbers" list o'zgaruvchilari bor.
# divide(d) - bu funksiya klassadagi "numbers" list elementlarini "d" qoldiqsiz bo'linsa bitta list yig'sin funksiyani ichida.
# va funksiya oxirida bolinadigonlarni listini return qilsin.

# class Myclaas10:
#     numbers=[23,40,8,55,45,60]
#
#     def divide(self,d):
#         bolinma = [num for num in self.numbers if num % d == 0]
#
#         return bolinma
# son=Myclaas10()
# d=10
# natija=son.divide(d)
# print(f"   Numbers   ro'yxatidagi  d ga qoldiqsiz  bo'linadigan sonlar:  {natija}")

