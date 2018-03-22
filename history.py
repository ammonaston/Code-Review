from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        request.session.get('last_five', [])

        request.last_five = [] #used to hold objects (products)

        if request.session.get('last_five'):
            for i in request.session.get('last_five'):
                request.last_five.append(cmod.Product.objects.get(id = i))

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        request.last_five = request.last_five[0:6]

        tempList = []

        for i in request.last_five:
            tempList.append(i.id)

        request.session['last_five'] = tempList

        return response
