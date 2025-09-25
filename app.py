import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from io import BytesIO

st.title("📊 Dummy Google Sheets Processing App")

# --- Authenticate with Google Sheets ---
scope = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive"]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"], scopes=scope
)
client = gspread.authorize(creds)

# --- Enter your Google Sheet ID here ---
SHEET_ID = "1FcfiH10iRBAPrNp3AXdYTo6JFUhFS1JS_Z0kKJfTkwU"  # Example: 1abcdEfghIjkLmnoPqrStuVwXyZ123456789
SHEET_NAME = "Sheet1"

# Load data from Google Sheets
try:
    sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
    data = sheet.get_all_records()
    df = pd.DataFrame(data)

    st.subheader("📂 Original Data")
    st.dataframe(df.head())

    # Dummy calculation: Add column with doubled values for numeric columns
    df_processed = df.copy()
    for col in df_processed.select_dtypes(include="number").columns:
        df_processed[f"{col}_double"] = df_processed[col] * 2

    st.subheader("✅ Processed Data")
    st.dataframe(df_processed.head())

    # Download processed data as Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df_processed.to_excel(writer, index=False, sheet_name="Processed")
    processed_data = output.getvalue()

    st.download_button(
        label="📥 Download Processed Excel",
        data=processed_data,
        file_name="processed_file.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

except Exception as e:
    st.error(f"❌ Error: {e}")
