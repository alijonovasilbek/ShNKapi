from rest_framework import serializers
from article_app.models import ArticleModel
from journal_app.models import JournalModel


class ArticleSerializerViewcount(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = '__all__'


class JournalSerializerLast(serializers.ModelSerializer):
    class Meta:
        model = JournalModel
        fields = '__all__'


#Search articledan shu fieldlardan qidiradi
class ArticleSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ['article_title_uz', 'article_title_en', 'article_desc_uz',
                  'article_desc_en', 'article_date', 'article_view_count']


#Journaldan shu fieldlardan qidiradi
class JournalSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalModel
        fields = ['journal_desc_uz', 'journal_desc_en', 'journal_date']


