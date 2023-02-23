from rest_framework import serializers
from.models import users

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = users
        fields = [
        "first_name",
        "last_name",
        "email",
        "mobile",
        "password",
        ]


    def create(self,validated_data):
        password = validated_data.pop("password")
        user = users.objects.create_user(password = password, **validated_data)
        return user
    
    def update(self,instance,validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))
        
        return super().update(instance,validated_data)


