from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.edit import CreateView, FormView
from .forms import RegisterForm, LoginForm


class RegisterView(CreateView):

    form_class = RegisterForm
    template_name = "account/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class LoginView(FormView):
    form_class = LoginForm
    template_name = "account/login.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        request = self.request
        cleaned_data = form.cleaned_data
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = (
                request.POST.get("next")
                or request.GET.get("next")
                or self.get_success_url()
            )
            return redirect(next_url)
        else:
            form.add_error(None, "Invalid username or password")
            return self.form_invalid(self, form)


class LogoutView(View):
    def get(self, request):
        return redirect("home")

    def post(self, request):
        logout(request)
        return redirect("login")
