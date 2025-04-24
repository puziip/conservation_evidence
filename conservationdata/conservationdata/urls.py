from django.contrib import admin
from django.urls import path
from evidence import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('average_score/', views.average_score_by_species),
    path('high_score_interventions/', views.high_effectiveness_interventions),
]
