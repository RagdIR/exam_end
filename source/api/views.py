from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie

from pip._vendor.requests import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from webapp.models import Users, Friends


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')

class AddViewSet(LoginRequiredMixin, ViewSet):

    queryset = Users.objects.all()

    @action(methods=['post'], detail=True)

    def post(self, request, pk=None):
        user = get_object_or_404(Users, pk=pk)
        add, created = Friends.objects.get_or_create(user=user, friend=request.user)
        if created:
            return Response({'pk': pk})
        else:
            return Response(status=403)

class DellViewSet(LoginRequiredMixin, ViewSet):

    @action(methods=['delete'], detail=True)

    def delete(self, request, pk=None):
        user = get_object_or_404(Users, pk=pk)
        add = get_object_or_404(user.friends, user=request.user)
        add.delete()
        return Response({'pk': pk})