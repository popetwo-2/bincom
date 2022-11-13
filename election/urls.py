from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_polling_units, name='index'),
    path('results/<int:uniqueid>/', views.get_result_polling_unit, name='results'),
    #   path('search_results/', views.search_view, name='search'),
    path('result_per_lga/', views.total_result_per_lga, name='per_lga'),
    #   path('new/', views.new_page, name='new'),
    path('upload/', views.upload_results, name='upload'),
    path('all_results/', views.results, name='all_results'),
]