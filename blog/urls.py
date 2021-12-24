from django.urls import path

from . import views


app_name = 'blog' # 视图函数命名空间
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>', views.detail, name='detail') # path converters
]