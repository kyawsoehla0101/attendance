from rest_framework import serializers
from .models import Attendance, PersonProfile

class AttendanceSerializer(serializers.ModelSerializer):
    person_name = serializers.CharField(source='person.name', read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'person_name', 'date', 'timestamp', 'action']

class PersonProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonProfile
        fields = ['id', 'user', 'name', 'reg_no']
