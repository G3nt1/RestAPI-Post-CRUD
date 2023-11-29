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


@api_view(['DELETE'])
def delete_post(request):
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({'success': 'The post deleted successfully'}, status=200)
    except Post.DoesNotExist:
        return Response({'Error': 'The post does not exist'}, status=404)


@api_view(['GET'])
def get_post(request):
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({'Error': 'The post does not exist'})


@api_view(['PUT'])
def update_post(request):
    post_id = request.data.get('post_id')
    new_title = request.data.get('new_title')
    new_content = request.data.get('new_content')

    try:
        post = Post.objects.get(id=post_id)
        if new_title:
            post.title = new_title
        if new_content:
            post.content = new_content
        post.save()
        return Response({'success': 'The post updated successfully Updated'}, status=200)

    except Post.DoesNotExist:
        return Response({'Error': 'The post does not exist'})
