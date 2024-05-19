from rest_framework.fields import SerializerMethodField
from rest_framework.fields import SerializerMethodField

from .models import TagsModel,JournalModel
from rest_framework import  serializers


"""http://127.0.0.1:8000/journal/tags/?lang=en 'GET' dan foydalanganda query param orqali
kerakli tilni olishingiz mumkin default holatda ikkala tilni ham qaytaradi"""


class TagsGetSerializer(serializers.ModelSerializer):
     tags_lan=SerializerMethodField(method_name='get_lan',read_only=True)
     class Meta:
         model=TagsModel
         fields=('id','tags_lan')

     def get_lan(self,obj):
         try:
             lang=self.context['request'].GET['lang']
             if lang=='en':
                 return obj.tag_name_en
             return obj.tag_name_uz
         except:
             return {
                 'tag_uz':obj.tag_name_uz,
                 'tag_en':obj.tag_name_en
             }


"""http://127.0.0.1:8000/journal/tags/ 'GET' 
dan boshqa holatlarda hamma maydonlarni oladi"""


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model=TagsModel
        fields='__all__'


class JournalGetSerializer(serializers.ModelSerializer):
    journal_lan = SerializerMethodField(method_name='get_lan', read_only=True)
    journal_tags_name = SerializerMethodField(method_name='get_journal_tags', read_only=True)

    class Meta:
        model = JournalModel
        fields = ('id', 'journal_logo','journal_tags','journal_tags_name','journal_lan')

    def get_lan(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.journal_desc_en
            return obj.journal_desc_uz
        except:
            return {
                'journal_desc_uz': obj.journal_desc_uz,
                'journal_desc_en': obj.journal_desc_en
            }

    def get_journal_tags(self, obj):
        lang = self.context['request'].GET.get('lang', None)
        if lang == 'en':
            return [tag.tag_name_en for tag in obj.journal_tags.all()]
        elif lang == 'uz':
            return [tag.tag_name_uz for tag in obj.journal_tags.all()]
        else:
            return [{'tag_uz': tag.tag_name_uz, 'tag_en': tag.tag_name_en} for tag in obj.journal_tags.all()]


""" Bu serializer GET dan boshqa methodlar uchun ishlaydi yani PUT, PUTCH,DELETE"""
class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model=JournalModel
        fields=('id','journal_logo','journal_desc_uz','journal_desc_en','journal_tags')

