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
    
# ///////////

#  Dictionary

# car_0 = {'model': 'ferrari', 'rang': 'qizil'}
# print(car_0['model'])
# print(car_0['rang'])    
    
# en_uz = {'apple': 'olma', 'apricot': 'o\'rik', 'banana': 'banan'}

# print(en_uz['apricot'])
    
# mevalar ={'olma': 10000, 'tarvuz': 8000, 'qovun': 10000}
# print(mevalar['olma'])
    

# talaba_0 = {'ism': 'murod olimov',\
#             'yosh': 25,\
#             't_yil': 2000\
#             }

# print(f'{talaba_0['ism']}, {talaba_0['t_yil']}-yilda tugilgan,\
#  {talaba_0['yosh']} yoshda')
 
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# talaba_0['ism'] = 'abdulloh'

# del talaba_0['yosh']
# print(talaba_0)


# telefonlar = {
#     'ali': 'iphone X',
#     'vali': 'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310',
#     'anvar': 'pixel 3xl' 
#     }

# # phone =telefonlar['ali']
# # print(f'alining telfoni {phone}')

# meva = en_uz.get('book', 'bunday meva mavjud emas')
# print(meva)

#  vazifa

# otam = {'ism': 'Yunusxon', 't_yil': '1979', 'shahri': 'namangan'}
# print(f'Otamning ismi {otam['ism']}, {otam['t_yil']} da \
# {otam['shahri']}da tugilgan')

# sev_taomlar = {'otam': 'manti', 'onam': 'shashlik', 'ukam': 'somsa',\
# 'singlim_1': 'lavash', 'singlim2': 'osh'}

# print(f'Otamning sevimli taomi {sev_taomlar['otam']}')
# print(f'Onamni sevimli taomi {sev_taomlar['onam']}')
# print(f'Ukamni sevimli taomi {sev_taomlar['ukam']}')
            
# python_lugat = {'integer': 'butun son','float': 'onlik son',\
# 'string': 'matn','if': 'agar','else': 'agarki', 'true': 'ha',\
#  'false': 'yoq'}

# soz = input('soz kiriting ')

# # print(python_lugat.get( soz, 'bunday soz mavjud emas'))

# result = python_lugat.get(soz)

# if result == None:
#     print('bunday soz mavjud emas')
# else:
#     print(f'{soz.title()} sozi {result} boladi')


# ////////////

# lugat bilan ishlash

# talaba_0 = {
#     'ism': 'alijon',
#     'familya': 'shamshiyev',
#     'yosh': 22,
#     'fakultet': 'matematika',
#     'kurs': 4
#     }

# print(talaba_0.items())
# for key, value in talaba_0.items():
#     print(f'kalit: {key}')
#     print(f'qiymat: {value} \n')  
    
# telefonlar = {
#     'ali': 'iphone x',
#     'vali': 'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310',
#     'ilhom': 'iphone x',
#     'adham': 'iphone x',
#     'nozim': 'galaxy s9',
#     }

# for key, value in telefonlar.items():
#     print(f'{key.title()} ning telefoni {value}')
    
# print(telefonlar.keys())  
    
# for key in telefonlar.keys():
#     print(f'{key}') 
    
    
    
# mahsulotlar = {
#     'olma': 10000,
#     'anor': 20000,
#     'uzum': 40000,
#     'anjir':25000,
#     'shaftoli': 30000
#     }

# for key in mahsulotlar.keys():
#     print(f'mahsulotlarning kaliti {key.title()}')

# print('Dokondagi mahsulotlar:')
# for mahsulot in mahsulotlar:
#     print(f'{mahsulot.title()}')
    
# bozorlik = ['anor', 'uzum', 'non', 'baliq']

# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}")
    
    
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f'iltimos dokonimizga {buyum} ham olib keling')
    

# print('Dokonimizdagi mahsulotlar')
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
# print('foydalanuvchilar quyidagi telefonlarni ishlatishadi')
# for tel in telefonlar.values():
#     print(tel)    
    
