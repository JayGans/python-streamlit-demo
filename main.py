import streamlit as st

st.title("Hello App")
st.subheader("Brewed with streamlitdemo")
st.text("welcome to this webpage")
st.write("Choose your favorite language")

lang = st.selectbox("Your favorite language", ["Python", "Ruby", "Java"])
st.write(f"Your favorite language is {lang}")
st.success(f"Your favorite language is successfully set to {lang}")