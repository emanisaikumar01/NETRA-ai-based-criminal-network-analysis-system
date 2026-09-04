import json
from pathlib import Path

from entity_resolution import find_possible_matches
from network_analysis import build_network, analyze_network
from anomaly_detection import detect_anomalies
from lead_scoring import calculate_lead_scores


# ---------------------------------------------------------
# PATHS
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data" / "sample"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PEOPLE_FILE = DATA_DIR / "netra_demo_data.csv"
TRANSACTION_FILE = DATA_DIR / "netra_transactions.csv"
RELATIONSHIP_FILE = DATA_DIR / "netra_relationships.csv"

OUTPUT_FILE = PROCESSED_DIR / "netra_result.json"


# ---------------------------------------------------------
# NETRA ML PIPELINE
# ---------------------------------------------------------

def run_pipeline():

    print("\n" + "=" * 55)
    print("              NETRA AI/ML PIPELINE")
    print("=" * 55)

    # -----------------------------------------------------
    # 1. ENTITY RESOLUTION
    # -----------------------------------------------------

    print("\n[1/4] Running Entity Resolution...")

    entity_matches = find_possible_matches(
        str(PEOPLE_FILE),
        threshold=70
    )

    print(f"      Possible entity matches found: {len(entity_matches)}")


    # -----------------------------------------------------
    # 2. NETWORK ANALYSIS
    # -----------------------------------------------------

    print("\n[2/4] Running Network Analysis...")

    graph = build_network(str(RELATIONSHIP_FILE))

    network_insights = analyze_network(graph)

    print(f"      Entities in network: {graph.number_of_nodes()}")
    print(f"      Relationships: {graph.number_of_edges()}")

    if network_insights:
        top_entity = network_insights[0]
        print(
            f"      Structurally important entity: "
            f"{top_entity['entity']}"
        )


    # -----------------------------------------------------
    # 3. ANOMALY DETECTION
    # -----------------------------------------------------

    print("\n[3/4] Running Transaction Anomaly Detection...")

    anomaly_df = detect_anomalies(
        str(TRANSACTION_FILE)
    )

    anomalous_transactions = []

    for _, row in anomaly_df.iterrows():

        if row["status"] == "ANOMALY":

            anomalous_transactions.append({
                "transaction_id": str(row["transaction_id"]),
                "sender": str(row["sender"]),
                "receiver": str(row["receiver"]),
                "amount": float(row["amount"]),
                "status": str(row["status"])
            })

    print(
        f"      Anomalous transactions found: "
        f"{len(anomalous_transactions)}"
    )


    # -----------------------------------------------------
    # 4. INVESTIGATIVE LEAD SCORING
    # -----------------------------------------------------

    print("\n[4/4] Calculating Investigative Lead Priority...")

    lead_scores = calculate_lead_scores(
        str(PEOPLE_FILE),
        str(TRANSACTION_FILE),
        str(RELATIONSHIP_FILE)
    )

    print(f"      Entities scored: {len(lead_scores)}")


    # -----------------------------------------------------
    # FINAL RESULT
    # -----------------------------------------------------

    result = {
        "system": "NETRA",
        "purpose": "Investigative Decision Support",
        "entity_matches": entity_matches,
        "network_insights": network_insights,
        "anomalies": anomalous_transactions,
        "lead_scores": lead_scores
    }

    return result


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

if __name__ == "__main__":

    result = run_pipeline()

    # Create processed directory if it doesn't exist
    PROCESSED_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save final result
    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            indent=4,
            ensure_ascii=False
        )

    # -----------------------------------------------------
    # DISPLAY SUMMARY
    # -----------------------------------------------------

    print("\n" + "=" * 55)
    print("             NETRA PIPELINE COMPLETE")
    print("=" * 55)

    print(
        f"\nPossible Entity Matches : "
        f"{len(result['entity_matches'])}"
    )

    print(
        f"Network Entities        : "
        f"{len(result['network_insights'])}"
    )

    print(
        f"Anomalous Transactions  : "
        f"{len(result['anomalies'])}"
    )

    print(
        f"Entities Scored         : "
        f"{len(result['lead_scores'])}"
    )

    # Show highest-priority investigative lead
    if result["lead_scores"]:

        top_lead = max(
            result["lead_scores"],
            key=lambda x: x["score"]
        )

        print("\n" + "-" * 55)
        print("TOP INVESTIGATIVE LEAD")
        print("-" * 55)

        print(f"Entity   : {top_lead['entity']}")
        print(f"Priority : {top_lead['priority']}")
        print(f"Score    : {top_lead['score']}/100")

        print("\nWHY THIS LEAD?")

        for reason in top_lead["reasons"]:
            print(f"  ✓ {reason}")

        print("\nEVIDENCE GAPS")

        for gap in top_lead["evidence_gaps"]:
            print(f"  ⚠ {gap}")

    print("\n" + "-" * 55)
    print("Final result saved to:")
    print(OUTPUT_FILE)
    print("-" * 55)

    print(
        "\n⚠ NETRA provides investigative leads, "
        "not determinations of guilt."
    )

    print("=" * 55)