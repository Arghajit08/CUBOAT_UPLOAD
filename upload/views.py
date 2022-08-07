from django.shortcuts import render
from .serializers import UploadSerializers
# Create your views here.
from .models import Upload
from rest_framework.views import APIView
from rest_framework.response import Response

def home(request):
    return render(request, "index.html")
    #Here i will get data from site
    #Then i will create instance of Upload for each data fetched
    #Then i will save instance of Upload in database
    #Next create get api foe all uploads
def result(request):
    title=request.GET['title']
    author1=request.GET['author1']
    author2=request.GET['author2']
    author3=request.GET['author3']
    publication_link=request.GET['publication_link']
    print(title,author1,author2,author3,publication_link)
    serializer = UploadSerializers(data=request.GET)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return render(request, "result.html")

class GetView(APIView):
    def get(self, request):
        user = Upload.objects.all()
        serializer = UploadSerializers(user,many=True)
        return Response(serializer.data)
