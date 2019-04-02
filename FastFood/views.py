from django.shortcuts import render
from django.forms import ModelForm
from .models import Category, Product


class ClientForm(ModelForm):
    class Meta:
        model = Category
        exclude = []


def home(request):
    categories = ClientForm()
    return render(request, 'index.html', {"categories":categories})


def menu(request):
    products = Product.objects.all()
    return render(request, 'menu.html', {'products': products})


def elements(request):
    return render(request, 'elements.html', {})


def contact_us(request):
    return render(request, 'contact-us.html', {})


def about(request):
    return render(request, 'about.html', {})


def blogDetails(request):
    return render(request, 'blog-details.html', {})


def blogHome(request):
    return render(request, 'blog-home.html', {})