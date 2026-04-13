from django.db import models

class Product(models.Model):
    CURRENCY_CHOICES =[
        ('NGN', 'Naira'),
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='NGN')
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.currency}{self.price}"