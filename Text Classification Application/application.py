from flask import Flask, request, jsonify
#Initializing
app = Flask(__name__)

#Route
@app.route("/classify", methods=["POST"])
def classify():
    text = request.json.get("text")
    if not text:
        return jsonify({"error": "Missing text input"}), 400
    proba = predict_proba(text)
    return jsonify({"topics": proba})
if __name__ == "__main__":
    app.run(debug=True)