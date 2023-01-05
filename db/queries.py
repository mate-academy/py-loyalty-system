import init_django_orm  # noqa: F401

from django.db.models import QuerySet, Q, F
from db.models import LoyaltyProgram, LoyaltyProgramParticipant, Customer
import datetime


def all_loyalty_program_names() -> QuerySet:
    return LoyaltyProgram.objects.values_list("name", "bonus_percentage")


def not_active_customers() -> QuerySet:
    start_period = datetime.date(2021, month=1, day=1)
    end_period = datetime.date(2022, month=1, day=1)
    return LoyaltyProgramParticipant.objects.filter(
        last_activity__gt=start_period,
        last_activity__lt=end_period).values(
        "customer__first_name")


def most_active_customers() -> QuerySet:
    return LoyaltyProgramParticipant.objects.order_by(
        "-sum_of_spent_money").values_list(
        "customer__first_name",
        "customer__last_name",
        "sum_of_spent_money"
    )[:5]


def clients_with_i_and_o() -> QuerySet:
    return Customer.objects.filter(
        Q(first_name__startswith="I") | Q(last_name__contains="o"))


def bonuses_less_then_spent_money() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money")).values(
        "customer__phone_number")
