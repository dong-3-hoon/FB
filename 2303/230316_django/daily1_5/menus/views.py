from django.shortcuts import render

# Create your views here.
def food(request):
    food = ["피자", "치킨", "국밥", "초밥", "민초흑당제로마라탕"]
    mymenu=request.GET.get('mymenu')
    context={
        'mymenu':mymenu,
        'food':food,
    }
    return render(request, 'menus/food.html', context)
def receipt(request):
    return render(request, 'menus/receipt.html')
def drink(request):
    drink=["cider", "coke", "miranda", "fanta", "eye of finetree"]
    mymenu=request.GET.get('mymenu')
    context={
        'mymenu':mymenu,
        'drink':drink,
    }
    return render(request, 'menus/drink.html', context)