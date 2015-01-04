from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from FitnessApp.models import *

from pprint import pprint
import datetime

def str2bool(v):
    return v.lower() in "true"

# Create your views here.
def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def userman(request):
    return render_to_response('user-management.html', context_instance=RequestContext(request))

def equipman(request):
    return render_to_response('equipment-management.html', context_instance=RequestContext(request))

def dashboard(request):
    return render_to_response('dashb.html', context_instance=RequestContext(request))

def datavisualization(request):
    return render_to_response('data-visualization.html', context_instance=RequestContext(request))

def usercreate(request):
    if request.method == 'GET':
        return render_to_response('user-create.html', context_instance=RequestContext(request))
    else:
        isTrainer = str2bool(request.POST.get('IsTrainer', "False"))
        FirstName = str(request.POST.get('FirstName', ""))
        LastName = str(request.POST.get('LastName', ""))
        BirthDate = str(request.POST.get('BirthDate', ""))
        BirthDate = datetime.datetime.strptime(BirthDate, '%m/%d/%Y').date()
        Gender = str(request.POST.get('Gender', ""))
        Email = str(request.POST.get('Email', ""))
        PhoneNumber = '+'+str(request.POST.get('PhoneNumber', ""))
        Disabilities = str(request.POST.get('Disabilities', ""))
        Disabilities = Disabilities.split(',')

        try:
            Users.objects.get(UserFirstName=FirstName, UserLastName=LastName, UserBday=BirthDate, UserPhoneNumber=PhoneNumber)
            return HttpResponse("User already exists.")
        except Users.DoesNotExist:
            Users.objects.create(UserFirstName=FirstName, UserLastName=LastName, UserBday=BirthDate, 
                UserGender=Gender, UserEmail=Email, UserPhoneNumber=PhoneNumber, IsTrainer=isTrainer)
            UserObj = Users.objects.get(UserFirstName=FirstName, UserLastName=LastName, UserBday=BirthDate, UserPhoneNumber=PhoneNumber)
            
            #pprint(Disabilities)
            for disability in Disabilities:
                UserDisabilities.objects.create(FitnessUser=UserObj, Disability=str(disability))
            return HttpResponse('Entered successfully.')

def usertables(request):
    return render_to_response('user-tables.html', context_instance=RequestContext(request))

def searchuser(request):
    if request.method == 'GET':
        return render_to_response('user-search.html', context_instance=RequestContext(request))
    else:
        isTrainer = str2bool(request.POST.get('IsTrainer', "False"))
        FirstName = str(request.POST.get('FirstName', ""))
        LastName = str(request.POST.get('LastName', ""))
        BirthDate = str(request.POST.get('BirthDate', ""))
        Gender = str(request.POST.get('Gender', ""))
        Email = str(request.POST.get('Email', ""))
        PhoneNumber = '+'+str(request.POST.get('PhoneNumber', ""))
        Disabilities = str(request.POST.get('Disabilities', ""))
        
        if BirthDate != "":
            BirthDate = datetime.datetime.strptime(BirthDate, '%m/%d/%Y').date()

        UserFilt = Users.objects.filter(IsTrainer=isTrainer, UserFirstName__contains=FirstName, 
            UserLastName__contains=LastName, UserBday__contains=BirthDate, UserGender__contains=Gender, 
            UserEmail__contains=Email, UserPhoneNumber__contains=PhoneNumber)
        
        data = {
            'UserSet': UserFilt,
        }
        return render_to_response('user-tables.html', data, context_instance=RequestContext(request))

def showallusers(request):
    if request.method == 'GET':
        data = {
            'UserSet': Users.objects.all(),
        }
        return render_to_response('user-tables.html', data, context_instance=RequestContext(request))

def deleteuser(request):
    if request.method == 'POST':
        userid = int(request.POST.get('id', 0))
        Users.objects.get(id=userid).delete()
    return HttpResponse('User Deleted!')

def equipcreate(request):
    if request.method == 'POST':
        equipName = str(request.POST.get('EquipName', None))
        equipPrice = float(request.POST.get('EquipPrice', 0))
        contactEmail = str(request.POST.get('EquipEmail', None))
        contactPhone = '+'+str(request.POST.get('EquipPhone', ''))

        pprint(equipName)

        try:
            Equipment.objects.get(ItemName=equipName)
            return HttpResponse('Equipment exists in inventory already.')
        except Equipment.DoesNotExist:
            Equipment.objects.create(ItemName=equipName, BoughtPrice=equipPrice, ContactEmail=contactEmail, ContactPhone=contactPhone)
            return HttpResponse('Entered successfully.')
    else:
        return render_to_response('equip-create.html', context_instance=RequestContext(request))

def equipsearch(request):
    if request.method == 'GET':
        return render_to_response('equip-search.html', context_instance=RequestContext(request))
    else:
        equipName = str(request.POST.get('EquipName', ''))
        equipPrice = float(request.POST.get('EquipPrice', 0))
        contactEmail = str(request.POST.get('EquipEmail', ''))
        contactPhone = '+'+str(request.POST.get('EquipPhone', ''))
        
        Equipfilt = Equipment.objects.filter(ItemName__contains=equipName, BoughtPrice=equipPrice, ContactEmail__contains=contactEmail, ContactPhone__contains=contactPhone)
        
        data = {
            'EquipmentSet': Equipfilt,
        }
        return render_to_response('equip-tables.html', data, context_instance=RequestContext(request))

def equipdelete(request):
    if request.method == 'POST':
        equipid = int(request.POST.get('id', 0))
        Equipment.objects.get(id=equipid).delete()
    return HttpResponse('Equipment Deleted!')

def showallequip(request):
    if request.method == 'GET':
        data = {
            'EquipmentSet': Equipment.objects.all(),
        }
        return render_to_response('equip-tables.html', data, context_instance=RequestContext(request))
