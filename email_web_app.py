import streamlit as st
import openai

openai.api_key = st.secrets["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"]
from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("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")

# Streamlit app interface
st.set_page_config(page_title="Autopitch App", page_icon="📧")
st.title("🎤 Autopitch - AI-Powered Email Pitch Generator")

# Text input for product or service
product_description = st.text_area("Describe your product/service:")

# Generate button
if st.button("Generate Pitch"):
    if not product_description:
        st.warning("Please enter a description of your product.")
    else:
        with st.spinner("Generating your pitch..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful assistant that writes concise, engaging sales pitch emails based on product descriptions."
                        },
                        {
                            "role": "user",
                            "content": f"Write a short and professional email pitch for the following product: {product_description}"
                        }
                    ],
                    temperature=0.7,
                    max_tokens=300
                )
                pitch = response['choices'][0]['message']['content']
                st.success("✅ Pitch Generated!")
                st.write(pitch)
            except Exception as e:
                st.error(f"⚠️ Error generating pitch: {str(e)}")
