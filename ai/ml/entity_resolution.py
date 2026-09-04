import pandas as pd
from difflib import SequenceMatcher


# ---------------------------------------------------------
# NAME SIMILARITY
# ---------------------------------------------------------

def name_similarity(name1, name2):
    """
    Calculate similarity between two names.
    Returns a value between 0 and 1.
    """

    name1 = str(name1).lower().strip()
    name2 = str(name2).lower().strip()

    return SequenceMatcher(
        None,
        name1,
        name2
    ).ratio()


# ---------------------------------------------------------
# COMPARE TWO ENTITIES
# ---------------------------------------------------------

def compare_entities(entity1, entity2):
    """
    Compare two entities using:
    - Name similarity
    - Phone number
    - Vehicle number
    - Location
    """

    name_sim = name_similarity(
        entity1["name"],
        entity2["name"]
    )

    phone_match = (
        str(entity1["phone"]).strip()
        == str(entity2["phone"]).strip()
    )

    vehicle_match = (
        str(entity1["vehicle"]).strip()
        == str(entity2["vehicle"]).strip()
    )

    location_match = (
        str(entity1["location"]).strip().lower()
        == str(entity2["location"]).strip().lower()
    )

    # -----------------------------------------------------
    # WEIGHTED MATCH SCORE
    # -----------------------------------------------------

    score = (
        (name_sim * 40)
        + (25 if phone_match else 0)
        + (20 if vehicle_match else 0)
        + (15 if location_match else 0)
    )

    return {
        "entity_1": str(entity1["person_id"]),
        "entity_2": str(entity2["person_id"]),
        "score": float(round(score, 2)),
        "name_similarity": float(round(name_sim, 2)),
        "phone_match": bool(phone_match),
        "vehicle_match": bool(vehicle_match),
        "location_match": bool(location_match)
    }


# ---------------------------------------------------------
# FIND POSSIBLE ENTITY MATCHES
# ---------------------------------------------------------

def find_possible_matches(file_path, threshold=70):
    """
    Compare every pair of entities and return
    possible matches above the specified threshold.
    """

    df = pd.read_csv(file_path)

    matches = []

    for i in range(len(df)):

        for j in range(i + 1, len(df)):

            entity1 = df.iloc[i]
            entity2 = df.iloc[j]

            result = compare_entities(
                entity1,
                entity2
            )

            if result["score"] >= threshold:

                matches.append(result)

    return matches


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

if __name__ == "__main__":

    file_path = "data/sample/netra_demo_data.csv"

    matches = find_possible_matches(
        file_path,
        threshold=70
    )

    print("\n" + "=" * 40)
    print("       NETRA ENTITY RESOLUTION")
    print("=" * 40)

    if not matches:

        print("\nNo possible entity matches found.")

    else:

        for match in matches:

            print("\nPossible Entity Match")
            print("-" * 40)

            print(
                f"Entities: "
                f"{match['entity_1']} ↔ "
                f"{match['entity_2']}"
            )

            print(
                f"Match Score: "
                f"{match['score']}/100"
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

            if match["phone_match"]:
                print("✓ Same phone number")

            if match["vehicle_match"]:
                print("✓ Same vehicle")

            if match["location_match"]:
                print("✓ Same location")

            print(
                "\n⚠ This is a possible entity match "
                "and requires human verification."
            )