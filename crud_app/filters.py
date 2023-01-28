import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class StaffFilters(django_filters.FilterSet):
    start_date = DateFilter(field_name='register_date', lookup_expr='gte')
    end_date = DateFilter(field_name='register_date', lookup_expr='lte')
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ['register_date']