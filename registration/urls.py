from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signin/', SignUpView.as_view(), name='signup'),
]