import init_django_orm  # noqa: F401

from django.db.models import QuerySet, Q, F

from db.models import LoyaltyProgram
from db.models import Customer
from db.models import LoyaltyProgramParticipant


def all_loyalty_program_names() -> QuerySet:
    return LoyaltyProgram.objects.all().values_list(
        "name", "bonus_percentage"
    )


def not_active_customers() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        Q(last_activity__year__lt="2022") & Q(
            last_activity__year__gte="2021"
        )
    ).values("customer__first_name")


def most_active_customers() -> QuerySet:
    queryset = LoyaltyProgramParticipant.objects.order_by(
        "-sum_of_spent_money"
    )[:5]
    return queryset.values_list(
        "customer__first_name",
        "customer__last_name",
        "sum_of_spent_money"
    )


def clients_with_i_and_o() -> QuerySet:
    queryset = Customer.objects.all()
    return queryset.filter(
        Q(first_name__startswith="I") | Q(
            last_name__contains="o"
        )
    )


def bonuses_less_then_spent_money() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F(
            "sum_of_spent_money"
        )
    ).values("customer__phone_number")
