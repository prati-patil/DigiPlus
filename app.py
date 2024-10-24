from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Simulated node data
nodes = [
    {"id": 1, "packets_generated": 0, "link_load": 0, "packets_in_queue": 0},
    {"id": 2, "packets_generated": 0, "link_load": 0, "packets_in_queue": 0},
    {"id": 3, "packets_generated": 0, "link_load": 0, "packets_in_queue": 0},
]

def simulate_traffic():
    for node in nodes:
        node["packets_generated"] += random.randint(0, 9)  # Random packets generated (0-9)
        node["link_load"] = random.randint(0, 100)  # Random link load (0-100)
        node["packets_in_queue"] = random.randint(0, 19)  # Random packets in queue (0-19)

@app.route('/api/nodes', methods=['GET'])
def get_nodes():
    simulate_traffic()  # Update node data
    return jsonify(nodes)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
