import init_django_orm  # noqa: F401
from db.models import LoyaltyProgram, LoyaltyProgramParticipant
from django.db.models import F, Q, QuerySet

from django.db.models import QuerySet


def all_loyalty_program_names() -> QuerySet:
    queryset = LoyaltyProgram.objects.filter().values_list("name",
                                                           "bonus_percentage")
    return queryset


def not_active_customers() -> QuerySet:
    queryset = LoyaltyProgramParticipant.objects.filter(
        last_activity__lt="2022-01-01",
        last_activity__gt="2021-01-01"
    ).values("customer__first_name")
    return queryset


def most_active_customers() -> QuerySet:
    queryset = LoyaltyProgramParticipant.objects.\
        filter().values_list("customer__first_name",
                             "customer__last_name",
                             "sum_of_spent_money"
                             ).order_by("-sum_of_spent_money")[:5]
    return queryset


def clients_with_i_and_o() -> QuerySet:
    queryset = LoyaltyProgramParticipant. \
        objects.filter(
            Q(customer__first_name__startswith="I") | Q
            (customer__last_name__contains="o"))
    return queryset


def bonuses_less_then_spent_money() -> QuerySet:
    queryset = LoyaltyProgramParticipant.objects. \
        filter(active_bonuses__lt=F("sum_of_spent_money")). \
        values("customer__phone_number")
    return queryset
