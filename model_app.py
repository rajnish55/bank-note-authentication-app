import streamlit as st
import pickle

with open("model.pkl", 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Bank note Authenticator", layout="centered")

st.title("🏦 Bank Note Authentication App")    
st.markdown("**Enter values below to make a prediction.**")

def to_float(values, default = None):
    try:
        return float(values)
    except ValueError:
        return default


with st.form("input_form"):
    variance = to_float(st.text_input("Variance"))
    skewness = to_float(st.text_input("skewness"))
    curtosis = to_float(st.text_input("curtosis"))
    entropy = to_float(st.text_input("entropy"))
    submitted = st.form_submit_button("Predict")

if submitted:
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    st.success(f"Output = {prediction}")

# prediction = 0
# if st.button("Predict"):
#     prediction = model.predict([[variance, skewness, curtosis, entropy]])
# st.write(f"Output = {prediction}")
# # st.write(prediction)
# st.success("Output is {}".format(prediction))