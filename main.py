import streamlit as st

st.title("Hi I'm Rishabh")

with st.form(enter_to_submit=True, key="abc",clear_on_submit=True):
    a = st.text_input("Enter your message for me")
    if st.form_submit_button():
        st.success("form submitted successfully")
        print(f"{a}")
        if a == "birthday":
            st.balloons()
        elif a == "cold":
            st.snow()
        else:
            st.write("Thanks for visiting")
