from django.shortcuts import render

from orderapp.models import UserService


# Create your views here.
def get_service(request):
    all_service = UserService.objects.filter(user_id=request.user.id)
    print(all_service)