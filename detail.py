from django import forms
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext, RedirectException
from catalog import models as cmod
from formlib import Formless
import math

@view_function
def process_request(request, product:cmod.Product):

    if product in request.last_five:
        request.last_five.remove(product)

    else:
        if len(request.last_five) > 6:
            request.last_five.pop()

    request.last_five.insert(0, product)

    context={
        'product': product,
        'category': product.category.pk,
    }

    return request.dmp.render('detail.html', context)
