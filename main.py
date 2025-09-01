import streamlit as st
from scripts.assessments import run_assessments
from scripts.utils import save_results

st.set_page_config(page_title="Cognitive Assessment Platform", layout="wide")

st.title("🧠 Cognitive Assessment & Dementia Screening Platform")

st.markdown("This platform integrates validated cognitive assessment tools (MoCA, MMSE, SLUMS, AD8, Mini-Cog) "
            "with additional gait and speech-based measures.")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to", ["Home", "Run Assessment", "Results"])

if page == "Home":
    st.subheader("Welcome")
    st.write("Use this app to conduct standardized cognitive assessments, "
             "store anonymized results, and analyze risk scores.")
elif page == "Run Assessment":
    run_assessments()
elif page == "Results":
    save_results()
