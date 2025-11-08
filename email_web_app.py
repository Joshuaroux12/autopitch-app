import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load .env for local development
load_dotenv()

# Use key from Streamlit secrets (deployed) or .env (local)
openai.api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Autopitch App", page_icon="📧")
st.title("🎤 Autopitch — AI‑Powered Email Pitch Generator")

product_description = st.text_area("Describe your product or service:")

if st.button("Generate Pitch"):
    if not product_description:
        st.warning("Please enter a description of your product.")
    else:
        with st.spinner("Generating your pitch…"):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an assistant writing a concise, engaging email pitch."},
                        {"role": "user", "content": f"Write a short, professional email pitch for the following product: {product_description}"}
                    ],
                    temperature=0.7,
                    max_tokens=300
                )
                pitch = response['choices'][0]['message']['content']
                st.success("✅ Pitch Generated!")
                st.write(pitch)
            except Exception as e:
                st.error(f"⚠️ Error generating pitch: {str(e)}")
