from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from django.views.static import serve
from haima_ec.settings import MEDIA_ROOT

from goods.view_base import GoodsListView

from rest_framework.documentation import include_docs_urls

from goods.views import GoodsListViewSet, CategoryViewSet, BannerViewset, IndexCategoryViewset, HotSearchsViewset
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from trade.views import ShoppingCartViewset, OrderViewset, AlipayView
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from users.views import SmsCodeViewset, UserViewset

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet,basename='goods')

# 配置Category的url
router.register(r'categorys', CategoryViewSet,basename='categorys')

# 配置codes的url
router.register(r'code', SmsCodeViewset,basename='cede')

# 配置users的url
router.register(r'users', UserViewset, basename="users")

# 配置用户收藏的url
router.register(r'userfavs', UserFavViewset, basename="userfavs")

# 配置用户留言的url
router.register(r'messages', LeavingMessageViewset, basename="messages")

# 配置收货地址
router.register(r'address',AddressViewset , basename="address")

# 配置购物车的url
router.register(r'shopcarts', ShoppingCartViewset, basename="shopcarts")

# 配置订单的url
router.register(r'orders', OrderViewset, basename="orders")

# 配置首页轮播图的url
router.register(r'banners', BannerViewset, basename="banners")

# 热搜词
router.register(r'hotsearchs', HotSearchsViewset, basename="hotsearchs")

# 首页系列商品展示url
router.register(r'indexgoods', IndexCategoryViewset, basename="indexgoods")

goods_list = GoodsListViewSet.as_view({
    'get': 'list',
})

urlpatterns = [

    # 首页
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),

    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

    # drf文档，title自定义
    path('docs', include_docs_urls(title='取胜之道')),
    path('api-auth/', include('rest_framework.urls')),

    # 商品列表页
    re_path('^', include(router.urls)),
    # token
    path('api-token-auth/', views.obtain_auth_token),

    # jwt的token认证接口
    # path('jwt-auth/', obtain_jwt_token),
    # jwt的认证接口
    path('login/', obtain_jwt_token),


    # 配置支付宝支付相关接口的url
    path('alipay/return/', AlipayView.as_view(), name="alipay"),

    # 第三方登录
    path('', include('social_django.urls', namespace='social'))

]
