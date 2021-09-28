from django.contrib import admin

# Register your models here.

from .models import Diarys, Doctors, Schedules, Specialties, Appointments


class SchedulesInline(admin.TabularInline):
    model = Schedules


class DiarysAdmin(admin.ModelAdmin):

    list_display = ['doctor', 'day']
    search_fields = ['doctor', 'day']
    list_filter = ['doctor', 'day']
    inlines = [
        SchedulesInline,
    ]


class SchedulesAdmin(admin.ModelAdmin):
    def appointment_2(self, obj):
        if obj.appointment:
            return obj.appointment.user.username
        return ''

    appointment_2.short_description = 'Consulta'
    list_display = ['diary', 'hour', 'appointment_2']
    search_fields = ['diary', 'hour']


class SpecialtiesAdmin(admin.ModelAdmin):

    list_display = ['name']
    search_fields = ['name']


class DoctorsAdmin(admin.ModelAdmin):

    list_display = ['name', 'crm', 'specialtie', 'telephone', 'email']
    search_fields = ['name', 'crm', 'specialtie']
    list_filter = ['name', 'crm', 'specialtie']


class AppointmentsAdmin(admin.ModelAdmin):

    list_display = ['doctor', 'day', 'schedule', 'user', 'date_appointment']
    search_fields = ['doctor', 'day', 'schedule', 'date_appointment', 'user']
    list_filter = ['doctor', 'day']


admin.site.register(Doctors, DoctorsAdmin)
admin.site.register(Diarys, DiarysAdmin)
admin.site.register(Schedules, SchedulesAdmin)
admin.site.register(Specialties, SpecialtiesAdmin)
admin.site.register(Appointments, AppointmentsAdmin)
