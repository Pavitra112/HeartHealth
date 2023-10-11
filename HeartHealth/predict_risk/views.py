from django.shortcuts import render
from .forms import Predict_Form
from accounts.models import UserProfileInfo
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from sklearn.linear_model import LinearRegression
import numpy as np
@login_required(login_url='/')
def PredictRisk(request,pk):
    predicted = False
    answer=0
    predictions=0
    if request.session.has_key('user_id'):
        u_id = request.session['user_id']

    if request.method == 'POST':
        form = Predict_Form(data=request.POST)
        profile = get_object_or_404(UserProfileInfo, pk=pk)
        # Extract values from form fields and convert them to integers
        age = int(form['age'].value())
        gender = int(form['gender'].value())
        cp = int(form['cp'].value())
        resting_bp = int(form['resting_bp'].value())
        serum_cholesterol = int(form['serum_cholesterol'].value())
        fasting_blood_sugar = int(form['fasting_blood_sugar'].value())
        resting_ecg = int(form['resting_ecg'].value())
        max_heart_rate = int(form['max_heart_rate'].value())
        exercise_induced_angina = int(form['exercise_induced_angina'].value())
        st_depression = float(form['st_depression'].value())
        st_slope = int(form['st_slope'].value())

        # Create a features list with the extracted and converted values
        features = [[age, gender, cp, resting_bp, serum_cholesterol, fasting_blood_sugar, resting_ecg, max_heart_rate, exercise_induced_angina, st_depression, st_slope]]

        lr = LinearRegression()
        lr.intercept_ = [0.04036609]
        lr.coef_ = np.array([[ 0.00265557, -0.16398325,  0.1116549 ,  0.00084365, -0.0004857 , 0.1416075, -0.0008661,  -0.00122041,  0.17004547,  0.05761804 , 0.22223918]])
        predictions = lr.predict(features) 
        answer = int(str(predictions[0][0])[0])
        sn = int(str(predictions[0][0])[2])
        pred = form.save(commit=False)
        
        predicted = True
        if answer == 1:
            colors = "table-danger"
            pred.result=1
        else:
            if sn > 5:
                answer = 1
                colors = "table-danger"
                pred.result=1
            else:
                colors = "table-success"
                pred.result=0
        pred.profile = profile
        pred.save()

    if predicted:
        return render(request, 'predict.html',
                      {'form': form,'predicted': predicted,'user_id':u_id,'predictions':answer,'result':answer,'colors':colors})
        
    else:
        form = Predict_Form()

        return render(request, 'predict.html',
                      {'form': form,'predicted': predicted,'user_id':u_id,'predictions':answer})
