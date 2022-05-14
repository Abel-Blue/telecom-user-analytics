import streamlit as st
import pandas as pd
import os
import sys


def app():

    st.title("User Experience Analysis")

    st.header("Data Visualization")
    df_avgThr = pd.read_csv('data/top10avgThroughput.csv')
    df_rtt = pd.read_csv('data/top10rtt.csv')
    df_tcp = pd.read_csv('data/top10tcp.csv')
    df_frqThr = pd.read_csv('data/most_freqAvgThr.csv')
    df_frqrtt = pd.read_csv('data/most_freqRTT.csv')
    df_frqtcp = pd.read_csv('data/most_freqTCP.csv')

    st.header("Top 10 Users Experience metrics")
    st.subheader("Average Throughput")
    st.dataframe(df_avgThr)
    st.bar_chart(df_avgThr.value_counts())

    st.subheader("Round Trip Time")
    st.dataframe(df_rtt)
    st.bar_chart(df_rtt.value_counts())

    st.subheader("TCP")
    st.dataframe(df_tcp)
    st.bar_chart(df_tcp.value_counts())

    st.header("Most Frequenct Users")
    st.subheader('frquent Average Throughput')
    st.dataframe(df_frqThr)
    st.bar_chart(df_frqThr.value_counts())

    st.subheader("frquent Round Trip Time")
    st.dataframe(df_frqrtt)
    st.bar_chart(df_frqrtt.value_counts())

    st.subheader("frquent TCP")
    st.dataframe(df_frqtcp)
    st.bar_chart(df_frqtcp.value_counts())

    st.header("Cluster with 2 group classification")
    st.image('data/clusterExp.png')
