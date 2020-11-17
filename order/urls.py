from django.urls import path

from order import views
from order.views import OrderListView

urlpatterns = [
    # 所有生产订单
    path('', OrderListView.as_view(), name='order_list'),
    # 删除订单
    path('delect/<int:pk>', views.order_del, name='order_del'),
    # 查看自己的订单
    path('owen/', views.order_mine, name='order_mine'),
]