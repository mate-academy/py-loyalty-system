import datetime

import init_django_orm  # noqa: F401

from django.db.models import F

from db.models import LoyaltyProgram, LoyaltyProgramParticipant, Customer


def all_loyalty_program_names():
    return LoyaltyProgram.objects.all().values_list(
        "name", "bonus_percentage")


def not_active_customers():
    start = datetime.date(2021, 1, 1)
    end = datetime.date(2022, 1, 1)
    return LoyaltyProgramParticipant.objects.filter(
        last_activity__date__gte=start,
        last_activity__date__lte=end).values(
        "customer")


def most_active_customers():
    return LoyaltyProgramParticipant.objects.all().values_list(
        "customer__first_name",
        "customer__last_name",
        "sum_of_spent_money"
    ).order_by("-sum_of_spent_money")[:5]


def clients_with_i_and_o():
    return Customer.objects.filter(
        first_name__startswith="I", last_name__contains="o")


def bonuses_less_then_spent_money():
    return LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money")
    ).values("customer__phone_number")
