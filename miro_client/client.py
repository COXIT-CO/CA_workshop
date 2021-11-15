from typing import List
import requests
import json
from database.db_client import DatabaseClient
from miro_client.miro_data_processes import get_all_shapes_from_widgets, increment_voting_text
from miro_client.miro_entities import Shape


class MiroApiClient:
    def __init__(self, base_url: str, auth_token: str, db_path: str = 'database/ids.json'):
        self.base_url = base_url
        self.auth_token = auth_token
        self.auth_header_as_dict = {
            'Authorization': f'Bearer {self.auth_token}',
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self.db_client = DatabaseClient(db_path)

    def get_all_shapes_by_board_id(self, board_id: str) -> List[Shape]:
        url = f'{self.base_url}/v1/boards/{board_id}/widgets/'
        response = requests.get(url, headers=self.auth_header_as_dict)
        collection_json = response.json()
        widgets_json = collection_json['data']
        return get_all_shapes_from_widgets(widgets_json)

    def vote_for_code_with_number(self, id, number) -> requests.Response:
        widgets = self.get_all_shapes_by_board_id(board_id=id)
        update_shape_id = self.db_client.get_id_by_num(number)
        url = f'{self.base_url}/v1/boards/{id}/widgets/{update_shape_id}'

        new_shape = increment_voting_text(widgets, update_shape_id)
        payload = {
            "text": new_shape.text
        }
        resp = requests.patch(url, data=json.dumps(payload), headers=self.auth_header_as_dict)
        return resp