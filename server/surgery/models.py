from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField('Fecha de Nacimiento')
    dni = models.IntegerField(default=0)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Surgeon(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Surgery(models.Model):
    patient = models.ForeignKey(Patient)
    surgeon = models.ForeignKey(Surgeon)
    date = models.DateTimeField('Fecha de Cirugía')

    def __str__(self):
        return "{0} {1}".format(self.patient.last_name, self.date)