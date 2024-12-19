from django.shortcuts import render, redirect


def index(request):
    return render(request, 'main/index.html')


def modal(request):
    return render(request, 'main/modal.html')




