from typing import List
import re
import requests
import json

from miro_client.miro_entities import Widget, create_widget_by_type
from database.db_client import DatabaseClient
from miro_client.exceptions import get_json_or_raise_exception, UnexpectedResponseException


class MiroApiClient:
    # Use cases
    def __init__(self, base_url: str, auth_token: str, db_path: str = 'database/ids.json'):
        self.base_url = base_url
        self.auth_token = auth_token
        self.auth_header_as_dict = {
            'Authorization': f'Bearer {self.auth_token}',
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self.db_client = DatabaseClient(db_path)

    def get_all_widgets_by_board_id(self, board_id: str) -> List[Widget]:
        url = f'{self.base_url}/v1/boards/{board_id}/widgets/'
        response = requests.get(url, headers=self.auth_header_as_dict)
        collection_json = get_json_or_raise_exception(response)

        try:
            widgets_json = collection_json['data']
            return [create_widget_by_type(w) for w in widgets_json]
        except Exception as e:
            raise UnexpectedResponseException(cause=e)

    def vote_for_code_with_number(self, id,  number) -> requests.Response:
        widgets = self.get_all_widgets_by_board_id(board_id=id)
        update_shape_id = self.db_client.get_id_by_num(number)
        url = f'{self.base_url}/v1/boards/{id}/widgets/{update_shape_id}'

        widget_to_update = next(item for item in widgets if item.obj_id == update_shape_id)
        incremented_text = int(re.search(r'\d+', widget_to_update.text).group())+1

        payload = {
            "text": f"<p>Votes : {incremented_text}</p>"
        }
        resp = requests.patch(url, data=json.dumps(payload), headers=self.auth_header_as_dict)
        return resp
