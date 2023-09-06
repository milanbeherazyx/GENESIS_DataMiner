import streamlit as st
import pandas as pd
from pystatis import init_config, Table, clear_cache
import io

# Set the page title
st.set_page_config(page_title="GENESIS Data Extractor")

# Initialize GENESIS credentials
st.sidebar.header("GENESIS Credentials")
username = st.sidebar.text_input("Username:")
password = st.sidebar.text_input("Password:", type="password")

# Initialize config if credentials are provided
if username and password:
    init_config(username=username, password=password)

# Table selection
st.sidebar.header("Table Selection")
table_name = st.sidebar.text_input("Table Name:")

# Extract and display data
if table_name:
    st.header(f"Data from Table: {table_name}")

    # Create a Table object
    table = Table(name=table_name)

    # Get the data (this will also check the cache)
    table.get_data()

    # Display the data in a Streamlit table
    st.dataframe(table.data)

    # Save the data to a local CSV file
    if not table.data.empty:
        st.subheader("Save Data Locally")
        save_locally = st.checkbox("Save data to a local CSV file")
        if save_locally:
            file_name = f"{table_name}.csv"
            table.data.to_csv(file_name, index=False)
            st.success(f"Data saved as {file_name}")

    # Clear the cache for this table
    clear_cache(table_name)

# Provide instructions
st.sidebar.markdown(
    """
    ## Instructions
    1. Enter your GENESIS username and password.
    2. Enter the table name you want to extract.
    3. Click on the 'Extract Data' button to display the table.
    4. Optionally, you can save the data to a local CSV file.
    """
)
