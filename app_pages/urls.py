from  django.urls import path
from .views import LatestArticleView,LatesJournalView,SearchView

urlpatterns = [
    path('latest-article1/', LatestArticleView.as_view(), name='latest-article'), #eng ko'p ko'rilgan article olish uchun endpoint
    path('latest-journal1/', LatesJournalView.as_view(), name='latest-journal'),  #oxirgi joylangan journal uchun endpoint
    path('search/', SearchView.as_view(), name='search') # umumiy search uchun endpoint
]