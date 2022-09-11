from django.db.models import Q, F

from db.models import LoyaltyProgramParticipant, LoyaltyProgram
import init_django_orm  # noqa: F401


def all_loyalty_program_names():
    return LoyaltyProgram.objects.all().values_list(
        "name",
        "bonus_percentage"
    )


def not_active_customers():
    queryset = LoyaltyProgramParticipant.objects.filter(
        last_activity__lt="2022-01-01",
        last_activity__gt="2021-01-01"
    )
    return queryset.values("customer__first_name")


def most_active_customers():
    queryset = LoyaltyProgramParticipant.objects.order_by(
        "-sum_of_spent_money"
    )
    return queryset.values_list("customer__first_name",
                                "customer__last_name",
                                "sum_of_spent_money")[0:5]


def clients_with_i_and_k():
    return LoyaltyProgramParticipant.objects.filter(
        Q(customer__first_name__startswith="I")
        | Q(customer__last_name__contains="o")
    )


def bonuses_less_then_spent_money():
    queryset = LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money")
    )
    return queryset.values("customer__phone_number")
