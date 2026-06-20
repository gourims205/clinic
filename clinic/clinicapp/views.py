from django.shortcuts import redirect,render
from .forms import *
from .models import *

# Create your views here.
def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book')
            
    else:
        form = AppointmentForm()        
    return render(request,"appointment.html",{"form":form})

def delete_appnt(request ,id):
        appnts = Appointment.objects.get(id = id)
        appnts.delete()
        return redirect('/Allappointments') 


def update_appnt(request ,id):
    appnt = Appointment.objects.get(id=id)
    if request.method =="POST":
        form = AppointmentForm(request.POST,instance = appnt)
        if form.is_valid():
            form.save()
            return redirect('/Allappointments')
    else :   
        form = AppointmentForm(instance= appnt)
    return render(request,'Update_appointment.html',{"form":form})    
        
        
def Allappointments(request):
    if request.method == "GET":
        appnts = Appointment.objects.all()
    return render(request , 'Allappointments.html',{"appointments":appnts})

def contact(request):
    return render(request,"contact.html")

def about(request):
     return render(request,"about.html")
 
def departments(request):
     return render(request,"departments.html")
 
def doctors(request):
     return render(request,"doctors.html")
    
    