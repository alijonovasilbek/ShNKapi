from  rest_framework.permissions import BasePermission


#journal faqatgina superuser qo'sha oladi qolgan user get qila oladi
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.method=='GET'
