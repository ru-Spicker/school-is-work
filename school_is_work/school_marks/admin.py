from django.contrib import admin
from .models import Scholar, Discipline, Mark, MarksCost, Trimester

admin.site.register(Scholar)
admin.site.register(Discipline)
admin.site.register(Mark)
admin.site.register(MarksCost)
admin.site.register(Trimester)
