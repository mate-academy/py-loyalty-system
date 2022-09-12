import init_django_orm  # noqa: F401


from db.models import Customer, LoyaltyProgram, LoyaltyProgramParticipant
from django.db.models import Q, F


def all_loyalty_program_names():

    return LoyaltyProgram.objects.all().values_list("name", "bonus_percentage")


def not_active_customers():
    not_active_customers = \
        LoyaltyProgramParticipant.objects.filter(
            last_activity__gt="2021-01-01",
            last_activity__lt="2022-01-01").values("customer__first_name")

    return not_active_customers


def most_active_customers():
    most_active_customers = LoyaltyProgramParticipant.objects.all()
    most_active_customers = LoyaltyProgramParticipant.objects.order_by(
        '-sum_of_spent_money')[0:5].values_list("customer__first_name",
                                                "customer__last_name",
                                                "sum_of_spent_money")

    return most_active_customers


def clients_with_i_and_k():

    clients_with_i_and_k = Customer.objects.filter(
        Q(first_name__startswith="I") | Q(last_name__contains="o"))

    return clients_with_i_and_k


def bonuses_less_then_spent_money():
    bonuses_less_then_spent_money = LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money")).values(
        "customer__phone_number")
    return bonuses_less_then_spent_money
