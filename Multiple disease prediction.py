# -*- coding: utf-8 -*-
"""
Created on Sun May  5 23:06:46 2024

@author: skeme
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


diabetes_model = pickle.load(open('C:/Users/skeme/OneDrive/Masaüstü/Multiple Disease Prediction/Saved MoDELS/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/skeme/OneDrive/Masaüstü/Multiple Disease Prediction/Saved MoDELS/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/skeme/OneDrive/Masaüstü/Multiple Disease Prediction/Saved MoDELS/parkinson_model.sav','rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System Using Machine Learning',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Liver Disease Prediction'
                            ],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)
    
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

    
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')
    
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
if selected == "Liver Disease Prediction":

    # page title
    st.title("Liver Disease Prediction using ML")