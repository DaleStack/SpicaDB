from spicadb import SpicaDB

db = SpicaDB()

users = db.collection("users")
user_id = users.insert({'name': 'Alice', 'age': 18})
print(f"Inserted user with ID: {user_id}")