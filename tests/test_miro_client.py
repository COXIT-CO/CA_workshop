from miro_client.client import MiroApiClient


def test_client_api_init():
    test_url = 'test_url'
    test_token = 'test_token'
    test_header = {
        "Authorization": f'Bearer {test_token}',
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    client = MiroApiClient(base_url=test_url,
                           auth_token=test_token,
                           db_path='../database/ids.json')
    assert client.base_url == test_url
    assert client.auth_token == test_token
    assert client.auth_header_as_dict == test_header


def test_get_all_widgets_by_board_id():
    pass


def test_vote_for_code_with_number():
    pass
