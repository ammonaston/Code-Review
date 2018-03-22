from catalog import models as cmod
class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        ##############################  ###########################################
                # Code to be executed for each request before
                # the view (and later middleware) are called.
        ##############################  ###########################################

        request.last_five = list(map(
            (lambda x: cmod.Product.objects.get(id=x)), 
            request.session.get('last_five', [])
        ))

        # middleware call
        response = self.get_response(request)

        ##############################  ###########################################
                # Code to be executed for each request/response after
                # the view is called.
        ##############################  ###########################################

        # change Product objects into ids
        productList = list(map(
            (lambda x: x.id), 
            request.last_five
        ))

        request.session['last_five'] = productList

        return response
