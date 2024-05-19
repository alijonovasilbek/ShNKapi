from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

"""Maqola yozish uchun talablar modeli"""


class RequirementsModel(models.Model):
    req_name_uz = models.CharField(max_length=333)
    req_name_en = models.CharField(max_length=333)
    req_text_uz = RichTextField()
    req_text_en = RichTextField()

    def __str__(self):
        return self.req_name_uz

    class Meta:
        ordering = ['-id']
        db_table = "Requirements table"
        verbose_name = "Requirements"


"""Tezkor savol-javoblar modeli"""


class FAQModel(models.Model):
    faq_question_uz = models.CharField(max_length=255)
    faq_question_en = models.CharField(max_length=255)
    faq_answer_uz = RichTextField()
    faq_answer_en = RichTextField()

    def __str__(self):
        return self.faq_question_uz

    class Meta:
        db_table='FAQ table'
        verbose_name='FAQS'
        ordering=['-id']





