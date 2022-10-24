import init_django_orm  # noqa: F401

from db.models import LoyaltyProgram, LoyaltyProgramParticipant
from django.db.models import QuerySet
from django.db.models import F, Q


def all_loyalty_program_names() -> QuerySet:
    return LoyaltyProgram.objects.values_list("name", "bonus_percentage")


def not_active_customers() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        customer__last_activity__in=["2021-01-01", "2022-01-01"]
    ).values_list("customers__first_name")


def most_active_customers() -> QuerySet:
    return LoyaltyProgramParticipant.objects.order_by(
        "-sum_of_spent_money"
    )[:5].values_list(
        "customer__first_name",
        "customer__last_name",
        "sum_of_spent_money"
    )


def clients_with_i_and_o() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        Q(first_name__startswith="I") | Q(last_name__contains="o")
    )


def bonuses_less_then_spent_money() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money")
    ).values_list("customer__phone_number")
