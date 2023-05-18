from django.shortcuts import render


def about(request):
    """ Выводит информацию о проекте """
    return render(request, 'pages/about.html')


def rules(request):
    """ Выводит информацию о правилах на проекте """
    return render(request, 'pages/rules.html')
