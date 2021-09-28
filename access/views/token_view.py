from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from access.serializers import TokenSerializer


class TokenView(APIView):
    """Lists the logged user's paychecks."""
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer

    def _access_api(self, data):
        username = data['username']
        password = data['password']

        try:
            user = User.objects.get(username=username)
            if user.check_password(password) is True and user.is_active:
                return user, False, ''
            else:
                return None, True, 'Login invalido. Tente outro login ou senha.'
        except User.DoesNotExist:
            return None, True, 'Login invalido. Tente outro login ou senha.'

    def post(self, request, format='json', *args, **kwargs):

        user, error, mens = self._access_api(request.data)
        if error:
            return Response(data={'detail': mens}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                token = Token.objects.get(user=user)
                token.delete()
            except Token.DoesNotExist:
                ...
            token = Token.objects.create(user=user)
            return Response(data={'token': str(token)}, status=status.HTTP_200_OK)
