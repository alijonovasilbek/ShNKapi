from .models import RequirementsModel,FAQModel
from .serializers import RequirementSerializer,FAQSerializer,RequirementsPostSerializer,FAQPostSerializer
from rest_framework.viewsets import  ModelViewSet
from journal_app.permissions import IsAdminOrReadOnly


class RequirementsView(ModelViewSet):
    queryset = RequirementsModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method=='GET':
            return  RequirementSerializer
        return RequirementsPostSerializer


class FAQView(ModelViewSet):
    queryset = FAQModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FAQSerializer
        return FAQPostSerializer


