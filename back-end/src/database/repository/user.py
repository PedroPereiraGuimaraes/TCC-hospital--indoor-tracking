from database.connection_db import Database
import json
from bson import json_util 

class UserDAO: # DAO - Data Access Object
    def __init__(self):
        self.db = Database(database="indoor_db", collection="user")

    def get_all(self):
        try:
            res = self.db.collection.find()
            print("total users: ", res)

            parsed_json = json.loads(json_util.dumps(res))

            return parsed_json
        except Exception as e:
            print(f"Houve um erro ao tentar pegar os usuários: {e}")
            return None
