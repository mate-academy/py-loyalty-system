import init_django_orm  # noqa: F401
from db.models import Customer, LoyaltyProgram, LoyaltyProgramParticipant
from django.db.models import QuerySet, Q, F


def all_loyalty_program_names() -> QuerySet:
    return LoyaltyProgram.objects.filter().values_list(
        "name",
        "bonus_percentage"
    )


def not_active_customers() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        last_activity__range=["2021-01-01", "2021-12-31"],
    ).values("customer__first_name")


def most_active_customers() -> QuerySet:
    customers = Customer.objects.all()
    order_customers = customers.order_by(
        "-loyaltyprogramparticipant__sum_of_spent_money"
    )
    most_active = order_customers.values_list(
        "first_name",
        "last_name",
        "loyaltyprogramparticipant__sum_of_spent_money"
    )[:5]

    return most_active


def clients_with_i_and_o() -> QuerySet:
    return Customer.objects.filter(
        Q(first_name__startswith="I") | Q(last_name__contains="o")
    )


def bonuses_less_then_spent_money() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money")
    ).values("customer__phone_number")
