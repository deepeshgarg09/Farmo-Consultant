from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import TextField,SubmitField
from wtforms.validators import NumberRange
import numpy as np 
import joblib
import numpy as np
import pandas as pd
from time import time
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


classifier = joblib.load("crop_pred.pkl")
reversefactor = joblib.load("reversefactor.pkl")

additional_info =pd.read_csv('Prediction.csv')

def model_prediction(arr) :

  a=classifier.predict(arr)
  a = np.vectorize(reversefactor.get)(a)
  return a

def array_changer(location,temperature,soil_type,season):
  crop_dict_one = {'Andhra Pradesh': np.array([[110.75, 9.74]]), 'Assam' : np.array([[156.2, 1.62]]), 'Bihar': np.array([[125.6,7.5]]), 'Chhattisgarh' : np.array([[130.4, 5]]) , 'Goa' : np.array([[295, 13]]), 'Gujrat': np.array([[115.7,35]]), 'Haryana' : np.array([[47.5, 15]]), 'Himachal Pradesh' :np.array([[127.5, 22]]), 'Jharkhand': np.array([[121.4,12]]), 'Karnataka' : np.array([[121.4, 22]]), 'Kerala' : np.array([[315.7, 20]]), 'Madhya Pradesh': np.array([[235.5,22]]), 'Maharashtra' : np.array([[246, 3.2]]), 'Manipur' : np.array([[148.8, 4]]),'Meghalaya': np.array([[117.5,4]]), 'Mizoram' : np.array([[257, 8]]), 'Nagaland' : np.array([[215, 18.1]]), 
             'Odisha': np.array([[215,5]]),'Punjab' : np.array([[60, 8.9]]), 'Rajasthan' : np.array([[48.8, 32]]), 'Sikkim': np.array([[299.5,50]]),
             'Tamil Nadu' : np.array([[145, 16.67]]),'Telangana' :np.array([[87.5, 8]]), 'Tripura': np.array([[238.5,6.7]]), 'Uttar Pradesh' : np.array([[134.65, 6]]), 'Uttarakhand' : np.array([[164.5, 7.5]]), 
             'West Bengal': np.array([[250,9]]), 'Andaman and Nicobar Islands' : np.array([[277, 3.5]]), 'Dadra & Nagar Haveli and Daman & Diu' : np.array([[89, 2]]),
             'Chandigarh': np.array([[105.5,28]]), 'Jammu and Kashmir': np.array([[111.5,17]]), 'Delhi' : np.array([[90,6.7]]),
             'Lakshdweep' : np.array([[30, 3.8]]), 'Puducherry': np.array([[137.5,12.3]]), 'Ladakh' : np.array([[15,22.3]])  }

  for i,j in crop_dict_one.items() :
    if i==location :
      loc = j     

  temp = np.array([[float(temperature)]])

  crop_dict_two = {'Alluvial': np.array([[1,0,0,0,0,0]]), 'Black':np.array([[0,1,0,0,0,0]]), 'Clayey': np.array([[0,0,1,0,0,0]]), 'Latterite': np.array([[0,0,0,1,0,0]]),  
                 'Red': np.array([[0,0,0,0,1,0]]), 'Sandy':np.array([[0,0,0,0,0,1]]) }

  for a,b in crop_dict_two.items() :
    if a==soil_type :
      soil = b                   

  crop_dict_three = { 'All Season': np.array([[1,0,0,0]]), 'Kharif': np.array([[0,1,0,0]]), 'Rabi': np.array([[0,0,1,0]]), 'Zaid': np.array([[0,0,0,1]]) }

  for c,d in crop_dict_three.items() :
    if c==season :
      season_ = d 

  final_arr = np.hstack((loc, temp, soil, season_))
  return final_arr


app = Flask(__name__)

app.config['SECRET_KEY'] = 'someRandomKey'

class FlowerForm(FlaskForm):
    loc = TextField('Location')
    temperature = TextField('Temperature')
    soil_type = TextField('Soil Type')
    season = TextField('Season')

    submit = SubmitField('Analyze')



@app.route('/', methods=['GET', 'POST'])
def index():
    form = FlowerForm()
    if form.validate_on_submit():

        session['loc'] = form.loc.data
        session['temperature'] = form.temperature.data
        session['soil_type'] = form.soil_type.data
        session['season'] = form.season.data
        # print(session['loc'])

        return redirect(url_for("prediction"))

    return render_template('index.html', form=form)


@app.route('/prediction')
def prediction():

    arr = array_changer(location=session['loc'],temperature=session['temperature'],soil_type=session['soil_type'],season=session['season'])

    results= model_prediction(arr)
    results=results[0]
    crop_string = results[0]
  
    final_df = additional_info[additional_info['Crops'].str.contains(crop_string)]

    fertilisers =final_df['Fertilisers required'].values[0]
    cost_of_cultivation = final_df['Cost of cultivation'].values[0]
    expected_revenues = final_df['Expected revenues'].values[0]
    seeds_required = final_df['Quantity of seeds per hectare'].values[0]
    duration_cultivation = final_df['Duration of cultivation'].values[0]
    mixed_cropping = final_df['Crops for mixed cropping'].values[0]


    return render_template('prediction.html',results=results, f=fertilisers,
     c =cost_of_cultivation, e= expected_revenues,s= seeds_required,d=duration_cultivation,
     m=mixed_cropping)


if __name__ == '__main__':
    app.run(debug=True)
