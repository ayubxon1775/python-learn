# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 11:14:53 2025

@author: Админ
"""

# sana 23.11.2025

# print arifmetik amallar
import math

#print ('"Nexia", "Tiko", "Damas" ko\'rganlar havas qilar')

# 5 ning 4-darajasini toping
#print('5 ning 4-darajasi', 5**4)

# 22 ni 4 ga bolganda qancha qoldiq qoladi
#print('22 ni 4 ga bolsa', 22/4 ,'qoldiq chiqadi')

# tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
#print("tomonlari 125 ga teng kvadratning yuzi", 125*125, "perimetri", 125*4)

# diametri 12 teng bolgan doiraning yuzini toping
#print('diametri 12 teng bolgan doiraning yuzi', 3.14*(12/2)**2)

# Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping
#print("Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi", math.sqrt((6*6) + (7*7)))


# /////////////////

# O'zgaruvchilar

# ism = "Abdulloh"
# yosh = 25
# print(ism)
# ism = "Muhammad"
# print(ism)
# print(yosh)

# a = 6
# b = 7
# c = (a+b)**2
# print(c)

# "Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring
# text = "hello world!"
# print(text)

# xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.
# xabar = "bugun havo ochiq boldi"
# print(xabar)
# xabar = 'kechga borib yomg\'ir yog\'di'
# print(xabar)
# class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va konsolga chiqaring (siz kutgan natija chiqdimi?)
# class = "11-a"
# print(class)

# radius = 5
# pi = 3.14159
# aylana_yuzi = pi * radius**2
# print("Radiusi", radius, "ga teng aylananing yuzi=", aylana_yuzi)

# ////////////

# Matn bilan ishlash (string)

# ism = "Ayubxon"
# shahar = "Qoqon"
# viloyat = "Farg'ona"
# matn = "men yangi 📱 oldim"
# smayl = '😊'


# ism = "Ahmad"
# print("Mening ismim " + ism)

# ism = "Ahad"
# familya = "Qayum"
# print(ism + familya)
# print(ism +' '+ familya)


# ism = "Ahad"
# familya = "Qayum"
# ism_sharif = f"{ism} {familya}"
# print(ism_sharif)

# ism = "James"
# familya = "Bond"
# print(f'Salom mening ismim {familya}. {ism} {familya}')

# print("hello \tworld")

# print("hello \nworld")

# ism = "james"
# familya = "bond"
# ism_sharif = f"{ism} {familya}"
# ism_sharif = ism_sharif.upper()

# print(ism_sharif.lower())
# print(ism_sharif.title())
# print(ism_sharif.capitalize())

# meva = "    olma      "
# print('men ' + meva.lstrip()+ "yaxshi ko'raman")
# print('men ' + meva.rstrip()+ " yaxshi ko'raman")
# print('men ' + meva.strip()+ " yaxshi ko'raman")


# ism = input("ismingizni kiriting ")
# print("Assalomu aleykum " + ism.title())

# kocha = input("qaysi ko'chada turasiz ")
# mahalla = input('qaysi mahallada turasiz ')
# tuman = input("qaysi tumanda turasiz ")
# viloyat = input("qaysi viloyatdansiz ")
# manzil = (f"{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati")
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.title())
# print(manzil.capitalize())


#/////////////

#sonlar

 
# a = 20
# b = 2.2
# temp = 36.6
# print(type(a))
# aholi_soni = 7_594_376_567
# print("aholi soni", aholi_soni)

# x, y, z = 10, 5.5, -56

# c = a*b

# d = 100//2

# radius = 20
# PI = 3.14159
# diametr = 2*radius
# print("aylana uzunligi", PI*diametr)

# ism = "Jobir"
# yosh = 36
# xabar = ism + " " + str(yosh) + " yoshda"
# print(xabar)

# t_yil = int(input("Tugilgan yilingizni kiriting "))
# yosh = 2025 - t_yil
# print("siz", yosh, "yoshda ekansiz")


# a = int("10")
# b = float("10")
# temp = str(36.6)

# son = int(input("istalgan sonni kiriting "))

# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur

# kvadrat = son**2
# kub = son**3
# print(f'{son} ning kvadrati {kvadrat} ga teng')
# print(f'{son} ning kubi {kub} ga teng')


# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur

# age = int(input("yoshingiz nechchida "))

# t_yil = 2025 - age

# print(f"Siz {t_yil} da tug'ilgansiz")

# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

# a = int(input("birinchi sonni kiriting \n>>> "))
# b = int(input("ikkinchi sonni kiriting \n>>> "))

# print(f'{a} + {b} = {a+b}')
# print(f'{a} - {b} = {a-b}')
# print(f'{a} * {b} = {a*b}')
# print(f'{a} / {b} = {a/b}')

#  lists (Royhatlar)

# mevalar = ['olma', 'anjir', 'shaftoli', 'orik']
# narhlar = [12000, 18000, 10900, 22000]
# sonlar = ['bir', 'ikki', 3, 4, 5]
# ismlar = []

# print('birinchi meva', mevalar[0])
# hayvonlar = ["it", "mushuk", 'sigir', "qoy", "quyon", "mushuk"]

# bozorlik = ["yog", "un", "piyoz", "banan", "gosht"]

# mahsulot = bozorlik.pop(3)

# print(f"men {mahsulot} sotib oldim")
# print(f"sotib olinmagan mahsulot: {bozorlik}")

# ismlar = ["Abdulbosit", "Akramjon", "Abdushohid"]

# print(f'Salom {ismlar[0]} dostim boringa shukur')
# print(f'Salom {ismlar[1]} dostim bugun korishaylik')
# print(f"Salom {ismlar[2]} men pythonni o'rganyapman. Agar sen bu habarni o'qigan bo'lsang demak sen hali ham IT sohasidasan.")

# sonlar = [12, 35, 5.5, -15, -15.5]
# print(sonlar[0] + 15)
# print(sonlar[1] - 35)
# print(sonlar[2] + 15)
# print(sonlar[3] + 15)
# print(sonlar[4] + 15)

# t_shaxslar = ["Muhammad SAV", "Abubakr Siddiq", "Abdulhamid" ]
# z_shaxslar = ["Muhammad Avvoma", "Arshad Madaniy", "Taqiy Usmoniy"]

# print(f"Men tarixiy insonlardan {t_shaxslar.pop(0)} bilan Zamonaviy shaxslardan esa {z_shaxslar.pop(2)} bilan suhbat qilishni istar edim")

# friends = []

# friends.append("Abdulbosit")
# friends.append("Akramjon")
# friends.append("Abdurrohman")
# friends.append("Abdushohid")
# friends.append("Abdulloh")

# friends.remove("Abdurrohman")
# friends.insert(0, "Musoxon")
# friends.insert(2, "Mutalli")
# friends.insert(-1, "shoh")

# print(friends)

# mehmonlar = []
# mehmonlar.append(friends.pop(3))
# mehmonlar.append(friends.pop(2))
# mehmonlar.append(friends.pop(1))
# print(f"kelgan mehmonlar {mehmonlar}")

# ////////////////////

# listlar bilan ishlash

# cars = ["Audi", "Bmw", "mercedes benz", "volvo", "general motors", "tayoto"]

# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print(f"eng arzon narh {arzon}. eng qimmat narh {qimmat}. jami summa {jami}")

# toys = ("bus", "car", "bear", "dino", "snake", "lizard")

# davlatlar = ["O'zbekiston", "Rossiya", "AQSh", "Saudia Arabia"]
# print(davlatlar)
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)
# sonlar=list(range(120, 1200, 2))
# print(sonlar)
# yigindi = sum(sonlar)
# print(f'sonlarning yigindisi {yigindi} boladi')
# eng_kichik = min(sonlar)
# eng_katta = max(sonlar)
# print(f'sonlardagi eng katta son va eng kichik sonni ayirmasi {eng_katta-eng_kichik} boladi')
# print(len(sonlar))
# print(sonlar[:20])
# print(sonlar[-20:])
# print(sonlar[530:550])

# taomlar=["osh", 'shashlik', 'shorva', 'manti', 'somsa']
# nonushta = taomlar[:]
# del(nonushta[1:5])
# nonushta.append('mastava')
# nonushta.append('bilinchi')
# print(taomlar)
# print(nonushta)
# nonushta = tuple(nonushta)
# nonushta[0] = "qaymoq va non"

# //////////////

# for

# mehmonlar = ['ali', 'vali', 'hasan', 'husan', 'olim']

# for mehmon in mehmonlar:
#     print(f'Hurmatli {mehmon} sizni 20-dekabr kuni nahorgi oshga taklif qilamiz')
#     print(f'hurmat bilan palonchiyevlar oilasi')

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f'{son} ning kvadrati {son**2} ga teng')
    
# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
    
# print(sonlar)
# print(sonlar_kvadrati)

# dostlar = []
# print("dostingizni ismini kiriting")

# for n in range(5):
#     dostlar.append(input(f'{n+1}-dostingizni ismini kiriting \n >>>> '))
# print(dostlar)

# vazifa

# ismlar = ["abdulbosit", "akram", 'abdurrohman', 'akramjon', 'abdushohid', 'ayubxon']

# for ism in ismlar:
#     print(f'{ism} dostim boringa shukr')
# print(f'kod {len(ismlar)} marta takrorlandi')


# for n in range(11, 100, 2):
#     print(n)
#     print(n**3)

# kinolar = []
# print("5 ta eng sevimli kinoni kiting")
# for kino in range(5):
#     kinolar.append(input(f'{kino+1}-kino nomi \n >>> '))
# print(kinolar)

# people = int(input("bugun nechta odam bilan suhbatlashdingiz "))
# ismlar =[]

# for n in range(people):
#     ismlar.append(input(f'{n+1}-suhbat qilgan odamingiz kim '))
# print(ismlar)

# /////////////

# if else

# avtolar = ["audi", 'bmw', 'volvo', 'hyundai']

# for avto in avtolar:
#     if avto == "bmw":
#         print(avto.upper())
#     else:
#         print(avto.title())
        

# ism = "Ali"

# ism.lower() == "ali"


# ism = input("Ismingiz nima \n >>> ")
# if ism.lower() != 'ali':
#     print(f'uzr, {ism.title()} biz Alini kutyapmiz')
# else:
#     print('Salom, Ali')

# javob = float(input('12*6 nechchiga teng \n >>> '))
# if javob != 72:
#     print("javob hato")


# yosh = int(input("Yoshingizni kiriting \n >>> "))
# if yosh >= 18:
#     print("Hush kelibsiz")
# else:
#     print("mumkin emas")
    
# login = input("Yangi login tanlang:")
# if len(login) <= 5:
#     print("login 5 ta harfdan koproq bolishi shart")


# yil = int(input('tugilgan yilingizni kiriting: \n >>> '))
# if 2025-yil<18:
#     print(f'yoshingiz {2025-yil} da ekan')
#     print('kirish mumkin emas')
# else:
#     print("hush kelibsiz")

# yosh = int(input('yoshingiz nechchida >>>'))
# if yosh>65: print("siz covid 19 risk guruhida ekansiz")

# x, y = 25, 50
# print("x > y") if x>y else print('x<y')

# cars = ['toyoto', 'mazda', 'hyundai', 'gm', 'kia']

# for car in cars:
#     if car == "gm":
#         print(car.upper())
#     else:
#         print(car.title())
        

# for car in cars:
#     if car != "gm":
#         print(car.title())
#     else:
#         print(car.upper())

# login = input("loginni kiriting \n >>>")
# if login.lower() == "admin":
#     print("foydalanuvchilar ro'yxatini ko'rasizmi")
# else:
#     print(f"hush kelibsiz {login.title()}")


# son1 = int(input("1-sonni kiriting "))
# son2 = int(input("2-sonni kiriting "))
# if son1 == son2:
#    print('ikki son teng')

# son = int(input("son kiriting "))
# print("son musbat") if son > 0 else print("son manfiy")


# son = float(input("son kiritng: "))
# print(f'{son} sonning ildizi {son ** (1/2)}') if son > 0 else print("musbat son kiting")

# //////////

#  if elif else


# yosh = int(input('yoshingizni kiriting '))
# if yosh <= 4:
#     narh = 0
# elif yosh <= 12:
#     narh = 5000
# elif yosh <= 18:
#     narh = 8000
# else:
#     narh = 10000
# print(f'sizga kirish {narh} som')
    

# kun = input("bugun qanday kun? >>>")
# if kun.lower()=='shanba' or kun.lower() =='yakshanba':
#     print('dam olish kuni')
# else:
#     print('bugun ish kuni')


# kun = input("bugun qanday kun >>> ")
# harorat = float(input('bugun harorat qanday >>> '))

# if (kun.lower()=='yakshanba' or kun.lower() =="shanba") and harorat>=30:
#     print('ketdik chomilishga boramiz')
# elif (kun.lower()=='yakshanba' or kun.lower() =="shanba") and harorat<30:
#     print('bugun chomilishga bormaymiz')
    
# narh = 15000
# choy = True
# salat = True

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000

# print(f'Jami {narh} som')   


# narh = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assort = 0

# if choy:
#     print('mijoz choy sotib oldi')
#     narh = narh + 3000

# if salat:
#     print('mijoz salat sotib oldi')
#     narh = narh + 5000

# if non:
#     print('mijoz non sotib oldi')
#     narh = narh + 2000

# if kompot:
#     print('mijoz kompot sotib oldi')
#     narh = narh + 5000

# if assort:
#     print('mijoz assort sotib oldi')
#     narh = narh + 15000

# print(f'Jami {narh} boldi')

# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# 'manti' in menu

# ovqat = input('Nima ovqat buyurasiz \n >>> ')
# if ovqat.lower() in menu:
#     print("buyurtmangiz qabul qilindi")
# else:
#     print('bunday taom bizda yoq')


# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f'menuda {taom} bor')
#     else:
#         print(f'kechirasiz menuda {taom} yoq')

# son = int(input('juft son kiriting: '))
# if son % 2 == 0:
#     print('Rahmat')
# else:
#     print('bu son juft emas')



# age = int(input('yoshingizni kiriting '))
# if age <= 4 or age >= 60:
#     print('sizga muzeyga kirish bepul')
# elif age <= 18:
#     print('sizga muzeyga kirish 10000 som')
# elif age > 18:
#     print('sizga muzeyga kirish 20000 som')



# son1 = float(input('1-sonni kiriting '))
# son2 = float(input('2-sonni kiriting '))
# if son1 == son2:
#     print(f'{son1}={son2}')
# elif son1 > son2:
#     print(f'{son1}>{son2}')
# else:
#     print(f'{son1}<{son2}')    
    


    
# bozor = ['piyoz', 'karam', 'sabzi', 'kartoshka', 'shalgom', 'balgar', 'bodring', 'pomidor', 'sarimsoq', 'joxori']
# mahsulotlar = []


# for n in range(5):
#     mahsulotlar.append(input(f"Savatga {n+1}-mahsulotni kiriting "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in mahsulotlar:
#     if mahsulot in bozor:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
        
# if mavjud_emas:
#     print(f'dokonimizda quyidagi mahsulotlar yoq:')
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print('siz soragan mahsulotlar dokonda bor')


   
# users = ['ayyubiy', 'ayyub', 'djigar', 'polohmon', 'ikrom']

# login = input("yangi login tanglang ")

# if login in users:
#     print('login band yangi login tanglang')        
# else:
#     print(f'Hush kelibsiz, {login.title()}')



# son = int(input('butun son kiriting '))

# for n in range(2,11):
#     if not (son%n):
#         print(f'{son} soni {n} ga qoldiqsiz bolinadi')

    
# /////////////////////

#  SintaxError

# print ("Hello world")
# for n in range(10): 
#   print(n)
#   print(n+1)
    
# son = int(input("Istalgan sonni kiriting"))
# print(f'{son} ning kvadrati {son**2} ga teng')   
    
    
    
    
    
    
    
    
    
    