import streamlit as st
import pandas as pd

# MUST be first Streamlit command
st.set_page_config(page_title="Book Finder", layout="centered")

st.title("📚 YMCI HYD BOOK TREASURE")
st.write("Search books by **Book Name** or **Receiver Name**")

try:
    df = pd.read_excel("books.xlsx")

    available_books_df = df[df["RECIPIENT"].isna() | (df["RECIPIENT"].str.strip() == "")]

    # Get unique available book names
    available_books = sorted(available_books_df["BOOK NAME"].dropna().unique())

    col1, col2 = st.columns(2)

    with col1:
        search_type = st.selectbox(
            "Search Type",
            ["AVAILABLE BOOKS","BOOK NAME", "RECIPIENT"]
        )

    with col2:
        if search_type == "AVAILABLE BOOKS":
            selected_book = st.selectbox(
                "Select Available Book",
                available_books
            )
        else:
            query = st.text_input("Enter value")

    st.divider()

    # Logic
    if search_type == "AVAILABLE BOOKS":
        result = available_books_df[
            available_books_df["BOOK NAME"] == selected_book
        ]

    elif search_type == "BOOK NAME" and query:
        result = df[df["BOOK NAME"].str.contains(query, case=False, na=False)]

    elif search_type == "RECIPIENT" and query:
        result = df[df["RECIPIENT"].str.contains(query, case=False, na=False)]

    else:
        result = pd.DataFrame()
        
    if not result.empty:
        st.success(f"{len(result)} record(s) found")
        st.dataframe(result, use_container_width=True)
    else:
        st.warning("No records found")

except Exception as e:
    st.error(f"Error occurred: {e}")
