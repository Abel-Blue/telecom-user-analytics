import streamlit as st
import pandas as pd
import os
import sys


def app():

    st.title("User Engagement Analysis")

    st.header("Data Visualization")
    df_email = pd.read_csv('../../data/top10_email_users.csv.csv')
    df_game = pd.read_csv('../../data/top10_gameApp_users.csv')
    df_google = pd.read_csv('../../data/top10_google_users.csv')
    df_netflix = pd.read_csv('../../data/top10_netflix_users.csv')
    df_otherAct = pd.read_csv('../../data/top10_otherAct_users.csv')
    df_social = pd.read_csv('../../data/top10_socialMedia_users.csv')
    df_youtube = pd.read_csv('../../data/top10_youtube_users.csv')
    df_session = pd.read_csv('../../data/top10_user_session.csv')
    df_DLUL = pd.read_csv('../../data/top10_DLUL_users.csv')

    st.header("Top 10 Users Engaged Per Each Application")
    st.subheader("Email App")
    st.dataframe(df_email)
    st.bar_chart(df_email.value_counts())

    st.subheader("Game App")
    st.dataframe(df_game)
    st.bar_chart(df_game.value_counts())

    st.subheader("Google App")
    st.dataframe(df_google)
    st.bar_chart(df_google.value_counts())

    st.subheader("Netflix App")
    st.dataframe(df_netflix)
    st.bar_chart(df_netflix.value_counts())

    st.subheader("Other App")
    st.dataframe(df_otherAct)
    st.bar_chart(df_otherAct.value_counts())

    st.subheader("Social Media App")
    st.dataframe(df_social)
    st.bar_chart(df_social.value_counts())

    st.subheader("Youtube App")
    st.dataframe(df_youtube)
    st.bar_chart(df_youtube.value_counts())

    st.header("Top 3 Most Used Applications")
    st.image('../../data/top10apps.png')

    st.subheader("Top 10 users based on session count")
    st.dataframe(df_session)
    st.bar_chart(df_session.value_counts())

    st.subheader("Top 10 users based on download and upload count")
    st.dataframe(df_session)
    st.bar_chart(df_session.value_counts())

    st.header("3 groups k-means clustering")
    st.image('../../data/engclusters.png')
