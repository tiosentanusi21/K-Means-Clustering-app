import streamlit as st
import pandas as pd

def show():
    st.title("📊 Tabel Data (Excel)")

    uploaded_file = st.file_uploader("Unggah Dataset Responden (Excel)", type=["xlsx", "xls"])

    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)
            st.session_state["data"] = df
            st.success("✅ Data berhasil diunggah.")
            st.write("### Tabel Data")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Gagal membaca file: {e}")
    else:
        st.info("Silakan unggah file Excel terlebih dahulu.")
