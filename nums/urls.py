from django.urls import path

from . import views

app_name = 'nums'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:modelno>/', views.viewmodel, name = 'viewmodel'),
    path('allmodels/', views.allmodels, name = 'allmodels'),
    path('predict/', views.predict, name = 'predict'),
]
