from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import People
from api.serializers import PeopleSerializer


class PeopleCreateView(APIView):
    serializer_class = PeopleSerializer

    def post(self, request, *args, **kwargs):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            people = serializer.save()
            return Response(serializer.data)
        else:
            return Response(data={'detail': 'Invalid input'}, status=400)


class PeopleReadView(RetrieveAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    lookup_field = 'iin'
