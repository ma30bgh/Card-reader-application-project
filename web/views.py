import os
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from kartKhan.settings import BASE_DIR
# Create your views here.
from web.models import register, login
from .serializer import registerSerializer


def loginPage(request):
    return render(request,'web/login.html')

@csrf_exempt
def loginUser(request):
    codeMeli = request.POST['codeMeli']
    password = request.POST['password']
    print(codeMeli + ' :  ' + password)
    checkLogin = login.objects.filter(codeMeli=codeMeli,password=password)
    print(checkLogin)
    if checkLogin.exists():
        data = {
            'isSuccess': True,
            'message': 'عملیات با موفقیت انجام شد',
            'codeMeli': codeMeli
        }
        return JsonResponse(data)
    else:
        data = {
            'isSuccess': False,
            'message': 'خطایی رخ داده است'
        }
        return JsonResponse(data)

@csrf_exempt
def registerPage(request,pk):
    checkRegister = ''
    try:
        checkRegister = register.objects.get(codeMeli=pk)
        print(checkRegister)
    except Exception as e:
        print(e)
    # data = ''
    # if checkRegister.exists():
    #     data = registerSerializer(checkRegister, many=False)
    #     print(data.data)
    bestarType = register.bestarType
    malekType = register.malekType
    return render(request, 'web/registerData.html',{'codeMeli':pk,'loginData': checkRegister, 'bestarType': bestarType, 'malekType': malekType})

