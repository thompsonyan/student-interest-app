import streamlit as st
import requests

# Set the Hugging Face Inference API model and your access token
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
headers = {"Authorization": "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"}  # Replace with your own Hugging Face Token

st.set_page_config(page_title="Lightweight Q&A Bot", page_icon="🤖")
st.title("🤖 Lightweight Q&A Bot (flan-t5-small)")
st.markdown("No need to download the model, it runs completely in the Hugging Face cloud.")

user_input = st.text_area("Please enter your question:", "What is Artificial Intelligence?")

if st.button("Generate Answer"):
    if not user_input.strip():
        st.warning("Please enter content")
    else:
        with st.spinner("Thinking..."):
            payload = {"inputs": user_input}
            response = requests.post(API_URL, headers=headers, json=payload)

            if response.status_code == 200:
                result = response.json()
                st.success("Answer:")
                st.write(result[0]['generated_text'])
            else:
                st.error(f"Request failed, status code: {response.status_code}")
