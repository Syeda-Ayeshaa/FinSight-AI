import streamlit as st
import pandas as pd

from hyperapi_parser import extract_document
from table_processor import process_items
from validator import validate_totals
from anomaly_detector import detect_anomalies
from output_writer import save_output


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="FinSight AI",
    page_icon="💰",
    layout="wide"
)


# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("💰 FinSight AI")
    st.write("Financial Document Intelligence System")

    st.markdown("### Features")
    st.markdown("- Financial document extraction")
    st.markdown("- Invoice table reconstruction")
    st.markdown("- Tax calculation")
    st.markdown("- Financial validation")
    st.markdown("- Rule-based anomaly detection")
    st.markdown("- Explainable AI (XAI)")

    st.markdown("### Instructions")
    st.markdown("1. Upload a financial invoice PDF")
    st.markdown("2. System extracts structured data")
    st.markdown("3. Financial validation and anomaly detection are performed")


# ---------- HEADER ----------
st.title("💰 FinSight AI")
st.caption("AI-powered Financial Document Intelligence Pipeline")


# ---------- FILE UPLOAD ----------
uploaded_file = st.file_uploader("Upload Financial PDF", type=["pdf"])


if uploaded_file is not None:

    # Save uploaded file
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("Extracting financial data from document...")

    # Extract document data
    data = extract_document("temp.pdf")

    # Hidden debug JSON
    with st.expander("View Extracted JSON"):
        st.json(data)

    # Stop if extraction fails
    if "error" in data:
        st.error("Extraction failed. Please check API configuration.")
        st.stop()

    # ---------- TABLE PROCESSING ----------
    table_df = process_items(data)

    st.subheader("📄 Line Items Table")

    if table_df.empty:
        st.warning("No line items detected.")
        st.stop()

    st.dataframe(table_df, use_container_width=True)


    # ---------- ANOMALY DETECTION ----------
    table_df = detect_anomalies(table_df)

    st.subheader("⚠ Anomaly Detection")

    def highlight_anomaly(row):
        if row["anomaly_flag"] == -1:
            return ["color: red; font-weight: bold"] * len(row)
        return [""] * len(row)

    styled_table = table_df.style.apply(highlight_anomaly, axis=1)

    st.dataframe(styled_table, use_container_width=True)

    if -1 in table_df["anomaly_flag"].values:
        st.warning("Suspicious line items detected.")
    else:
        st.success("No anomalies detected.")


    # ---------- FINANCIAL VALIDATION ----------
    validation = validate_totals(data, table_df)

    st.subheader("📊 Financial Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Subtotal", validation["computed_subtotal"])
    col2.metric("Tax", validation["tax"])
    col3.metric("Expected Total", validation["expected_total"])
    col4.metric("Actual Total", validation["actual_total"])


    # ---------- VALIDATION RESULT ----------
    st.subheader("✅ Validation Result")

    if validation["status"] == "VALID":
        st.success("VALID: " + validation["explanation"])
    else:
        st.error("ERROR: " + validation["explanation"])


    # ---------- EXPLAINABLE AI ----------
    st.subheader("🔍 Explainability (XAI)")

    st.write("Line Item Calculations:")
    for step in validation["calculation_steps"]:
        st.write(step)

    st.write(validation["subtotal_explanation"])
    st.write(f"Tax = {validation['tax']}")
    st.write(validation["final_explanation"])


    # ---------- SAVE OUTPUT ----------
    save_output(data, validation)

    st.success("Processing completed. Output saved to outputs/extracted_data.json")