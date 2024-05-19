from rest_framework.fields import SerializerMethodField

from .models import RequirementsModel,FAQModel
from rest_framework import serializers

"""http://127.0.0.1:8000/journal/?lang=en queryparam orqali tilni ajratib
 olish mumkin default holatda 2 ta tilda ham uzatadi"""


class RequirementSerializer(serializers.ModelSerializer):
    req_name_lan = SerializerMethodField(method_name='get_lan', read_only=True)
    req_text_lan = SerializerMethodField(method_name='get_lan1', read_only=True)

    class Meta:
        model = RequirementsModel
        fields = ('id', 'req_name_lan','req_text_lan')

    def get_lan(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.req_name_en
            return obj.req_name_uz
        except:
            return {
                'tag_uz': obj.req_name_uz,
                'tag_en': obj.req_name_en
            }

    def get_lan1(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.req_text_en
            return obj.req_text_uz
        except:
            return {
                'tag_uz': obj.req_text_uz,
                'tag_en': obj.req_text_en
            }



class RequirementsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=RequirementsModel
        fields='__all__'


"""http://127.0.0.1:8000/faq/?lang=en yordamin tilni tanlashingiz ham mumkin"""


class FAQSerializer(serializers.ModelSerializer):
    faq_question_lan = SerializerMethodField(method_name='get_lan', read_only=True)
    faq_answer_lan = SerializerMethodField(method_name='get_lan1', read_only=True)

    class Meta:
        model = RequirementsModel
        fields = ('id', 'faq_question_lan','faq_answer_lan')

    def get_lan(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.faq_question_en
            return obj.faq_question_uz
        except:
            return {
                'faq_question_uz': obj.faq_question_uz,
                'faq_question_en': obj.faq_question_en
            }

    def get_lan1(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.faq_answer_en
            return obj.faq_answer_uz
        except:
            return {
                'faq_answer_uz': obj.faq_answer_uz,
                'faq_answer_en': obj.faq_answer_en
            }


class FAQPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=FAQModel
        fields='__all__'