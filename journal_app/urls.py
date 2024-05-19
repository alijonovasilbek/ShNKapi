from rest_framework.routers import DefaultRouter
from .views import TagsView,JournalView

router=DefaultRouter()

router.register(r'tags',TagsView,basename='tags')
router.register(r'journal',JournalView,basename='journal')

urlpatterns=router.urls