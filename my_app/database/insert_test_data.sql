INSERT INTO dm_property (city, street, number)
VALUES ('Milan', 'Viale Fulvio Testi', '1');

INSERT INTO dm_contract (
        date_start,
        date_end,
        is_active,
        rent_net_eur,
        expense_coverage_eur,
        total_eur
    )
VALUES (
        DATE('now', "-1 month"),
        DATE('now', "+11 month"),
        TRUE,
        1000.00,
        100.00,
        1100.00
    );

INSERT INTO dm_tenant (first_name, last_name)
VALUES ('Mario', 'Rossi');

INSERT INTO ft_contract (property_id, contract_id, tenant_id)
VALUES (1, 1, 1);