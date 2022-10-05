from django.db.models import QuerySet
import init_django_orm  # noqa: F401
from db.models import LoyaltyProgram, LoyaltyProgramParticipant
from datetime import datetime
from django.db.models import F, Q


def all_loyalty_program_names() -> QuerySet:
    queryset = LoyaltyProgram.objects.filter(
    ).values_list("name", "bonus_percentage")
    return queryset


def not_active_customers() -> QuerySet:

    queryset = LoyaltyProgramParticipant.objects.filter(
        last_activity__gt=datetime(2021, 1, 1),
        last_activity__lt=datetime(2022, 1, 1)
    ).values("customer__first_name")
    return queryset


def most_active_customers() -> QuerySet:
    queryset = LoyaltyProgramParticipant.objects.filter(

    ).values_list(
        "customer__first_name",
        "customer__last_name",
        "sum_of_spent_money"
    ).order_by("-sum_of_spent_money")[:5]
    return queryset


def clients_with_i_and_o() -> QuerySet:
    queryset = LoyaltyProgramParticipant.objects.filter(
        Q(customer__first_name__startswith="I")
        | Q(customer__last_name__contains="o")
    )
    return queryset


def bonuses_less_then_spent_money() -> QuerySet:
    queryset = LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money")
    ).values("customer__phone_number")
    return queryset


if __name__ == "__main__":
    print(not_active_customers())
