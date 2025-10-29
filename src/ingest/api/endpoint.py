from flask import Blueprint, request, jsonify

# Create a Blueprint for the API endpoint
ingest_api = Blueprint('ingest_api', __name__)

@ingest_api.route('/ingest', methods=['POST'])
def ingest_data():
    """
    Endpoint to receive data from ESP devices.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Placeholder for validation and dispatch logic
        # validated_data = validate_data(data)
        # dispatch_data(validated_data)

        return jsonify({"message": "Data received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500