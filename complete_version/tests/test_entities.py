from complete_version.entities.miro_objects import *


def test_base_object_init():
    test_id = 'test_id'
    test_type = MiroObjectType.WIDGET
    obj = BaseMiroObject(test_id, test_type)
    assert obj.obj_id == test_id
    assert obj.obj_type == test_type


def test_widget_init():
    test_id = 'test_id'
    test_type = MiroObjectType.WIDGET
    obj = Widget(test_id, test_type)

    assert obj.obj_id == test_id
    assert obj.obj_type == test_type
    assert obj.capabilities == dict()
    assert obj.metadata == dict()


def test_shape_init():
    test_id = 'test_id'
    test_type = MiroObjectType.SHAPE
    test_text = 'test_text'
    obj = Shape(test_id, test_text)
    assert obj.obj_id == test_id
    assert obj.obj_type == test_type
    assert obj.capabilities == dict()
    assert obj.metadata == dict()
    assert obj.text == test_text
