from django.contrib import admin
from .models import Surgeon, Patient, Surgery

admin.site.register(Surgeon)
admin.site.register(Patient)
admin.site.register(Surgery)