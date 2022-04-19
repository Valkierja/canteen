import imp
from django.contrib import admin

# Register your models here.

from canteenapp.models import ChaoCai, DinnerTable
admin.site.register(ChaoCai)
admin.site.register(DinnerTable)
