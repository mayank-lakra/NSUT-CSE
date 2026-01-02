# Fraud Detection Backend

Backend service for fraud/anomaly detection using rule-based and AI-generated signals.  
This service exposes APIs to ingest transaction data and persist results into PostgreSQL.

---

## 🔹 Features
- REST API for transaction ingestion
- PostgreSQL database integration
- Ready for AI anomaly score integration
- Clean separation of Backend, AI, and DevOps responsibilities
- Easily deployable by DevOps

---

## 🔹 Tech Stack
- Python
- Flask
- PostgreSQL
- psycopg2

---

## 🔹 API Endpoints

### POST /predict
Accepts transaction data and stores it in the database.

#### Request Body
```json
{
  "transaction_id": "string",
  "vendor_id": "string",
  "sector": "string",
  "item_category": "string",
  "amount": number
}
