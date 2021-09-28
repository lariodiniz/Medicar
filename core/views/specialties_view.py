from rest_framework.generics import ListAPIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from core.models import Specialties
from core.serializers import SpecialtiesSerializer


class SpecialtiesPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class SpecialtiesView(ListAPIView):
    """Lists the specialties."""
    queryset = Specialties.objects.all()
    # A Paginação não foi pedida no projeto backend porem existe no projetp
    # frontend por isso deixei implementado, porem, comentado para seguir
    # as exigencias do projeto backend.
    #pagination_class = SpecialtiesPagination
    serializer_class = SpecialtiesSerializer

    def get_queryset(self):
        queryset = Specialties.objects.all()
        name = self.request.query_params.get('search')
        if name is not None:
            queryset = queryset.filter(name__contains=name)
        return queryset
