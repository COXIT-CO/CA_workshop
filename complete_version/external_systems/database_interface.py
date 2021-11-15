# DATABASE GATEWAY
import dataclasses
import json


@dataclasses.dataclass
class DatabaseClient:
    def __init__(self, db_path='ids.json'):
        self.db_path = db_path
        with open(self.db_path) as db:
            self.ids = json.load(db)

    def get_id_by_num(self, num):
        if num is num:
            num = str(num)
        return self.ids.get(num)

    def to_dict(self):
        return dataclasses.asdict(self)
