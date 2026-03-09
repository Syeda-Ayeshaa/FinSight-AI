FinSight AI

AI-Powered Financial Document Intelligence System

FinSight AI is a financial document processing system that extracts structured data from invoices and validates financial calculations automatically. The system converts complex financial documents into clean, machine-readable data while ensuring numerical consistency and transparency through explainable validation.

Problem Statement

Financial documents such as invoices, tax forms, and insurance claims often contain complex layouts and multiple line items. Traditional OCR and automation systems struggle with:

Extracting structured financial data from unstructured documents

Maintaining numerical accuracy

Validating financial totals

Detecting suspicious or inconsistent values

These limitations make automated financial workflows unreliable.

Solution

FinSight AI builds a financial document intelligence pipeline that:

Accepts financial documents as input

Extracts structured invoice data

Reconstructs line-item tables

Calculates subtotal and tax values

Validates financial totals

Detects suspicious values using rule-based anomaly detection

Provides explainable calculations through XAI

Displays results through an interactive dashboard

Key Features

• Financial document extraction
• Invoice line-item reconstruction
• Automated subtotal and tax calculation
• Financial validation of totals
• Rule-based anomaly detection
• Explainable AI for calculation transparency
• Interactive dashboard using Streamlit
• Structured JSON output generation

System Architecture
Financial Document (PDF)
        │
        ▼
Document Extraction
        │
        ▼
Structured Data (JSON)
        │
        ▼
Table Reconstruction
        │
        ▼
Financial Validation
        │
        ▼
Rule-Based Anomaly Detection
        │
        ▼
Explainable AI (XAI)
        │
        ▼
Interactive Dashboard
Technology Stack

Python
Streamlit
Pandas
Requests

Project Structure
FinSight-AI
│
├── app.py
├── hyperapi_parser.py
├── table_processor.py
├── validator.py
├── anomaly_detector.py
├── output_writer.py
│
├── data
│   └── sample_invoice.pdf
│
├── outputs
│
├── requirements.txt
└── README.md
Example Workflow

Upload a financial invoice PDF

The system extracts invoice information

Line-item table is reconstructed

Subtotal and tax are calculated

Invoice totals are validated

Anomaly detection flags suspicious values

Explainable AI shows calculation reasoning

Explainable AI (XAI)

FinSight AI provides transparent reasoning for financial validation by showing step-by-step calculations.

Example:

2 × 600 = 1200
5 × 20 = 100
3 × 50 = 150

Subtotal = 1200 + 100 + 150 = 1450
Tax = 100
Final Total = 1450 + 100 = 1550

This ensures auditability and trust in financial automation.

Running the Project Locally

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

The dashboard will open at:

http://localhost:8501
Deployment

The application can be deployed easily using Streamlit Community Cloud.

Steps:

Upload project to GitHub

Connect repository to Streamlit Cloud

Deploy using app.py as the main file

Future Improvements

• Support multi-page financial documents
• Advanced anomaly detection using ML models
• Integration with enterprise accounting systems
• Real-time financial analytics dashboard

Author

Syeda Ayesha Siddikha
AIML Engineering Student
Acharya Institute of Technology
