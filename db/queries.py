import init_django_orm  # noqa: F401
from django.db.models import F, Sum, Q, QuerySet
from db.models import LoyaltyProgram, LoyaltyProgramParticipant, Customer


def all_loyalty_program_names() -> QuerySet:
    return LoyaltyProgram.objects.all().values_list("name", "bonus_percentage")


def not_active_customers() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        last_activity__gte="2021-01-01",
        last_activity__lt="2022-01-01"
    ).values("customer__first_name")


def most_active_customers() -> QuerySet:
    return Customer.objects.annotate(
        total_spent=Sum("loyaltyprogramparticipant__sum_of_spent_money")
    ).order_by("-total_spent").values_list(
        "first_name", "last_name", "total_spent"
    )[:5]


def clients_with_i_and_o() -> QuerySet:
    return Customer.objects.filter(
        Q(first_name__startswith="I") | Q(last_name__icontains="o")
    ).values("id")


def bonuses_less_then_spent_money() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        customer__loyaltyprogramparticipant__active_bonuses__lt=F(
            "sum_of_spent_money")
    ).values("customer__phone_number")
