from flask import Flask, jsonify
from flask_cors import CORS
import views


app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    title = "homepage"
    return jsonify({"title": title})

app.add_url_rule('/present', view_func=views.present)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)