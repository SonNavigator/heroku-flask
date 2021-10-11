from flask import Flask, json, jsonify


app = Flask(__name__)


data = {
    'name': "Son",
    'fb': "STACKPYTHON"
}


@app.route('/api')
def hello():
    # Serialize an object, then return to JSON format
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)



