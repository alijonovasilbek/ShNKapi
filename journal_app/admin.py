from django.contrib import admin
from .models import TagsModel,JournalModel
# Register your models here.

admin.site.register(TagsModel)
admin.site.register(JournalModel)