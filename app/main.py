import datetime
import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from django.db.models import F, Q

from db.models import LoyaltyProgram, LoyaltyProgramParticipant, Customer


def all_loyalty_program_names() -> QuerySet:
    queryset = LoyaltyProgram.objects.all()\
        .values_list("name", "bonus_percentage")

    return queryset


def not_active_customers() -> QuerySet:
    queryset = LoyaltyProgramParticipant.objects.\
        filter(
            last_activity__gte=datetime.date(2021, 1, 1),
            last_activity__lte=datetime.date(2021, 12, 31)
        ).\
        values("customer__first_name")

    return queryset


def most_active_customers() -> QuerySet:
    queryset = LoyaltyProgramParticipant.objects.all().\
        values_list("customer__first_name",
                    "customer__last_name",
                    "sum_of_spent_money").\
        order_by("-sum_of_spent_money")

    return queryset[0:5]


def clients_with_i_and_o() -> QuerySet:
    queryset = Customer.objects.\
        filter(Q(first_name__startswith="I") | Q(last_name__icontains="o"))

    return queryset


def bonuses_less_then_spent_money() -> QuerySet:
    queryset = LoyaltyProgramParticipant.objects.\
        filter(active_bonuses__lt=F("sum_of_spent_money")). \
        values("customer__phone_number",)

    return queryset


if __name__ == "__main__":
    loyalty_programs = all_loyalty_program_names()
    print(loyalty_programs)
    for loyalty_program in loyalty_programs:
        print(loyalty_program)

    not_active_customers = not_active_customers()
    print(not_active_customers)
    for not_active_customer in not_active_customers:
        print(not_active_customer)

    most_active_customers = most_active_customers()
    print(most_active_customers)
    for most_active_customer in most_active_customers:
        print(most_active_customer)

    clients = clients_with_i_and_o()
    print(clients)
    for clients in clients:
        print(clients)

    bonuses = bonuses_less_then_spent_money()
    print(bonuses)
    for bonus in bonuses:
        print(bonus)
