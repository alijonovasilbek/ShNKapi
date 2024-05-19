from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password','first_name','last_name','birth_date','organization','scientific_degree','info')


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PasswordEmailCodeSend(serializers.Serializer):
    email=serializers.EmailField(required=True)


class PasswordCodeCheck(serializers.Serializer):
    code = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
