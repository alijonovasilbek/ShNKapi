from rest_framework.routers import DefaultRouter
from .views import RequirementsView,FAQView
router=DefaultRouter()

router.register(r'requirements',RequirementsView,basename='requirements')
router.register(r'faq',FAQView,basename='faq')

urlpatterns=router.urls