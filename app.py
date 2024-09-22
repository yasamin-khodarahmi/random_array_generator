import os
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import numpy as np
from pymongo import MongoClient
from bson import ObjectId
import logging
from dotenv import load_dotenv

# Load environment variables and set up logging
load_dotenv()
logging.basicConfig(level=logging.INFO)

# Initialize Flask app and SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
socketio = SocketIO(app, cors_allowed_origins="*")

# MongoDB connection
client = MongoClient(os.getenv('MONGO_URI', 'mongodb://localhost:27017/'))
db = client[os.getenv('DB_NAME', 'random_arrays')]
collection = db[os.getenv('COLLECTION_NAME', 'arrays')]

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@socketio.on('generate_array')
def generate_array(data):
    """Generate a random array and broadcast it to all clients."""
    try:
        size = max(int(data['size']), 10000)
        min_val, max_val = int(data['min']), int(data['max'])
        random_array = np.random.randint(min_val, max_val + 1, size=size)
        array_id = collection.insert_one({'array': random_array.tolist()}).inserted_id
        emit('new_array', {'array': random_array.tolist()[:100], 'id': str(array_id), 'total_size': size}, broadcast=True)
    except Exception as e:
        logging.error(f"Error generating array: {str(e)}")
        emit('error', {'message': str(e)})

@app.route('/get_arrays', methods=['GET'])
def get_arrays():
    """Retrieve all array IDs from the database."""
    try:
        arrays = list(collection.find({}, {'_id': 1}))
        return jsonify([str(arr['_id']) for arr in arrays])
    except Exception as e:
        logging.error(f"Error retrieving array IDs: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/get_array/<array_id>', methods=['GET'])
def get_array(array_id):
    """Retrieve a specific array from the database."""
    try:
        array = collection.find_one({'_id': ObjectId(array_id)})
        if array:
            return jsonify({'array': array['array'][:100], 'total_size': len(array['array'])})
        return jsonify({'error': 'Array not found'}), 404
    except Exception as e:
        logging.error(f"Error retrieving array {array_id}: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    socketio.run(app, debug=os.getenv('DEBUG', 'False').lower() == 'true', port=port)
