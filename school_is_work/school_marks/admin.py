from django.contrib import admin
from .models import Scholar, Discipline, Mark, MarksCost

admin.site.register(Scholar)
admin.site.register(Discipline)
admin.site.register(Mark)
admin.site.register(MarksCost)
