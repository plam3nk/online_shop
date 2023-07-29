from django.shortcuts import render
from django.contrib.auth import views as auth_views, login, get_user_model
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views

from online_shop.accounts.forms import RegisterUserForm, ProfileEditForm, ProfileDeleteForm

# Create your views here.

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    form_class = RegisterUserForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'

    model = UserModel

    profile_image = static('images/person.png')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile_image'] = self.profile_image

        return context


class ProfileEditView(views.UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        pk = self.object.pk

        success_url = reverse_lazy('profile details', kwargs={'pk': pk})

        return success_url


# Test password - vaDSMPNGg96HE*J&

class ProfileDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    form_class = ProfileDeleteForm
    success_url = reverse_lazy('login user')
