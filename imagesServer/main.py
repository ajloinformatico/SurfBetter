from flask import Flask
from route import api_images

app = Flask(__name__)
app.register_blueprint(api_images)



if __name__ == '__main__':
    app.run(debug=True, port=8000, host=0000)