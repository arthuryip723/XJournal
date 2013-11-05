from django.http import HttpResponse

def index(request):
#     return HttpResponse("Hello, world. You're at the journal index.")
    return HttpResponse(request.user.username == 'su')