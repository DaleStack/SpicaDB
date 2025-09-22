import json
import uuid
import os
from typing import Dict, Any

class SpicaDB:
    def __init__(self, db_folder='spicadb_data'):
        """ Initialize DB with a folder to store collection files """
        self.db_folder = db_folder
        self.collections = {}

        if not os.path.exists(self.db_folder):
            os.makedirs(self.db_folder)

    def collection(self, name: str):
        """ Get or create collection """
        if name not in self.collections:
            self.collections[name] = Collection(name, self.db_folder)
        return self.collections[name]


class Collection:
    def __init__(self, name: str, db_folder: str):
        self.name = name
        self.filename = os.path.join(db_folder, f"{name}.json")
        self.store = self._load_collection()

    def _load_collection(self) -> Dict[str, Any]:
        """ Load collection data to json file """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def _save(self):
        """ Save collection data to JSON file """
        with open(self.filename, 'w') as file:
            json.dump(self.store, file, indent=2)

        
