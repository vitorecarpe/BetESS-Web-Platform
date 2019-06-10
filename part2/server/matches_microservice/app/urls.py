from django.urls import include, path
from . import views
from django.views.generic import TemplateView, RedirectView

app_name = 'Matches'
urlpatterns = [
    path('teams/', views.gTeamsView, name='teams'),
    path('events/', views.gEventsView, name='event'),
    #path('change_event/', views.cEventView, name='cevent'),
    #path('del_event/<int:id>/', views.dEventView, name='devent'),
    #path('get_events/', views.gEventsView, name='gevento'),
    #path('get_event/<int:id>/', views.gEventView, name='gevent'),
]