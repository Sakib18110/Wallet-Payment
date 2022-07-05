
from django.shortcuts import render, redirect
from .models import User, Wallet
from .serializers import WalletSerializer
from .forms import CustomUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


def home(request):
    return render(request, 'walletapp/homepage.html')

def walletview(request):
    wallet_item = Wallet.objects.filter(user=request.user)
    context = {'wallet_item': wallet_item}
    return render(request, 'walletapp/wallet.html', context)

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form =  CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Registerd Successfully!! Login to Continue.')
            return redirect('/login')
    return render(request, 'walletapp/auth/register.html', context={'form':form})


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in.')
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged In Successfully!!')
                return redirect('/')
            messages.error(request, 'Invalid Username or Password.')
            return redirect('/login')
        return render(request, 'walletapp/auth/login.html')


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged Out Successfully.')
    return redirect('/')


class WalletView(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer



