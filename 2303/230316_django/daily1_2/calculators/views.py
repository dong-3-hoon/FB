from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculators/calculation.html')
def result(request):
    d1 = int(request.GET.get('d1'))
    d2 = int(request.GET.get('d2'))
    pl = d1+d2
    mi = d1-d2
    cm=d1*d2
    if d2==0:
        sk=0
    else:
        sk=d1/d2
    context = {
        'mi':d1-d2,
        'cm':d1*d2,
        'sk':sk,
        'd1':d1,
        'd2':d2,
    }
    return render(request, 'calculators/result.html', context)
