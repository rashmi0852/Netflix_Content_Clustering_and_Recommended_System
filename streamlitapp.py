# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import joblib

# Load the cosine similarity matrix
cosine_sim = joblib.load('cosine_sim.joblib')

# Load the recommendation function
recommend_content = joblib.load('recommendation_function.joblib')

# Load the netflix_data DataFrame
netflix_data = joblib.load('netflix_data.joblib')

# Title and Description
st.title("Recommendation App")
st.write("Enter the name of a movie or TV show, and get recommendation!")

# Input box for user input
user_input = st.text_input("Enter a movie or TV show:")

# Button to get recommendations
if st.button("Get Recommendation"):
    # Get recommendations based on user input
    recommendations = recommend_content(user_input, cosine_sim=cosine_sim, data=netflix_data)
    
    # Display recommendations
    st.write("Here are some recommendations:")
    for recommendation in recommendations:
        st.write(recommendation)

