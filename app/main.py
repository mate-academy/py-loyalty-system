import init_django_orm  # noqa: F401


from db.models import Customer, LoyaltyProgram, LoyaltyProgramParticipant
from django.db.models import Q, F


def all_loyalty_program_names():
    list = []
    loyalty_program_names = LoyaltyProgram.objects.all()
    for programs in loyalty_program_names:
        list.append((programs.name, programs.bonus_percentage))
    return list


def not_active_customers():
    not_active_customers = \
        LoyaltyProgramParticipant.objects.filter(
            last_activity__gt="2021-01-01",
            last_activity__lt="2022-01-01")
    list = []
    for i in not_active_customers:
        list.append({"customer__first_name": i.customer.first_name})
    return list


def most_active_customers():
    list = []
    not_active_customers = LoyaltyProgramParticipant.objects.all()
    not_active_customers = LoyaltyProgramParticipant.objects.order_by(
        '-sum_of_spent_money')[0:5]
    for i in not_active_customers:
        list.append((i.customer.first_name,
                     i.customer.last_name,
                     i.sum_of_spent_money))

    return list


def clients_with_i_and_k():

    clients_with_i_and_k = Customer.objects.filter(
        Q(first_name__startswith="I") | Q(last_name__contains="o"))

    return clients_with_i_and_k


def bonuses_less_then_spent_money():
    bonuses_less_then_spent_money = LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money"))
    list = []
    for i in bonuses_less_then_spent_money:
        list.append({"customer__phone_number": i.customer.phone_number})
    return list
