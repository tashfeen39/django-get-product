from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from django.db.models import Count
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px


# Create your views here.


def home(request):
    return render(request, 'product/home.html')


def product(request):
    firstName1 = request.POST.get('firstName1')
    lastName1 = request.POST.get('lastName1')
    number1 = request.POST.get('number1')
    firstName2 = request.POST.get('firstName2')
    lastName2 = request.POST.get('lastName2')
    number2 = request.POST.get('number2')
    product = int(number1)*int(number2)
    User.objects.create(firstName1=firstName1, lastName1=lastName1, number1=number1,
                        firstName2=firstName2, lastName2=lastName2, number2=number2, product=product)
    # User.objects.all().delete()

    return render(request, 'product/get_product.html', {'user1': firstName1 + ' ' + lastName1, 'user2': firstName2 + ' ' + lastName2, 'product': product})


def all_users(request):
    user_list = User.objects.all()
    queryset = User.objects.values('product').annotate(count=Count('product'))

    
    x_data = [item['product'] for item in queryset]
    y_data = [item['count'] for item in queryset]
    fig = px.bar(x=x_data, y=y_data)
    fig.show()

    return render(request, 'product/user_list.html', locals())
