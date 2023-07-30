DROP TABLE IF EXISTS ft_contract;
DROP TABLE IF EXISTS dm_property;
DROP TABLE IF EXISTS dm_contract;
DROP TABLE IF EXISTS dm_tenant;
CREATE TABLE dm_property (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL,
    street TEXT NOT NULL,
    number TEXT NOT NULL
);
CREATE TABLE dm_contract (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_start DATE NOT NULL,
    date_end DATE NOT NULL,
    is_active BOOLEAN NOT NULL,
    rent_net_eur DECIMAL(8, 2) NOT NULL,
    expense_coverage_eur DECIMAL(8, 2) DEFAULT 0.00,
    total_eur DECIMAL(8, 2) NOT NULL
);
CREATE TABLE dm_tenant (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
CREATE TABLE ft_contract (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    contract_id INTEGER NOT NULL,
    tenant_id INTEGER NOT NULL,
    FOREIGN KEY (property_id) REFERENCES dm_property (id),
    FOREIGN KEY (contract_id) REFERENCES dm_contract (id),
    FOREIGN KEY (tenant_id) REFERENCES dm_tenant (id)
)