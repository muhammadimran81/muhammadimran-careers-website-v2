from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def my_first_flask_app():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)