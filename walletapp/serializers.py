from django.forms import ValidationError
from requests import request
from rest_framework import serializers
from .models import Wallet, WalletType, User
from rest_framework.validators import UniqueTogetherValidator


class WalletSerializer(serializers.ModelSerializer):
                 
    class Meta:
        model = Wallet
        fields = ['pay_type', 'user', 'balance']
        validators = [
            UniqueTogetherValidator(
                queryset=Wallet.objects.all(),
                fields=['pay_type', 'user']
            )
        ]
    
    