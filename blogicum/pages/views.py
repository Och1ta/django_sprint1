from django.shortcuts import render


def about(request):
    """ Выводит информацию о проекте """
    template_name = 'pages/about.html'
    return render(request, template_name)


def rules(request):
    """ Выводит информацию о правилах на проекте """
    template_name = 'pages/rules.html'
    return render(request, template_name)

