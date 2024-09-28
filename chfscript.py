from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")  # Use your MongoDB URI if hosted remotely
db = client["typeform_db"]  # Replace with your database name
collection = db["responses"]  # Collection name

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Get the data sent by Typeform
    print(f"New Typeform Response: {data}")
    
    # Step 2: Insert the data into MongoDB
    result = collection.insert_one(data)  # Insert data into the collection
    
    # Respond back to confirm receipt of the webhook
    return jsonify({'status': 'received', 'inserted_id': str(result.inserted_id)}), 200

if __name__ == '__main__':
    app.run(port=5000)