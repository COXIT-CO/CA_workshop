import json
from enum import Enum


class MiroObjectType(str, Enum):
    BOARD = 'board'
    WIDGET = 'widget'
    USER_MINI = 'user'
    SHAPE = 'shape'
    LINE = 'line'
    TEXT = 'text'

    def __repr__(self) -> str:
        return self.value


class JsonSerializableMixin:

    def __repr__(self) -> str:
        return json.dumps(self.__dict__)


class BaseMiroObject(JsonSerializableMixin):
    def __init__(self, obj_id: str,
                 obj_type: MiroObjectType):
        self.obj_id = obj_id
        self.obj_type = obj_type


class Widget(BaseMiroObject):

    def __init__(self, obj_id: str,
                 obj_type=MiroObjectType.WIDGET):
        super().__init__(obj_id, obj_type)
        self.obj_id = obj_id
        self.obj_type = obj_type
        self.capabilities = dict()
        self.metadata = dict()


class Shape(Widget):

    def __init__(self, obj_id: str, text: str,
                 x_pos: float, y_pos: float,
                 width: float, height: float,
                 rotation: float):
        super().__init__(obj_id, MiroObjectType.SHAPE)
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.rotation = rotation  # number of degrees clockwise


def create_widget_by_type(widget_json) -> Widget:
    widget_type = widget_json['type']
    if widget_type == MiroObjectType.SHAPE:
        return Shape(obj_id=widget_json['id'],
                     text=widget_json['text'],
                     x_pos=widget_json['x'],
                     y_pos=widget_json['y'],
                     width=widget_json['width'],
                     height=widget_json['height'],
                     rotation=widget_json['rotation'])
    else:
        return Widget(obj_id=widget_json['id'])
