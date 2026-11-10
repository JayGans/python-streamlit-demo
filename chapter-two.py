import streamlit as st

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Your chai is ready")


add_masala = st.checkbox("Add masala")

if add_masala:
    st.write("Masala added in your chai")

tea_type = st.radio("Pick your chai base:",["Milk","Water","Almond Milk"])
st.write(f"Your chai type is {tea_type}")

flavour = st.selectbox("Choose flavour: ", ["Adrak", "Kesar", "Tulsi"])
st.write(f"Your flavour is {flavour}")

sugar =  st.slider("Select Sugar Leve : ",0,5,2)
st.write(f"Your sugar is {sugar}")

cups = st.number_input("How many cups", min_value=1,max_value=10, step=1)
st.write(f"Your selected cups {cups}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Your name is {name}")

dob =st.date_input("Enter your date of birth")
st.write(f"Your date of birth is {dob}")