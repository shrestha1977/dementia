import streamlit as st

def run_assessments():
    st.header("Run Cognitive Assessments")
    selected_test = st.selectbox("Select a Test", ["MoCA", "MMSE", "SLUMS", "AD8", "Mini-Cog"])

    if selected_test == "MoCA":
        st.write("Montreal Cognitive Assessment (MoCA) is widely used for early detection of MCI/AD.")
        score = st.number_input("Enter MoCA Score (0-30)", 0, 30)
        if score < 26:
            st.error("Possible cognitive impairment detected.")
        else:
            st.success("Normal cognitive performance.")
    elif selected_test == "MMSE":
        st.write("Mini-Mental State Examination (MMSE).")
        score = st.number_input("Enter MMSE Score (0-30)", 0, 30)
        if score < 24:
            st.error("Possible dementia detected.")
        else:
            st.success("Normal cognitive performance.")
    elif selected_test == "SLUMS":
        st.write("Saint Louis University Mental Status (SLUMS) Exam.")
        score = st.number_input("Enter SLUMS Score (0-30)", 0, 30)
        if score < 21:
            st.error("Possible dementia detected.")
        elif 21 <= score <= 26:
            st.warning("Possible mild cognitive impairment.")
        else:
            st.success("Normal cognitive performance.")
    elif selected_test == "AD8":
        st.write("AD8 Dementia Screening Interview (informant-based).")
        score = st.number_input("Enter AD8 Score (0-8)", 0, 8)
        if score >= 2:
            st.error("Possible cognitive impairment detected.")
        else:
            st.success("Normal cognitive performance.")
    elif selected_test == "Mini-Cog":
        st.write("Mini-Cog Screening Tool.")
        score = st.radio("Clock Drawing + Recall Result", ["Normal", "Abnormal"])
        if score == "Abnormal":
            st.error("Possible cognitive impairment detected.")
        else:
            st.success("Normal cognitive performance.")
