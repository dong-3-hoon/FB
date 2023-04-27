from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    print(request.GET["message"])
    message = request.GET.get('message')
    context = {
        'message':message,
        'key' : request.GET.get('key')
    }
    return render(request, 'articles/catch.html', context)