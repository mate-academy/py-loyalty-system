import pytest
from app.main import (
    all_loyalty_program_names,
    not_active_customers,
    most_active_customers,
    clients_with_i_and_k,
    bonuses_less_then_spent_money,
)


@pytest.mark.django_db
def test_all_loyalty_program_names(django_db_setup):
    result = all_loyalty_program_names()
    assert list(result) == [("Base level", 5),
                            ("Middle level", 10),
                            ("Gold level", 20)]


@pytest.mark.django_db
def test_not_active_customers(django_db_setup):
    result = not_active_customers()
    print(result)
    assert list(result) == [
        {"customer__first_name": "Alona"},
        {"customer__first_name": "Dariia"},
        {"customer__first_name": "Ivanna"},
    ]


@pytest.mark.django_db
def test_most_active_customers(django_db_setup):
    result = most_active_customers()
    assert list(result) == [
        ("Ivan", "Ivanov", 12000),
        ("Eleonora", "Ivanova", 10059),
        ("Alona", "Burga", 2000),
        ("Ivan", "Hryshko", 2000),
        ("Vadim", "Kuhar", 1090),
    ]


@pytest.mark.django_db
def test_clients_with_i_and_k(django_db_setup):
    result = clients_with_i_and_k()
    assert result.count() == 9


@pytest.mark.django_db
def test_bonuses_less_then_spent_money(django_db_setup):
    result = bonuses_less_then_spent_money()
    assert list(result) == [
        {"customer__phone_number": "380666666666"},
        {"customer__phone_number": "380666752638"},
        {"customer__phone_number": "380636535353"},
        {"customer__phone_number": "380766666666"},
        {"customer__phone_number": "380669866666"},
        {"customer__phone_number": "38066666666"},
    ]
