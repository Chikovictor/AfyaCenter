from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import AppointmentForm, ContactForm

# Create your views here.

def index(request):
    return render(request, 'Index.html')

def about(request):
    return render(request, 'About.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Contact')
    else:
        form = ContactForm()
        return render(request, 'Contact.html', {'form': form})

def doctors(request):
    return render(request, 'Doctors.html')

def departments(request):
    return render(request, 'Departments.html')

 #fetch only active doctors,departments and services
def services(request):
    if request.method == "POST":            #processes submitted data using the appointment form
        form = AppointmentForm(request.POST)
        if form.is_valid():                  #if it passes all validation criteria e.g character number,...
            form.save()                            #saves the form instance and then....
            return HttpResponse("Appointment Booked Successfully.We will get in touch Soon😊")
    else:
        form = AppointmentForm()             #on GET displays the initial form display i.e empty form for user input
        return render(request, 'Services.html',{'form':form})          # passes the form instance to the template for rendering

def successful(request):
    return render(request, 'Successful.html')