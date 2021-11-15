import requests
import re
import json
import dataclasses
from enum import Enum

AUTH_TOKEN = '7avPu0XGaswfMPGRTQ1ufVWtVrs'
BOARD_ID = 'o9J_ljuLrH8='
DB_PATH = 'ids.json'


class MiroObjectType(str, Enum):
    BOARD = 'board'
    WIDGET = 'widget'
    FRAME = 'frame'
    SHAPE = 'shape'
    LINE = 'line'
    TEXT = 'text'

    def __repr__(self) -> str:
        return self.value


@dataclasses.dataclass
class MiroShapeObject:
    obj_id: str
    text: str
    obj_type: MiroObjectType = MiroObjectType.SHAPE


def get_id_by_num(db_path, num):
    with open(db_path) as db:
        ids = json.load(db)
        if num is num:
            num = str(num)
        return ids.get(num)


if __name__ == "__main__":
    print("Welcome to the practical part of the workshop!")
    choice = -1

    while choice < 1 or choice > 5:
        if choice != -1:
            print("Don't try to cheat. Possible answers: 1, 2, 3, 4, 5")
        choice = int(input("Enter your choice:  "))

    url = f'https://api.miro.com/v1/boards/{BOARD_ID}/widgets/'
    header = {
        'Authorization': f'Bearer {AUTH_TOKEN}',
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    existed_widgets_response = requests.get(url, headers=header)
    collection_json = existed_widgets_response.json()
    widgets_json = collection_json['data']
    board_widgets = []

    for widget_json in widgets_json:
        widget_type = widget_json['type']
        if widget_type == MiroObjectType.SHAPE:
            found_shape = MiroShapeObject(obj_id=widget_json['id'],
                                          text=widget_json['text'])
            board_widgets.append(found_shape)

    update_shape_id = get_id_by_num(DB_PATH, choice)
    upd_url = url + update_shape_id
    widget_to_update = next(item for item in board_widgets if item.obj_id == update_shape_id)
    incremented_text = int(re.search(r'\d+', widget_to_update.text).group()) + 1

    payload = {
        "text": f"<p>Votes : {incremented_text}</p>"
    }
    result = requests.patch(upd_url, data=json.dumps(payload), headers=header)
    if result.status_code == 200:
        print("Great! Thanks for your answer")
