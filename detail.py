from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod

@view_function
def process_request(request, prod:cmod.Product):

    for index, item in enumerate(request.last_five):
        if item.id == prod.id:
            request.last_five.pop(index)
        elif len(request.last_five) > 6:
            request.last_five.pop

    request.last_five.insert(0, prod)

    p1 = cmod.Product.objects.get(id = request.dmp.urlparams[0])
    c2 = cmod.Category.objects.get(id = p1.category_id)
    name = c2.name

    context = {
        'product': p1,
        'category_name': name,
    }
    return request.dmp.render('detail.html', context)
