import json
from django.core import serializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import GetUserSerializer

from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse


class GetUser(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GetUserSerializer

    def get(self, request, email, format=None):

        obj = User.objects.get(email=email)

        data = serializers.serialize('json', [obj, ])

        struct = json.loads(data)
        data = json.dumps(struct[0])

        return HttpResponse(data)
