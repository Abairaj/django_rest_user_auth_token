from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import UserSerializer
from .models import users
from rest_framework.authtoken.models import Token
# Create your views here.




class UserCreateAPIView(APIView):
    def post(self,request):
        print('entered here ----------------')
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = users.objects.get(email = serializer.data['email'])
            token_obj,_ = Token.objects.get_or_create(user = user)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
    