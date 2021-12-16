from django.urls import path

from webapp.views import index_view, calculate_view

urlpatterns = [
    path('', index_view),
    path('calculate/', calculate_view)
]