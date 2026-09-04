import pandas as pd
import networkx as nx


def build_network(file_path):
    """Build a relationship graph from the relationship dataset."""

    df = pd.read_csv(file_path)

    graph = nx.Graph()

    for _, row in df.iterrows():
        graph.add_edge(
            row["source"],
            row["target"],
            relationship=row["relationship"],
            case_id=row["case_id"]
        )

    return graph


def analyze_network(graph):
    """Calculate network centrality measures."""

    degree_centrality = nx.degree_centrality(graph)
    betweenness_centrality = nx.betweenness_centrality(graph)

    results = []

    for node in graph.nodes():

        results.append({
            "entity": node,
            "degree_centrality": round(
                degree_centrality[node], 3
            ),
            "betweenness_centrality": round(
                betweenness_centrality[node], 3
            ),
            "connections": graph.degree(node)
        })

    results.sort(
        key=lambda x: (
            x["betweenness_centrality"],
            x["degree_centrality"]
        ),
        reverse=True
    )

    return results


if __name__ == "__main__":

    file_path = "data/sample/netra_relationships.csv"

    graph = build_network(file_path)
    results = analyze_network(graph)

    print("\n========================================")
    print("        NETRA NETWORK ANALYSIS")
    print("========================================")

    print(f"\nEntities in network: {graph.number_of_nodes()}")
    print(f"Relationships: {graph.number_of_edges()}")

    print("\nNETWORK INSIGHTS")
    print("----------------------------------------")

    for result in results:

        print(
            f"\nEntity: {result['entity']}"
        )

        print(
            f"Connections: {result['connections']}"
        )

        print(
            f"Degree Centrality: "
            f"{result['degree_centrality']}"
        )

        print(
            f"Betweenness Centrality: "
            f"{result['betweenness_centrality']}"
        )

    if results:

        top_entity = results[0]

        print("\n----------------------------------------")
        print("STRUCTURALLY IMPORTANT ENTITY")
        print("----------------------------------------")

        print(
            f"Entity: {top_entity['entity']}"
        )

        print(
            f"Connections: {top_entity['connections']}"
        )

        print(
            f"Betweenness Centrality: "
            f"{top_entity['betweenness_centrality']}"
        )

        print(
            "\nInterpretation:"
        )

        print(
            "This entity has relatively high structural "
            "importance within the observed network."
        )

        print(
            "\n⚠ Network centrality does not indicate guilt "
            "and requires human investigation."
        )