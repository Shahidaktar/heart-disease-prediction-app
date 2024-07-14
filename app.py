import streamlit as st 
import pickle 

st.set_page_config(page_title="Heart Disease Prediction",layout="wide",page_icon = 'heart.png')
heart_disease_model = pickle.load(open('heart.pkl','rb'))


st.title("Heart Disease Prediction Using Machine Learning")
col1, col2, col3  = st.columns(3)

with col1:
    age = st.text_input("Age")
with col2:
    sex = st.text_input("Sex")
with col3:
    cp = st.text_input("Chest Pain Types")
with col1:
    trestbps = st.text_input("Resting Blood Pressure")
with col2:
    chol = st.text_input("Serum Cholestroal in mg/dl")
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
heart_disease_result = ""
if st.button("Heart Disease Test Result"):
    user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    user_input = [float(x) for x in user_input]
    prediction = heart_disease_model.predict([user_input])
    if prediction[0]==1:
        heart_disease_result = "This person is having heart disease"
    else:
        heart_disease_result = "This person does not have any heart disease"
st.success(heart_disease_result)


footer_html = """<div style='text-align: center;'>
  <p>Developed by Shahid Aktar Mandal</p>
</div>"""
st.markdown(footer_html, unsafe_allow_html=True)


