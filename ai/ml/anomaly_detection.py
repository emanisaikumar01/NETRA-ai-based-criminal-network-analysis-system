import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(file_path, contamination=0.2):
    """
    Detect unusual transaction amounts using Isolation Forest.
    """

    df = pd.read_csv(file_path)

    # Isolation Forest expects numerical features.
    X = df[["amount"]]

    model = IsolationForest(
        contamination=contamination,
        random_state=42
    )

    predictions = model.fit_predict(X)

    # -1 = anomaly, 1 = normal
    df["prediction"] = predictions

    df["status"] = df["prediction"].map({
        1: "NORMAL",
        -1: "ANOMALY"
    })

    return df


if __name__ == "__main__":

    file_path = "data/sample/netra_transactions.csv"

    results = detect_anomalies(file_path)

    print("\n========================================")
    print("       NETRA ANOMALY DETECTION")
    print("========================================")

    for _, row in results.iterrows():

        print(
            f"\nTransaction: {row['transaction_id']}"
        )

        print(
            f"Sender: {row['sender']}"
        )

        print(
            f"Receiver: {row['receiver']}"
        )

        print(
            f"Amount: ₹{row['amount']:,.2f}"
        )

        print(
            f"Status: {row['status']}"
        )

        if row["status"] == "ANOMALY":
            print(
                "⚠ Transaction significantly deviates "
                "from the observed transaction pattern."
            )

    print("\n========================================")
    print("Note: An anomaly is not evidence of criminal activity.")
    print("Human investigator review is required.")
    print("========================================")