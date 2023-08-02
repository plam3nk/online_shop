from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from online_shop.products.models import Product
from online_shop.web.forms import ContactForm
from online_shop.web.models import Contact


# Create your views here.


class IndexPageView(views.ListView):
    template_name = 'core/index.html'
    model = Product
    extra_context = {
        'products': Product.objects.filter().order_by('-id')[:8]
    }


class ShopPageView(views.ListView):
    template_name = 'core/shop.html'
    model = Product

    extra_context = {
        'products': Product.objects.all()
    }


class ContactPageView(views.CreateView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy('index')


class WhyPageView(views.TemplateView):
    template_name = 'core/why.html'


@method_decorator(staff_member_required(login_url=reverse_lazy("login user")), name='dispatch')
class ListContactView(LoginRequiredMixin, views.ListView):
    model = Contact
    template_name = 'core/../../templates/contacts/list-contacts.html'

    def get_queryset(self):
        queryset = Contact.objects.all()

        return queryset


@method_decorator(staff_member_required(login_url=reverse_lazy("login user")), name='dispatch')
class DeleteContactView(LoginRequiredMixin, views.DeleteView):
    model = Contact
    template_name = 'contacts/delete-contact.html'
    success_url = reverse_lazy('list-contacts')