@csrf_exempt
def registerData(request):

    name = request.POST['name']
    family = request.POST['family']
    fatherName = request.POST['fatherName']
    birthday = request.POST['birthday']
    codeMeli = request.POST['codeMeli']
    serialMeli = request.POST['serialMeli']
    shomareSh = request.POST['shomareSh']
    serialSh = request.POST['serialSh']
    seriSh = request.POST['seriSh']
    sadereh = request.POST['sadereh']
    ostan = request.POST['ostan']
    shahr = request.POST['shahr']
    neshaniShop = request.POST['neshaniShop']
    codePosti = request.POST['codePosti']
    telephonShop = request.POST['telephonShop']
    shomareParvane = request.POST['shomareParvane']
    codeRehgiri = request.POST['codeRehgiri']
    senf = request.POST['senf']
    teleHamrah = request.POST['teleHamrah']
    bestareErtebat = request.POST['bestareErtebat']
    malekiyat = request.POST['malekiyat']
    mohlateEjareFrom = request.POST['mohlateEjareFrom']
    mohlateEjareTo = request.POST['mohlateEjareTo']
    nameMoaref = request.POST['nameMoaref']
    familyMoaref = request.POST['familyMoaref']
    telMoaref = request.POST['telMoaref']
    neshaniMoaref = request.POST['neshaniMoaref']
    shomareHesab = request.POST['shomareHesab']
    nameBank = request.POST['nameBank']
    shomareShaba = request.POST['shomareShaba']
    shomareHesabTow = request.POST['shomareHesabTow']
    nameBankTwo = request.POST['nameBankTwo']
    shomareShabaTwo = request.POST['shomareShabaTwo']
    nameFamilyKarshenas = request.POST['nameFamilyKarshenas']
    paziresh = request.POST['paziresh']

    javazKasb = request.FILES.get('javazKasb', '')
    ejarehName = request.FILES.get('ejarehName', '')
    sanadMalek = request.FILES.get('sanadMalek', '')
    tsvirShenasnameh = request.FILES.get('tsvirShenasnameh', '')
    rooyeCartmeli = request.FILES.get('rooyeCartmeli', '')
    poshtCartmeli = request.FILES.get('poshtCartmeli', '')
    tsvirEmzaMohr = request.FILES.get('tsvirEmzaMohr', '')
    sabinFormFirst = request.FILES.get('sabinFormFirst', '')
    sabinFormTwo = request.FILES.get('sabinFormTwo', '')

    pazireshData = ''
    if paziresh == 'false':
        pazireshData = False
    else:
        pazireshData = True
    loginData = login.objects.get(codeMeli=codeMeli)
    try:
        checkReg = register.objects.filter(codeMeli=codeMeli)
        if checkReg.exists():

            addRegister = register.objects.get(codeMeli=codeMeli)
            addRegister.name = name
            addRegister.family = family
            addRegister.fatherName = fatherName
            addRegister.birthday = birthday
            addRegister.serialMeli = serialMeli
            addRegister.shomareSh = shomareSh
            addRegister.serialSh = serialSh
            addRegister.seriSh = seriSh
            addRegister.sadereh = sadereh
            addRegister.ostan = ostan
            addRegister.shahr = shahr
            addRegister.neshaniShop = neshaniShop
            addRegister.codePosti = codePosti
            addRegister.telephonShop = telephonShop
            addRegister.shomareParvane = shomareParvane
            addRegister.codeRehgiri = codeRehgiri
            addRegister.senf = senf
            addRegister.teleHamrah = teleHamrah
            addRegister.bestareErtebat = bestareErtebat
            addRegister.malekiyat = malekiyat
            addRegister.mohlateEjareFrom = mohlateEjareFrom
            addRegister.mohlateEjareTo = mohlateEjareTo
            addRegister.nameMoaref = nameMoaref
            addRegister.familyMoaref = familyMoaref
            addRegister.telMoaref = telMoaref
            addRegister.neshaniMoaref = neshaniMoaref
            addRegister.shomareHesab = shomareHesab
            addRegister.nameBank = nameBank
            addRegister.shomareShaba = shomareShaba
            addRegister.shomareHesabTow = shomareHesabTow
            addRegister.nameBankTwo = nameBankTwo
            addRegister.shomareShabaTwo = shomareShabaTwo
            addRegister.nameFamilyKarshenas = nameFamilyKarshenas
            addRegister.paziresh = pazireshData
        else:
            addRegister = register(name=name,family=family,fatherName=fatherName,birthday=birthday,codeMeli=loginData,serialMeli=serialMeli,shomareSh=shomareSh, serialSh=serialSh,
                             seriSh=seriSh,sadereh=sadereh,ostan=ostan,shahr=shahr,neshaniShop=neshaniShop,codePosti=codePosti,telephonShop=telephonShop,shomareParvane=shomareParvane,
                             codeRehgiri=codeRehgiri,senf=senf,teleHamrah=teleHamrah,bestareErtebat=bestareErtebat,malekiyat=malekiyat,mohlateEjareFrom=mohlateEjareFrom,
                             mohlateEjareTo=mohlateEjareTo,nameMoaref=nameMoaref, familyMoaref=familyMoaref,telMoaref=telMoaref,neshaniMoaref=neshaniMoaref,shomareHesab=shomareHesab,
                             nameBank=nameBank, shomareShaba=shomareShaba, shomareHesabTow=shomareHesabTow,nameBankTwo=nameBankTwo,shomareShabaTwo=shomareShabaTwo,nameFamilyKarshenas=nameFamilyKarshenas,
                             paziresh=pazireshData)
        addRegister.save()
        print(javazKasb)
        if javazKasb != '':
            file_name = javazKasb.name

            if not os.path.exists(BASE_DIR + '/media/%s' % 'javazKasb'):
                os.makedirs(BASE_DIR + '/media/%s' % 'javazKasb')

            with open(BASE_DIR + '/media/%s/%s.%s' % ('javazKasb', codeMeli, file_name.split('.')[-1]), 'wb') as f:
                f.write(javazKasb.read())
            javazKasbAddress = '/media/%s/%s.%s' % ('javazKasb', codeMeli, file_name.split('.')[-1])
            addRegister.javazKasb = javazKasbAddress

        if ejarehName != '':
            file_name = ejarehName.name

            if not os.path.exists(BASE_DIR + '/media/%s' % 'ejarehName'):
                os.makedirs(BASE_DIR + '/media/%s' % 'ejarehName')

            with open(BASE_DIR + '/media/%s/%s.%s' % ('ejarehName', codeMeli, file_name.split('.')[-1]), 'wb') as f:
                f.write(ejarehName.read())
            ejarehNameAddress = '/media/%s/%s.%s' % ('ejarehName', codeMeli, file_name.split('.')[-1])
            addRegister.ejarehName = ejarehNameAddress

        if sanadMalek != '':
            file_name = sanadMalek.name

            if not os.path.exists(BASE_DIR + '/media/%s' % 'sanadMalek'):
                os.makedirs(BASE_DIR + '/media/%s' % 'sanadMalek')

            with open(BASE_DIR + '/media/%s/%s.%s' % ('sanadMalek', codeMeli, file_name.split('.')[-1]), 'wb') as f:
                f.write(sanadMalek.read())
            sanadMalekAddress = '/media/%s/%s.%s' % ('sanadMalek', codeMeli, file_name.split('.')[-1])
            addRegister.sanadMalek = sanadMalekAddress

        if tsvirShenasnameh != '':
            file_name = tsvirShenasnameh.name

            if not os.path.exists(BASE_DIR + '/media/%s' % 'tsvirShenasnameh'):
                os.makedirs(BASE_DIR + '/media/%s' % 'tsvirShenasnameh')

            with open(BASE_DIR + '/media/%s/%s.%s' % ('tsvirShenasnameh', codeMeli, file_name.split('.')[-1]), 'wb') as f:
                f.write(tsvirShenasnameh.read())
            tsvirShenasnamehAddress = '/media/%s/%s.%s' % ('tsvirShenasnameh', codeMeli, file_name.split('.')[-1])
            addRegister.tsvirShenasnameh = tsvirShenasnamehAddress

        if rooyeCartmeli != '':
            file_name = rooyeCartmeli.name

            if not os.path.exists(BASE_DIR + '/media/%s' % 'rooyeCartmeli'):
                os.makedirs(BASE_DIR + '/media/%s' % 'rooyeCartmeli')

            with open(BASE_DIR + '/media/%s/%s.%s' % ('rooyeCartmeli', codeMeli, file_name.split('.')[-1]), 'wb') as f:
                f.write(rooyeCartmeli.read())
            rooyeCartmeliAddress = '/media/%s/%s.%s' % ('rooyeCartmeli', codeMeli, file_name.split('.')[-1])
            addRegister.rooyeCartmeli = rooyeCartmeliAddress

        if poshtCartmeli != '':
            file_name = poshtCartmeli.name

            if not os.path.exists(BASE_DIR + '/media/%s' % 'poshtCartmeli'):
                os.makedirs(BASE_DIR + '/media/%s' % 'poshtCartmeli')

            with open(BASE_DIR + '/media/%s/%s.%s' % ('poshtCartmeli', codeMeli, file_name.split('.')[-1]), 'wb') as f:
                f.write(poshtCartmeli.read())
            poshtCartmeliAddress = '/media/%s/%s.%s' % ('poshtCartmeli', codeMeli, file_name.split('.')[-1])
            addRegister.poshtCartmeli = poshtCartmeliAddress

        if tsvirEmzaMohr != '':
            file_name = tsvirEmzaMohr.name

            if not os.path.exists(BASE_DIR + '/media/%s' % 'tsvirEmzaMohr'):
                os.makedirs(BASE_DIR + '/media/%s' % 'tsvirEmzaMohr')

            with open(BASE_DIR + '/media/%s/%s.%s' % ('tsvirEmzaMohr', codeMeli, file_name.split('.')[-1]), 'wb') as f:
                f.write(tsvirEmzaMohr.read())
            tsvirEmzaMohrAddress = '/media/%s/%s.%s' % ('tsvirEmzaMohr', codeMeli, file_name.split('.')[-1])
            addRegister.tsvirEmzaMohr = tsvirEmzaMohrAddress

        if sabinFormFirst != '':
            file_name = sabinFormFirst.name

            if not os.path.exists(BASE_DIR + '/media/%s' % 'sabinFormFirst'):
                os.makedirs(BASE_DIR + '/media/%s' % 'sabinFormFirst')

            with open(BASE_DIR + '/media/%s/%s.%s' % ('sabinFormFirst', codeMeli, file_name.split('.')[-1]), 'wb') as f:
                f.write(sabinFormFirst.read())
            sabinFormFirstAddress = '/media/%s/%s.%s' % ('sabinFormFirst', codeMeli, file_name.split('.')[-1])
            addRegister.sabinFormFirst = sabinFormFirstAddress

        if sabinFormTwo != '':
            file_name = sabinFormTwo.name

            if not os.path.exists(BASE_DIR + '/media/%s' % 'sabinFormTwo'):
                os.makedirs(BASE_DIR + '/media/%s' % 'sabinFormTwo')

            with open(BASE_DIR + '/media/%s/%s.%s' % ('sabinFormTwo', codeMeli, file_name.split('.')[-1]), 'wb') as f:
                f.write(sabinFormTwo.read())
            sabinFormTwoAddress = '/media/%s/%s.%s' % ('sabinFormTwo', codeMeli, file_name.split('.')[-1])
            addRegister.sabinFormTwo = sabinFormTwoAddress




        addRegister.save()

        data = {
            'isSuccess': True,
            'message': 'عملیات با موفقیت انجام شد'
        }
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {
            'isSuccess': False,
            'message': 'خطایی رخ داده است'
        }
        return JsonResponse(data)