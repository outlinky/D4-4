from django_filters import FilterSet, DateFilter
from .models import Post
import django.forms

class NewsFilter(FilterSet):
    dateCreation = DateFilter(
        lookup_expr='gte',
        widget=django.forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )
    class Meta:
        model = Post
        fields = {
            'title':['icontains'],
            'author':['exact'],
            'dateCreation':[],
        }