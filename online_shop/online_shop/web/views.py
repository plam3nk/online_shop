from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from online_shop.products.models import Product
from online_shop.web.forms import ContactForm, TestimonialForm
from online_shop.web.models import Contact, Testimonial


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


class TestimonialsPageView(views.ListView):
    template_name = 'core/testimonials.html'
    model = Testimonial
    paginate_by = 1
    ordering = ['-id']

    context_object_name = 'reviews'


class CreateTestimonialPageView(LoginRequiredMixin, views.CreateView):
    template_name = 'core/create-testimonial.html'
    form_class = TestimonialForm
    model = Testimonial
    success_url = reverse_lazy('testimonials')

    def form_valid(self, form):
        user = self.request.user

        existing_review = Testimonial.objects.filter(user=user).first()
        if existing_review:
            form.add_error(None, 'You have already submitted a review.')
            return self.form_invalid(form)

        form.instance.user = user
        return super().form_valid(form)


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
