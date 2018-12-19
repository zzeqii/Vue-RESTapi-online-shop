from django.views.generic.base import View  
from django.http import HttpResponse  
import json  
  
from goods.models import Goods  
from django.views.generic import ListView  
  
  
# class GoodsListView(View):  
#     def get(self, request):  
#         """ 
#             implement the good list through the django view 
#             :param request: 
#             :return: 
#             """  
#         json_list = []  
#         goods = Goods.objects.all()[:10]  
#         for good in goods:  
#             json_dict = {}  
#             json_dict["name"] = good.name  
#             json_dict["category"] = good.category.name  
#             json_dict["market_price"] = good.market_price  
#             json_list.append(json_dict)  
  
#         return HttpResponse(json.dumps(json_list), content_type="application/json") 

from django.views.generic.base import View  
from django.http import HttpResponse, JsonResponse  
import json  
  
from goods.models import Goods  
from django.views.generic import ListView  
  
  
class GoodsListView(View):  
    def get(self, request):  
        """ 
            
            :param request: 
            :return: 
            """  
        json_list = []  
        goods = Goods.objects.all()[:10]  
        '''''for good in goods: 
            json_dict = {} 
            json_dict["name"] = good.name 
            json_dict["category"] = good.category.name 
            json_dict["market_price"] = good.market_price 
            json_list.append(json_dict)'''  
  
        ''''' 
        from django.forms.models import model_to_dict 
        for good in goods: 
            json_dict=model_to_dict(good) 
            json_list.append(json_dict) 
        '''  
  
        from django.core import serializers  
        json_data = serializers.serialize('json', goods)  
        json_data = json.loads(json_data)  
        # return HttpResponse(json.dumps(json_data), content_type="application/json")  
        # return HttpResponse(json_data, content_type="application/json")  
        return JsonResponse(json_data, safe=False)