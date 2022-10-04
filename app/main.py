from django.db.models import Q, F

from db.models import Customer, LoyaltyProgram, LoyaltyProgramParticipant


def all_loyalty_program_names():
    """Getting names and bonus percentages of existing loyalty programs"""
    return LoyaltyProgram.objects.values_list("name", "bonus_percentage")


def not_active_customers():
    """Getting participants who were active in the period
    from 2021-01-01 to 2022-01-01"""
    return LoyaltyProgramParticipant.objects.filter(
        last_activity__gt="2021-01-01"). \
        filter(last_activity__lt="2022-01-01"). \
        values("customer__first_name")


def bonuses_less_then_spent_money():
    """Getting phone numbers of customers who have active
    bonuses less than the sum of spent money"""
    return LoyaltyProgramParticipant.objects. \
        filter(active_bonuses__lt=F("sum_of_spent_money")). \
        values("customer__phone_number")


def most_active_customers():
    """Getting names, last names and the sum of
    sent money of 5 the most active customers"""
    spent_money = LoyaltyProgramParticipant.objects
    spent_money = spent_money.order_by("-sum_of_spent_money")[:5]
    return spent_money.values_list(
        "customer__first_name",
        "customer__last_name",
        "sum_of_spent_money"
    )


def clients_with_i_and_o():
    """Getting customers whose name starts
    at 'I' or the last name contains 'o' """
    return Customer.objects.filter(Q(first_name__startswith="I")
                                   | Q(last_name__icontains="o"))
