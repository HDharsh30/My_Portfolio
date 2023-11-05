from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact_me(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        query = Contact(name=name, email=email, desc=message)
        query.save()
    return render(request, 'index.html')