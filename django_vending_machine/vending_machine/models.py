from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Inventory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=False, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventories"


class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hundred = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    fifty = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    twenty = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    ten = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    five = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    one = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def wallet_sum(self):
        total = (self.hundred*100) +  (self.fifty*50) + (self.twenty*20) + (self.ten*10) + (self.five*5) + (self.one)
        return total

    def __str__(self):
        total = self.wallet_sum()
        return f"{self.user.username} | RM {total}"
