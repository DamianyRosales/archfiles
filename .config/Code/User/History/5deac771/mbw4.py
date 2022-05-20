from clientprofile.models import ClientProfile

from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientProfile
        fields = '__all__'

