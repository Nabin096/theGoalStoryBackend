from .models import *
from rest_framework import serializers
class ElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elements
        fields='__all__'

class BlogsMetaDataSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=BlogsMetaData
        fields = ('blogId', 'previewText', 'previewImage', 'date', 'author','title')
