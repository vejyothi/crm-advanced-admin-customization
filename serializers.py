from rest_framework import serializers
from testapp.models import roles,user_status,User,Contact_Status,Contact,task_status,todo_type,todo_desc,Notes

class rolesSerializer(serializers.ModelSerializer):

    class Meta:
        model=roles
        fields='__all__'
class user_statusSerializer(serializers.ModelSerializer):

    class Meta:
        model=user_status
        fields='__all__'      
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'      
class Contact_StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model=Contact_Status
        fields='__all__'   
class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model=Contact
        fields='__all__'   
class task_statusSerializer(serializers.ModelSerializer):

    class Meta:
        model=task_status
        fields='__all__'   
class todo_typeSerializer(serializers.ModelSerializer):

    class Meta:
        model=todo_type
        fields='__all__'   
class todo_descSerializer(serializers.ModelSerializer):

    class Meta:
        model=todo_desc
        fields='__all__'   
class NotesSerializer(serializers.ModelSerializer):

    class Meta:
        model=Notes
        fields='__all__'   
        