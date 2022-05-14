import streamlit as st
import pandas as pd
import os
import sys


def app():

    st.title("User Satisfaction Analysis")

    st.header("Data Visualization")
    df_satisf = pd.read_csv('data/top10_satisfied_customers.csv')
    df_score = pd.read_csv('data/score_table.csv')

    st.header("Top 10 Satisfied Customers")
    st.dataframe(df_satisf)
    st.bar_chart(df_satisf.value_counts())

    st.subheader("Score Table")
    st.dataframe(df_score)
    st.bar_chart(df_score.value_counts())

    st.header("User Clustering based on both scores")
    st.image('data/satisfaction.png')
