from django.urls import include, path
from . import views
from django.views.generic import TemplateView, RedirectView

app_name = 'Betting'
urlpatterns = [
    #path('bet/<str:result>/<int:amount>/<float:odd>/<float:profit>/', views.betView, name='bet'),
    #path('change_bet/<int:id>/<str:result>/<int:amount>/<float:odd>/<float:profit>/', views.cBetView, name='cbet'),
    path('bets/', views.gBetsView, name='gbets'),
    #path('get_bets/<str:id>/', views.gBetView, name='gbet'),
    path('notifs/', views.gNotificationsView, name='notifs'),
    path('notifs/<int:user>/', views.gNotificationUserView, name='notif_user'),
    #path('notif/', views.notifView, name='notif'),
    #path('del_notif/<int:id>/', views.dNotificationView, name='dnotif'),
    #path('get_notif/<int:id>/', views.gNotificationsView, name='gnotif'),
]