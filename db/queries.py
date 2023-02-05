import init_django_orm  # noqa: F401

from django.db.models import QuerySet, Q, F
from db.models import LoyaltyProgram, LoyaltyProgramParticipant, Customer


def all_loyalty_program_names() -> QuerySet:
    return LoyaltyProgram.objects.all().values_list("name", "bonus_percentage")


def not_active_customers() -> QuerySet:
    customers_name = LoyaltyProgramParticipant.objects.all()
    customers_name = customers_name.filter(
        Q(last_activity__gt="2021-01-01") & Q(last_activity__lt="2022-01-01")
    )
    return customers_name.values("customer__first_name")


def most_active_customers() -> QuerySet:
    customers = LoyaltyProgramParticipant.objects.all()
    customers = customers.order_by("-sum_of_spent_money")[:5]
    return customers.values_list(
        "customer__first_name",
        "customer__last_name",
        "sum_of_spent_money"
    )


def clients_with_i_and_o() -> QuerySet:
    return Customer.objects.filter(
        Q(first_name__startswith="I") | Q(last_name__contains="o")
    ).all()


def bonuses_less_then_spent_money() -> QuerySet:
    customer_number = LoyaltyProgramParticipant.objects.all()
    customer_number = customer_number.filter(
        active_bonuses__lt=F("sum_of_spent_money")
    )
    return customer_number.values("customer__phone_number")
