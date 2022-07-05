from django.db import models
from django.contrib.auth.models import User


class WalletType(models.Model):
    name = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
    

class Wallet(models.Model):
    pay_type = models.ForeignKey(WalletType, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    balance = models.IntegerField()

    def __str__(self):
        return f"{self.pay_type.name}"
    
