from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("portfolio.html")

@app.route("/about_me")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/works')
def works():
    return render_template("works.html")


if __name__ == "__main__":
    app.run(debug=True, port=7000)
