import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import model

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

deliveries = []
delivery_id_counter = 1

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/deliveries")
def get_deliveries():
    return jsonify(deliveries)

@app.get("/deliveries/<int:delivery_id>")
def get_delivery(delivery_id: int):
    d = next((x for x in deliveries if x["id"] == delivery_id), None)
    if not d:
        return jsonify({"error": "not found"}), 404
    return jsonify(d)

@app.post("/create_delivery")
def create_delivery():
    global delivery_id_counter
    data = request.get_json(force=True)
    required = ["payload", "priority", "dropoff"]
    if any(k not in data for k in required):
        return jsonify({ "error": "payload, priority, dropoff required" }), 400

    start = [10, 10]
    end = data["dropoff"]
    route = model.generate_route(start, end, data["priority"])

    delivery = {
        "id": delivery_id_counter,
        "payload": data["payload"],
        "priority": data["priority"],
        "dropoff": end,
        "route": route,
        "status": "In Progress",
        "eta_minutes": max(1, len(route) // 2)
    }
    deliveries.append(delivery)
    delivery_id_counter += 1
    return jsonify({ "status": "success", "delivery": delivery }), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
