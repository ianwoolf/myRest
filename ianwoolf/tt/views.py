from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import render, render_to_response, RequestContext
from .forms import peopleForm
#rest_form
from django.contrib.auth.models import User, Group
#rest_ser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from tt.serializers import UserSerializer, GroupSerializer, peopleSerializer, test2Serializer
from tt.models import people, test2
import util

#from rest_framework.response import Response
from django.conf import settings 
def home(request):
    form = peopleForm(request.POST or None)            #form model
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("zz.html",
                              locals(),
                              context_instance=RequestContext(request))

class PeopleList2(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = people.objects.all()
    serializer_class = peopleSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class PeopleDetail2(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,  generics.GenericAPIView):
    queryset = people.objects.all()
    serializer_class = peopleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
#~~~~~~~~~~~~~~~~~~~~~~~~~~
class PeopleList3(generics.ListCreateAPIView):
    queryset = people.objects.all()
    serializer_class = peopleSerializer


class PeopleDetail3(generics.RetrieveUpdateDestroyAPIView):
    queryset = people.objects.all()
    serializer_class = peopleSerializer
class DBMVList3(generics.ListCreateAPIView):
    queryset = test2.objects.all()
    serializer_class = test2Serializer


class DBMVDetail3(generics.RetrieveUpdateDestroyAPIView):
    queryset = test2.objects.all()
    serializer_class = test2Serializer
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def myown(request):
    return render_to_response("index.html",
                             )
def myown2(request):
    if request.method == 'GET':
        Num = request.REQUEST.get('Num','null')
        pass
    elif request.method == 'POST':
        Num = request.REQUEST.post('Num','null')
        pass
    result = util.ReadGpData(Num)
    print result
    return render_to_response("gup.html",)
    return HttpResponse(result)
