from flask import Flask, request, jsonify
import psycopg2
from datetime import datetime

app = Flask(__name__)
@app.route("/")
def home():
    return "SERVER IS RUNNING"

# DATABASE CONNECTION
conn = psycopg2.connect(
    host="localhost",
    database="fraud_db",
    user="postgres",
    password="mayank123",  # <-- replace this
    port=5432
)
cursor = conn.cursor()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    cursor.execute(
        """
        INSERT INTO audit_log (
            timestamp, transaction_id, vendor_id, sector,
            item, amount, risk_score, risk_level, fraud_status, action
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            datetime.now(),
            data.get("transaction_id"),
            data.get("vendor_id"),
            data.get("sector"),
            data.get("item_category"),
            data.get("amount"),
            90,
            "HIGH",
            "FRAUD",
            "TEST INSERT"
        )
    )
    conn.commit()

    return jsonify({"status": "inserted into db"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
