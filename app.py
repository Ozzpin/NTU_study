from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model_1 = joblib.load("regression")
        r_1 = model_1.predict([[rates]])
        model_2 = joblib.load("tree")
        r_2 = model_1.predict([[rates]])
        return render_template("index.html", result1 = r_1, result2 = r_2)
    else:
        return render_template("index.html", result1 = "WAITING", result2 = "WAITING")

if __name__ == "__main__":
    app.run()
