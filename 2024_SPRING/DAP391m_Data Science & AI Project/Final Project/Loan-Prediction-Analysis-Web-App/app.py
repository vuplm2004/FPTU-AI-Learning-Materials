import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st
import pickle

pickle_in = open("model_classifier.pkl", "rb")
my_model = pickle.load(pickle_in)


def predict_data(model, input_data):
    predict_array = np.array(
        [
            input_data["Gender"][0],
            input_data["Married"][0],
            input_data["Dependents"][0],
            input_data["Education"][0],
            input_data["Self_Employed"][0],
            input_data["CoapplicantIncome"][0],
            input_data["LoanAmount"][0],
            input_data["Loan_Amount_Term"][0],
            input_data["Credit_History"][0],
            input_data["Property_Area"][0],
        ]
    )

    final_array = [
        predict_array[0],
        predict_array[1],
        predict_array[2],
        predict_array[3],
        predict_array[4],
        predict_array[5],
        predict_array[6],
        predict_array[7],
        predict_array[8],
        predict_array[9],
    ]

    predictions = model.predict([final_array])
    return predictions


def run_data():
    st.set_page_config(page_title="Loan Prediction Web App")
    st.sidebar.header("Loan Prediction App")
    st.sidebar.info(
        "This app is created to predict whether an applicant is eligible for a loan or not."
    )
    st.title("Please fill this form..")

    gender = st.selectbox("Gender", ["Male", "Female"])
    if st.checkbox("Married"):
        married = "yes"
    else:
        married = "no"

    dependents = st.selectbox("Dependents", [0, 1, 2, "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_emp = st.selectbox("Self Employed", ["Yes", "No"])
    # app_income = st.number_input('Applicant Income', min_value = 1000, max_value = 10000, value = 1000)
    co_app_income = st.number_input(
        "Coapplicant Income", min_value=1000, max_value=10000, value=1000
    )
    loan_amount = st.number_input(
        "Loan Amount", min_value=100, max_value=10000, value=100
    )

    loan_amount_term = st.selectbox("Loan Amount Term", [1010, 2000, 3500])
    credit_history = st.selectbox("Credit History", [0, 1])
    property_area = st.selectbox("Property Area", ["Semiurban", "Rural", "Urban"])

    output = ""

    my_dict = {
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_emp,
        # 'ApplicantIncome': app_income,
        "CoapplicantIncome": co_app_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_amount_term,
        "Credit_History": credit_history,
        "Property_Area": property_area,
    }

    input_data = pd.DataFrame([my_dict])

    input_data = input_data.apply(lambda x: x.astype("category").cat.codes)
    if st.button("Predict"):
        output = predict_data(model=my_model, input_data=input_data)
        if output == 1:
            st.success("The applicant is eligible for loan")
        else:
            st.error("The applicant is not eligible for loan")


if __name__ == "__main__":
    run_data()
