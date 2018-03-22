from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        item_list = request.session.get('last_five', '')
        productList = []
        for item in item_list:
            productList.append(cmod.Product.objects.get(pk=item))

        request.last_five = productList

        response = self.get_response(request)

        productIDs = []
        for product in request.last_five:
            productIDs.append(product.id)

        request.session['last_five'] = productIDs
        print(productIDs)

        return response
