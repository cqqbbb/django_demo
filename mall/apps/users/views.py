from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User

# Create your views here.


class RegisterUsernameCountAPIView(APIView):
    def get(self, request, username):
        count = User.objects.filter(username=username).count()
        context = {
            'count':count,
            'username': username
        }
        return Response(context)
