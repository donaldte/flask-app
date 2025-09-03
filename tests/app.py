from flask import Flask, jsonify

# Créer une instance de l'application Flask
app = Flask(__name__)

# Route simple pour tester l'API
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Flask!"})

# Point d'entrée pour lancer l'application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)