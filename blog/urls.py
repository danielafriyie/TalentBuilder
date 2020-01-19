from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:blog_id>/<int:year>/<int:month>/<int:day>/<slug:blog_title>/', views.blog, name='detail_blog')
]
