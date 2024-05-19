from rest_framework.routers import DefaultRouter
from .views import SphereView,KeywordView,ArticleView,CommentView

router=DefaultRouter()

router.register(r'sphere',SphereView,basename='sphere')
router.register(r'keyword',KeywordView,basename='keyword')
router.register(r'article',ArticleView,basename='article')
router.register(r'comment',CommentView,basename='comment')

urlpatterns=router.urls

