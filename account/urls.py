from django.urls import path,include

from .views import UserAccountRegistrationView,UserAccountLoginView,UserAccountLogoutView

urlpatterns = [
    path('register/', UserAccountRegistrationView.as_view(), name='register'),
    path('login/', UserAccountLoginView.as_view(), name='login'),
    path('logout/',UserAccountLogoutView.as_view(),name='logout')
]
