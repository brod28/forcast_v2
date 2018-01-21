from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed,ParseError
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed,ParseError
from rest_framework.views import APIView
from django.contrib.auth import authenticate
import datetime

class Login(APIView):
    """
        Login API, 
        expected params:
        username and password
        return:
        token
    """
    def post(self, request, format=None):
        try:
            # authenticate user based on username and password from the request
            user = authenticate(username=request.data['username'], password=request.data['password'])
        except:
            raise ParseError({"message":"something went wrong"})
        if user is not None:
            
            # getting or creating token to response back 
            token,created = Token.objects.get_or_create(user=request.user)

            if not created:
                # update the created time of the token to keep it valid
                token.created = datetime.datetime.utcnow()
                token.save()
            
            # response token key
            return Response({"token":token.key})
        else:
            raise AuthenticationFailed({"message":"You did provide correct username and password"})
            