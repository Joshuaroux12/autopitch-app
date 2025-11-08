import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import csv
import openai
import pandas as pd

openai.api_key = os.getenv("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")  # 🔑 Replace with your real OpenAI API key

st.title("💼 AI Cold Email Generator")
uploaded_file = st.file_uploader("Upload your leads.csv", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success(f"Uploaded {len(df)} leads")

    if st.button("Generate Emails"):
        st.info("Generating emails, please wait...")

        emails = []
        for _, lead in df.iterrows():
            prompt = (
                f"You are an expert cold email copywriter. Write a short, friendly, personalized cold email to "
                f"{lead['contact_name']}, who is the {lead['job_title']} at {lead['company']} ({lead['website']}), "
                f"a company in the {lead['industry']} industry."
            )

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=150
            )
            email_text = response['choices'][0]['message']['content']
            emails.append(email_text)

        df["generated_email"] = emails

        st.download_button(
            label="📥 Download Emails CSV",
            data=df.to_csv(index=False),
            file_name="personalized_emails.csv",
            mime="text/csv"
        )
