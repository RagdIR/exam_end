from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from webapp.models import Users, Message


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'users'
    model = Users
    paginate_by = 10
    paginate_orphans = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Users.objects.all().order_by('user')
        return data

class MessageView(ListView):
    template_name = 'messages/mymessages.html'
    context_object_name = 'messages'
    model = Message
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Message.objects.all().order_by('pub_date')
        return data

