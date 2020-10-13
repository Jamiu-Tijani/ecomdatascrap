from rest_framework import serializers
from . import models

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.data
        fields = ['title', 'url','img_link','description']
    

