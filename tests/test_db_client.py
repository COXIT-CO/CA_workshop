from database.db_client import DatabaseClient


def test_db_client_init():
    client = DatabaseClient('database/ids.json')
    assert len(client.ids) == 5


def test_get_id_by_num():
    client = DatabaseClient('database/ids.json')
    res = client.get_id_by_num(1)
    assert res == '3074457367605439232'
