from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home():
    title = 'Customer Check in Predictify'
    return render_template("index.html", title = title)
@app.route("/results")
def Results():
    title = 'Result'
    return render_template("result.html",title=title)
if __name__ == "_main_":
    app.run(debug=False)