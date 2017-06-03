# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Treasure
from .forms import TreasureForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    return render(request, 'index.html', {'treasures': treasures, 'form':form})


def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})

def post_treasure(request):
    form = TreasureForm(request.POST)
    if form.is_valid():
        treasure = Treasure(name=form.cleaned_data['name'],
                            value=form.cleaned_data['value'],
                            material=form.cleaned_data['material'],
                            location=form.cleaned_data['location'],
                            img_url=form.cleaned_data['img_url'])
        treasure.save()
        return HttpResponseRedirect('/')


# class Treasure:
#     def __init__(self, name, value, material, location, img_url):
#         self.name = name
#         self.value = value
#         self.material = material
#         self.location = location
#         self.img_url = img_url
#
# treasures = [
#     Treasure('Gold Nugget', 500.00, 'Gold', "Curly's Creek, NM", 'example.com/nugget.jpg'),
#     Treasure("Fool's Gold", 0, 'Pyrite', "Fool's Fails, CO", 'cdn.shopify.com/s/files/1/0081/4402/products/sticker_grande.jpg?v=1479972797'),
#     Treasure('Coffee Can', 20.00, 'Tin', 'Acme, CA', 'example.com/coffee-can.jpg')
# ]