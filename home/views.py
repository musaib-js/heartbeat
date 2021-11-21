from django.shortcuts import render
from .models import donation_plea
from django.contrib import messages



# Create your views here.
def signup(request):
    return render(request, 'home.html')

def donationplea(request):
    if request.method == "POST":
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        requirement = request.POST["requirement"]
        birthdate = request.POST["birthdate"]
        birthmonth = request.POST["birthmonth"]
        birthyear = request.POST["birthyear"]
        gender = request.POST["gender"]
        message = request.POST["message"]

        newplea = donation_plea(full_name = fullname, email = email, contact = contact, requirement = requirement, birth_date = birthdate, birth_month = birthmonth, birth_year = birthyear, gender= gender, message = message)
        newplea.save()
        messages.success(request,  "Your Plea Has Been Submitted")


    return render (request, 'recepient.html')

def donate(request):
    return render (request, 'donate.html')

def cards(request):
    return render(request, 'cards.html')

def pleas(request):
    pleas = donation_plea.objects.all()
    context = {"pleas":pleas}
    return render(request, 'pleas.html', context)
