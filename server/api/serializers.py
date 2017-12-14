from rest_framework import serializers
from surgery.models import Patient


class PatientSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    birthdate = serializers.DateField()
    dni = serializers.IntegerField()

    def create(self, validated_data):
        return Patient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.dni = validated_data.get('dni', instance.dni)
        instance.save()
        return instance