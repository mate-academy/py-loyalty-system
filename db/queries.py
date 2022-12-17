import init_django_orm  # noqa: F401

import datetime

from django.db.models import QuerySet, Q, F
from db.models import Customer, LoyaltyProgram, LoyaltyProgramParticipant


def all_loyalty_program_names() -> QuerySet:
    return LoyaltyProgram.objects.all().values_list("name", "bonus_percentage")


def not_active_customers() -> QuerySet:
    dt1 = datetime.date(2021, 1, 1)
    dt2 = datetime.date(2022, 1, 1)

    query = LoyaltyProgramParticipant.objects.filter(
        last_activity__gt=dt1,
        last_activity__lt=dt2
    )
    return query.values("customer__first_name")


def most_active_customers() -> QuerySet:
    query = LoyaltyProgramParticipant.objects.order_by("-sum_of_spent_money")
    return query[:5].values_list(
        "customer__first_name",
        "customer__last_name",
        "sum_of_spent_money"
    )


def clients_with_i_and_o() -> QuerySet:
    return Customer.objects.filter(
        Q(first_name__startswith="I") | Q(last_name__contains="o")
    )


def bonuses_less_then_spent_money() -> QuerySet:
    all_cust = LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money")
    )
    return all_cust.values("customer__phone_number")
