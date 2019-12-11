from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from myapi.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
