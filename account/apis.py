from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status
from .serializers import (
	AccountSerializer, LoginSerializer,
)
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import (
	ValidationError, AuthenticationFailed,
	NotFound,
)

from .utils import (
	get_tokens_for_user,
)

from .models import Account


class RegisterApi(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
				{
					"detail": "Registration Successful!"
				},
				status.HTTP_201_CREATED
			)
        print(f"Errors: {serializer.errors}")
        raise ValidationError("Invalid form fields")
    
    
class LoginApi(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get("email", "")
            password = serializer.validated_data.get("password", "")
            
            try:
                user = Account.objects.get(email=email)
            except Account.DoesNotExist:
                raise NotFound("Invalid User Details")
            
            if user.check_password(password):
                data = {}
                data["message"] = "Login successful!"
                data["token"] = get_tokens_for_user(user)
                data["user"] = AccountSerializer(user).data
                return Response(
					{
						"detail": data,
					},
					status.HTTP_200_OK
				)
            raise AuthenticationFailed("Invalid email or password!")
        print(f"Errors: {serializer.errors}")
        raise AuthenticationFailed("Invalid form values")