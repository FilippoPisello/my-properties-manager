import datetime

import pytest

from my_app import data_structures as ds


def test_setting_contract_end_date_to_before_start_date_raises_error():
    with pytest.raises(ValueError):
        ds.Contract.dummy(
            date_start=datetime.date(2020, 1, 1),
            date_end=datetime.date(2019, 12, 31),
        )


def test_contract_is_active_if_today_is_between_start_and_end_date():
    today = datetime.date.today()
    contract = ds.Contract.dummy(
        date_start=today - datetime.timedelta(days=30),
        date_end=today + datetime.timedelta(days=30),
    )
    assert contract.is_active


def test_contract_is_inactive_if_today_is_after_end_date():
    today = datetime.date.today()
    contract = ds.Contract.dummy(
        date_start=today - datetime.timedelta(days=60),
        date_end=today - datetime.timedelta(days=30),
    )
    assert not contract.is_active


def test_contract_total_value_is_rent_plus_expense_coverage():
    contract = ds.Contract.dummy(
        rent_net_eur=1000,
        expense_coverage_eur=100,
    )
    assert contract.total_eur == 1100
