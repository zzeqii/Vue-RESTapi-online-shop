from .serializers import GoodsSerializer  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import mixins  
from rest_framework import generics  
from rest_framework.pagination import PageNumberPagination  
from django_filters.rest_framework import DjangoFilterBackend  
from rest_framework import viewsets  
from rest_framework import status  
from rest_framework import filters  
from .models import Goods  
from .filters import GoodsFilter  
  
  
class GoodsPagination(PageNumberPagination):  
    page_size = 10  
    page_size_query_param = 'page_size'  
    page_query_param = "p"  
    max_page_size = 100  
  
  
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):  
    """list item, page seperation, searcing, filter and sorting"""  
    queryset = Goods.objects.all()  
    serializer_class = GoodsSerializer  
    pagination_class = GoodsPagination  
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)  
    filter_class = GoodsFilter  
    search_fields = ('name', 'goods_brief', 'goods_desc')  
    ordering_fields=('sold_num','add_time')

    #retrieving the clicks of items
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

