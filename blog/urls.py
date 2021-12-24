from django.urls import path

from . import views

app_name = 'blog'  # 视图函数命名空间
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name='detail'),  # path converters
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tags/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('aboutme', views.aboutme, name='aboutme')
]
