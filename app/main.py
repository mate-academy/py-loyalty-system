import datetime

from django.db.models import Q, F

import init_django_orm  # noqa: F401
from db.models import Customer, LoyaltyProgram, LoyaltyProgramParticipant


def all_loyalty_program_names():
    return LoyaltyProgram.objects.all().values_list("name", "bonus_percentage")


def not_active_customers():
    customers = LoyaltyProgramParticipant.objects.order_by(
        "customer__first_name").filter(
        last_activity__lt=datetime.date(2022, 1, 1),
        last_activity__gt=datetime.date(2021, 1, 1)).\
        values_list("customer__first_name")
    return [{"customer__first_name": customer[0]} for customer in customers]


def most_active_customers():
    return LoyaltyProgramParticipant.objects.order_by(
        "-sum_of_spent_money").all()[:5].values_list(
        "customer__first_name",
        "customer__last_name",
        "sum_of_spent_money")


def clients_with_i_and_k():
    return Customer.objects.filter(
        Q(first_name__startswith="I") | Q(last_name__contains="o")
    )


def bonuses_less_then_spent_money():
    phones = LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money")
    ).values_list("customer__phone_number")
    return [{"customer__phone_number": phone[0]} for phone in phones]
