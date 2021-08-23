from flask import Flask, render_template, request
import numpy as np
import pickle
from sklearn import *

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    
    if request.method == "POST" :
        try:
            age =                   float(request.form.get('age'))
            bmi =                   float(request.form.get('bmi'))
            avg_glucose_level =     float(request.form.get('avg_glucose_level'))
            smoking_status =               int(request.form.get('smoking'))
            work_type =                  int(request.form.get('work'))
            gender =                int(request.form.get('gender'))
            hypertension =          int(request.form.get('hypertension'))
            heart_disease =          int(request.form.get('heartdisease'))
            ever_married =               int(request.form.get('married'))
            Residence_type =             int(request.form.get('residence'))

            work_type_Never_worked = int(work_type == 5)
            work_type_Private = int(work_type == 1)
            work_type_Self_employed = int(work_type == 2)
            work_type_children = int(work_type == 4)
            smoking_status_formerly_smoked = int(smoking_status == 1)
            smoking_status_never_smoked = int(smoking_status == 2)
            smoking_status_smokes = int(smoking_status == 3)
            
            features = np.array([[gender, age, hypertension, heart_disease, ever_married, Residence_type, avg_glucose_level, bmi, 
                                   work_type_Never_worked, work_type_Private,
                                work_type_Self_employed, work_type_children, smoking_status_formerly_smoked, smoking_status_never_smoked, smoking_status_smokes]])

            input = open('modelpredict.pickle','rb')
            trained_model = pickle.load(input)

            prediction = trained_model.predict(features)
            
            if prediction == 1:
                text = "The customer is likely to have a stroke "
            else:
                text = "The customer is not likely to have a stroke"

            return render_template("index4.html", pred = text)
        
        except:
            return "Please enter valid values"

    else:
        return render_template("index4.html")


if __name__ == "__main__":
    app.run(debug = True)