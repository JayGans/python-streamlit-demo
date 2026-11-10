import streamlit as st
import pandas as pd

st.title("Chai sale dashboard")
file = st.file_uploader('Upload your csv file', type = ["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary states")
    st.write(df.describe())

if file:
    names = df['Name'].unique()
    selected_names =st.selectbox("Select a state",names)
    filter_data=df[df['Name']==selected_names]
    st.dataframe(filter_data)

