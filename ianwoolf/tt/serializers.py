from django.contrib.auth.models import User, Group
from tt.models import people, test2
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
class peopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = people
        fields = ('id','name','city','Email')
class test2Serializer(serializers.ModelSerializer):
    class Meta:
        model = test2
        fields = ('id','title','rating','actier','yingping','daoyan')
