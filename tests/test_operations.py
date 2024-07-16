from database_suite import TestDatabase

class TestInsert(TestDatabase):

    def test_insert(self):
        query= "INSERT INTO test_table (id,name) values (1,'akshay');"
        self.cursor.execute(query)
        self.conn.commit()
        insert_query = "SELECT * FROM test_table;"
        self.cursor.execute(insert_query)
        new_id = self.cursor.fetchone()[1]
        self.conn.commit()
        assert new_id== 'akshay'
        assert new_id is not None

    def test_delete(self):
        insert_query = "SELECT * FROM test_table;"
        self.cursor.execute(insert_query)
        new_id = self.cursor.fetchone()[1]
        self.conn.commit()
        assert new_id== 'akshay'
        assert new_id is not None
        delete_query= "DELETE FROM test_table;"
        self.cursor.execute(delete_query)
        insert_query = "SELECT * FROM test_table;"
        self.cursor.execute(insert_query)
        new_id = self.cursor.fetchone()
        assert new_id is None

