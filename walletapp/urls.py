
from django.urls import path, include
from walletapp import views
from .views import WalletView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('walletview', views.WalletView, basename='walletview')


urlpatterns = [
    path('', views.home),
    path('wallet/', views.walletview),

    path('walletview/', include(router.urls)),
    # path('walletview/', WalletView.as_view()),

    path('register/', views.register),
    path('login/', views.loginpage),
    path('logout/', views.logoutpage),

]