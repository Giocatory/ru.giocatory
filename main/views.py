from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def main(request):
    user_name = request.GET.get('user_name')
    user_email = request.GET.get('user_email')
    user_text = request.GET.get('user_text')

    return render(request, 'index.html')