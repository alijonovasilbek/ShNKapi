from django.shortcuts import render
from .serializers import TagsSerializer,JournalSerializer,TagsGetSerializer,JournalGetSerializer
from .models import  TagsModel,JournalModel
from rest_framework.viewsets import  ModelViewSet
from .permissions import IsAdminOrReadOnly



class TagsView(ModelViewSet):
    queryset = TagsModel.objects.all()
    # serializer_class = TagsSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method=="GET":
            return TagsGetSerializer
        return TagsSerializer


class JournalView(ModelViewSet):
    queryset = JournalModel.objects.all()
    # serializer_class = JournalSerializer
    permission_classes = [IsAdminOrReadOnly]


    def get_serializer_class(self):
        if self.request.method=='GET':
            return JournalGetSerializer
        return JournalSerializer