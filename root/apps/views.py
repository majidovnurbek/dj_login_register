from django.contrib.auth import authenticate,login
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import LoginForm, RegisterForm
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'



class RegisterView(FormView):
    template_name = 'auth/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user=authenticate(self.request,username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None,'invalid username or password')
            return self.form_invalid(form)
