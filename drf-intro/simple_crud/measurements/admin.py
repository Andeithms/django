from django.contrib import admin
from .models import Project, Measurement


class ProjectAdmin(admin.ModelAdmin):
    pass


class MeasurementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Measurement, MeasurementAdmin)
