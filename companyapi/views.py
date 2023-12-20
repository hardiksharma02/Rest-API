from django.http import HttpResponse
from django.http import JsonResponse
def home_page (request):
    print("home page request")
    friends=[
        'ankit',
        'Ravi',
        'Uttam'
    ]
    return JsonResponse(friends,safe=False)