import init_django_orm  # noqa: F401

import datetime

from django.db.models import QuerySet, Q, F
from db.models import Customer, LoyaltyProgram, LoyaltyProgramParticipant


def all_loyalty_program_names() -> QuerySet:
    return LoyaltyProgram.objects.all().values_list("name", "bonus_percentage")


def not_active_customers() -> QuerySet:
    query = LoyaltyProgramParticipant.objects.all()
    dt1 = datetime.date(2021, 1, 1)
    dt2 = datetime.date(2022, 1, 1)
    name_list = query.filter(last_activity__gt=dt1, last_activity__lt=dt2)
    return name_list.values("customer__first_name")


def most_active_customers() -> QuerySet:
    active_cust = LoyaltyProgramParticipant.objects.all()
    ordered = active_cust.order_by("-sum_of_spent_money")[:5]
    return ordered.values_list("customer__first_name",
                               "customer__last_name",
                               "sum_of_spent_money")


def clients_with_i_and_o() -> QuerySet:
    query = Customer.objects.all()
    return query.filter(Q(first_name__startswith="I")
                        | Q(last_name__contains="o"))


def bonuses_less_then_spent_money() -> QuerySet:
    all_customers = LoyaltyProgramParticipant.objects.all()
    filtered = all_customers.filter(active_bonuses__lt=F("sum_of_spent_money"))
    return filtered.values("customer__phone_number")
