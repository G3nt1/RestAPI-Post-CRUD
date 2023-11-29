from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


# Create your views here.
@api_view(['GET'])
def home(request):
    posts = Post.objects.all()
    serialize = PostSerializer(posts, many=True)
    return Response(serialize.data)


@api_view(['POST', 'GET'])
def create_post(request):
    data = request.data
    serialize = PostSerializer(data=data)
    if serialize.is_valid():
        serialize.save()
        return Response({'success': 'The post created successfully'}, status=201)
    else:
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
