from django_filters import FilterSet, filters
from ht_web_service.apps.ht.models import *
from ht_web_service.apps.ht.search import search


class HistoryFilter(FilterSet):
    date = filters.DateFilter(field_name='date__date',
                              help_text='date of change | '
                                        'format: %Y-%m-%d %H:%M:%S')
    feature_id = filters.NumberFilter(field_name='feature_id',
                                      help_text='id of feature')
    user_id = filters.NumberFilter(field_name='user_id',
                                   help_text="id of user which changed")

    attribute = filters.CharFilter(field_name='attribute',
                                   help_text="name of changeable attribute")

    class Meta:
        model = History
        fields = ['feature_id', 'user_id', 'date', 'attribute']


class _FeatureFilter:

    def filtering(self, queryset, start_date='', end_date=None, attributes_str=None, search_query=None):
        result_queryset = queryset

        # full text search
        if search_query not in (None, ''):
            search_hits = search(search_query).hits
            result_queryset = result_queryset.filter(id__in=[int(hit.meta.id) for hit in search_hits])

        # filtering by history
        if attributes_str is not None:
            attributes = attributes_str.split(',')
        else:
            attributes = None

        input_kwargs = {'date__gte': start_date, 'date__lte': end_date, 'attribute__in': attributes}
        res_kwargs = {}
        for key in input_kwargs:
            if input_kwargs[key] is not None:
                res_kwargs[key] = input_kwargs[key]
        if len(res_kwargs) is not 0:
            histroies = History.objects.filter(**res_kwargs)
            result_queryset = result_queryset.filter(id__in=[item.feature.id for item in histroies])

        return result_queryset


class FeatureFilter(FilterSet):

    search = filters.CharFilter(name='search',
                                method='full_text_search',
                                help_text='Full text search')
    changeable_attributes = filters.CharFilter(name='attributes',
                                               method='filtering_by_attributes',
                                               help_text='Changeable attributes')
    start_changes = filters.CharFilter(name='date_start',
                                       method='filtering_by_histroty_date_start',
                                       help_text='start date of change | '
                                                 'format: %Y-%m-%d %H:%M:%S')
    end_changes = filters.CharFilter(name='date_end',
                                     method='filtering_by_histroty_date_end',
                                     help_text='end date of change | '
                                               'format: %Y-%m-%d %H:%M:%S')

    def full_text_search(self, queryset, name, value):
        if value not in (None, ''):
            search_hits = search(value)['hits']
            return queryset.filter(id__in=[int(hit['_id']) for hit in search_hits])

    def filtering_by_attributes(self, queryset, name, value):
        if value not in (None, ''):
            attributes = value.split(',')
            histroies = History.objects.filter(attribute__in=attributes)
            return queryset.filter(id__in=[item.feature.id for item in histroies])

    def filtering_by_histroty_date_start(self, queryset, name, value):
        if value not in (None, ''):
            histroies = History.objects.filter(date__gte=value)
            return queryset.filter(id__in=[item.feature.id for item in histroies])

    def filtering_by_histroty_date_end(self, queryset, name, value):
        if value not in (None, ''):
            histroies = History.objects.filter(date__lte=value)
            return queryset.filter(id__in=[item.feature.id for item in histroies])

    class Meta:
        model = Feature
        fields = ['search', 'changeable_attributes', 'start_changes', 'end_changes']
