from rest_framework import serializers

from api.models import People
from datetime import datetime


class PeopleSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = People
        fields = ['iin', 'age']

    def get_age(self, obj):
        iin = obj.iin
        year = int(iin[:2]) + 1900
        month = int(iin[2:4])
        day = int(iin[4:6])
        birthdate = datetime(year, month, day)
        current_date = datetime.now()
        age = current_date.year - birthdate.year - (
                (current_date.month, current_date.day) < (birthdate.month, birthdate.day))

        return age


