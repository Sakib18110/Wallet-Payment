from requests import request
from rest_framework import serializers
from .models import Wallet, WalletType, User


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ['pay_type', 'user', 'balance']
    
        