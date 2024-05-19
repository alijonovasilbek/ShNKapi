from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import EmailSerializer


class SendEmailView(APIView):

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']

            try:
                send_mail(
                    subject,
                    message=f'Xabar Mavzusi : {subject}\n'
                            f'xabar matni :  {message}\n'
                            f'xabarchi emaili : {email}',
                    from_email='alijonovasilbek058@gmail.com',
                    recipient_list=[email],
                    fail_silently=False,
                )
                return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""{
    "email": "recipient@example.com",
    "subject": "Test Subject",
    "message": "This is a test message."
}

emailga xabar yubormoqchi bo'lsangiz brauzerda shu ko'rinishda yuborsangiz bo'ladi
"""