from django.urls import path
from . import views

app_name = 'vote'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:district_num>/ballot', views.ballot, name="ballot"),
    path('finished', views.tally, name="tally"),
    path('votetotals', views.votetotals, name="votetotals")
]
