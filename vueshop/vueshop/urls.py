"""vueshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# # import xadmin
# # xadmin.autodiscover()
# # from xadmin.plugins import xversion
# # xversion.register_models()

# urlpatterns = [
#     #path('admin/', admin.site.urls)
#     path('xadmin/', xadmin.site.urls)
#     # path('xadmin/',include(xadmin.site.urls))
# ]

# -*- coding: utf-8 -*-
# from django.conf.urls import include, url
# from django.urls import include, path
# from vueshop.settings import MEDIA_ROOT  
# from django.views.static import serve
# #from goods.views_base import GoodsListView
# from goods.views import GoodsListViewSet
# from rest_framework.documentation import include_docs_urls 
# # Uncomment the next two lines to enable the admin:
# import xadmin
# xadmin.autodiscover()


# from xadmin.plugins import xversion
# xversion.register_models()

# #from django.contrib import admin
# goods_list = GoodsListViewSet.as_view({  
#     'get': 'list',  
# })

# urlpatterns = [
#     path(r'xadmin/', xadmin.site.urls),
#     path(r'ueditor/',include('DjangoUeditor.urls')),
#     path(r'media/', serve, {"document_root": MEDIA_ROOT}),
#     path(r'goods/views',goods_list,name="goods-list"),
#     path(r'docs/',include_docs_urls(title="Jess Vueshop"))
# ]

from django.views.static import serve
from rest_framework.documentation import include_docs_urls

import xadmin
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from vueshop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet
# from goods.views import GoodsListView,
# from goods.views_base import GoodsListView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


# goods_list = GoodsListViewSet.as_view({
#      'get': 'list',
#  })
router = DefaultRouter()

# goods url
router.register(r'goods', GoodsListViewSet, base_name="goods")



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # producing the image displace by using the django server
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    # rich text url
    path('ueditor/', include('DjangoUeditor.urls')),

    # goods list
    # path('goods/', GoodsListView.as_view(),name="goods-list"),
    #path('goods/', goods_list,name="goods-list"),
    re_path('^', include(router.urls)),
    
    path('docs/', include_docs_urls(title='Jess doc')),

    # home page
    path('index/', TemplateView.as_view(template_name='index.html'), name='index')

    # re_path('static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),

   
]


