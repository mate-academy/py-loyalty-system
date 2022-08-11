# Loyalty system

**Please note:** read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)
before starting.

Loyalty programs are created to encourage customers to choose your service with great competitiveness. 
The shop has several loyalty programs because the more a person buys in the store - the bigger his/her 
discount. Let's imagine that you have already created your loyalty system.

It has the next models:

```python
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
```

You can see mentioned models [here](app/db/models.py).

You have to make the following functions:

1. **`def all_loyalty_program_names()`**

This function returns all names and bonus percentages of existing loyalty programs.

2. **`def not_active_customers()`**

This function returns all names of loyalty participants who were active in the period from 2021-01-01 to 2022-01-01.

3. **`def most_active_customers()`**

This function returns names, last names and the sum of sent money 5 of the most active customers - persons who spent the biggest amount of money.

4. **`def  clients_with_i_and_k()`**

This function returns all customers whose name starts at “I” or the last name contains “o”.

5. **`def bonuses_less_then_spent_money()`**

This function returns all phone numbers of customers who have active bonuses less than the sum of spent money.

**Don't forget** to make migrations:
```python
python manage.py makemigrations
python manage.py migrate
```

Implement the described task [here](app/main.py).
