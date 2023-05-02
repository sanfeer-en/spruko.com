from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
def formpage(request):
    return render(request, 'form.html')