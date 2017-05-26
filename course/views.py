# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from course.models import *
import GDAX
import time

def index(request):
    publicClient = GDAX.PublicClient(product_id="BTC-USD")
    history = publicClient.getProductHistoricRates(granularity=60)
    id = 0
    publicClient = GDAX.PublicClient(product_id="BTC-USD")
    current_coure = publicClient.getProductOrderBook(level=1)
    bids = current_coure[u'bids']
    bids=bids[0]
    bids=bids[0]
    asks = current_coure[u'asks']
    asks=asks[0]
    asks=asks[0]
    q = Current(1,0,bids,asks) 
    q.save()
    while id < 10:
        l = history[id]
        id += 1
        tim = time.strftime('%H:%M:%S',time.gmtime(float(l[0])))
        q = LastTime(id,tim,l[1],l[2])
        q.save()

    lasttime = LastTime.objects.all()
    current = Current.objects.all()
    return render(request, 'bitcoin/index.html', {'current': current, 'lasttime': lasttime})

# Create your views here.
