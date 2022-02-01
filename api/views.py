from operator import ge
from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RegisterSerializers, EditProfileSerializer
from rest_framework.response import Response
from .models import User
from util.utils import Util
import requests
import json
from django.http.response import Http404


class BackEndAssessment(generics.GenericAPIView):
    serializer_class = RegisterSerializers
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            username = serializer.validated_data['username']
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            password = Util.generate_password()
            otp = Util.generate_otp()

            email_body = f''' Hello {username} this is your auto generated password : {password} and otp: {otp}. 
            Thanks for registering'''
            data = {"email_body": email_body, 'to_email': [email],
                    'email_subject': "Registration details"}

            try:
                Util.send_email(data)
                user = User.objects.create(
                    email=email,
                    password=Util.encode_password(password),
                    username=username,
                    otp=otp,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                return Response({"success": f"{username} created successfully and email sent, please check your mail"},
                                status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BackendAssessmentUpdate(generics.GenericAPIView):
    serializer_class = EditProfileSerializer
    queryset = User.objects.all()

    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response({"message": "User data updated successfully",
                            "user_data": serializer.data}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BackendAssessmentGet(generics.GenericAPIView):
    serializer_class = EditProfileSerializer
    queryset = User.objects.all()
    def get(self, *args, **kwargs):
        api_key = "d2d3e4f69596b98f5f12532bfc485c0a"
        lat = "48.208176"
        lon = "16.373819"
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (
            lat, lon, api_key)
        response = requests.get(url)
        data = response.json()
        return Response({"data": data}, status=status.HTTP_200_OK)
