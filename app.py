from flask import Flask

app = Flask(__name__)
@app.route("/")
def my_first_flask_app():
    return "Test the flask web"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)