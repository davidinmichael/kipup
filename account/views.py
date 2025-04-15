from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterView(View):
    def get(self, request):
        return render(request, "account/register.html")
