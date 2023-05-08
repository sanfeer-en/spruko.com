from django.shortcuts import render , redirect
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')
def formpage(request):
    return render(request, 'form.html')
def tableview(request):
    return render(request, 'table.html')
def form(request):
    if request.method == 'POST':
        fullname = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phonenumber = request.POST.get('number')
        Dofbirth = request.POST.get('dateofbirth')
        userdetails = UserDeatils.objects.create(username = fullname , passwords = password , email = email , number = phonenumber , birth = Dofbirth) 
        userdetails.save()

        return redirect("/table")
    return render(request,'form.html')
def table(request):
    userinput = UserDeatils.objects.all()
    return render(request,'table.html',{"userdata":userinput})
def delete(request , id):
    userinput = UserDeatils.objects.get(id=id)
    userinput.delete()
    return redirect("/table")

def edit(request,id):
    userinput = UserDeatils.objects.get(id=id)
    return render(request,'edit.html',{"userdata":userinput})
def update(request,id):
    userinput = UserDeatils.objects.get(id=id)
    if request.method == 'POST' :
        userinput.userName = request.POST['username']
        userinput.email = request.POST['email']
        userinput.phoneNumber = request.POST['number']
        userinput.password = request.POST['password']
        userinput.dofbirth = request.POST['dateofbirth']
        userinput.save()
        return redirect ("/table")
    
