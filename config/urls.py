from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Swagger Sozlamalari
schema_view = get_schema_view(
   openapi.Info(
      title="JOURNAL API with articles",
      default_version='v1',
      description="You can find interesting magazines and articles on this api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,)
)

# SimpleJWT uchun token olish va tokenni yangilash
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Swagger uchun url va boshqa applar uchun url
urlpatterns += [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path("admin/", admin.site.urls),
   path('users/',include('users.urls')),
    path('',include('journal_app.urls')),
    path('',include('requirement_faq_app.urls')),
    path('',include('contact_app.urls')),
    path('',include('article_app.urls')),
    path('',include('app_pages.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
