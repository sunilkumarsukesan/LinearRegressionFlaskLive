from flask import Flask, render_template, request,session,url_for,redirect,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] ='mysecretkey'

class InfoForm(FlaskForm):
    Avg_Area_Income = StringField('Avg Area Income',validators=[DataRequired()])
    Avg_Area_House_Age	= StringField('Avg_Area_House_Age',validators=[DataRequired()])
    Avg_Area_Number_of_Rooms = StringField('Avg_Area_Number_of_Rooms',validators=[DataRequired()])
    Avg_Area_Number_of_Bedrooms= StringField('Avg_Area_Number_of_Bedrooms',validators=[DataRequired()])
    Area_Population	= StringField('Area_Population',validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def homepage():
    form = InfoForm()
    if form.validate_on_submit():
        pred = joblib.load("E:\\Data Science\\My Learnings\\DataScience\\01 Linear Regression\\Project1 Reading\\housingmodel.pkl")
        value = pred.predict([[float(form.Avg_Area_Income.data),
        float(form.Avg_Area_House_Age.data),float(form.Avg_Area_Number_of_Rooms.data),
        float(form.Avg_Area_Number_of_Bedrooms.data),float(form.Area_Population.data)]])[0]
        session['value']= round(value,2)
        return redirect(url_for('predictedPrice'))
    return render_template ("homepage.html",form=form)

@app.route('/predictedPrice')
def predictedPrice():
    return render_template('predictedPrice.html')

@app.errorhandler(404)
def pagenotfound(e):
    return render_template("404.html"),404

if __name__ == '__main__':
    app.run(debug=True)
