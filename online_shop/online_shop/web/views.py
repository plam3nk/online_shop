from django.shortcuts import render
from django.views import generic as views

from online_shop.products.models import Product
from online_shop.web.forms import SearchForm


# Create your views here.

def index(request):
    search_form = SearchForm(request.GET)

    context = {
        'search_form': search_form,
    }
    return render(request, template_name='index.html')


class ShopPage(views.ListView):
    template_name = 'shop.html'
    model = Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()

        return context


def contact_page(request):
    return render(request, template_name='contact.html')


def testimonial_page(request):
    return render(request, template_name='testimonial.html')


def why_page(request):
    return render(request, template_name='why.html')
