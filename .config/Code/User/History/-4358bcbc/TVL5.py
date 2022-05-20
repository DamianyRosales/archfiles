from django.http import Http404, JsonResponse
from clientprofile.serializers import ClientSerializer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework import permissions, status
from .models import ClientProfile

# Create your views here.

class ClientList_view(APIView):

    permission_classes = [permissions.AllowAny]
    parser_classes = (JSONParser, FormParser, MultiPartParser, FileUploadParser)

    def get(self, request, format = None):
        clients = ClientProfile.objects.all()
        serializer = ClientSerializer(clients, many = True)

        return JsonResponse(data=serializer.data, safe = False)


    def post(self, request, format = None):
        
        serializer = ClientSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return JsonResponse(data=serializer.datam, status = status.HTTP_201_CREATED)
        
        return JsonResponse(data=serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ClientDetail_view(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = (JSONParser, FormParser, MultiPartParser, FileUploadParser)

    def get_object(self, pk):
        try:
            return ClientProfile.objects.get(pk = pk)
        except ClientProfile.DoesNotExist:
            raise Http404

    def get(self, pk, request, format = None):
        client = self.get_object(pk = pk)
        serializer = ClientSerializer(client)

        return JsonResponse(data=serializer.data, safe = False)


    def put(self, request, pk, format=None):

        client = self.get_object(pk = pk)
        serializer = ClientSerializer(client, data = request.data)

        if serializer.is_valid():
            serializer.save()
            
            return JsonResponse(data=serializer.data, status = status.HTTP_200_OK)
        
        return JsonResponse(data=serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format = None):
        client = self.get_object(pk = pk)
        client.delete()

        return JsonResponse(status = status.HTTP_204_NO_CONTENT) 
