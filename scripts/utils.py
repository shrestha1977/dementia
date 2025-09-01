import streamlit as st
import pandas as pd

def save_results():
    st.header("Saved Results")
    if "results" not in st.session_state:
        st.session_state["results"] = []
    
    new_entry = st.text_input("Enter patient/session ID to log result")
    if st.button("Save Current Session"):
        st.session_state["results"].append({"SessionID": new_entry, "Status": "Saved"})
        st.success("Result saved.")
    
    if st.session_state["results"]:
        df = pd.DataFrame(st.session_state["results"])
        st.dataframe(df)
