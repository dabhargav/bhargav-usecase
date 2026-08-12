import streamlit as st
import os
from agents.audit_agent import AuditAgent
from core.config import LOG_DIR

st.set_page_config(page_title="AI Audit Agent Demo", layout="wide")
st.title("🤖 Intelligent Audit Trail Agent")

agent = AuditAgent()

# User Input
user_request = st.text_input("Enter a business request:", "Approve a credit extension of $5,000")

if st.button("Execute Agent Action"):
    with st.spinner("Agent processing and compiling audit trail..."):
        decision, log_file = agent.run_compliance_check(user_request)
        
        st.success("Execution Complete!")
        st.subheader("Agent Decision:")
        st.write(decision)
        
        st.info(f"📄 Audit trail saved to folder as: `{log_file}`")

# Sidebar to view generated audit logs live
st.sidebar.title("📁 Live audit_logs/ Folder")
log_files = [f for f in os.listdir(LOG_DIR) if f.endswith('.txt')]
if log_files:
    selected_file = st.sidebar.selectbox("Select a log to view details:", sorted(log_files, reverse=True))
    with open(os.path.join(LOG_DIR, selected_file), "r") as f:
        st.sidebar.code(f.read(), language="text")
else:
    st.sidebar.write("No logs recorded yet.")
