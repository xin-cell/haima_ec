from django.urls import path,include,re_path
import  xadmin
from django.views.static import serve
from haima_ec.settings import MEDIA_ROOT

from goods.view_base import GoodsListView

from rest_framework.documentation import include_docs_urls

from goods.views import GoodsListViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#配置goods的url
router.register(r'goods', GoodsListViewSet)


# 配置Category的url
router.register(r'categorys', CategoryViewSet)

urlpatterns = [
    path("users/",include('apps.users.urls')),
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),



    # drf文档，title自定义
    path('docs',include_docs_urls(title='仙剑奇侠传')),
    path('api-auth/',include('rest_framework.urls')),

    # 商品列表页
    re_path('^', include(router.urls)),
]
