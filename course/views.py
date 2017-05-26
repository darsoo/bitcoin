# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from course.models import *
import GDAX
import time

def index(request):
    publicClient = GDAX.PublicClient(product_id="BTC-USD")
    current_course = publicClient.getProductOrderBook(level=1)
    history_1_min = publicClient.getProductHistoricRates(granularity=60)
    history_10_sec = publicClient.getProductHistoricRates(granularity=10)

    bids = current_course[u'bids']
    bids=bids[0]
    bids=bids[0]
    asks = current_course[u'asks']
    asks=asks[0]
    asks=asks[0]
    current_time = timezone.now()
    q = Current(1,current_time,bids,asks) 
    q.save()


    bids_sum = 0
    asks_sum = 0
    id = 0
    while id < 60:
        l = history_10_sec[id]  
        id += 1
        bids_sum = (bids_sum + l[1])
        asks_sum = (asks_sum + l[2])
    avg_of_bids = bids_sum/60
    avg_of_asks = asks_sum/60
    q = Average(id,avg_of_bids,avg_of_asks)
    q.save()



    id = 0
    while id < 10:
        l = history_1_min[id]
        id += 1
        time_ = time.strftime('%H:%M:%S',time.gmtime(float(l[0])))
        q = LastTime(id,time_,l[1],l[2])
        q.save()

    average = Average.objects.all()
    lasttime = LastTime.objects.all()
    current = Current.objects.all()
    return render(request, 'bitcoin/index.html', {'current': current, 'lasttime': lasttime, 'average': average })

# Create your views here.
