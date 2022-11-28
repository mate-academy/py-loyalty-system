import init_django_orm  # noqa: F401

from django.db.models import QuerySet


def all_loyalty_program_names() -> QuerySet:
    pass


def not_active_customers() -> QuerySet:
    pass


def most_active_customers() -> QuerySet:
    pass


def clients_with_i_and_o() -> QuerySet:
    pass


def bonuses_less_then_spent_money() -> QuerySet:
    pass
