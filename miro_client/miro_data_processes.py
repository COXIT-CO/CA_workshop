import re
from typing import List
from miro_client.miro_entities import MiroObjectType, Shape


def get_all_shapes_from_widgets(widgets_json: List[dict]) -> List[Shape]:
    board_widgets = []

    for widget_json in widgets_json:
        widget_type = widget_json['type']
        if widget_type == MiroObjectType.SHAPE:
            found_shape = Shape(obj_id=widget_json['id'],
                                text=widget_json['text'])
            board_widgets.append(found_shape)

    return board_widgets


def increment_voting_text(board_widgets: List[Shape], update_shape_id: str) -> Shape:
    widget_to_update = next(item for item in board_widgets if item.obj_id == update_shape_id)
    incremented_num = int(re.search(r'\d+', widget_to_update.text).group()) + 1
    widget_to_update.text = f"<p>Votes : {incremented_num}</p>"
    return widget_to_update
