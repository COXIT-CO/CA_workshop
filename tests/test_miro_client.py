from miro_client.client import MiroApiClient

from miro_client.miro_entities import *
from miro_client.miro_data_processes import *


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
                           db_path='database/ids.json')
    assert client.base_url == test_url
    assert client.auth_token == test_token
    assert client.auth_header_as_dict == test_header


def test_get_all_shapes_from_widgets():
    test_widgets_json = [
        {'id': '3074457367605439232', 'style': {'backgroundOpacity': 1.0, 'backgroundColor': '#ffffffff', 'borderColor':'#1a1a1a', 'borderStyle': 'normal', 'borderOpacity': 1.0, 'borderWidth': 2.0, 'fontSize': 14, 'fontFamily': 'Arial', 'textColor': '#1a1a1a', 'textAlign': 'center', 'textAlignVertical': 'middle', 'shapeType': 'callout'}, 'text': '<p>Votes : 2</p>', 'x': -81.246976613329, 'y': -1595.03753099837, 'width': 206.615064610596, 'height': 63.9708825889426, 'rotation': 0.0, 'type': 'shape', 'createdAt': '2021-11-14T18:12:28Z', 'modifiedAt': '2021-11-14T18:36:24Z', 'modifiedBy': {'type': 'user', 'name': 'Єгор Жорновий', 'id': '3074457363886482721'}, 'createdBy': {'type': 'user', 'name': 'Єгор Жорновий', 'id': '3074457363886482721'}},
        {'id': '3074457367605439248', 'startWidget': {'id': '3074457367605439230'}, 'endWidget': {'id': '3074457367605439232'}, 'style': {'borderColor': '#000000', 'borderStyle': 'normal', 'borderWidth': 1.0, 'lineEndType': 'opaque_block','lineStartType': 'none', 'lineType': 'bezier'}, 'type': 'line', 'createdAt': '2021-11-14T18:12:28Z','modifiedAt': '2021-11-14T18:13:05Z','modifiedBy': {'type': 'user', 'name': 'Єгор Жорновий', 'id': '3074457363886482721'},'createdBy': {'type': 'user', 'name': 'Єгор Жорновий', 'id': '3074457363886482721'}}
        ]
    res = get_all_shapes_from_widgets(test_widgets_json)
    expected_result = [Shape(test_widgets_json[0]['id'], test_widgets_json[0]['text'])]
    assert res[0].__dict__ == expected_result[0].__dict__


def test_increment_voting_text():
    test_data = {'id': '1234', 'text': '<p>Votes : 2</p>'}
    test_shape = Shape(test_data['id'], test_data['text'])
    res = increment_voting_text([test_shape], '1234')
    assert res.text == '<p>Votes : 3</p>'
