from django.urls import path

from core.views import (SpecialtiesView, DoctorsView,
                        DiarysView, AppointmentsView,
                        AppointmentsDeleteView)

app_name = "core"

urlpatterns = [

    path('medicos/', DoctorsView.as_view(), name='doctors'),
    path('especialidades/', SpecialtiesView.as_view(), name='specialties'),
    path('agendas/', DiarysView.as_view(), name='diarys'),
    path('consultas/<int:appointment_id>', AppointmentsDeleteView.as_view(),
         name='appointments_delete'),
    path('consultas/', AppointmentsView.as_view(), name='appointments'),

]
