from spicadb import SpicaDB

db = SpicaDB(db_folder="my_db")

users = db.collection("users")
user_id = users.insert({'name': 'Alice', 'age': 18})
print(f"Inserted user with ID: {user_id}")