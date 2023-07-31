from django.shortcuts import render
from django.views import generic as views

from online_shop.products.models import Product
from online_shop.web.forms import SearchForm


# Create your views here.
class IndexPage(views.ListView):
    template_name = 'index.html'
    model = Product
    extra_context = {
        'products': Product.objects.filter().order_by('-id')[:8]
    }

    id = 5


class ShopPage(views.ListView):
    template_name = 'shop.html'
    model = Product

    extra_context = {
        'products': Product.objects.all()
    }


def contact_page(request):
    return render(request, template_name='contact.html')


def testimonial_page(request):
    return render(request, template_name='testimonial.html')


def why_page(request):
    return render(request, template_name='why.html')
