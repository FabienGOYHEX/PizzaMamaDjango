from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.


def index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'menu/index.html', {'my_pizzas_key': pizzas})
    '''pizzas = Pizza.objects.all()
    pizzas_names_and_price = [pizza.name + " : " +
                              str(pizza.price) + " €" for pizza in pizzas]
    pizzas_names_and_Price_str = ", ".join(pizzas_names_and_price)

    return HttpResponse("Nos pizza : " + pizzas_names_and_Price_str)'''
