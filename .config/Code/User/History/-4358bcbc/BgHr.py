import json
from django.shortcuts import render
from django.http import JsonResponse
from clientprofile import serializers
from clientprofile.serializers import ClientSerializer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework import permissions, status
from .models import ClientProfile

# Create your views here.

class client_view(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = (JSONParser, FormParser, MultiPartParser)

    def get(self, request):
        clients = ClientProfile.objects.all()
        serializer = ClientSerializer(clients, many = True)

        return JsonResponse(data=serializer.data, safe = False)



    def post(self, request):
        
        serializer = ClientSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return JsonResponse(data=serializer.datam, status = status.HTTP_201_CREATED)
        
        return JsonResponse(data=serializer.errors, status = status.HTTP_400_BAD_REQUEST)



