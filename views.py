from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  roles,user_status,User,Contact_Status,Contact,task_status,todo_type,todo_desc,Notes

from testapp.serializers import rolesSerializer,user_statusSerializer,UserSerializer,Contact_StatusSerializer,Contact_StatusSerializer,ContactSerializer,task_statusSerializer,todo_typeSerializer,todo_descSerializer,NotesSerializer
# Create your views here.
# from django.shortcuts import render
# from django.http import  HttpResponse
# Create your views here.
from .models import roles

def view_post(request):
    notess = notes.objects.all() 
    context = {'notess': notess}
    return render(request, 'frontend/notes.html', context)
 

class rolesList(APIView):

    def get(self,request):
         roles1=roles.objects.all()
         serializer=rolesSerializer(roles1,many=True)
         return Response(serializer.data)
    def post(self):
        pass
class user_statusList(APIView):

    def get(self,request):
         user_status1=user_status.objects.all()
         serializer=user_statusSerializer(user_status1,many=True)
         return Response(serializer.data)
    def post(self):
        pass
class UserList(APIView):

    def get(self,request):
         User1=User.objects.all()
         serializer=UserSerializer(User1,many=True)
         return Response(serializer.data)
    def post(self):
        pass
class Contact_StatusList(APIView):

    def get(self,request):
         Contact_Status1=user_status.objects.all()
         serializer=Contact_StatusSerializer(Contact_Status1,many=True)
         return Response(serializer.data)
    def post(self):
        pass
class ContactList(APIView):

    def get(self,request):
         Contact1=Contact.objects.all()
         serializer=user_statusSerializer(Contact1,many=True)
         return Response(serializer.data)
    def post(self):
        pass
class task_statusList(APIView):

    def get(self,request):
         task_status1=task_status.objects.all()
         serializer=task_statusSerializer(task_status1,many=True)
         return Response(serializer.data)
    def post(self):
        pass
class todo_typeList(APIView):

    def get(self,request):
         todo_type1=todo_type.objects.all()
         serializer=todo_typeSerializer(todo_type1,many=True)
         return Response(serializer.data)
    def post(self):
        pass
class todo_descList(APIView):

    def get(self,request):
         todo_desc1=todo_desc.objects.all()
         serializer=todo_descSerializer(todo_desc1,many=True)
         return Response(serializer.data)
    def post(self):
        pass
class NotesList(APIView):

    def get(self,request):
         Notes1=Notes.objects.all()
         serializer=NotesSerializer(Notes1,many=True)
         return Response(serializer.data)
    def post(self):
        pass
