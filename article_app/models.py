from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import  RichTextField
from journal_app.models import JournalModel


User=get_user_model()


class ArticleSphereModel(models.Model):
    sphere_name_uz=models.CharField(max_length=222)
    sphere_name_en=models.CharField(max_length=222)

    def __str__(self):
        return self.sphere_name_uz

    class Meta:
        verbose_name='ArticleSphereModel'
        db_table='Sphere table'


class ArticleKeywordModel(models.Model):
    key_name_uz = models.CharField(max_length=222)
    key_name_en = models.CharField(max_length=222)

    def __str__(self):
        return self.key_name_uz

    class Meta:
        verbose_name = 'KeyWord'
        db_table = 'Keyword table'



"""Article uchun Model yaratildi figmada paper 
 va umumiy hammasi 2 ta til uchun mo'jjallandi"""


class ArticleModel(models.Model):
    article_title_uz=models.CharField(max_length=333)
    article_title_en=models.CharField(max_length=333)
    article_desc_uz=models.CharField(max_length=333)
    article_desc_en=models.CharField(max_length=333)
    article_text_uz=RichTextField()
    article_text_en=RichTextField()
    article_references=models.CharField(max_length=333)
    article_file=models.FileField(upload_to='article/')
    article_date=models.DateTimeField(auto_now_add=True)
    article_view_count=models.IntegerField(default=0)
    article_keywords=models.ForeignKey(ArticleKeywordModel,on_delete=models.CASCADE)
    article_sphere=models.ForeignKey(ArticleSphereModel,on_delete=models.CASCADE)
    article_journal=models.ForeignKey(JournalModel,on_delete=models.CASCADE)
    article_author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.article_title_uz

    class Meta:
        db_table='Article table'
        verbose_name='Article'
        ordering=['-article_date']


#Articlega comment ya'ni figmadagi Annotation
class ArticleCommentsModel(models.Model):
    comment_text=models.CharField(max_length=222)
    comment_article=models.ForeignKey(ArticleModel,on_delete=models.CASCADE)
    comment_user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text

    class Meta:
        db_table='ArticleComment table'
        verbose_name='ArticleComment'
