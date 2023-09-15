from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import People
from api.serializers import PeopleSerializer


class PeopleCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            iin = serializer.validated_data['iin']
            people = serializer.save(iin=iin)
            return Response(serializer.data)
        else:
            Response({'detail': 'Invalid input', 'errors': serializer.errors}, status=400)


class PeopleReadView(RetrieveAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    lookup_field = 'iin'
