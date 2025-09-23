import json
import uuid
import os
from typing import Dict, List, Any, Optional
import glob

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
        self.colletion_folder = os.path.join(db_folder, name)

        if not os.path.exists(self.colletion_folder):
            os.makedirs(self.colletion_folder)

    def _get_document_path(self, doc_id: str) -> str:
        """ Get file path for a document """
        return os.path.join(self.colletion_folder, f"{doc_id}.json")

    def _generate_id(self) -> str:
        """ Generate unique document ID """
        return str(uuid.uuid4())

    def _save_document(self, doc_id: str, document: Dict[str, Any]):
        """ Save individual document to file """
        file_path = self._get_document_path(doc_id)
        with open(file_path, 'w') as file:
            json.dump(document, file, indent=2)

    def _load_document(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """ Load individual document from file """
        file_path = self._get_document_path(doc_id)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return None
    
    def _get_all_document_ids(self) -> List[str]:
        """ Get all document IDs in collection """
        pattern = os.path.join(self.colletion_folder, "*.json")
        files = glob.glob(pattern)
        return [os.path.splitext(os.path.basename(f))[0] for f in files]

