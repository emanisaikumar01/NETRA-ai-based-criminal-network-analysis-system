import pandas as pd
from difflib import SequenceMatcher


def name_similarity(name1, name2):
    """Calculate similarity between two names."""
    return SequenceMatcher(
        None,
        name1.lower().strip(),
        name2.lower().strip()
    ).ratio()


def compare_entities(entity1, entity2):
    """
    Compare two entity records using multiple signals.

    Returns a match score and an explanation of the matching signals.
    """

    name_score = name_similarity(entity1["name"], entity2["name"])

    phone_match = (
        entity1["phone"] == entity2["phone"]
        and entity1["phone"] != ""
    )

    vehicle_match = (
        entity1["vehicle"] == entity2["vehicle"]
        and entity1["vehicle"] != ""
    )

    location_match = (
        entity1["location"].lower().strip()
        == entity2["location"].lower().strip()
        and entity1["location"] != ""
    )

    # Weighted score
    score = (
        0.40 * name_score
        + 0.25 * int(phone_match)
        + 0.20 * int(vehicle_match)
        + 0.15 * int(location_match)
    )

    reasons = []

    if name_score >= 0.80:
        reasons.append("High name similarity")

    if phone_match:
        reasons.append("Same phone number")

    if vehicle_match:
        reasons.append("Same vehicle")

    if location_match:
        reasons.append("Same location")

    return {
        "entity_1": entity1["person_id"],
        "entity_2": entity2["person_id"],
        "name_similarity": round(name_score, 2),
        "phone_match": phone_match,
        "vehicle_match": vehicle_match,
        "location_match": location_match,
        "match_score": round(score * 100, 2),
        "reasons": reasons
    }


def find_possible_matches(file_path, threshold=70):
    """Find possible duplicate/entity matches in the dataset."""

    df = pd.read_csv(file_path)

    results = []

    for i in range(len(df)):
        for j in range(i + 1, len(df)):

            result = compare_entities(
                df.iloc[i],
                df.iloc[j]
            )

            if result["match_score"] >= threshold:
                results.append(result)

    return results


if __name__ == "__main__":

    file_path = "data/sample/netra_demo_data.csv"

    matches = find_possible_matches(file_path)

    print("\n========================================")
    print("       NETRA ENTITY RESOLUTION")
    print("========================================")

    if not matches:
        print("\nNo possible entity matches found.")

    else:
        for match in matches:

            print("\nPossible Entity Match")
            print("----------------------------------------")

            print(
                f"Entities: {match['entity_1']} ↔ "
                f"{match['entity_2']}"
            )

            print(
                f"Match Score: {match['match_score']}/100"
            )

            print(
                f"Name Similarity: "
                f"{match['name_similarity']}"
            )

            print(
                f"Phone Match: "
                f"{match['phone_match']}"
            )

            print(
                f"Vehicle Match: "
                f"{match['vehicle_match']}"
            )

            print(
                f"Location Match: "
                f"{match['location_match']}"
            )

            print("\nWHY?")
            for reason in match["reasons"]:
                print(f"✓ {reason}")

            print(
                "\n⚠ This is a possible entity match "
                "and requires human verification."
            )