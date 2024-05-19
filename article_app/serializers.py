from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import ArticleSphereModel,ArticleKeywordModel,ArticleCommentsModel,ArticleModel


class SphereGetSerializer(serializers.ModelSerializer):
    sphere_lan = SerializerMethodField(method_name='get_lan', read_only=True)

    class Meta:
        model = ArticleSphereModel
        fields = ('id', 'sphere_lan')

    def get_lan(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.sphere_name_en
            return obj.sphere_name_uz
        except:
            return {
                'sphere_uz': obj.sphere_name_uz,
                'sphere_en': obj.sphere_name_en
            }


class SphereSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArticleSphereModel
        fields="__all__"


class KeywordGetSerializer(serializers.ModelSerializer):
    sphere_lan = SerializerMethodField(method_name='get_lan', read_only=True)

    class Meta:
        model = ArticleKeywordModel
        fields = ('id', 'sphere_lan')

    def get_lan(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.key_name_en
            return obj.key_name_uz
        except:
            return {
                'keyword_uz': obj.key_name_uz,
                'keyword_en': obj.key_name_en
            }


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArticleKeywordModel
        fields="__all__"


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArticleCommentsModel
        fields="__all__"
        extra_kwargs={
            'comment_user':{'read_only':True}
        }


#Faqat article get uchun serializer 2 ta tilda
class ArticleGetSerializer(serializers.ModelSerializer):
    article_title_lan = SerializerMethodField(method_name='get_lan', read_only=True)
    article_desc_lan = SerializerMethodField(method_name='get_lan1', read_only=True)
    article_text_lan = SerializerMethodField(method_name='get_lan2', read_only=True)
    article_keyword_lan=SerializerMethodField(method_name='get_lan3',read_only=True)
    article_sphere_lan=SerializerMethodField(method_name='get_lan4',read_only=True)
    article_journal_lan=SerializerMethodField(method_name='get_lan5',read_only=True)
    article_author_username=SerializerMethodField(method_name='get_author',read_only=True)
    article_comments = CommentsSerializer(many=True, read_only=True, source='articlecommentsmodel_set')

    class Meta:
        model = ArticleModel
        fields = ('id', 'article_title_lan','article_desc_lan',
                  'article_text_lan','article_references','article_file',
                  'article_view_count','article_sphere',
                  'article_journal','article_author','article_sphere_lan','article_keyword_lan',
                  'article_journal_lan','article_author_username','article_comments')

    def get_lan(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.article_title_en
            return obj.article_title_uz
        except:
            return {
                'title_uz': obj.article_title_uz,
                'title_en': obj.article_title_en
            }

    def get_lan1(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.article_desc_en
            return obj.article_desc_uz
        except:
            return {
                'desc_uz': obj.article_desc_uz,
                'desc_en': obj.article_desc_en
            }

    def get_lan2(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.article_text_en
            return obj.article_text_uz
        except:
            return {
                'article_text_uz': obj.article_text_uz,
                'article_text_en': obj.article_text_en
            }

    def get_lan3(self, obj):
        lang = self.context['request'].GET.get('lang', None)
        if lang == 'en':
            return  obj.article_keywords.key_name_en
        elif lang == 'uz':
            return obj.article_keywords.key_name_uz
        else:
            return   {
                'article_key_name_uz':obj.article_keywords.key_name_uz ,
                'article_key_name_en': obj.article_keywords.key_name_en
            }

    def get_lan4(self, obj):
        lang = self.context['request'].GET.get('lang', None)
        if lang == 'en':
            return obj.article_sphere.sphere_name_en
        elif lang == 'uz':
            return obj.article_sphere.sphere_name_uz
        else:
            return {
                'article_sphere_uz': obj.article_sphere.sphere_name_uz ,
                'article_sphere_en': obj.article_sphere.sphere_name_en
            }

    def get_lan5(self, obj):
        lang = self.context['request'].GET.get('lang', None)
        if lang == 'en':
            return obj.article_journal.journal_desc_en
        elif lang == 'uz':
            return obj.article_journal.journal_desc_uz
        else:
            return {
                'article_journal_uz': obj.article_journal.journal_desc_uz,
                'article_journal_en': obj.article_journal.journal_desc_en
            }

    def get_author(self, obj):
       return obj.article_author.username


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArticleModel
        fields="__all__"
        extra_kwargs={
            'article_author':{'read_only':True},
            'article_view_count':{'read_only':True},
            'article_date':{'read_only':True}
        }






