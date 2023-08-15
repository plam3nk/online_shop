from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from online_shop.products.models import Product
from online_shop.web.forms import CreateContactForm, CreateTestimonialForm, CreateDiscountForm
from online_shop.web.models import Contact, Testimonial, Discount


# Create your views here.


class IndexPageView(views.ListView):
    template_name = 'core/index.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter().order_by('-id')[:8]

        return context


class ShopPageView(views.ListView):
    template_name = 'core/shop.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()

        return context


class ContactPageView(views.CreateView):
    template_name = 'core/contact.html'
    form_class = CreateContactForm
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
    form_class = CreateTestimonialForm
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


@method_decorator(staff_member_required(login_url=reverse_lazy("login user")), name='dispatch')
class ListAllDiscountsView(views.ListView):
    model = Discount
    template_name = 'discount/all-discounts-admin.html'

    def get_queryset(self):
        queryset = Discount.objects.all()

        return queryset


class ListUserDiscountsView(LoginRequiredMixin, views.ListView):
    model = Discount
    template_name = 'discount/user-discounts.html'

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Discount.objects.filter(user_id=user_id)

        return queryset


@method_decorator(staff_member_required(login_url=reverse_lazy("login user")), name='dispatch')
class DeleteDiscountView(views.DeleteView):
    model = Discount
    template_name = 'discount/delete-discount.html'
    success_url = reverse_lazy('index')


@method_decorator(staff_member_required(login_url=reverse_lazy("login user")), name='dispatch')
class CreateDiscountView(views.CreateView):
    model = Discount
    form_class = CreateDiscountForm
    template_name = 'discount/create-discount.html'
    success_url = reverse_lazy('all-discounts')

