from django_mako_plus import view_function, jscontext
from catalog import models as cmod

@view_function
def process_request(request, product: cmod.Product):

    for index, i in enumerate(request.last_five):
        if i.id == product.id:
            request.last_five.pop(index)
        else:
            request.last_five.pop

    request.last_five.insert(0, product)

    context = {
        'product': product,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'image': product.image_url(),
        'images': product.image_urls(),
    }

    return request.dmp.render('detail.html', context, )
