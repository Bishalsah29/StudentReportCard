from pydoc import text
from django.shortcuts import render , redirect
from django.http import HttpResponse
from vege.seed import *
from home.utils import send_email_to_client , send_email_with_attachment
from django.conf import settings
import os

def send_email(request):
    subject = "Django Email with Attachment"
    message = "This email contains an attachment sent from Django."
    recipient_list = ["vshalsah29@gmail.com"]
    file_path = f"{settings.BASE_DIR}/main.xlsx" # Update with the actual file path 
    
    send_email_with_attachment(subject, message, recipient_list, file_path)
    return redirect('/')
   


# Create your views here.

def home(request):
    seed_db(100)
    
    Car.objects.create(car_name = f"Nexon - {random.randint(0,100)}" )
    
    
    peoples = [
            {'name': 'Bishal', 'age': 22, 'city': 'chandigardh'},
            {'name': 'Bob', 'age': 17, 'city': 'Los Angeles'},
            {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
            {'name': 'Diana', 'age': 28, 'city': 'Miami'},
            {'name': 'Ethan', 'age': 15, 'city': 'San Francisco'}       
    ]
   

    return render(request, "home/index.html", context={'peoples': peoples, 'text': text, 'page':'Django 2026 tutorials'}) 



def about(request):
    context = {'page':'About'}
    return render(request, "home/about.html", context)


def contact(request):
    context = {'page':'Contact'}
    return render(request, "home/contact.html", context)


def success_page(request): 
    context = {'page':'Success'} 
    return render(request, "home/success.html", context)    

