import streamlit as st

st.title("Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://www.seema.com/wp-content/uploads/2022/07/Masala-Chai.jpg",width=100)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://www.indianveggiedelight.com/wp-content/uploads/2023/06/ginger-tea.jpg",width=100)

    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Vote Masala Chai")
elif vote2:
    st.success("Vote Adrak Chai")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Select your tea", ["Yes", "No"])
st.write(f"Wlcome {name} Your tea is {tea}")

with st.expander("Show chai making instructions"):
    st.write("""
    1. Boil water with tea leaves.
    2. Add milk and sugar """)

st.markdown("# Welcome to chai App")

