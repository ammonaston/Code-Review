from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # holds IDs
        request.session.get('last_five', [])

        request.last_five = []

        #holds the products
        if request.session.get('last_five'):
            for item in request.session.get('last_five'):
                request.last_five.append(cmod.Product.objects.get(id = item))

        response = self.get_response(request)

        request.last_five = request.last_five[0:6]

        templist = []
        for item in request.last_five:
            templist.append(item.id)

        request.session['last_five'] = templist


        return response
