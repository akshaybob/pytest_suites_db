import sql_query_test as sql
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def connect_to_db():
    """Function to establish a database connection"""
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST
    )
    return conn

class TestDatabase:
    conn=connect_to_db()
    cursor= conn.cursor()

    @classmethod
    def setup_class(cls):

        for query in sql.create_tables_query:
            cls.cursor.execute(query)

        cls.conn.commit()

    @classmethod
    def teardown_class(cls):
        
        for drop_query in sql.drop_tables:
            cls.cursor.execute(drop_query)

        cls.conn.commit()
        cls.cursor.close()
        cls.conn.close()
