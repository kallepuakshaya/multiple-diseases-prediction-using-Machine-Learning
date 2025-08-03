# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 12:40:00 2025

@author: PC
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
diabetic_model=pickle.load(open('diabeticdiseases_trained_model.sav','rb'))
heart_diseases_model=pickle.load(open('heartdiseases_trained_model.sav','rb'))
with st.sidebar:
    selected=option_menu('multiple diseases predictive system',['Diabetic prediction','Heart diseases prediction'],default_index=0)
if(selected=='Diabetic prediction'):
    st.title('Diabetic prediction using ml')
    col1,col2,col3=st.columns(3)
    with col1:
         Pregnancies=st.text_input('no.of.pregnacies')
    with col2:
         Glucose=st.text_input('glucose level')
    with col3:
         BloodPressure=st.text_input('Bloodpressure value')
    with col1:
         SkinThickness=st.text_input('skin thick ness')
    with col2:
         Insulin=st.text_input('insulin level')
    with col3:
         BMI=st.text_input('BMI')
    with col1:
         DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function')
    with col2:
         Age=st.text_input('Age of a person')
    
    diab_diagnosis=''
    if st.button('diabetic test result'):
        diab_prediction=diabetic_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if (diab_prediction[0]==1):
            diab_diagnosis='the person is diabetic'
        else:
            diab_diagnosis='the person is not diabetic'
    st.success(diab_diagnosis)

     
     
   # Heart Disease Prediction Page
if (selected == 'Heart diseases prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
    
        try:
            heart_prediction = heart_diseases_model.predict([[
        float(age), float(sex), float(cp), float(trestbps),
        float(chol), float(fbs), float(restecg), float(thalach),
        float(exang), float(oldpeak), float(slope), float(ca), float(thal)
    ]])
        except ValueError as e:
               print("Invalid input:", e)                
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)

        




