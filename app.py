
import numpy as np
from flask import Flask, request, render_template
import pickle


app=Flask(__name__)

model = pickle.load(open(r'C:/Users/Rami Reddy/Desktop/chu/model.pkl', 'rb'))

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/churnpredictor')
def churnpredictor():
    return render_template('churnpredictor.html')

@app.route('/predict',methods=['POST'])
def predict():
  st_features= [x for x in request.form.values()]
  features=[np.array(st_features)]
  prediction=model.predict(features)

  labels = {
    0: "Churned",
    1: "Joined",
    2: "Stayed"
    }

  predicted_label = labels.get(prediction[0], "Unknown")

  output = predicted_label
  return render_template('churnpredictor.html',prediction_text='Customer Churn Prediction for given details is {}'.format(output))

if __name__=="__main__":
  app.run(debug=True)

