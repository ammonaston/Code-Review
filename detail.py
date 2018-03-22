# from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
# import math

@view_function
def process_request(request, product:cmod.Product=None):

    object_not_found = True
    if product is not None:
        id = product.id
        if len(request.last_five) == 0:
            request.last_five.insert(0, product)
        # loop through last_five
        for index, p in enumerate(request.last_five):
            # if pulling from history, pop out of list and add to top
            if p.id == id:
                request.last_five.insert(0, request.last_five.pop(index))
                object_not_found = False

        if object_not_found:
            request.last_five.insert(0, product)
            request.last_five = request.last_five[0:6]

    context = {
        'product': product
    }

    return request.dmp.render('detail.html', context)
