import streamlit as st
import requests

st.title("Simple Model Interface")
st.write("Enter a prompt to generate text using the FastAPI model.")

prompt = st.text_input("Prompt", "What is veganism?")

if st.button("Generate Text"):
    if prompt:
        api_url = "http://34.46.213.152:8000/generate-text/"

        data = {"prompt": prompt}
        response = requests.post(api_url, json=data)
        
        if response.status_code == 200:
            st.write("Generated Text:")
            st.write(response.json())
        else:
            st.write("Error:", response.status_code)
