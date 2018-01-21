from rest_framework.response import Response
from weather import Weather
from .serializers import ForcastSerializer
from .models import Forcast
from rest_framework.views import APIView
from rest_framework.authentication import  BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed,ParseError

class ForcastDetails(APIView):
    """
        /api/forcast/{city}
        return 
        today's weather
    """
    # access to this endpoint just to authenticated with token users
    authentication_classes = ( BasicAuthentication,TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        try:
            # get city from url
            city = kwargs.get('city', '')
            if city=='':
                raise ParseError({"message":"city is not provided"})
            
            # third party library to get weather forcase by city name
            weather = Weather()
            location = weather.lookup_by_location(city)
            condition = location.condition()

            # parse third party object to model
            forcast = Forcast().parse(condition)

            # serializer the model to json and response it
            result=ForcastSerializer(forcast).data
            return Response(result)
        except:
            raise ParseError({"message":"something went wrong"})



