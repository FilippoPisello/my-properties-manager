from my_app.database import adapter as ad
from my_app.database.actions import (
    connect_db,
    instantiate_db,
    populate_db_with_test_data,
)
from my_app.paths import TEST_DB_INSTANCE_NAME


def test_connect_db():
    """Test that the database connection is established."""
    db = connect_db(TEST_DB_INSTANCE_NAME)
    assert db is not None


def test_test_data_can_populate_db():
    """Test that the test data succeed in populating the database."""
    db = connect_db(TEST_DB_INSTANCE_NAME)
    instantiate_db(db)
    populate_db_with_test_data(db)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM dm_contract")
    contracts = cursor.fetchall()
    assert len(contracts) == 1


def test_fetching_a_contract_that_does_not_exist_returns_none():
    """Test that fetching a contract that does not exist causes error code."""
    db = connect_db(TEST_DB_INSTANCE_NAME)
    instantiate_db(db)
    populate_db_with_test_data(db)

    contract = db.execute(
        """
        SELECT * FROM dm_contract WHERE id = ?
        """,
        (9999,),
    ).fetchone()
    assert contract is None


class TestDataModelIntegration:
    """Test that the data model structures and the db are compatible."""

    @classmethod
    def setup_class(cls):
        """Connect to the test db."""
        cls.db = connect_db(TEST_DB_INSTANCE_NAME)

    @classmethod
    def teardown_class(cls):
        """Close the db connection."""
        cls.db.close()

    def setup_method(self):
        instantiate_db(self.db)
        populate_db_with_test_data(self.db)

    #  For the following tests, it is enough for the instantiation to succeed

    def test_property(self):
        _property = self.db.execute("SELECT * FROM dm_property").fetchone()
        ad.property_from_db(_property)
        assert True

    def test_tenant(self):
        tenant = self.db.execute("SELECT * FROM dm_tenant").fetchone()
        ad.tenant_from_db(tenant)
        assert True

    def test_contract(self):
        contract = self.db.execute("SELECT * FROM dm_contract").fetchone()
        ad.contract_from_db(contract)
        assert True
