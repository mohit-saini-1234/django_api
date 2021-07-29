from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework import status
# Create your views here.

from todo.models import Todo
from todo.serializers import TodoSerializer


@api_view()
def index(request):
    todo = Todo.objects.get(pk=1)
    ser = TodoSerializer(todo)
    return Response(request.query_params) 


@api_view(["POST"])
def dummy(request):
    todo = Todo(task=request.data["task"])
    todo.save()
    return Response(request.data) 

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


