from django.contrib import admin
from .models import Scholar, Discipline, Mark, MarksCost, Trimester, Grade, School


class MarksAdmin(admin.ModelAdmin):
	list_filter = ['scholar']


class MarksInline(admin.TabularInline):
	model = Mark
	extra = 3


class ScholarAdmin(admin.ModelAdmin):
	inlines = [MarksInline]


admin.site.register(Scholar, ScholarAdmin)
admin.site.register(Discipline)
admin.site.register(Mark, MarksAdmin)
admin.site.register(MarksCost)
admin.site.register(Trimester)
admin.site.register(Grade)
admin.site.register(School)

