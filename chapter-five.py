import streamlit as st
import requests

st.title("Live currency Convertor")
amount = st.number_input("Enter the amount in INR", min_value=1)
targeted_currency = st.selectbox("Convert To:", ["USD","EUR","GBP","JPY"])

if st.button("Convert"):
    url = "https://open.er-api.com/v6/latest/INR"
    r = requests.get(url)
    if r.status_code == 200:
      data = r.json()
      rate = data['rates'][targeted_currency]
      converted = rate * amount
      st.success(f"{amount} INR = {round(converted,2)}  {targeted_currency}")
    else:
        st.error("Failed to fetch conversion rate")

