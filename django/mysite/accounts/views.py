from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, username=email, password=password)

    return Response({'success': False, 'message': 'Identifiants invalides.'}, status=status.HTTP_401_UNAUTHORIZED)
