from triangle.models import FirstModelLog


class CustomMiddleware(object):
    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):
        get_path = request.path
        get_method = request.method
        if get_path != "/admin/":
            FirstModelLog.objects.create(path=get_path, method=get_method)
        response = self.get_response(request)
        return response
