from django.shortcuts import render
from .models import Business
from django.db.models import F
from .serializer import BusinessSerializers
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User, auth


# Create your views here.
def mainhome(request):
    
    obj = Business.objects.annotate(property=F('asset') - F('liability')).order_by('property')
    context = {'obj' : obj }
    return render(request, 'myapp/index.html', context)

def base(request):
    
    q = Business.objects.all()
    prop = {'q' : q }
    return render(request, 'myapp/base.html', prop)


class business_api(APIView):
    def get(self,request):
        data = Business.objects.annotate(property=F('asset') - F('liability')).order_by('property')
        serializer = BusinessSerializers(data, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        try:
            serializer = BusinessSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status =status.HTTP_200_OK)
            else:
                return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
           return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BusinessSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

