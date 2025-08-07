import streamlit as st
import ollama
import io

st.set_page_config(page_title="Credit Memo Generator", layout="wide")

st.title("📄 Credit Memo Generator using Local LLM")
st.markdown("Generate a structured credit memo based on customer financial behavior.")

with st.expander("ℹ️ About this App", expanded=False):
    st.write("This tool uses a local LLM model via Ollama to generate credit memos for customer assessment. Useful for analysts or credit underwriters.")

# Main form for user input
with st.form("memo_form"):
    st.subheader("🧾 Customer Information")
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Customer Name", placeholder="e.g. John Doe")
        income = st.text_input("Annual Income (USD)", placeholder="e.g. 75000")
        behavior_score = st.slider("Behavioral Score", 0, 100, 70)

    with col2:
        credit_utilization = st.slider("Credit Utilization (%)", 0, 100, 30)
        missed_payments = st.slider("Missed Payments (past 12 months)", 0, 12, 1)
        recent_transactions = st.text_area("Recent Transactions Summary", height=150)

    submitted = st.form_submit_button("🚀 Generate Memo")

# Post-submission LLM logic
if submitted:
    if not name or not income.isdigit():
        st.warning("⚠️ Please enter a valid name and numeric income.")
    else:
        with st.spinner("Generating memo using local model..."):

            prompt = f"""
You are a Credit Analyst. Based on the following customer data, generate a professional credit memo.
- Name: {name}
- Annual Income: ${income}
- Behavioral Score: {behavior_score}
- Credit Utilization: {credit_utilization}%
- Missed Payments: {missed_payments}
- Transaction Summary: {recent_transactions}

Structure the memo under:
1. Customer Overview
2. Financial Behavior
3. Risk Assessment
4. Recommendation
"""

            try:
                response = ollama.chat(
                    model="mistral", 
                    messages=[{"role": "user", "content": prompt}]
                )
                memo = response['message']['content']

                st.success("✅ Memo Generated")
                st.subheader("📝 Credit Memo")
                st.text_area("Generated Output", memo, height=400)

                # Allow download
                memo_bytes = memo.encode('utf-8')
                st.download_button(
                    label="📥 Download Memo as .txt",
                    data=memo_bytes,
                    file_name=f"credit_memo_{name.replace(' ', '_')}.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"❌ Error: {e}")
