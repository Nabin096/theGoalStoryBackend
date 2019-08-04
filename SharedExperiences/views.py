from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import BlogIdForm
from django.core.paginator import Paginator
from rest_framework import status
# Create your views here.

class getBlogApi(APIView):
    def get(self, request,id):
        elements = Elements.objects.filter(blogId=id).order_by('sequenceNo')
        serializers=ElementsSerializer(elements,many=True,context={'request': request})

        return Response(serializers.data)


class getAllBlogs(APIView):
    def get(self,request,id,genre=None):
        try:
            if genre == "all":
                elements = BlogsMetaData.objects.filter().order_by('-date')
            else:
                elements = BlogsMetaData.objects.filter(genre=genre).order_by('-date')

            paginator = Paginator(elements, 4)
            page = paginator.page(id)
            serialiser = BlogsMetaDataSerialiser(instance=page, many=True, context={'request': request})
            return Response(serialiser.data)
        except:
            pass



class getTopBlog(APIView):
    def get(self,request,genre):
        if genre == "all":
            element = BlogsMetaData.objects.filter().order_by('-blogId')[0]
        else:
            element = BlogsMetaData.objects.filter(genre=genre).order_by('-blogId')[0]
        serialiser=BlogsMetaDataSerialiser(element,context={'request': request})
        return Response(serialiser.data)