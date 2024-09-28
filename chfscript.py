from flask import Flask, request, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_data():
    # Get the data sent from Typeform
    data = request.get_json()
    
    # Process the data (simple echo in this case)
    # You can also include validation, transformation, etc.
    response = process_data(data)

    # Store the response in MongoDB
    store_in_mongodb(response)
    
    return jsonify({"status": "success", "data": response}), 200

def process_data(data):
    # Add your logic to process the Typeform data here
    processed_data = {
        'name': data['form_response']['answers'][0]['text'],  # Example: extract a name
        'email': data['form_response']['answers'][1]['email'], # Example: extract an email
        # Add other fields as needed
    }
    return processed_data

def store_in_mongodb(data):
    # MongoDB connection
    client = MongoClient("mongodb://localhost:27017/")
    db = client['typeform_db']
    collection = db['form_responses']
    
    # Insert the processed data into MongoDB
    collection.insert_one(data)

if __name__ == '__main__':
    app.run(debug=True)