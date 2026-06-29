from django.contrib import admin
from .models import Employee
from .models import Circular
from .models import Register

admin.site.register(Employee)
admin.site.register(Circular)
admin.site.register(Register)