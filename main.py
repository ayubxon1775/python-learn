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

kocha = input("qaysi ko'chada turasiz ")
mahalla = input('qaysi mahallada turasiz ')
tuman = input("qaysi tumanda turasiz ")
viloyat = input("qaysi viloyatdansiz ")
manzil = (f"{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati")
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())


























