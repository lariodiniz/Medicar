from datetime import datetime
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination


from core.models import Diarys
from core.serializers import DiarysSerializer


class DiarysPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class DiarysView(ListAPIView):
    """Lists the diarys."""
    queryset = Diarys.objects.all().order_by('day', 'schedules__hour')
    # A Paginação não foi pedida no projeto backend porem existe no projetp
    # frontend por isso deixei implementado, porem, comentado para seguir
    # as exigencias do projeto backend.
    #pagination_class = DiarysPagination
    serializer_class = DiarysSerializer

    def get_queryset(self):

        queryset = Diarys.objects.filter(
            day__gte=datetime.now().date(), schedules__hour__gte=datetime.now().time(), schedules__appointment=None).order_by('day')
        doctor = self.request.query_params.getlist('medico')
        if len(doctor) > 0:
            queryset = queryset.filter(doctor__id__in=doctor)

        specialtie = self.request.query_params.getlist('especialidade')
        if len(specialtie) > 0:
            queryset = queryset.filter(doctor__specialtie_id__in=specialtie)

        initial_date = self.request.query_params.get('data_inicio')
        if initial_date is not None:
            queryset = queryset.filter(day__gte=initial_date)

        final_date = self.request.query_params.get('data_final')
        if initial_date is not None:
            queryset = queryset.filter(day__lte=final_date)
        return queryset

        return queryset
