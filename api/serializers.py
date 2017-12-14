from rest_framework import serializers


class PatientSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    birthdate = serializers.DateField()
    dni = serializers.IntegerField()