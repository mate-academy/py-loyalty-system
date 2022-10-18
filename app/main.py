import json

import init_django_orm  # noqa: F401

from django.db.models import QuerySet, F, Q

from db.models import LoyaltyProgramParticipant, Customer, LoyaltyProgram


def make_data() -> None:
    with open("test_data.json", "r") as file_in:
        data = json.load(file_in)

    for field in data:
        if field["model"] == "db.loyaltyprogram":
            LoyaltyProgram.objects.create(
                name=field["fields"]["name"],
                bonus_percentage=field["fields"]["bonus_percentage"])
        if field["model"] == "db.customer":
            Customer.objects.create(
                first_name=field["fields"]["first_name"],
                last_name=field["fields"]["last_name"],
                phone_number=field["fields"]["phone_number"])
        if field["model"] == "db.loyaltyprogramparticipant":
            LoyaltyProgramParticipant.objects.create(
                last_activity=field["fields"]["last_activity"],
                active_bonuses=field["fields"]["active_bonuses"],
                sum_of_spent_money=field["fields"]["sum_of_spent_money"],
                customer_id=field["fields"]["customer_id"],
                loyalty_program_id=field["fields"]["loyalty_program_id"])


def all_loyalty_program_names() -> QuerySet:
    return LoyaltyProgram.objects.all().values_list("name", "bonus_percentage")


def not_active_customers() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        last_activity__gt="2021-01-01",
        last_activity__lt="2022-01-01").values("customer__first_name")


def most_active_customers() -> QuerySet:
    return LoyaltyProgramParticipant.objects.order_by(
        "-sum_of_spent_money")[:5].values_list("customer__first_name",
                                               "customer__last_name",
                                               "sum_of_spent_money")


def clients_with_i_and_o() -> QuerySet:
    return Customer.objects.filter(
        Q(first_name__startswith="I") | Q(last_name__icontains="o"))


def bonuses_less_then_spent_money() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F(
            "sum_of_spent_money")).values("customer__phone_number")
