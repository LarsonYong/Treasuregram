# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


# Create your views here.
def index(request):
    name = 'Gold Nugget'
    value = 1000.00
    context = {'treasure_name': name, 'treasure_val': value}

    return render(request, 'index.html', {'treasures': treasures})


class Treasure:
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location

treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM"),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Fails, CO"),
    Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA')
]