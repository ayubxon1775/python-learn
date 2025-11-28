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

friends = []

friends.append("Abdulbosit")
friends.append("Akramjon")
friends.append("Abdurrohman")
friends.append("Abdushohid")
friends.append("Abdulloh")

friends.remove("Abdurrohman")
friends.insert(0, "Musoxon")
friends.insert(2, "Mutalli")
friends.insert(-1, "shoh")

print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(1))
print(f"kelgan mehmonlar {mehmonlar}")









