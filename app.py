import streamlit as st
import pandas as pd
import speech_recognition as sr
from viz import Visualizer
from queryengine import QueryEngine
import os
print("Current working directory:", os.getcwd())

# Initialize global variables
uploaded_file = None
query_engine = None

# Streamlit App
st.title("Interactive Data Analysis and Visualization")
st.write("Upload a dataset, ask questions, and visualize the results.")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset preview:")
    st.write(df.head())

    # Initialize QueryEngine
    query_engine = QueryEngine(df)

# Input method: Text or Audio
input_type = st.radio("Choose your input type:", ["Text", "Audio"])

if input_type == "Text":
    user_question = st.text_input("Ask a question about the dataset:")
elif input_type == "Audio":
    recognizer = sr.Recognizer()
    st.write("Record your question:")
    audio_button = st.button("Record")
    if audio_button:
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = recognizer.listen(source)
            try:
                user_question = recognizer.recognize_google(audio)
                st.write(f"You said: {user_question}")
            except sr.UnknownValueError:
                st.error("Sorry, could not understand the audio.")
                user_question = None
else:
    user_question = None

# Process question
if user_question and query_engine:
    try:
        st.write("Processing your question...")
        query_result = query_engine.generate_query(user_question)
        st.write("Query Result:")
        st.write(query_result)

        # Visualization options
        st.write("Choose visualization:")
        chart_type = st.selectbox("Chart Type", ["Bar Chart", "Line Chart", "Scatter Plot"])
        x_col = st.selectbox("X-axis column", query_result.columns)
        y_col = st.selectbox("Y-axis column", query_result.columns)

        if st.button("Generate Chart"):
            visualizer = Visualizer()
            if chart_type == "Bar Chart":
                visualizer.bar_chart(query_result, x_col, y_col)
            elif chart_type == "Line Chart":
                visualizer.line_chart(query_result, x_col, y_col)
            elif chart_type == "Scatter Plot":
                visualizer.scatter_plot(query_result, x_col, y_col)
    except Exception as e:
        st.error(f"Error: {e}")
