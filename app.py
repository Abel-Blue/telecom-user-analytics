import os
import sys
import streamlit as st
from multiapp import MultiApp
sys.path.insert(0, './dashboard')
from applications import model, user_engagement, experience_analytics, satisfaction_analysis

st.set_page_config(page_title="Telecom User Data Visualization", layout="wide")

app = MultiApp()

st.sidebar.markdown("""
# Telecom User Data Analysis
""")

# Add all your application here
app.add_app("Model", model.app)
app.add_app("user_engagement", user_engagement.app)
app.add_app("experience_analytics", experience_analytics.app)
app.add_app("satisfaction_analysis", satisfaction_analysis.app)

# The main app
app.run()
