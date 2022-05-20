import json
from django.shortcuts import render
from django.http import JsonResponse
from clientprofile.serializers import ClientSerializer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework import permissions
from .models import ClientProfile
# Create your views here.

class client_view(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = (JSONParser, FormParser, MultiPartParser)

    def post(self, request, format = None):
        serializer = ClientSerializer(data=request.data)