# for tel in set(telefonlar.values()):
#     print(tel)    
        
    
# toys = {'ball', 'car', 'lamp', 'ball'}    
    
# vazifa

# python_lugat = {
#     'integer': 'butun son',
#     'float': 'onlik son',
#     'string': 'matn',
#     'if': 'agar',
#     'else': 'agarki',
#     'true': 'ha',
#     'false': 'yoq',
#     'list': 'royxat',
#     'dictionary': 'lugat',
#     'for': 'sikl',
#     }

# print('lugatlar')
# for kalit in sorted(python_lugat):
#     print(f'{kalit} - {python_lugat[kalit]}')


# davlatlar = {
#     "o'zbekiston": "toshkent",
#     "aqsh": "washington",
#     "rossiya": "moskva",
#     "qozogiston": "ostona",
#     "saudiya": "jidda",
#     "qirg'iziston": "bishkek",
#     }


# print('Davlatlar royxatlar')
# for davlat in sorted(davlatlar):
#     print(davlat.upper())


# print('Poytaxtlar royxatlar')
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())

# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# capital = davlatlar.get(country)
# if capital == None:
#     print(f'bizdan bunday {dv_kirit} yoq')
# else:
#     print(f'{country} ning poytaxti {capital}' )


# ovqatlar = {
#     'osh': 25000,
#     'shashlik': 15000,
#     'shorva': 20000,
#     'manti':10000,
#     'somsa': 10000,
#     'lagmon': 25000,
#     'norin': 30000,
#     'salat': 8000,
#     'kabob': 22000,
#     'qotirma': 28000,
#     }
    
# print('3 taom buyurtma bering \n')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f'{n+1}-buyurtmani bering '))
    
# for buyurtma in buyurtmalar:
#     if buyurtma in ovqatlar:
#         print(f'{buyurtma.title()} ning narxi {ovqatlar[buyurtma]} som')
#     else:
#         print(f'{buyurtma} bunday taom bizda yoq')
            

#  //////////////

# nesting

# car0 = {
#         'model': 'lacetti',
#         'rang': 'oq',
#         'yil': 2018,
#         'narh': 13000,
#         'km': 50000,
#         'karobka': 'avtomat'
#         }
    
# car1 = {
#         'model': 'nexia 3',
#         'rang': 'qora',
#         'yil': 2015,
#         'narh': 9000,
#         'km': 89000,
#         'karobka': 'mehanika'
#         } 
    
# car2 = {
#         'model': 'gentra',
#         'rang': 'qizil',
#         'yil': 2019,
#         'narh': 15000,
#         'km': 20000,
#         'karobka': 'mehanika'
#         }  



# cars = [car0, car1, car2]
# for car in cars:
#     print(f'{car['model'].title()}, '
#           f'{car['rang']} rang, '
#           f'{car['yil']}-yil, {car['narh']} $'
#           ) 

# print(f'{cars[0]['model']}',
#       f'{cars[0]['rang']}'
#       )


# malibus = []
# for n in range(10):
#     new_car = {
#                'model': 'malibu',
#                'rang': None,
#                'yil': 2025,
#                'narh': None,
#                'km': 0,
#                'karobka': 'avtomat' 
#         }
#     malibus.append(new_car)

# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'
    
# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'    
    
# for malibu in malibus[6:]:
#     malibu['rang'] = 'qora'
#     malibu['karobka'] = 'mexanika'


# for malibu in malibus:
#     if malibu['karobka'] == 'avto':
#         malibu['narh'] = 40000
#     else:
#         malibu['narh'] = 35000

# for malibu in malibus:
#     print(malibu)

# dasturchilar = {
#     'ali': ['python', 'c++'],
#     'vali': ['html', 'css', 'js'],
#     'hasan': ['php', 'sql'],
#     'husan': ['python', 'php'],
#     'maryam': ['c++', 'c#']
#     }

