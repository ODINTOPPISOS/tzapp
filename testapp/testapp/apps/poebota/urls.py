# Создаём привязки для views
from django.urls import path
from . import views
app_name = 'poebota'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.create, name='create'),
]
#path('searc', views.searc, name='searc'),