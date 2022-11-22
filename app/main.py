import init_django_orm  # noqa: F401

from datetime import datetime
from db.models import Customer, LoyaltyProgram, LoyaltyProgramParticipant
from django.db.models import F, Q, QuerySet


def all_loyalty_program_names() -> QuerySet:
    return LoyaltyProgram.objects.all().values_list("name", "bonus_percentage")


def not_active_customers() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        last_activity__gt=datetime(2021, 1, 1),
        last_activity__lt=datetime(2022, 1, 1)
    ).values("customer__first_name")


def most_active_customers() -> QuerySet:
    return LoyaltyProgramParticipant.objects.all().order_by(
        "-sum_of_spent_money"
    ).values_list(
        "customer__first_name",
        "customer__last_name",
        "sum_of_spent_money"
    )[:5]


def clients_with_i_and_o() -> QuerySet:
    return Customer.objects.filter(
        Q(first_name__startswith="i") | Q(last_name__contains="o")
    )


def bonuses_less_then_spent_money() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money")
    ).values("customer__phone_number")
