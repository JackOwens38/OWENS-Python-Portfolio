import streamlit as st
import pandas as pd

st.title("Tourist Reviews!")
st.markdown("# Welcome to my streamlit app!")

df = pd.read_csv("data/tourism_dataset_5000.csv")

st.write("Want to read reviews of some of the most popular tourist destinations in the world? This streamlit allows you to pick a locaiton, and then shows plenty of reviews that give various ratings on each location. Choose a site below!")

site = st.selectbox("Select a site", df["Site Name"].unique())
filtered_df = df[df["Site Name"] == site]
st.write(f"Reviews for {site}:")
st.dataframe(filtered_df)

satisfaction = st.slider("Use this slide to filter out reviews with satisfaction scores below what you select.", 0, 5)
satisfied_df = filtered_df[df["Satisfaction"]>=satisfaction]
st.write(f"Reviews for {site} with a minimum satisfaction rating of {satisfaction}:")
st.dataframe(satisfied_df)
