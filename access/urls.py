from django.urls import path

from access.views import (UserView, TokenView)

app_name = "users"

urlpatterns = [

    path('', UserView.as_view(), name='create'),
    path('login', TokenView.as_view(), name='token'),


]
