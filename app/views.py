from django.shortcuts import render
from .models import *

# Create your views here.
def japan(request):
    data = {'Invalid': '', 'Valid': ''}
    if request.method == "POST":
        UserName = request.POST['user']
        Email = request.POST['email']
        Password = request.POST['pass']
        CPassword = request.POST['repass']

        if Password == CPassword:
            SU = SignUp.objects.get_or_create(UserName = UserName, Email = Email, Password = Password, CPassword = CPassword)[0]
            SU.save()
            data['Valid'] = "Register Successfully"
        else:
            data['Invalid'] = "Password incorrect"

    return render(request, 'assigment.html', data)