# for ism, tillar in dasturchilar.items():
#     print(f'\n{ism.title()} quyidagi tillarni biladi')
#     for til in tillar:
#         print(f'{til.upper()} ', end='')


# hamkasblar = {
#     'ali': {'familiya': 'valiyev',
#             't_yil': 1995,
#             'malumot': 'oliy',
#             'tillar': ['python', 'c++']
#             },
    
#     'vali': {'familiya': 'aliyev',
#             't_yil': 2001,
#             'malumot': 'orta maxsus',
#             'tillar': ['html', 'css', 'js']
#             },
                       
#     'hasan': {'familiya': 'husanov',
#             't_yil': 1999,
#             'malumot': 'maxsus',
#             'tillar': ['python', 'php']
#             }
#     }


# for ism, info in hamkasblar.items():
#     print(f'\n{ism.title()} {info['familiya'].title()}, '
#           f'{info['t_yil']}-yilda tugilgan.\n'
#           f'Malumoti: {info['malumot']}.\n'
#           "Quyidagi dasturlash tillarini biladi"
#           )
#     for til in info['tillar']:
#         print(til)


# vazifa

# buxoriy = {
#         'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
#         't_yil': 810,
#         'manzil': "Buxoro",
#         'yosh': 60,
#         'asarlar': ["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#         }
    
# qodiriy = {
#         'ism': 'Abdulla Qodoriy',
#         't_yil': 1894,
#         'manzil': "Toshkent",
#         'yosh': 44,
#         'asarlar': ["O'tkan kunlar","Mehrobdan Chayon","Obid ketmon"],
#         }
    
# vohidov = {
#        'ism': 'Erkin Vohidov',
#        't_yil': 1936,
#        'manzil': "Farg'ona",
#        'yosh': 80,
#        'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"],
#         }

# navoiy = {
#         'ism': 'Alisher Navoiy',
#         't_yil': 1441,
#         'manzil': "Xirot",
#         'yosh': 60,
#         'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#         }      


# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"\n{ism} ning mashxur asarlari: ")
#     for asar in asarlar:
#         print(asar)
        
        
# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }


# for key, values in kinolar.items():
#     print(f'\n{key.title()}ning sevimli kinosi')
#     for value in values:
#         print(f'{value}')

          
# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }     

# for davlat, malumot in davlatlar.items():
#     print(f'{davlat.title()}ning poytaxti {malumot['poytaxt']} ' ,
#           f'Hududi {malumot['maydon']} '
#           f'Aholisi {malumot['aholi']} '
#           f'Pul birligi {malumot['pul birligi']}'
#           )

# foy_davlat = input('qaysi davlatni malumoti kerak ')

# if foy_davlat in davlatlar:
#     info = davlatlar[foy_davlat]
#     print(f'{foy_davlat.title()}ning poytaxti {info['poytaxt']} ' ,
#           f'Hududi {info['maydon']} '
#           f'Aholisi {info['aholi']} '
#           f'Pul birligi {info['pul birligi']}'
#           )
# else:
#     print('bizda bunday davlat yoq')        
# 

# ////////////


# input() va while

# ism = input('Ismingizni kiriting ')
# savol = f'Salom, {ism.title()}. Yoshingiz nechchida '
# yosh = input(savol)
# yosh = int(yosh)
# height = input('Boyingiz necha metr ')
# height = float(height)


# son = 1
# while son <=5:
#     print(son, end=" ")
#     son += 1

# print('dastur tugadi')

# print('Kiritilgan sonning kvadratini qaytaruvchi dastur')
# savol = 'Istalgan son kiriting'
# savol += "(dasturni toxtatish uchun 'exit' deb yozing ): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('dastur tugadi')


# print('Kiritilgan sonning kvadratini qaytaruvchi dastur')
# savol = 'Istalgan son kiriting'
# savol += "(dasturni toxtatish uchun 'exit' deb yozing ): "

# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print('dastur toxtadi')


# print('Kiritilgan sonning kvadratini qaytaruvchi dastur')
# savol = 'Istalgan son kiriting'
# savol += "(dasturni toxtatish uchun 'exit' deb yozing ): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)

# print('dastur toxtadi')    

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f'{son} ning kvadrati {son**2} ga teng')


# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f'{son} ning kvadrati {son**2} ga teng')


# son = 0
# while son < 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)

# son = 0
# while son < 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)


# son = 0
# while son < 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)

# son = 0
# while son < 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)


# vazifa


# kitob = "yoqtirgan kitoblarni kiriting "
# kitob += "dasturni toxtatish uchun 'exit' deb yozing "

# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(kitob)
# print('dastur tugadi')
        
  
# age = ('yoshingizni kiriting ')
# age += ('dasturni toxtatish uchun "quit" deb yozing ')
# age_result= ''

# while age_result != 'exit':
#     age_result = int(input(age))
#     if age_result <= 7:
#         print('chipta narxi 2000 som')
#     elif age_result > 7 and age_result <= 18:
#         print('chipta narxi 3000 som')
#     elif age_result > 18 and age_result < 65:
#         print('chipta narxi 10000 som')
#     else:
#         print('chipta bepul')


# age = 'Yoshingizni kiriting '

# while True:
#     qiymat = input(age)
#     if qiymat == 'exit' or qiymat == 'stop':
#         break
#     yosh = int(qiymat)
    
#     if yosh < 7:
#         narh = 2000
#     elif 7 <= yosh < 18:
#         narh = 3000
#     elif 18 <= yosh < 65:
#         narh = 10000
#     else: narh = 0
    
#     if narh ==0:
#         print('Sizga bepul')
#     else:
#         print(f'chiptalar {narh} som')





# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")


#////////////////

# while list dictionary

