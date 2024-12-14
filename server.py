from flask import Flask, request, jsonify

app = Flask(__name__)

data = [
    {"id": 111, "name": "One", "short_sentence": "this is one"},
    {"id": 222, "name": "Two", "short_sentence": "this is Two"},
]

@app.route("/my-policies", methods=["GET"])
def handle_query():
    ref_number = request.args.get("refNumber")
    
    if not ref_number:
        return jsonify({"error": "refNumber is required"}), 400
    
    try:
        ref_number = int(ref_number)
    except ValueError:
        return jsonify({"error": "refNumber must be a valid integer"}), 400

    result = next((item for item in data if item["id"] == ref_number), None)
    
    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "Object not found for refNumber"}), 404

if __name__ == "__main__":
    app.run(debug=True)