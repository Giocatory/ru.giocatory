from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import UsersMessages


def main(request):
    if request.method == 'POST':
        # user_name = request.GET.get('user_name')
        # user_email = request.GET.get('user_email')
        # user_text = request.GET.get('user_text')

        message = UsersMessages()
        message.name = request.POST.get('user_name')
        message.email = request.POST.get('user_email')
        message.message = request.POST.get('user_text')
        message.save()

    return render(request, 'index.html')