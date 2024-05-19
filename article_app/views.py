from rest_framework.viewsets import ModelViewSet
from .serializers import (SphereSerializer,SphereGetSerializer,KeywordGetSerializer,
                          KeywordSerializer,ArticleGetSerializer,ArticleSerializer,CommentsSerializer)
from .models import ArticleSphereModel,ArticleKeywordModel,ArticleCommentsModel,ArticleModel,JournalModel
from journal_app.permissions import  IsAdminOrReadOnly
from .permissions import IsAuthorOrReadOnly,CommentPermission
from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework import  filters
from .paginations import  ArticlePagination
from  time import  time


class SphereView(ModelViewSet):
    queryset = ArticleSphereModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method=="GET":
            return SphereGetSerializer
        return SphereSerializer


class KeywordView(ModelViewSet):
    queryset = ArticleKeywordModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method=="GET":
            return KeywordGetSerializer
        return KeywordSerializer


"""Article uchun view_count ko'rishlar soni bunda cookie dan foydalandim
va bunda user 10 sekund oralatib view countni oshirishi mumkin tinmay f5 bosilganda ham
10 sekundan keyin bittasi qabul qilinadi"""


class ArticleView(ModelViewSet):
    queryset = ArticleModel.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = ArticlePagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['article_sphere', 'article_title_uz','article_keywords','article_journal','article_author']
    search_fields = ['article_title_uz']

    def get_serializer_class(self):
        if self.request.method=="GET":
            return ArticleGetSerializer
        return  ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(article_author=self.request.user)
        return serializer.save

    def retrieve(self, request,pk=None, *args, **kwargs):
        if 'viewed' in request.COOKIES:
            if time()-float(request.COOKIES['viewed'])>10:
                up=True
            else:
                up=False
        else:
            up=True

        if up:
            art=ArticleModel.objects.get(pk=pk).article_view_count
            ArticleModel.objects.filter(pk=pk).update(article_view_count=art+1)
        response=super().retrieve(request,pk,*args,**kwargs)
        response.set_cookie('viewed',time())
        return response


#Comment uchun view bunda comment yozgan
# userni muallif sifatida avtomatik qo'shadi
class CommentView(ModelViewSet):
    queryset = ArticleCommentsModel.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [CommentPermission]

    def perform_create(self, serializer):
        serializer.save(comment_user=self.request.user)
        return serializer.save




