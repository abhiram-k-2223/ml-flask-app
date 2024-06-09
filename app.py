from flask import Flask, url_for, render_template, request
from forms import InputForm  # Assuming you have a forms.py with InputForm defined

import pandas as pd
import joblib

app = Flask(__name__)
app.config["SECRET_KEY"] = "abhiram"

model = joblib.load('stars.joblib')
le = joblib.load('le.joblib')

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    message = ""  # Initialize message here
    if form.validate_on_submit():
        x_new = pd.DataFrame({
            'Temperature (K)': [form.temperature.data],
            'Luminosity (L/Lo)': [form.Luminosity.data],
            'Radius (R/Ro)': [form.radius.data],
            'Absolute magnitude (Mv)': [form.Absmag.data]
        })
        prediction = model.predict(x_new)[0]
        category = le.inverse_transform([prediction])[0]
        message = f'You are looking at a {category} star!!!'
    return render_template("predict.html", title="Prediction", form=form, output=message)

if __name__ == "__main__":
    app.run(debug=True)


