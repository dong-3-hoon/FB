from django.shortcuts import render

# Create your views here.
def prices(request, product, rotn):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if product not in product_price.keys():
        total = 0
    else:
        total = product_price[product] * rotn
    context = {
        'product':product,
        'rotn':rotn,
        'total':total,
        'product_price':product_price,
    }
    return render(request, "prices/prices.html", context)