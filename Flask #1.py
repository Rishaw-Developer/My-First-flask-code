from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home/<name>/<int:age>")
def home(name, age):
    return f"<h1>Hello {name} {age}</h1>"


@app.route("/")
def get():
    return "hey"


@app.route("/title")
def html_hai():
	return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
