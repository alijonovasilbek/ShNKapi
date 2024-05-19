from  rest_framework.permissions import BasePermission


#Articleni faqat authori yoki superuser tahrirlay oladi
#qolgan userlarga faqat get
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.method in ['GET']:
            return True
        return obj.article_author == request.user


#bu permission comment faqat o'zi yozgan user update delete qila oladi
#qolgan userlar uchun faqat get methodi ishlaydi
class CommentPermission(BasePermission):
    def has_permission(self, request, view):
        if  request.method=="GET":
            return True
        return request.user
