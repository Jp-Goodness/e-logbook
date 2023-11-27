# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('select_week/', views.select_week, name='select_week'),
    path('activity/<int:day_id>/', views.activity_detail, name='activity_detail'),
    path('assess_activity/<int:activity_id>/', views.assess_activity, name='assess_activity'),
]
