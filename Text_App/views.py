#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer 
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def task_list(request):
	if request.method=='GET':
		obj= Task.objects.all()
		serializer= TaskSerializer(obj,many=True)
		return Response(serializer.data)
	elif request.method=='POST':
		serializer= TaskSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)