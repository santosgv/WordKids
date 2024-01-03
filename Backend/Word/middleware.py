class CustomCorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "https://154.49.246.53/"
        response["Access-Control-Allow-Headers"] = "https://154.49.246.53/"

        # Code to be executed for each request/response after
        # the view is called.

        return response