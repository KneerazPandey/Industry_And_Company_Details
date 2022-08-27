from django.urls import path
from . import views


urlpatterns = [
    path('industry-type/', views.industry_type_list_view, name='industry-type'),
    path('company-detail/', views.create_company_detail_view, name='company-detail'),
    path('company-display/', views.display, name='company-display'),
    path('search-show/', views.search_show_view, name='search-show'),
]