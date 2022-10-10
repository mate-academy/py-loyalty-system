import init_django_orm  # noqa: F401
from db.models import LoyaltyProgram, LoyaltyProgramParticipant
from django.db.models import F, Q, QuerySet


def all_loyalty_program_names() -> QuerySet:
    query = LoyaltyProgram.objects.all().values_list(
        "name", "bonus_percentage"
    )
    return query


def not_active_customers() -> QuerySet:
    query = LoyaltyProgramParticipant.objects.filter(
        last_activity__gt="2021-01-01",
        last_activity__lt="2022-01-01"
    ).values("customer__first_name")
    return query


def most_active_customers() -> QuerySet:
    query = LoyaltyProgramParticipant.objects.filter(
    ).values_list("customer__first_name",
                  "customer__last_name",
                  "sum_of_spent_money").order_by(
        "-sum_of_spent_money")[:5]
    return query


def clients_with_i_and_o() -> QuerySet:
    query = LoyaltyProgramParticipant.objects.filter(
        Q(customer__first_name__startswith='I')
        | Q(customer__last_name__contains="o")
    )
    return query


def bonuses_less_then_spent_money() -> QuerySet:
    query = LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money")
    ).values("customer__phone_number")
    return query
