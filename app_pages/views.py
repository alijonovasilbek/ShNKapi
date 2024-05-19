from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from article_app.models import ArticleModel
from journal_app.models import JournalModel
from django.db.models import Q
from .serializers import (ArticleSerializerViewcount,JournalSerializerLast,
                          ArticleSearchSerializer,JournalSearchSerializer)


#Bu view esa articllardan ko'rishlar soni bo'yicha
# eng ko'pini olib beradi yani paper
class LatestArticleView(APIView):
    def get(self, request):
        article = ArticleModel.objects.order_by('-article_view_count').first()
        if article:
            serializer = ArticleSerializerViewcount(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'No articles found'}, status=status.HTTP_404_NOT_FOUND)


#bu view esa oxirgi joylangan
# journalni olib beradi yani publication
class LatesJournalView(APIView):
    def get(self, request):
        article = JournalModel.objects.order_by('-journal_date').first()
        if article:
            serializer = JournalSerializerLast(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'No articles found'}, status=status.HTTP_404_NOT_FOUND)


# Bu search view umumiy search hisoblanadi va journal va articledan
# qidiradi masalan http://127.0.0.1:8000/search/?q=texnologiya
class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', None)
        if not query:
            return Response({'detail': 'Please provide a search query.'}, status=status.HTTP_400_BAD_REQUEST)

        # Search in ArticleModel
        article_results = ArticleModel.objects.filter(
            Q(article_title_uz__icontains=query) |
            Q(article_title_en__icontains=query) |
            Q(article_desc_uz__icontains=query) |
            Q(article_desc_en__icontains=query)
        )

        # Search in JournalModel
        journal_results = JournalModel.objects.filter(
            Q(journal_desc_uz__icontains=query) |
            Q(journal_desc_en__icontains=query)
        )

        articles_serializer = ArticleSearchSerializer(article_results, many=True)
        journals_serializer = JournalSearchSerializer(journal_results, many=True)

        return Response({
            'articles': articles_serializer.data,
            'journals': journals_serializer.data
        }, status=status.HTTP_200_OK)
