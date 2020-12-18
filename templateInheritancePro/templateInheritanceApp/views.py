# Template Inheritance - Create a navbar at the top of our page, it wouldn’t make sense to continually
# have the same navbar HTML code in each individual .html file. Instead we set it to the base.html file
# and inherit it using template inheritance.
# Template inheritance allows us to create a base template we can inherit from.

from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'templateInheritanceApp/index.html')


def other(request):
    return render(request, 'templateInheritanceApp/other.html')


def relative(request):
    return render(request, 'templateInheritanceApp/relative_url_templates.html')
