from django.shortcuts import render

# Create your views here.
def hello(request,name):
    context = {
        'n2':name
    }
    return render(request, "myapp2/hello.html", context)