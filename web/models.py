from django.db import models

# Create your models here.

class login(models.Model):
    codeMeli = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=30)

class register(models.Model):
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=25)
    fatherName = models.CharField(max_length=20)
    birthday = models.CharField(max_length=15)
    codeMeli = models.ForeignKey(login, on_delete=models.CASCADE, to_field='codeMeli')
    serialMeli = models.CharField(max_length=10)
    shomareSh = models.CharField(max_length=10)
    serialSh = models.CharField(max_length=6)
    seriSh = models.CharField(max_length=3)
    sadereh = models.CharField(max_length=50)
    ostan = models.CharField(max_length=50)
    shahr = models.CharField(max_length=50)
    neshaniShop = models.CharField(max_length=300)
    codePosti = models.CharField(max_length=10)
    telephonShop = models.CharField(max_length=8)
    shomareParvane = models.CharField(max_length=50)
    codeRehgiri = models.CharField(max_length=50)
    senf = models.CharField(max_length=25)
    teleHamrah = models.CharField(max_length=11)
    bestarType = [
        ('Dialup', 'Dialup Type'),
        ('GPRS', 'GPRS Type'),
        ('Combo', 'Combo Type'),
        ('WIFI', 'WIFI Type'),
    ]
    bestareErtebat = models.CharField(max_length=6, choices=bestarType, default='Dialup') #Dialup, GPRS, Combo, WIFI
    malekType = [
        ('ملکی', 'نوع ملکی'),
        ('سرقفلی', 'نوع سرقفلی'),
        ('استیجاری', 'نوع استیجاری'),
    ]
    malekiyat = models.CharField(max_length=8, choices=malekType, default='ملکی') #ملکی، سرقفلی، استیجاری
    mohlateEjareFrom = models.CharField(max_length=15)
    mohlateEjareTo = models.CharField(max_length=15)
    nameMoaref = models.CharField(max_length=20)
    familyMoaref = models.CharField(max_length=25)
    telMoaref = models.CharField(max_length=11)
    neshaniMoaref = models.CharField(max_length=300)
    shomareHesab = models.CharField(max_length=20)
    nameBank = models.CharField(max_length=50)
    shomareShaba = models.CharField(max_length=16)
    shomareHesabTow = models.CharField(max_length=20)
    nameBankTwo = models.CharField(max_length=50)
    shomareShabaTwo = models.CharField(max_length=16)
    nameFamilyKarshenas = models.CharField(max_length=100)
    paziresh = models.BooleanField(default=False)
    javazKasb = models.CharField(max_length=300)
    ejarehName = models.CharField(max_length=300)
    sanadMalek = models.CharField(max_length=300)
    tsvirShenasnameh = models.CharField(max_length=300)
    rooyeCartmeli = models.CharField(max_length=300)
    poshtCartmeli = models.CharField(max_length=300)
    tsvirEmzaMohr = models.CharField(max_length=300)
    sabinFormFirst = models.CharField(max_length=300)
    sabinFormTwo = models.CharField(max_length=300)
