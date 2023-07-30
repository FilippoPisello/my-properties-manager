import datetime
from typing import Self

from pydantic import BaseModel, NonNegativeFloat, model_validator


class Property(BaseModel):
    id: int
    city: str
    street: str
    number: int


class Tenant(BaseModel):
    id: int
    first_name: str
    last_name: str


class Contract(BaseModel):
    id: int
    date_start: datetime.date
    date_end: datetime.date
    rent_net_eur: NonNegativeFloat
    expense_coverage_eur: NonNegativeFloat = 0

    @model_validator(mode="after")
    def end_date_greater_than_start_date(self):
        """Ensure that the contract end date is greater than the start date."""
        if self.date_end <= self.date_start:
            raise ValueError("End date must be greater than start date.")
        return self

    @property
    def is_active(self) -> bool:
        """Return True if the contract is active, False otherwise."""
        return self.date_start <= datetime.date.today() <= self.date_end

    @property
    def total_eur(self) -> NonNegativeFloat:
        """Return the total value of the contract."""
        return self.rent_net_eur + self.expense_coverage_eur

    @classmethod
    def dummy(cls, **kwargs) -> Self:
        """Create an instance of the class with dummy data.

        Use for testing purposes.
        """
        data = {
            "id": 1,
            "date_start": datetime.date(2020, 1, 1),
            "date_end": datetime.date(2020, 12, 31),
            "rent_net_eur": 1000,
            "expense_coverage_eur": 0,
        } | kwargs
        return cls(**data)
