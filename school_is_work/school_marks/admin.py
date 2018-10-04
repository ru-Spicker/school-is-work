from django.contrib import admin
from .models import Scholar, Discipline, Mark, MarksCost, Trimester, Grade, School

admin.site.register(Scholar)
admin.site.register(Discipline)
admin.site.register(Mark)
admin.site.register(MarksCost)
admin.site.register(Trimester)
admin.site.register(Grade)
admin.site.register(School)
