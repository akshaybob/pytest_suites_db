
create_tables_query = [
"""
CREATE TABLE test_table(
    id INTEGER,
    name VARCHAR(50) NOT NULL
    );
""",
"""
CREATE TABLE demo_table(
    id INTEGER,
    name VARCHAR(50) NOT NULL
    );
"""
]

drop_tables = [
    """DROP TABLE IF EXISTS test_table;""",
    """DROP TABLE IF EXISTS demo_table;""",
]