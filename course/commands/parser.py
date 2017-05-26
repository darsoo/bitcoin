
from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll
from course.models import *
import GDAX


class Command(BaseCommand):

    def history(self)
        publicClient = GDAX.PublicClient(product_id="BTC-USD")
        history = publicClient.getProductHistoricRates(granularity=60)
        id = 0
        while id < 10:
            l = history[id]
            id += 1
            q = LastTime(id,l[0],l[1],l[2])
            q.save()

    def Current(self)

        publicClient = GDAX.PublicClient(product_id="BTC-USD")
        current_coure = publicClient.getProductOrderBook(level=1)
        bids = current_coure[u'bids']
        bids=bids[0]
        bids=bids[0]
        print bids
        asks = current_coure[u'asks']
        asks=asks[0]
        asks=asks[0]
        print asks



