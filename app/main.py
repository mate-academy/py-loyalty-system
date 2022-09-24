import init_django_orm  # noqa: F401

from django.db.models import F, Q

from db.models import Customer
from db.models import LoyaltyProgram
from db.models import LoyaltyProgramParticipant


def all_loyalty_program_names():
    return LoyaltyProgram.objects.all().values_list(
        "name", "bonus_percentage")


def not_active_customers():
    return LoyaltyProgramParticipant.objects.filter(
        last_activity__gt="2021-01-01",
        last_activity__lt="2022-01-01"
    ).values("customer__first_name")


def most_active_customers():
    return LoyaltyProgramParticipant.objects.order_by(
        "-sum_of_spent_money"
    )[:5].values_list(
        "customer__first_name", "customer__last_name",
        "sum_of_spent_money")


def clients_with_i_and_k():
    return Customer.objects.filter(Q(
        first_name__startswith="I") | Q(last_name__contains="o"))


def bonuses_less_then_spent_money():
    return LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money")
    ).values("customer__phone_number")
