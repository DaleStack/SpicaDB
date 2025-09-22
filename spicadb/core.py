import json
import uuid
import os

class SpicaDB:
    def __init__(self, db_folder='spicadb_data'):
        """ Initialize DB with a folder to store collection files """
        self.db_folder = db_folder
        self.collections = {}

        if not os.path.exists(self.db_folder):
            os.makedirs(self.db_folder)

