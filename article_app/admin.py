from django.contrib import admin
from .models import ArticleSphereModel,ArticleKeywordModel,ArticleCommentsModel,ArticleModel,JournalModel
# Register your models here.

admin.site.register(ArticleModel)
admin.site.register(ArticleSphereModel)
admin.site.register(ArticleKeywordModel)
admin.site.register(ArticleCommentsModel)
