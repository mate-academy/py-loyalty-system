from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=20)


class LoyaltyProgram(models.Model):
    name = models.CharField(max_length=64)
    bonus_percentage = models.IntegerField()


class LoyaltyProgramParticipant(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loyalty_program = models.ForeignKey(LoyaltyProgram, on_delete=models.PROTECT)
    last_activity = models.DateField(auto_now=True)
    active_bonuses = models.IntegerField(default=0, null=True, blank=True)
    sum_of_spent_money = models.IntegerField(default=0)
