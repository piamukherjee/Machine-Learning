import joblib
import streamlit as st
import pandas as pd

model = joblib.load('rf_predictcalories.joblib')
X_test_point= pd.DataFrame(columns=['Gender','Age','Height','Weight','Duration', 
'Heart_Rate', 'Body_Temp'])
Y_test_point= pd.DataFrame(columns=['Calories'])



st.write("# I have built a model to predict calories burnt through exercise")
duration= st.number_input("Enter your exercise duration")
X_test_point.loc[0]=[1,45,180,40,duration,100,37.5]
Y_test_point=model.predict(X_test_point)
if duration !=0:
    st.write("Calories burnt=", Y_test_point)
