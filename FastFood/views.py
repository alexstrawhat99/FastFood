from django.shortcuts import render
from django.forms import ModelForm
from .models import Category


class ClientForm(ModelForm):
    class Meta:
        model = Category
        exclude = []


def home(request):
    categories = ClientForm()
    return render(request, 'home.html', {"categories": categories})
