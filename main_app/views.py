# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Treasure


# Create your views here.
def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})


def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})


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