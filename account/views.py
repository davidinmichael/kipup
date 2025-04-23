from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response


class RegisterView(View):
    def get(self, request):
        return render(request, "account/register.html")

class LoginView(View):
    def get(self, request):
        return render(request, "account/login.html")

class ProfileView(View):
    def get(self, request):
        user = request.user
        context = {
            "user": user,
        }
        return render(request, "account/profile.html", context)
