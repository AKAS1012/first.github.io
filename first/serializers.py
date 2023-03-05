from .models import My_Name
from rest_framework import serializers

class MyNameSerializers(serializers.ModelSerializer):
    class Meta:
        model=My_Name
        fields= '__all__'