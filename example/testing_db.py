from spicadb import SpicaDB

db = SpicaDB(db_folder="my_db")

pets = db.collection("pets")
pet_id = pets.insert({'name': 'Navi', 'type': "Cat"})
print(f"Inserted pet with ID: {pet_id}")

data = pets._load_document(pet_id)
print(f"Loaded pet ID: {pet_id}")

print(f"All Document IDs: {pets._get_all_document_ids()}")