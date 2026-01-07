import streamlit as st
import pandas as pd

# MUST be first Streamlit command
st.set_page_config(page_title="Book Finder", layout="centered")

st.title("📚 YMCI HYD BOOK TREASURE")
st.write("Search books by **Book Name** or **Receiver Name**")

try:
    df = pd.read_excel("books.xlsx")

    col1, col2 = st.columns(2)

    with col1:
        search_type = st.selectbox(
            "Search Type",
            ["BOOK NAME", "RECIPIENT"]
        )

    with col2:
        query = st.text_input("Enter value")

    st.divider()

    if query:
        if search_type == "BOOK NAME":
            result = df[df["BOOK NAME"].str.contains(query, case=False, na=False)]
        else:
            result = df[df["RECIPIENT"].str.contains(query, case=False, na=False)]

        if not result.empty:
            st.success(f"{len(result)} record(s) found")
            st.dataframe(result, use_container_width=True)
        else:
            st.warning("No records found")

except Exception as e:
    st.error(f"Error occurred: {e}")