# print('Yaqin dostlaringizni royxatini tuzamiz. ')
# ismlar = []
# n=1
# while True:
#     savol = f'{n}-dostingizni ismini kiriting '
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qoshasizmi (ha/yo'q) ")
#     n+=1
#     if takrorlash != 'ha':
#         break

# print('dostlaringizni royxati')
# for ism in ismlar:
#     print(ism.title())

# print("Dostingizni yoshini saqlaymiz ")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input('dostingizni ismini kiriting ')
#     yosh = input(f'{ism.title()} ning yoshini kiriting ')
#     dostlar[ism] = int(yosh)
    
#     javob = input("Yana malumot qoshasizmi (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
        
# for ism, yosh in dostlar.items():
#     print(f'{ism.title()} {yosh} yoshda')


# cars = ['lacetti', 'nexia', 'toyoto', 'nexia', 'audi', 'malibu', 'nexia']
# car = 'lacetti'
# while car in cars:
#     cars.remove(car)
# print(cars)


# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f'{talaba.title()}ning bahosini kiriting: ')
#     print(f'{talaba.title()} baholandi')
#     baholangan_talabalar[talaba] = int(baho)


# print('buyurtma qabul qilish ')
# buyurtmalar = []
# ishora = True
# n = 1
# while ishora:
#     savol = f'{n}-mahsulotni nomini kiriting '
#     mahsulot = input(savol)
#     buyurtmalar.append(mahsulot)
#     takrorlash = input("Yana mahsulot qo'shasizmi ('ha/yoq) ")
#     n+= 1    
#     if takrorlash != 'ha':
#         break
    
# print('Buyurtmalar royxati ')
# for buyurtma in buyurtmalar:
#     print(buyurtma.title())


# print('e-bozor uchun mahsulot royxati ')
# mahsulotlar = {}
# ishora = True
# n = 0
# while ishora:
#     mahsulot = input(f'{n+1} Mahsulot nomini kiriting ')
#     narh = input(f'{mahsulot.title()} narhini kiriting ')
#     mahsulotlar[mahsulot] = int(narh)
#     javob = input('Yana mahsulot qoshmoqchi bolsangiz("ha/yoq") deb yozing ')
# # %%
#     n+= 1

#     if javob == "yo'q":
#         ishora = False
        
# # %%
# for mahsulot, narh in mahsulotlar.items():

#     print(f'{mahsulot}ning narhi {narh} som ')
    


# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f'{buyurtma.title()}-{narh} som')
#     else:
#         print(f'bizda {buyurtma} yoq')



# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print('Assalomu aleykum')
# salom_ber()

# def salom_ber(ism):
#     """Foydalanuvchini ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f'Assalomu aleykum, hurmatli {ism.title()}!')

# salom_ber('hasan')
# salom_ber('olim')
 
# salom_ber()

# def toliq_ism(ism, familya):
#     """Foydalanuvchi ism va familyasini jamlab chiqaruvchi funksiya"""
#     print(f'Foydalanuvchi ism {ism.title()}\n'
#           f'Foydalanuvchi familyasi {familya.title()}')

# toliq_ism('olim', 'hakimov')
# toliq_ism('ayubxon', 'ahmatxonov')  

# def yosh_hisobla(ism, t_yil):
#     """Foydalanuvchi ism va tug'ilgan yilini jamlab chiqaruvchi funksiya"""
#     print(f'Foydalanuvchi ism {ism.title()}\n'
#           f'Foydalanuvchi tugilgan yili {t_yil}')

# yosh_hisobla(t_yil=1997, ism='olim')
# toliq_ism(2000, 'ahmatxonov')  

# def yosh_hisobla(t_yil, joriy_yil = 2025):
#     """Foydalanuvchi tugilgan yilidan uning yoshini hisoblaydi"""
#     print(f'Siz {joriy_yil-t_yil} yoshdasiz')
# yosh_hisobla(2000, 2025)
# yosh_hisobla(2000)
# yosh_hisobla(2025,2025)
# yosh_hisobla(2025,2025)

# vazifa

# def yosh_ism(ism, yosh):
#     """Foydalanuvchi ismi va yoshini kiritadigan funksiya"""
#     print(f'{ism.title()} {2025-yosh}-yilda tugilgan')
    
# yosh_ism('ayubxon', 25)


# def kvadrat_kub(son):
#     """Foydalanuvchi kiritgan sonni kvadrati va kubini aniqlovchi funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga teng \n"
#           f"{son} ning kubi {son**3} ga teng")
# kvadrat_kub(5)



# 
# def juft_toq(son):
#     """Foydalanuvchi kiritgan sonni juft yoki toq ekanini aniqlovchi funksiya"""
#     if son % 2 == 0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")
        
# juft_toq(12985)
# 

# def son_ol(son1, son2):
#     """Foydalanuvchidan ikkita son oladigan va qaysi biri katta yoki kichik ekanini aniqlovchi funksiya"""
#     if son1 > son2:
#         print(son1)
#     if son1 < son2:
#         print(son2)    
#     if son1 == son2:
#         print('sonlar teng')


# def son_ol(x, y=2):
#     print(f'{x} ning {y} darajasi {x**y} ga teng')
    
# son_ol(2,5)


# def bolinish(son):
#     for n in range(2,10):
#         if not son%n:
#             print(f'{son} {n} ga qoldiqsiz bolinadi ')

# bolinish(15)


# def toliq_ism_yasa(ism, familya):
#     """To'liq ismni qaytaruvchi funksiya"""
#     ism_yasa = f"{ism} {familya}"
#     return ism_yasa
# result = toliq_ism_yasa('ayubxon', 'axmatxonov')
# result1 = toliq_ism_yasa('sobitxon', 'axmatxonov')

# print(f'Darsga kelgamagan talabalar {result} {result1}')


# def toliq_ism_yasa(ism, familya, otasining_ismi = ''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {familya} {otasining_ismi}"
#     else:
#         toliq_ism = f"{ism} {familya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa('ayubxon', 'axmatxonov')
# talaba2 = toliq_ism_yasa('sobitxon', 'axmatxonov', 'Yusufxon ogli')

# print(f'Darsga kelmagan oquvchilar {talaba1} {talaba2}')


# def avto_info(kompaniya, model, rang, korobka, yili, narh = None):
#     avto = {'kompaniya': kompaniya,
#         'model': model,
#         'rang': rang,
#         'korobka': korobka,
#         'yili': yili,
#         'narh': narh,
#         }
#     return avto

# avto1 = avto_info('GM', 'jentra', 'oq', 'avtomat', 2023,)
# avto2 = avto_info('BMW', 'BMW-7', 'oq', 'avtomat', 2025, 55000)

# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomobillar')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Nomalum"
#     print(f'{avto['rang']} {avto['model']}.Narhi: {narh}')
    
    
# def oraliq(min, max, qadam = 1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar
# print(oraliq(0, 10,2))

# def avto_info(kompaniya, model, rang, korobka, yili, narhi = None):
#     avto = {'kompaniya': kompaniya,
#         'model': model,
#         'rang': rang,
#         'korobka': korobka,
#         'yili': yili,
#         'narhi': narhi,
#         }
#     return avto

# print('Saytimizdagi avtolar royxatini shakllantiramiz')
# avtolar = []
# while True:
#     print('\nQuyidagi malumotlarni kiriting ', end='')
#     kompaniya=input('ishlab chiqaruvchi ')
#     model=input('Modeli ')
#     rang=input('Rangi ')
#     korobka=input('Karobka ')
#     yili=input('ishlab chiqarilgan yili ')
#     narhi=input('Narhi ')
    
#     avtolar.append(avto_info(kompaniya, model, rang, korobka, yili, narhi))
#     javob = input("Yana avto qo'shasizmi (yes/no): ")
#     if javob == 'no':
#         break
    
# print('\n Salonimizdagi avtolar: ')
# for avto in avtolar:
#     if avto['narhi']:
#         narhi=avto['narhi']
#     else:
#         narhi='Nomalum'
#     print(f'{avto['rang'].title()} {avto['model'].title()}, {korobka} karobka. Narhi: {narhi}')
        
    
# def mijoz_info (ism, familya, t_yil, t_joy, email_add = '', mobil_num = '' ):
#     mijoz = {'ism': ism,
#             'familya': familya,
#             't_yil': t_yil,
#             'yosh': 2025-t_yil,
#             't_joy': t_joy,
#             'email_add': email_add,
#             'mobil_num': mobil_num,
#             }
#     return mijoz
# print('Foydalanuvchi malumotlarini shakllantiramiz ')
# mijozlar = []
# while True:
#     ism = input('Ism: ')
#     familya = input('familya: ')
#     t_yil = int(input('Tugilgan yili: '))
#     t_joy = input('Tugilgan joyi: ')
#     email_add = input('Email addresi: ')
#     mobil_num = input('Mobil raqami: ')
#     mijozlar.append(mijoz_info(ism, familya, t_yil, t_joy, email_add, mobil_num ))
#     javob = input("Yana mijoz qo'shasizmi (yes/no)")
#     if javob == 'no':
#         break
# print ('\n Mijozlarimiz ')
# for mijoz in mijozlar:
#     print(
#        f"{mijoz['ism'].title()} {mijoz['familya'].title()},"
#        f"{mijoz['yosh']} yoshda, telefoni: {mijoz['mobil_num']}"
#        )    
    

# def sonlar(a,b,c):
#     print(max(a, b, c))
    
# sonlar(5,666,187)
    
def fibonachchi(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1] + sonlar[x-2])
    return sonlar
print(fibonachchi(5))
    
    
    
    
    