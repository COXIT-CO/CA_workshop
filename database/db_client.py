# DATABASE GATEWAY
import dataclasses


@dataclasses.dataclass
class DatabaseClient:
    db_path = 'database/ids.json'
    
    def get_id_by_num(num):

        return blocks_ids.get(num)