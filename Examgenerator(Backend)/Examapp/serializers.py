from rest_framework import serializers
from Examapp.models import Admin, Question, Result, Users

class QuestionSerilizer(serializers.ModelSerializer):
     
    qno = serializers.IntegerField()
    qtext=serializers.CharField(max_length=50,default='null')
    answer=serializers.CharField(max_length=50,default='null')
    op1=serializers.CharField(max_length=50,default='null')
    op2=serializers.CharField(max_length=50,default='null')
    op3=serializers.CharField(max_length=50,default='null')
    op4=serializers.CharField(max_length=50,default='null')
    subject=serializers.CharField(max_length=50,default='null')
                                   
    class Meta:
            model=Question
            fields='__all__'

class UsersSerilizers(serializers.ModelSerializer):
      
      class Meta:
            model=Users
            fields='__all__'


class AdminSerilizer(serializers.ModelSerializer):
      
      class Meta:
            model=Admin
            fields='__all__'


class ResultSerilizers(serializers.ModelSerializer):
      
      class Meta:
            model=Result
            fields='__all__'