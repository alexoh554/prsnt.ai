from flask import Flask, jsonify
from flask_cors import CORS
import views


app = Flask(__name__)

CORS(app)


app.add_url_rule('/image_search', view_func=views.image_search)

app.add_url_rule('/cohere', view_func=views.cohere)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
