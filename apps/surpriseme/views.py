# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.contrib import messages
from django.shortcuts import render, redirect #, HttpResponse

VALUES = ['raindrops on roses', 'whiskers on kittens', 'bright copper kettles',
          'warm woolen mittens', 'brown paper packages tied up with strings',
          'cream-colored ponies', 'crisp apple strudel', 'doorbells',
          'sleighbells', 'schnitzel with noodles',
          'wild geese that fly with the moon on their wings']
SPECIFICATIONS = 'Please provide an integer from 0 to 11.'

# Create your views here.
def index(request):
    # print "No surplus words or unnecessary actions."
    return render(request, 'surpriseme/index.html')

def surprise(request):
    if request.method == 'POST':
        # print request.POST['number']
        try:
            if int(request.POST['number']) == 0:
                request.session['surpriselist'] = []
                return redirect('/results')
            elif int(request.POST['number']) > 11:
                messages.error(request, SPECIFICATIONS)
                return redirect('/')
            else:
                random.shuffle(VALUES)
                # print VALUES
                surpriselist = []
                for thing in range(0, int(request.POST['number'])):
                    # print thing
                    surpriselist.append(VALUES[thing])
                request.session['surpriselist'] = surpriselist
                return redirect('/results')
        except (TypeError, ValueError):
            messages.error(request, SPECIFICATIONS)
            return redirect('/')
    else:
        return redirect('/')

def results(request):
    context = {}
    context['surpriselist'] = []
    for each in range(0, len(request.session['surpriselist'])):
        context['surpriselist'].append(request.session['surpriselist'][each])
    # print context
    return render(request, 'surpriseme/results.html', context)
    