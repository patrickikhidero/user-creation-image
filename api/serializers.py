from dataclasses import fields
from django.urls import clear_script_prefix
from  rest_framework import  serializers
from .models import User
import cloudinary.uploader



class RegisterSerializers(serializers.ModelSerializer):

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = ['email', 'username', 'profile_image', 'first_name', 'last_name']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs



class EditProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    profile_image = serializers.ImageField(required=False) or serializers.URLField(required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_image']
    
    def validate_profile_image(self, profile_image):
        try:
            image = cloudinary.uploader.upload(profile_image)
            return image["url"]
        except Exception as error:
            raise serializers.ValidationError(str(error))
            
    def to_representation(self, obj):
        return {"username": obj.username,
                "first_name": obj.first_name,
                "last_name": obj.last_name,
                "email": obj.email,
                "profile_image": obj.profile_image
                }
