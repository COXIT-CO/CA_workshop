import json
from enum import Enum


class MiroObjectType(str, Enum):
    BOARD = 'board'
    WIDGET = 'widget'
    FRAME = 'frame'
    SHAPE = 'shape'
    LINE = 'line'
    TEXT = 'text'

    def __repr__(self) -> str:
        return self.value


class JsonSerializableMixin:
    # Interface Segregation Example
    def __repr__(self) -> str:
        return json.dumps(self.__dict__)


class BaseMiroObject(JsonSerializableMixin):
    def __init__(self, obj_id: str, obj_type: MiroObjectType):
        self.obj_id = obj_id
        self.obj_type = obj_type


class Widget(BaseMiroObject):
    def __init__(self, obj_id: str, obj_type=MiroObjectType.WIDGET):
        super().__init__(obj_id, obj_type)
        self.obj_id = obj_id
        self.obj_type = obj_type
        self.capabilities = dict()
        self.metadata = dict()


class Shape(Widget):
    def __init__(self, obj_id: str, text: str):
        super().__init__(obj_id, MiroObjectType.SHAPE)
        self.text = text
