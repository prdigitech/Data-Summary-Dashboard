import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Data Summary Dashboard",  
    page_icon="📊",                       
    layout="centered"                     
)

st.title("Data Summary Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Overview")
    st.write(df.head()) 

    st.subheader("Data Summary")    
    st.write(df.describe()) 

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select a Value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Visualize Data")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column]) 

else:
    st.write("Please upload a CSV file to get started.....")

st.markdown(
    """
    <hr style="margin-top: 50px; margin-bottom: 10px; border-color: #444;">
    <div style="text-align: center; font-size: 13px; color: #bbb;">
        Created by <b>Pratik Ramdasi</b> · 
        <a href="https://github.com/prdigitech" target="_blank" style="color: #bbb; text-decoration: none;">
            GitHub
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

