import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from django.db.models import F, Q
from db.models import LoyaltyProgram, Customer, LoyaltyProgramParticipant


def all_loyalty_program_names() -> QuerySet:
    return LoyaltyProgram.objects.all().values_list("name", "bonus_percentage")


def not_active_customers() -> QuerySet:
    customers = Customer.objects.filter(
        Q(loyaltyprogramparticipant__last_activity__gt="2021-01-01")
        & Q(loyaltyprogramparticipant__last_activity__lt="2022-01-01")
    )
    return customers.annotate(
        customer__first_name=F("first_name")
    ).values("customer__first_name")


def most_active_customers() -> QuerySet:
    return Customer.objects.all().order_by(
        "-loyaltyprogramparticipant__sum_of_spent_money"
    )[:5].values_list("first_name",
                      "last_name",
                      "loyaltyprogramparticipant__sum_of_spent_money")


def clients_with_i_and_o() -> QuerySet:
    return Customer.objects.filter(
        Q(first_name__startswith="I")
        | Q(last_name__contains="o")
    )


def bonuses_less_then_spent_money() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        sum_of_spent_money__gt=F("active_bonuses")
    ).values("customer__phone_number")
