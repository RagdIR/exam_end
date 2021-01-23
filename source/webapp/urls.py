from django.urls import path
from webapp.views import IndexView, MessageView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('/mymessages/', MessageView.as_view(), name='mymessages')
]

