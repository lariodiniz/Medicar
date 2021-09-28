from rest_framework.generics import ListAPIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from core.models import Doctors
from core.serializers import DoctorsSerializer


class DoctorsPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class DoctorsView(ListAPIView):
    """Lists the Doctos."""
    queryset = Doctors.objects.all()
    # A Paginação não foi pedida no projeto backend porem existe no projetp
    # frontend por isso deixei implementado, porem, comentado para seguir
    # as exigencias do projeto backend.
    # pagination_class = DoctorsPagination
    serializer_class = DoctorsSerializer

    def get_queryset(self):
        queryset = Doctors.objects.all()
        name = self.request.query_params.get('search')

        if name:
            especialidades = self.request.query_params.getlist('especialidade')
            if len(especialidades) > 0:
                queryset = queryset.filter(
                    name__contains=name, specialtie__id__in=especialidades)
            else:
                queryset = queryset.filter(name__contains=name)
        else:
            especialidades = self.request.query_params.getlist('especialidade')
            if len(especialidades) > 0:
                queryset = queryset.filter(specialtie__id__in=especialidades)
        return queryset
