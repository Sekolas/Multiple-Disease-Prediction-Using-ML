# -*- coding: utf-8 -*-
"""
Created on Sun May  5 23:06:46 2024

@author: skeme
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import lightgbm


diabetes_model = pickle.load(open('C:/Users/skeme/OneDrive/Masaüstü/Multiple Disease Prediction/Saved MoDELS/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/skeme/OneDrive/Masaüstü/Multiple Disease Prediction/Saved MoDELS/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/skeme/OneDrive/Masaüstü/Multiple Disease Prediction/Saved MoDELS/parkinson_model.sav','rb'))

Liver_model = pickle.load(open('C:/Users/skeme/OneDrive/Masaüstü/Multiple Disease Prediction/Saved MoDELS/liver_diseasemodel.sav','rb'))

kidney_model = pickle.load(open('C:/Users/skeme/OneDrive/Masaüstü/Multiple Disease Prediction/Saved MoDELS/kidney_disease.sav','rb'))

Thyroid_model = pickle.load(open('C:/Users/skeme/OneDrive/Masaüstü/Multiple Disease Prediction/Saved MoDELS/thryoid_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System Using Machine Learning',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Liver Disease Prediction',
                            'Kidney Disease Prediction',
                            'Thyroid Disease Prediction'                                                      
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
        
        empty_inputs = [index for index, value in enumerate(user_input) if value is None or value == '']
        
        if empty_inputs:
            
            st.error("Please fill all the fields.")
        
        else:
            user_input = [float(x) for x in user_input]
            
            diab_prediction = diabetes_model.predict([user_input])

            if (diab_prediction[0] == 0):
                diab_diagnosis = 'The person is not diabetic'
            else:
                diab_diagnosis = 'The person is diabetic'

    st.success(diab_diagnosis)

    
if selected == 'Heart Disease Prediction':
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
       

       user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
       
       empty_inputs = [index for index, value in enumerate(user_input) if value is None or value == '']
       
       if empty_inputs:
    
           st.error("Please fill all the fields.")
       else:
           user_input = [float(x) for x in user_input]

           heart_prediction = heart_disease_model.predict([user_input])

           if heart_prediction[0] == 1:
               heart_diagnosis = 'The person is having heart disease'
           else:
               heart_diagnosis = 'The person does not have any heart disease'
           

   st.success(heart_diagnosis)

    
if selected == "Parkinsons Prediction":

  # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
if selected == "Liver Disease Prediction":

    # page title
    st.title("Liver Disease Prediction using ML")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')

    with col2:
        gender = st.text_input('Gender')

    with col3:
        blb = st.text_input('Total_Bilirubin')

    with col1:
        blb2 = st.text_input('Direct_Bilirubin')

    with col2:
        alkln = st.text_input('Alkaline_Phosphotase')

    with col3:
        almn = st.text_input('Alamine_Aminotransferase')

    with col1:
        asprt = st.text_input('Aspartate_Aminotransferase')

    with col2:
        protein = st.text_input('Total_Protiens')

    with col3:
        albumin = st.text_input('Albumin')

    with col1:
        albm_glbm = st.text_input('Albumin_and_Globulin_Ratio')

    

    # code for Prediction
    liverdisease_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Liver Diseases Test Result"):

        user_input = [age, gender, blb, blb2, alkln,
                      almn, asprt, protein, albumin,albm_glbm]
        
        
        empty_inputs = [index for index, value in enumerate(user_input) if value is None or value == '']
        
        if empty_inputs:
     
            st.error("Please fill all the fields.")

        else:
            user_input = [float(x) for x in user_input]

            liver_prediction = Liver_model.predict([user_input])

            if liver_prediction[0] == 1:
                liverdisease_diagnosis = "The person has liver disease"
            else:
                liverdisease_diagnosis = "The person does not have liver disease"

    st.success(liverdisease_diagnosis)
    
if selected == "Kidney Disease Prediction":

    # page title
    st.title("Kidney Disease Prediction Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.text_input('age')

    with col2:
        bp = st.text_input('bp')

    with col3:
        sg = st.text_input('sg')

    with col4:
        al = st.text_input('al')

    with col5:
        su = st.text_input('su')

    with col1:
        rbc = st.text_input('rbc')

    with col2:
        pc = st.text_input('pc')

    with col3:
        ppc = st.text_input('ppc')

    with col4:
        ba = st.text_input('ba')

    with col5:
        bgr = st.text_input('bgr')

    with col1:
        bu = st.text_input('bu')

    with col2:
        sc = st.text_input('sc')

    with col3:
        sod = st.text_input('sod')

    with col4:
        pot = st.text_input('pot')

    with col5:
        hemo = st.text_input('hemo')

    with col1:
        pvc = st.text_input('pvc')

    with col2:
        wc = st.text_input('wc')

    with col3:
        rc = st.text_input('rc')

    with col4:
        htn = st.text_input('htn')

    with col5:
        dm = st.text_input('dm')

    with col1:
        cad = st.text_input('cad')

    with col2:
        appet = st.text_input('appet'),
        
    with col3:
        
        pe = st.text_input('pe')
        
    with col1:
        
        ane = st.text_input('ane')

    # code for Prediction
    kidney_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Kidney Diseases Test Result"):

        user_input = [age,bp,sg,al,su,rbc,pc,ppc,ba,bgr,bu,sc,sod,pot,hemo,pvc,wc,rc,htn,dm,cad,appet,pe,ane]
        
        empty_inputs = [index for index, value in enumerate(user_input) if value is None or value == '']
        
        if empty_inputs:
     
            st.error("Please fill all the fields.")

        else:
            user_input = [float(x) for x in user_input]

            kidney_prediction = kidney_model.predict([user_input])

            if kidney_prediction[0] == 1:
                kidney_diagnosis = "The person has kidney disease"
            else:
                kidney_diagnosis = "The person does not have kidney disease"

    st.success(kidney_diagnosis)

if selected == "Thyroid Disease Prediction":

    # page title
    st.title("Thyroid Disease Prediction Prediction Prediction using ML")
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.text_input('age')

    with col2:
        sex = st.text_input('sex')

    with col3:
        on_thyroxine = st.text_input('on thyroxine')

    with col4:
        query_on_thyroxine = st.text_input('query on thyroxine')

    with col1:
        on_antithyroid_medication = st.text_input('on antithyroid medication')

    with col2:
        sick = st.text_input('sick')

    with col3:
        pregnant = st.text_input('pregnant')

    with col4:
        thyroid_surgery = st.text_input('thyroid surgery')

    with col1:
        Shimmer = st.text_input('ba')

    with col2:
        I131_treatment = st.text_input('I131 treatment')

    with col3:
        query_hypothyroid = st.text_input('query hypothyroid')

    with col4:
        query_hyperthyroid = st.text_input('query hyperthyroid')

    with col1:
        lithium = st.text_input('lithium')

    with col2:
        goitre = st.text_input('goitre')

    with col3:
        tumor = st.text_input('tumor')

    with col4:
        hypopituitary = st.text_input('hypopituitary')

    with col1:
        psych = st.text_input('psych')

    with col2:
        TSH = st.text_input('TSH')

    with col3:
        T3 = st.text_input('T3')

    with col4:
        TT4 = st.text_input('TT4')

    with col1:
        T4U = st.text_input('T4U')

    with col2:
        FTI = st.text_input('FTI'),
 
    # code for Prediction
    thyroid_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Thyroid's Test Result"):

        user_input = [age,sex,on_thyroxine,query_on_thyroxine,on_antithyroid_medication,sick,pregnant,thyroid_surgery,Shimmer,
                      I131_treatment,query_hypothyroid,query_hyperthyroid,lithium,goitre,tumor, hypopituitary,psych,TSH,T3,TT4,T4U,FTI]
        
        empty_inputs = [index for index, value in enumerate(user_input) if value is None or value == '']
        
        if empty_inputs:
     
            st.error("Please fill all the fields.")

        else:
            user_input = [float(x) for x in user_input]
           
            thyroid_prediction = Thyroid_model.predict([user_input])

            if thyroid_prediction[0] == 1:
                thyroid_diagnosis = "The person has thyroid disease"
            else:
                thyroid_diagnosis = "The person does not have thyroid disease"

    st.success(thyroid_diagnosis)