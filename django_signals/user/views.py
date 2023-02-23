from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import UserSerializer

# Create your views here.

class UserCreateAPIView(APIView):
    def post(self,request):
        print('entered here ----------------')
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            UserSerializer.create(serializer.data)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
    