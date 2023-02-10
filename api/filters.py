# api/filters.py
import django_filters
from .models import Work

class WorkFilter(django_filters.FilterSet):
    work_type = django_filters.CharFilter(field_name='work_type', lookup_expr='iexact')
    class Meta:
        model = Work
        fields = ['work_type']
