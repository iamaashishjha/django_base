class Authentication:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/specific_route/':
            print("#####")
            # Custom logic for the specific route
            # ...

        response = self.get_response(request)

        if request.path == '/specific_route/':
            print("#####")
            # Custom logic for the specific route's response
            # ...

        return response