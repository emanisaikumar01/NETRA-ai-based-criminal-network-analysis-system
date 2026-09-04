import pandas as pd


def calculate_lead_scores(
    demo_file,
    transaction_file,
    relationship_file
):
    """
    Calculate an explainable Investigative Lead Priority score.

    This score prioritizes entities for human investigation.
    It does NOT represent probability of guilt.
    """

    # ----------------------------------------
    # LOAD DATASETS
    # ----------------------------------------

    people = pd.read_csv(demo_file)
    transactions = pd.read_csv(transaction_file)
    relationships = pd.read_csv(relationship_file)

    # ----------------------------------------
    # 1. NETWORK SIGNAL
    # ----------------------------------------

    connection_counts = {}

    for _, row in relationships.iterrows():

        source = row["source"]
        target = row["target"]

        connection_counts[source] = (
            connection_counts.get(source, 0) + 1
        )

        connection_counts[target] = (
            connection_counts.get(target, 0) + 1
        )

    # ----------------------------------------
    # 2. ANOMALY SIGNAL
    # ----------------------------------------

    normal_amounts = transactions[
        transactions["amount"] < 100000
    ]["amount"]

    average_amount = normal_amounts.mean()

    anomaly_transactions = transactions[
        transactions["amount"] > average_amount * 10
    ]

    anomaly_entities = set()

    for _, row in anomaly_transactions.iterrows():

        anomaly_entities.add(row["sender"])
        anomaly_entities.add(row["receiver"])

    # ----------------------------------------
    # 3. CASE ASSOCIATION SIGNAL
    # ----------------------------------------

    case_counts = (
        people.groupby("person_id")["case_id"]
        .nunique()
        .to_dict()
    )

    # ----------------------------------------
    # 4. CALCULATE LEAD SCORE
    # ----------------------------------------

    results = []

    for person_id in people["person_id"].unique():

        score = 0
        reasons = []
        evidence_gaps = []

        connections = connection_counts.get(
            person_id, 0
        )

        cases = case_counts.get(
            person_id, 0
        )

        # ------------------------------------
        # NETWORK CONTRIBUTION
        # ------------------------------------

        if connections >= 3:

            score += 35

            reasons.append(
                "High number of network connections"
            )

        elif connections >= 2:

            score += 20

            reasons.append(
                "Connected to multiple entities"
            )

        # ------------------------------------
        # ANOMALY CONTRIBUTION
        # ------------------------------------

        if person_id in anomaly_entities:

            score += 30

            reasons.append(
                "Associated with an anomalous transaction"
            )

        # ------------------------------------
        # CASE ASSOCIATION
        # ------------------------------------

        if cases >= 2:

            score += 20

            reasons.append(
                "Appears across multiple cases"
            )

        elif cases == 1:

            score += 5

        # ------------------------------------
        # EVIDENCE GAPS
        # ------------------------------------

        if person_id not in anomaly_entities:

            evidence_gaps.append(
                "No transaction anomaly observed"
            )

        else:

            evidence_gaps.append(
                "Transaction anomaly detected, "
                "but intent is not established"
            )

        if connections < 2:

            evidence_gaps.append(
                "Limited network connections"
            )

        # ------------------------------------
        # KEEP SCORE WITHIN 100
        # ------------------------------------

        score = min(score, 100)

        # ------------------------------------
        # PRIORITY LEVEL
        # ------------------------------------

        if score >= 70:

            priority = "HIGH"

        elif score >= 40:

            priority = "MEDIUM"

        else:

            priority = "LOW"

        results.append({
            "entity": person_id,
            "score": score,
            "priority": priority,
            "reasons": reasons,
            "evidence_gaps": evidence_gaps
        })

    return results


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":

    results = calculate_lead_scores(
        "data/sample/netra_demo_data.csv",
        "data/sample/netra_transactions.csv",
        "data/sample/netra_relationships.csv"
    )

    print("\n========================================")
    print("       NETRA LEAD PRIORITY")
    print("========================================")

    for result in results:

        print("\n----------------------------------------")

        print(
            f"Entity: {result['entity']}"
        )

        print(
            f"Lead Priority: {result['priority']}"
        )

        print(
            f"Score: {result['score']}/100"
        )

        print("\nWHY THIS LEAD?")

        if result["reasons"]:

            for reason in result["reasons"]:

                print(f"✓ {reason}")

        else:

            print(
                "No significant signals observed."
            )

        print("\nEVIDENCE GAPS")

        if result["evidence_gaps"]:

            for gap in result["evidence_gaps"]:

                print(f"⚠ {gap}")

        else:

            print(
                "No major evidence gaps identified."
            )

    print("\n========================================")

    print(
        "Note: Lead priority is NOT a guilt score."
    )

    print(
        "It is based only on observed data signals."
    )

    print(
        "Human investigator review is required."
    )

    print("========================================")