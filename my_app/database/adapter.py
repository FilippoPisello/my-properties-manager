"""Handle the data translation between the database and the application."""

from my_app import data_structures as ds


def property_from_db(data: dict) -> ds.Property:
    """Instantiate the Property instance from a record fetched from the db."""
    return ds.Property(**data)


def tenant_from_db(data: dict) -> ds.Tenant:
    """Instantiate the Tenant instance from a record fetched from the db."""
    return ds.Tenant(**data)


def contract_from_db(data: dict) -> ds.Contract:
    """Instantiate the Contract instance from a record fetched from the db."""
    return ds.Contract(
        id=data["id"],
        date_start=data["date_start"],
        date_end=data["date_end"],
        rent_net_eur=data["rent_net_eur"],
        expense_coverage_eur=data["expense_coverage_eur"],
    )
