from postcode.models import PLZO
from rest_framework import viewsets
from postcode.serializers import PostCodeSerializer


class PostCodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PLZO.objects.all().order_by('postcode')
    serializer_class = PostCodeSerializer


class PostCodeQueryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostCodeSerializer
    
    def get_queryset(self):
        queryset = PLZO.objects.all()
        filter_value = self.request.query_params.get('postcode', None)
        if filter_value is not None:
            queryset = queryset.filter(postcode=filter_value)
        return queryset
