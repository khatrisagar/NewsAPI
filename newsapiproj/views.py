from tkinter import NE
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from NewsAPI.serializers import NewsSerializers
from NewsAPI.models import News

class mainView(APIView):
    permission_classes =()

    def get(self, request, *args, **kwargs):
        qs = News.objects.all()
        serializer = NewsSerializers(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = NewsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)