from django.shortcuts import render
import random
# Create your views here.
def certifications1(request):
    context = {
        "name" : 'sehoon',
        "age" : random.randint(1, 100)
    }
    return render(request, "daily/certifications1.html", context)
def certifications2(request):
    context = {
        "name" : 'sedong',
        "age" : random.randint(1, 100)
    }
    return render(request, "daily/certifications2.html", context)
def certifications3(request):
    context = {
        "name" : 'sadohm',
        "age" : random.randint(1, 100)
    }
    return render(request, "daily/certifications2.html", context)