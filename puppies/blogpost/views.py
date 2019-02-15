from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from blogpost.models import Puppy
from blogpost.serializers import PuppySerializer, UserSerializer

# Create your views here.
@api_view(['GET','DELETE', 'PUT'])
def get_delete_update_puppy(request, pk):
    try:
        puppy = Puppy.objects.get(pk=pk)
    except Puppy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializers = PuppySerializer(puppy)
        return Response(serializers.data)

    elif request.method == 'DELETE':
        puppy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  
    elif  request.method == 'PUT':
        serializer = PuppySerializer(puppy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_puppies(request):
    if  request.method =='GET':
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data ={'name':request.data.get('name'),'age':request.data.get('age'),
        'breed':request.data.get('breed'),'color':request.data.get('color')}
        serializer=PuppySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_user(request):
    permission_classes = ()
    authentication_classes = ()
    if request.method =='POST':
        data = {'username':request.data.get('username'),'email':request.data.get('email'),
        'password':request.data.get('password')}
        
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    authentication_classes = ()
    if request.method == 'POST':
        data = {'username':request.data.get('username'),'email':request.data.get('email'),
        'password':request.data.get('password')}
        user = authenticate(data)
        if user:
            return Response({'token':user.auth_token.key})
        return Response({'error':'wrong credentials'},status=status.HTTP_404_NOT_FOUND)
