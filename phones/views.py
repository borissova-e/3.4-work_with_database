from django.shortcuts import render

from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    context = {'phones': Phone.objects.all().order_by(sort)}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
