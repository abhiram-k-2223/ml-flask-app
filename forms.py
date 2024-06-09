from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    DecimalField
)
from wtforms.validators import DataRequired

import pandas as pd
train = pd.read_csv(r'C:\Users\LENOVO T480\3D Objects\flask-ml-project\data\train.csv')
test = pd.read_csv(r'C:\Users\LENOVO T480\3D Objects\flask-ml-project\data\test.csv')
x_data = pd.concat([train,test],axis = 0)

class InputForm(FlaskForm):
    temperature = DecimalField(
        label = "Temperature in Kelvin",
        validators=[DataRequired()]
    )
    Luminosity = DecimalField(
        label = "Luminosity (L/Lo)"
    )
    radius = DecimalField(
        label = "Radius (R/Ro)",
        validators = [DataRequired()]
    )
    Absmag = DecimalField(
        label = "Absolute Magnitude (Mv)",
        validators = [DataRequired()]
    )
    submit = SubmitField("Submit")


