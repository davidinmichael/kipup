from django.urls import path
from .views import (
	RegisterView, LoginView,
	ProfileView,
)
from account.apis import (
	RegisterApi, LoginApi,
)


urlpatterns = [
	path("register/", RegisterView.as_view(), name="register"),
	path("login/", LoginView.as_view(), name="login"),
	path("profile/", ProfileView.as_view(), name="profile"),
	
	# API Endpoints
	path("api/register/", RegisterApi.as_view()),
	path("api/login/", LoginApi.as_view()),
]