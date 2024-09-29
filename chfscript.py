from flask import Flask, request, jsonify
from pymongo import MongoClient
import re
from pymongo.errors import ConnectionFailure

# Define your MongoDB connection string
mongo_uri = 'mongodb+srv://hackgt:hackgt@hackgtcluster.fltr4.mongodb.net/?retryWrites=true&w=majority&appName=HackGTCluster'  # Change this if necessary

client = MongoClient(mongo_uri)

app = Flask(__name__)

@app.route('/submit_task', methods=['POST'])
def submit_task():
    jmap = request.json  # Get the data sent by Typeform
    severity = jmap["data"]
    ex = re.sub(r'\*\*.*?\*\*:\s*', '', jmap["explanation"])

    # Process the task data (e.g., save to database)
    print(f"New task submitted: {data}")
    
    return jsonify({"message": "Task received", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True)

# client = MongoClient("hackgtcluster.fltr4.mongodb.net")  # Use your MongoDB URI if hosted remotely
# db = client["typeform_db"]  # Replace with your database name
# collection = db["responses"]  # Collection name

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     jmap = request.json  # Get the data sent by Typeform
#     severity = jmap["data"]
#     ex = re.sub(r'\*\*.*?\*\*:\s*', '', jmap["explanation"])

    
#     # Step 2: Insert the data into MongoDB
#     result = collection.insert_one(data)  # Insert data into the collection
    
#     # Respond back to confirm receipt of the webhook
#     return jsonify({'status': 'received', 'inserted_id': str(result.inserted_id)}), 200

if __name__ == '__main__':
    app.run(port=5000)