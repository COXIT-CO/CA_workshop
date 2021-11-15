from complete_version.external_systems.database_interface import DatabaseClient
from complete_version.external_systems.miro_interface import MiroApiClient

DB_PATH = 'ids.json'


def test_db_client_init():
    client = DatabaseClient(DB_PATH)
    assert len(client.ids) == 5


def test_get_id_by_num():
    client = DatabaseClient(DB_PATH)
    res = client.get_id_by_num(1)
    assert res == '3074457367605439232'


def test_miro_api_init():
    test_url = 'test_url'
    test_token = 'test_token'
    test_header = {
        "Authorization": f'Bearer {test_token}',
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    client = MiroApiClient(base_url=test_url,
                           auth_token=test_token,
                           db_path=DB_PATH)
    assert client.base_url == test_url
    assert client.auth_token == test_token
    assert client.auth_header_as_dict == test_header


def test_miro_vote_for_code_with_number():
    assert True


def test_miro_get_all_shapes_by_board_id():
    assert True



