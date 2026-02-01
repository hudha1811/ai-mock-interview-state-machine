import streamlit as st
from interview_engine import run_interview

st.set_page_config(page_title="AI Mock Interview", layout="centered")

st.title("🎤 AI Mock Interview Simulator")
st.write("Simulated AI-driven interview evaluation")

if st.button("▶ Run Interview"):
    result = run_interview(return_logs=True)

    st.subheader("📊 Final Result")
    st.metric("Final Score", result["final_score"])
    st.write("**Category:**", result["category"])

    st.subheader("📋 Feedback")
    for f in result["feedback"]:
        st.write("- ", f)

    st.subheader("🧭 Interview Timeline")
    for step in result["logs"]:
        st.markdown(
            f"""
            **State:** {step['state']}  
            **Score:** {step['score']} | **Stress:** {step['stress']}  
            ❓ {step['question']}  
            📝 Answer: {step['answer']}  
            ---
            """
        )
