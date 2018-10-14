from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('companies/', views.CompanyList.as_view(), name='company-list'),
    path('companies/<pk>/', views.CompanyDetail.as_view(), name='company-detail'),
    path('families/', views.FamilyList.as_view(), name='family-list'),
    path('families/<pk>/', views.FamilyDetail.as_view(), name='family-detail'),
    path('guides/', views.GuideList.as_view(), name='guide-list'),
    path('guides/<pk>/', views.GuideDetail.as_view(), name='guide-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<pk>/', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
