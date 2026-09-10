import streamlit as st
import networkx as nx
import random
import math
import time
import statistics
import matplotlib.pyplot as plt
import pandas as pd

from algorithms.qpso import qpso_vrp_optimization


# ============================================================
# QUANTUM-INSPIRED TRAFFIC ROUTE OPTIMIZATION
# ============================================================

st.set_page_config(
    page_title="QuantumRoute",
    page_icon="🚦",
    layout="wide"
)

# ============================================================
# FINAL SIH PROJECT OVERVIEW
# ============================================================

st.title("🚦 Quantum-Inspired Intelligent Traffic Route Optimization")

st.markdown("""
### Smart India Hackathon 2026 Prototype

This system uses **Quantum Particle Swarm Optimization (QPSO)**
to search for low-cost vehicle delivery routes on a
traffic-weighted road network.

The prototype evaluates:

- 🛣️ Graph-based road network modelling
- 🚚 Vehicle delivery route optimization
- 🚦 Traffic-aware route costs
- ⚛️ Quantum-inspired QPSO optimization
- 📉 Convergence analysis
- 🔁 Reliability testing
- ⏱️ Runtime benchmarking
- ⚖️ Algorithm comparison
- 📈 Scalability evaluation
- 🎯 Multi-objective transportation optimization
""")

st.info(
    "Core objective: minimize transportation route cost while "
    "considering travel time, distance and congestion."
)

st.divider()

st.title("🚦 Quantum-Inspired Intelligent Traffic Route Optimization")

st.write(
    "A classical-computer route optimization platform using "
    "Quantum Particle Swarm Optimization (QPSO)."
)


# ============================================================
# HELPER FUNCTION - CALCULATE ROUTE COST
# ============================================================

def calculate_route_cost(graph, route):

    total_cost = 0

    for i in range(len(route) - 1):

        start = route[i]
        end = route[i + 1]

        try:

            shortest_path = nx.shortest_path(
                graph,
                start,
                end,
                weight="weight"
            )

            for j in range(len(shortest_path) - 1):

                u = shortest_path[j]
                v = shortest_path[j + 1]

                total_cost += graph[u][v]["weight"]

        except nx.NetworkXNoPath:

            return float("inf")

    return total_cost


# ============================================================
# PART 1 - BASIC ROAD NETWORK
# ============================================================

print()
print("=" * 70)
print("PART 1 - BASIC ROAD NETWORK")
print("=" * 70)

G = nx.Graph()

G.add_edge("A", "B", weight=5)
G.add_edge("B", "C", weight=3)
G.add_edge("C", "E", weight=4)
G.add_edge("E", "F", weight=3)

G.add_edge("A", "D", weight=20)
G.add_edge("D", "E", weight=6)
G.add_edge("D", "F", weight=2)

print()
print("Basic road network created.")
print("Locations:", list(G.nodes()))
print("Roads:", list(G.edges(data=True)))


# ============================================================
# PART 2 - SHORTEST PATH
# ============================================================

print()
print("=" * 70)
print("PART 2 - SHORTEST PATH")
print("=" * 70)

source = "A"
target = "F"

shortest_path = nx.shortest_path(
    G,
    source,
    target,
    weight="weight"
)

shortest_distance = nx.shortest_path_length(
    G,
    source,
    target,
    weight="weight"
)

print()
print("Shortest route:")
print(" -> ".join(shortest_path))

print()
print("Shortest route cost:", shortest_distance)


# ============================================================
# PART 3 - TRAFFIC SIMULATION
# ============================================================

print()
print("=" * 70)
print("PART 3 - TRAFFIC SIMULATION")
print("=" * 70)

# Simulate heavy traffic on road A-D

G["A"]["D"]["weight"] = 50

traffic_path = nx.shortest_path(
    G,
    "A",
    "F",
    weight="weight"
)

traffic_distance = nx.shortest_path_length(
    G,
    "A",
    "F",
    weight="weight"
)

print()
print("Traffic condition simulated.")

print()
print("New optimized route:")
print(" -> ".join(traffic_path))

print()
print("New route cost:", traffic_distance)


# ============================================================
# PART 4 - ROUTE COST FUNCTION TEST
# ============================================================

print()
print("=" * 70)
print("PART 4 - ROUTE COST FUNCTION")
print("=" * 70)

test_route = [
    "A",
    "B",
    "C",
    "E",
    "F"
]

test_cost = calculate_route_cost(
    G,
    test_route
)

print()
print("Test route:")
print(" -> ".join(test_route))

print()
print("Route cost:", test_cost)


# ============================================================
# PART 5 - QPSO BASIC ROUTE OPTIMIZATION
# ============================================================

print()
print("=" * 70)
print("PART 5 - QPSO BASIC ROUTE OPTIMIZATION")
print("=" * 70)

delivery_points = [
    "B",
    "C",
    "D",
    "E",
    "F"
]

qpso_route5, qpso_cost5, qpso_convergence5 = (
    qpso_vrp_optimization(
        G,
        "A",
        delivery_points,
        particles=30,
        iterations=100
    )
)

print()
print("QPSO optimized route:")
print(" -> ".join(qpso_route5))

print()
print("QPSO optimized cost:", qpso_cost5)

print()
print(
    "Number of iterations:",
    len(qpso_convergence5)
)


# ============================================================
# PART 6 - QPSO CONVERGENCE VISUALIZATION
# ============================================================

print()
print("=" * 70)
print("PART 6 - QPSO CONVERGENCE VISUALIZATION")
print("=" * 70)

if qpso_convergence5:

    fig6 = plt.figure(figsize=(10, 6))

    plt.plot(
        range(1, len(qpso_convergence5) + 1),
        qpso_convergence5,
        label="QPSO"
    )

    plt.xlabel("Iteration")
    plt.ylabel("Route Objective Cost")

    plt.title(
        "QPSO Convergence"
    )

    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    st.pyplot(fig6)

    plt.close(fig6)


# ============================================================
# PART 7 - ROUTE VISUALIZATION
# ============================================================

print()
print("=" * 70)
print("PART 7 - ROUTE VISUALIZATION")
print("=" * 70)

positions7 = {
    "A": (0, 0),
    "B": (2, 2),
    "C": (4, 3),
    "D": (2, -2),
    "E": (6, 2),
    "F": (8, 0)
}

fig7 = plt.figure(figsize=(10, 6))

nx.draw(
    G,
    positions7,
    with_labels=True,
    node_size=1000
)

nx.draw_networkx_edge_labels(
    G,
    positions7,
    edge_labels=nx.get_edge_attributes(
        G,
        "weight"
    )
)

if qpso_route5:

    route_edges7 = list(
        zip(
            qpso_route5[:-1],
            qpso_route5[1:]
        )
    )

    nx.draw_networkx_edges(
        G,
        positions7,
        edgelist=route_edges7,
        width=3
    )

plt.title(
    "QPSO Optimized Traffic Route"
)

plt.tight_layout()

st.pyplot(fig7)

plt.close(fig7)


# ============================================================
# PART 8 - CLASSICAL PSO-STYLE BASELINE
# ============================================================

print()
print("=" * 70)
print("PART 8 - CLASSICAL PSO-STYLE BASELINE")
print("=" * 70)

# ============================================================
# ROUTE COST FUNCTION
# ============================================================

def calculate_route_cost(graph, route):

    total_cost = 0

    for i in range(len(route) - 1):

        start = route[i]
        end = route[i + 1]

        try:

            shortest_path = nx.shortest_path(
                graph,
                start,
                end,
                weight="weight"
            )

            for j in range(len(shortest_path) - 1):

                u = shortest_path[j]
                v = shortest_path[j + 1]

                total_cost += graph[u][v].get(
                    "weight",
                    1
                )

        except nx.NetworkXNoPath:

            return float("inf")

    return total_cost



def pso_vrp_optimization(
    graph,
    depot,
    delivery_points,
    particles=30,
    iterations=100
):

    swarm = []

    # --------------------------------------------------------
    # CREATE INITIAL PARTICLES
    # --------------------------------------------------------

    for _ in range(particles):

        points = delivery_points[:]

        random.shuffle(points)

        route = (
            [depot]
            + points
            + [depot]
        )

        cost = calculate_route_cost(
            graph,
            route
        )

        if cost != float("inf"):

            swarm.append({
                "route": route,
                "cost": cost
            })

    # --------------------------------------------------------
    # CHECK VALID SWARM
    # --------------------------------------------------------

    if not swarm:

        print(
            "PSO could not create valid routes."
        )

        return (
            None,
            float("inf"),
            []
        )

    # --------------------------------------------------------
    # INITIAL BEST
    # --------------------------------------------------------

    best_particle = min(
        swarm,
        key=lambda particle:
        particle["cost"]
    )

    best_route = (
        best_particle["route"][:]
    )

    best_cost = (
        best_particle["cost"]
    )

    convergence = []

    # --------------------------------------------------------
    # OPTIMIZATION LOOP
    # --------------------------------------------------------

    for iteration in range(iterations):

        for particle in swarm:

            new_route = (
                particle["route"][:]
            )

            if len(new_route) > 3:

                i, j = random.sample(
                    range(
                        1,
                        len(new_route) - 1
                    ),
                    2
                )

                (
                    new_route[i],
                    new_route[j]
                ) = (
                    new_route[j],
                    new_route[i]
                )

            new_cost = calculate_route_cost(
                graph,
                new_route
            )

            if (
                new_cost != float("inf")
                and new_cost < particle["cost"]
            ):

                particle["route"] = (
                    new_route
                )

                particle["cost"] = (
                    new_cost
                )

            if (
                particle["cost"]
                < best_cost
            ):

                best_route = (
                    particle["route"][:]
                )

                best_cost = (
                    particle["cost"]
                )

        convergence.append(
            best_cost
        )

    return (
        best_route,
        best_cost,
        convergence
    )


# ============================================================
# PART 9 - CLASSICAL PSO TEST
# ============================================================

print()
print("=" * 70)
print("PART 9 - CLASSICAL PSO TEST")
print("=" * 70)

pso_route9, pso_cost9, pso_convergence9 = (
    pso_vrp_optimization(
        G,
        "A",
        delivery_points,
        particles=30,
        iterations=100
    )
)

print()
print("Classical PSO-style route:")

if pso_route9:

    print(
        " -> ".join(pso_route9)
    )

print()
print(
    "Classical PSO-style cost:",
    pso_cost9
)


# ============================================================
# PART 10 - QPSO VS CLASSICAL PSO CONVERGENCE
# ============================================================

print()
print("=" * 70)
print("PART 10 - QPSO VS CLASSICAL PSO CONVERGENCE")
print("=" * 70)

fig10 = plt.figure(figsize=(10, 6))

if qpso_convergence5:

    plt.plot(
        range(
            1,
            len(qpso_convergence5) + 1
        ),
        qpso_convergence5,
        label="QPSO"
    )

if pso_convergence9:

    plt.plot(
        range(
            1,
            len(pso_convergence9) + 1
        ),
        pso_convergence9,
        label="Classical PSO-style"
    )

plt.xlabel("Iteration")

plt.ylabel(
    "Route Objective Cost"
)

plt.title(
    "QPSO vs Classical PSO Convergence"
)

plt.grid(True)

plt.legend()

plt.tight_layout()

st.pyplot(fig10)

plt.close(fig10)


# ============================================================
# PART 11 - REPEATED BENCHMARK
# ============================================================

print()
print("=" * 70)
print("PART 11 - REPEATED BENCHMARK")
print("=" * 70)

NUM_RUNS11 = 10

qpso_results11 = []
pso_results11 = []

qpso_times11 = []
pso_times11 = []

improvements11 = []

for run in range(NUM_RUNS11):

    # --------------------------------------------------------
    # QPSO
    # --------------------------------------------------------

    start_qpso11 = time.perf_counter()

    route_q11, cost_q11, conv_q11 = (
        qpso_vrp_optimization(
            G,
            "A",
            delivery_points,
            particles=30,
            iterations=100
        )
    )

    end_qpso11 = time.perf_counter()

    qpso_runtime11 = (
        end_qpso11
        - start_qpso11
    )

    # --------------------------------------------------------
    # CLASSICAL PSO
    # --------------------------------------------------------

    start_pso11 = time.perf_counter()

    route_p11, cost_p11, conv_p11 = (
        pso_vrp_optimization(
            G,
            "A",
            delivery_points,
            particles=30,
            iterations=100
        )
    )

    end_pso11 = time.perf_counter()

    pso_runtime11 = (
        end_pso11
        - start_pso11
    )

    # --------------------------------------------------------
    # STORE VALID RESULTS
    # --------------------------------------------------------

    if (
        cost_q11 != float("inf")
        and cost_p11 != float("inf")
    ):

        qpso_results11.append(
            cost_q11
        )

        pso_results11.append(
            cost_p11
        )

        qpso_times11.append(
            qpso_runtime11
        )

        pso_times11.append(
            pso_runtime11
        )

        if cost_p11 > 0:

            improvement11 = (
                (cost_p11 - cost_q11)
                / cost_p11
            ) * 100

            improvements11.append(
                improvement11
            )

        print()
        print(
            "Run",
            run + 1
        )

        print(
            "QPSO:",
            round(cost_q11, 3)
        )

        print(
            "Classical PSO:",
            round(cost_p11, 3)
        )


# ============================================================
# PART 11 - SUMMARY
# ============================================================

if qpso_results11 and pso_results11:

    average_qpso11 = statistics.mean(
        qpso_results11
    )

    average_pso11 = statistics.mean(
        pso_results11
    )

    best_qpso11 = min(
        qpso_results11
    )

    best_pso11 = min(
        pso_results11
    )

    average_qpso_time11 = statistics.mean(
        qpso_times11
    )

    average_pso_time11 = statistics.mean(
        pso_times11
    )

    if improvements11:

        average_improvement11 = (
            statistics.mean(
                improvements11
            )
        )

    else:

        average_improvement11 = 0.0

    print()
    print(
        "Average QPSO cost:",
        round(average_qpso11, 3)
    )

    print(
        "Average Classical PSO cost:",
        round(average_pso11, 3)
    )

    print(
        "Best QPSO cost:",
        round(best_qpso11, 3)
    )

    print(
        "Best Classical PSO cost:",
        round(best_pso11, 3)
    )

    print(
        "Average QPSO improvement:",
        round(
            average_improvement11,
            2
        ),
        "%"
    )

    print(
        "Average QPSO runtime:",
        round(
            average_qpso_time11,
            6
        ),
        "seconds"
    )

    print(
        "Average PSO runtime:",
        round(
            average_pso_time11,
            6
        ),
        "seconds"
    )

    st.subheader(
        "Repeated QPSO vs Classical PSO Benchmark"
    )

    benchmark_data11 = {
        "Metric": [
            "Average Cost",
            "Best Cost",
            "Average Runtime (s)",
            "Improvement (%)"
        ],

        "QPSO": [
            round(
                average_qpso11,
                3
            ),

            round(
                best_qpso11,
                3
            ),

            round(
                average_qpso_time11,
                6
            ),

            round(
                average_improvement11,
                2
            )
        ],

        "Classical PSO": [
            round(
                average_pso11,
                3
            ),

            round(
                best_pso11,
                3
            ),

            round(
                average_pso_time11,
                6
            ),

            "-"
        ]
    }

    st.table(
        benchmark_data11
    )


# ============================================================
# PART 12 - SCALABILITY BENCHMARK
# ============================================================

print()
print("=" * 70)
print("PART 12 - SCALABILITY BENCHMARK")
print("=" * 70)

sizes12 = [
    4,
    6,
    8,
    10
]

scalability_results12 = []

for size in sizes12:

    print()
    print(
        "Testing problem size:",
        size
    )

    G12 = nx.complete_graph(
        [
            chr(
                65 + i
            )
            for i in range(size)
        ]
    )

    for u, v in G12.edges():

        G12[u][v]["weight"] = (
            random.randint(1, 20)
        )

    nodes12 = list(
        G12.nodes()
    )

    depot12 = nodes12[0]

    delivery12 = nodes12[1:]

    qpso_values12 = []
    pso_values12 = []

    for _ in range(5):

        _, qcost12, _ = (
            qpso_vrp_optimization(
                G12,
                depot12,
                delivery12,
                particles=20,
                iterations=50
            )
        )

        _, pcost12, _ = (
            pso_vrp_optimization(
                G12,
                depot12,
                delivery12,
                particles=20,
                iterations=50
            )
        )

        if (
            qcost12 != float("inf")
            and pcost12 != float("inf")
        ):

            qpso_values12.append(
                qcost12
            )

            pso_values12.append(
                pcost12
            )

    if (
        qpso_values12
        and pso_values12
    ):

        avg_q12 = statistics.mean(
            qpso_values12
        )

        avg_p12 = statistics.mean(
            pso_values12
        )

        best_q12 = min(
            qpso_values12
        )

        best_p12 = min(
            pso_values12
        )

        if avg_p12 > 0:

            improvement12 = (
                (avg_p12 - avg_q12)
                / avg_p12
            ) * 100

        else:

            improvement12 = 0.0

        scalability_results12.append({
            "Size": size,
            "Avg QPSO": round(
                avg_q12,
                3
            ),
            "Avg PSO": round(
                avg_p12,
                3
            ),
            "Best QPSO": round(
                best_q12,
                3
            ),
            "Best PSO": round(
                best_p12,
                3
            ),
            "Improvement (%)": round(
                improvement12,
                2
            )
        })


# ============================================================
# DISPLAY PART 12 RESULTS
# ============================================================

if scalability_results12:

    st.subheader(
        "QPSO Scalability Benchmark"
    )

    st.table(
        scalability_results12
    )

print()
print("=" * 70)
print("PART 12 COMPLETE")
print("=" * 70)

# ============================================================
# PART 13 - LARGE TRAFFIC NETWORK
# ============================================================

print()
print("=" * 70)
print("PART 13 - LARGE TRAFFIC NETWORK")
print("=" * 70)

G13 = nx.Graph()

locations13 = [
    chr(65 + i)
    for i in range(15)
]

for node in locations13:
    G13.add_node(node)

for i in range(len(locations13) - 1):

    u = locations13[i]
    v = locations13[i + 1]

    G13.add_edge(
        u,
        v,
        weight=random.randint(3, 15)
    )

additional_edges13 = [
    ("A", "C"),
    ("A", "D"),
    ("B", "D"),
    ("C", "E"),
    ("D", "F"),
    ("E", "G"),
    ("F", "H"),
    ("G", "I"),
    ("H", "J"),
    ("I", "K"),
    ("J", "L"),
    ("K", "M"),
    ("L", "N"),
    ("M", "O")
]

for u, v in additional_edges13:

    G13.add_edge(
        u,
        v,
        weight=random.randint(3, 15)
    )

print()
print("Large traffic network created.")
print("Locations:", len(G13.nodes()))
print("Roads:", len(G13.edges()))


# ============================================================
# PART 14 - LARGE NETWORK QPSO
# ============================================================

print()
print("=" * 70)
print("PART 14 - LARGE NETWORK QPSO")
print("=" * 70)

delivery_points14 = locations13[1:11]

start14 = time.perf_counter()

route14, cost14, convergence14 = (
    qpso_vrp_optimization(
        G13,
        "A",
        delivery_points14,
        particles=30,
        iterations=100
    )
)

end14 = time.perf_counter()

runtime14 = end14 - start14

print()
print("Optimized route:")

if route14:
    print(" -> ".join(route14))

print()
print("Optimized cost:", round(cost14, 3))
print("Runtime:", round(runtime14, 6), "seconds")


# ============================================================
# PART 15 - LARGE NETWORK CONVERGENCE
# ============================================================

print()
print("=" * 70)
print("PART 15 - LARGE NETWORK CONVERGENCE")
print("=" * 70)

if convergence14:

    fig15 = plt.figure(figsize=(10, 6))

    plt.plot(
        range(1, len(convergence14) + 1),
        convergence14,
        label="QPSO"
    )

    plt.xlabel("Iteration")
    plt.ylabel("Objective Cost")

    plt.title(
        "QPSO Convergence on Large Traffic Network"
    )

    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    st.pyplot(fig15)

    plt.close(fig15)


# ============================================================
# PART 16 - LARGE NETWORK ROUTE VISUALIZATION
# ============================================================

print()
print("=" * 70)
print("PART 16 - LARGE NETWORK ROUTE VISUALIZATION")
print("=" * 70)

fig16 = plt.figure(figsize=(12, 8))

pos16 = nx.spring_layout(
    G13,
    seed=42
)

nx.draw(
    G13,
    pos16,
    with_labels=True,
    node_size=700
)

if route14:

    route_edges16 = list(
        zip(
            route14[:-1],
            route14[1:]
        )
    )

    nx.draw_networkx_edges(
        G13,
        pos16,
        edgelist=route_edges16,
        width=3
    )

plt.title(
    "QPSO Route on Large Traffic Network"
)

plt.tight_layout()

st.pyplot(fig16)

plt.close(fig16)


# ============================================================
# PART 17 - TRAFFIC CONGESTION SIMULATION
# ============================================================

print()
print("=" * 70)
print("PART 17 - TRAFFIC CONGESTION SIMULATION")
print("=" * 70)

G17 = G13.copy()

traffic_edges17 = [
    ("A", "C"),
    ("C", "E"),
    ("E", "G"),
    ("G", "I")
]

for u, v in traffic_edges17:

    if G17.has_edge(u, v):

        G17[u][v]["weight"] *= 4

print()
print("Traffic congestion applied.")

route17, cost17, convergence17 = (
    qpso_vrp_optimization(
        G17,
        "A",
        delivery_points14,
        particles=30,
        iterations=100
    )
)

print()
print("Traffic-aware route:")

if route17:
    print(" -> ".join(route17))

print()
print("Traffic-aware cost:", round(cost17, 3))


# ============================================================
# PART 18 - NORMAL VS TRAFFIC ROUTE
# ============================================================

print()
print("=" * 70)
print("PART 18 - NORMAL VS TRAFFIC ROUTE")
print("=" * 70)

if route14 and route17:

    print()
    print(
        "Normal route:",
        " -> ".join(route14)
    )

    print(
        "Normal cost:",
        round(cost14, 3)
    )

    print()

    print(
        "Traffic route:",
        " -> ".join(route17)
    )

    print(
        "Traffic cost:",
        round(cost17, 3)
    )


# ============================================================
# PART 19 - TRAFFIC REROUTING VISUALIZATION
# ============================================================

print()
print("=" * 70)
print("PART 19 - TRAFFIC REROUTING VISUALIZATION")
print("=" * 70)

fig19 = plt.figure(figsize=(12, 8))

pos19 = nx.spring_layout(
    G17,
    seed=42
)

nx.draw(
    G17,
    pos19,
    with_labels=True,
    node_size=700
)

if route17:

    route_edges19 = list(
        zip(
            route17[:-1],
            route17[1:]
        )
    )

    nx.draw_networkx_edges(
        G17,
        pos19,
        edgelist=route_edges19,
        width=4
    )

plt.title(
    "Traffic-Aware QPSO Rerouting"
)

plt.tight_layout()

st.pyplot(fig19)

plt.close(fig19)


# ============================================================
# PART 20 - ROUTE COST COMPARISON
# ============================================================

print()
print("=" * 70)
print("PART 20 - ROUTE COST COMPARISON")
print("=" * 70)

if (
    cost14 != float("inf")
    and cost17 != float("inf")
):

    comparison20 = {
        "Condition": [
            "Normal Traffic",
            "Heavy Traffic"
        ],

        "QPSO Cost": [
            round(cost14, 3),
            round(cost17, 3)
        ]
    }

    st.subheader(
        "Normal vs Traffic-Affected Route"
    )

    st.table(
        comparison20
    )


# ============================================================
# PART 21 - MULTIPLE QPSO RUNS
# ============================================================

print()
print("=" * 70)
print("PART 21 - MULTIPLE QPSO RUNS")
print("=" * 70)

NUM_RUNS21 = 10

results21 = []

for run in range(NUM_RUNS21):

    route21, cost21, convergence21 = (
        qpso_vrp_optimization(
            G17,
            "A",
            delivery_points14,
            particles=30,
            iterations=100
        )
    )

    if cost21 != float("inf"):

        results21.append(
            cost21
        )

        print(
            "Run",
            run + 1,
            ":",
            round(cost21, 3)
        )

        # ============================================================
# PART 22 - STATISTICAL ANALYSIS
# ============================================================

print()
print("=" * 70)
print("PART 22 - STATISTICAL ANALYSIS")
print("=" * 70)

if results21:

    average22 = statistics.mean(
        results21
    )

    best22 = min(
        results21
    )

    worst22 = max(
        results21
    )

    std22 = (
        statistics.stdev(results21)
        if len(results21) > 1
        else 0.0
    )

    print()
    print(
        "Average cost:",
        round(average22, 3)
    )

    print(
        "Best cost:",
        round(best22, 3)
    )

    print(
        "Worst cost:",
        round(worst22, 3)
    )

    print(
        "Standard deviation:",
        round(std22, 3)
    )


# ============================================================
# PART 23 - QPSO RESULT DISTRIBUTION
# ============================================================

print()
print("=" * 70)
print("PART 23 - QPSO RESULT DISTRIBUTION")
print("=" * 70)

if results21:

    fig23 = plt.figure(figsize=(10, 6))

    plt.hist(
        results21,
        bins=8
    )

    plt.xlabel(
        "Objective Cost"
    )

    plt.ylabel(
        "Frequency"
    )

    plt.title(
        "QPSO Objective Cost Distribution"
    )

    plt.grid(True)
    plt.tight_layout()

    st.pyplot(fig23)

    plt.close(fig23)


# ============================================================
# PART 24 - QPSO RUNTIME TEST
# ============================================================

print()
print("=" * 70)
print("PART 24 - QPSO RUNTIME TEST")
print("=" * 70)

runtime_results24 = []

for run in range(10):

    start24 = time.perf_counter()

    _, cost24, _ = (
        qpso_vrp_optimization(
            G17,
            "A",
            delivery_points14,
            particles=30,
            iterations=100
        )
    )

    end24 = time.perf_counter()

    runtime24 = (
        end24 - start24
    )

    if cost24 != float("inf"):

        runtime_results24.append(
            runtime24
        )

        print(
            "Run",
            run + 1,
            "runtime:",
            round(
                runtime24,
                6
            ),
            "seconds"
        )


# ============================================================
# PART 25 - RUNTIME SUMMARY
# ============================================================

print()
print("=" * 70)
print("PART 25 - RUNTIME SUMMARY")
print("=" * 70)

if runtime_results24:

    average_runtime25 = (
        statistics.mean(
            runtime_results24
        )
    )

    fastest_runtime25 = (
        min(runtime_results24)
    )

    slowest_runtime25 = (
        max(runtime_results24)
    )

    print()
    print(
        "Average runtime:",
        round(
            average_runtime25,
            6
        ),
        "seconds"
    )

    print(
        "Fastest runtime:",
        round(
            fastest_runtime25,
            6
        ),
        "seconds"
    )

    print(
        "Slowest runtime:",
        round(
            slowest_runtime25,
            6
        ),
        "seconds"
    )


# ============================================================
# PART 26 - SCALABILITY WITH LARGER NETWORK
# ============================================================

print()
print("=" * 70)
print("PART 26 - SCALABILITY TEST")
print("=" * 70)

sizes26 = [
    10,
    15,
    20,
    25
]

scalability26 = []

for size in sizes26:

    G26 = nx.Graph()

    nodes26 = [
        chr(65 + i)
        for i in range(size)
    ]

    G26.add_nodes_from(
        nodes26
    )

    # Ensure basic connectivity

    for i in range(
        len(nodes26) - 1
    ):

        G26.add_edge(
            nodes26[i],
            nodes26[i + 1],
            weight=random.randint(
                1,
                20
            )
        )

    # Additional random roads

    for _ in range(size * 2):

        u, v = random.sample(
            nodes26,
            2
        )

        G26.add_edge(
            u,
            v,
            weight=random.randint(
                1,
                20
            )
        )

    delivery26 = nodes26[
        1:min(10, size)
    ]

    start26 = time.perf_counter()

    _, cost26, _ = (
        qpso_vrp_optimization(
            G26,
            nodes26[0],
            delivery26,
            particles=20,
            iterations=50
        )
    )

    end26 = time.perf_counter()

    runtime26 = (
        end26 - start26
    )

    scalability26.append({
        "Locations": size,
        "Delivery Points": len(
            delivery26
        ),
        "Cost": round(
            cost26,
            3
        ),
        "Runtime (seconds)": round(
            runtime26,
            6
        )
    })

    print()
    print(
        "Locations:",
        size
    )

    print(
        "Cost:",
        round(
            cost26,
            3
        )
    )

    print(
        "Runtime:",
        round(
            runtime26,
            6
        ),
        "seconds"
    )


# ============================================================
# PART 27 - SCALABILITY TABLE
# ============================================================

print()
print("=" * 70)
print("PART 27 - SCALABILITY TABLE")
print("=" * 70)

st.subheader(
    "QPSO Scalability Analysis"
)

st.table(
    scalability26
)


# ============================================================
# PART 28 - SCALABILITY RUNTIME GRAPH
# ============================================================

print()
print("=" * 70)
print("PART 28 - SCALABILITY RUNTIME GRAPH")
print("=" * 70)

if scalability26:

    sizes28 = [
        item["Locations"]
        for item in scalability26
    ]

    runtimes28 = [
        item["Runtime (seconds)"]
        for item in scalability26
    ]

    fig28 = plt.figure(
        figsize=(10, 6)
    )

    plt.plot(
        sizes28,
        runtimes28,
        marker="o"
    )

    plt.xlabel(
        "Number of Locations"
    )

    plt.ylabel(
        "Runtime (seconds)"
    )

    plt.title(
        "QPSO Scalability - Computation Time"
    )

    plt.grid(True)
    plt.tight_layout()

    st.pyplot(fig28)

    plt.close(fig28)


# ============================================================
# PART 29 - FINAL ROUTE PERFORMANCE DASHBOARD
# ============================================================

print()
print("=" * 70)
print("PART 29 - FINAL ROUTE PERFORMANCE DASHBOARD")
print("=" * 70)

st.subheader(
    "QPSO Route Performance"
)

if route17:

    dashboard_data29 = {
        "Metric": [
            "Optimized Route",
            "Objective Cost",
            "Number of Stops",
            "Computation Time"
        ],

        "Value": [
            " -> ".join(route17),
            round(
                cost17,
                3
            ),
            len(route17) - 2,
            round(
                runtime14,
                6
            )
        ]
    }

    st.table(
        dashboard_data29
    )


# ============================================================
# PART 30 - PROJECT SUMMARY
# ============================================================

print()
print("=" * 70)
print("PART 30 - PROJECT SUMMARY")
print("=" * 70)

print()

print(
    "QuantumRoute uses QPSO for traffic-aware "
    "vehicle route optimization."
)

print()

print(
    "The system models roads as a weighted graph."
)

print()

print(
    "Traffic conditions are represented by "
    "changing road costs."
)

print()

print(
    "QPSO searches for a low-cost delivery route."
)

print()

print(
    "Multiple experiments evaluate convergence, "
    "reliability, runtime and scalability."
)

print()

print(
    "The platform is designed to support "
    "multi-objective transportation optimization."
)

print()

print("=" * 70)
print("PART 30 COMPLETE")
print("=" * 70)

print()

# ============================================================
# PART 31 — MULTI-OBJECTIVE TRAFFIC OPTIMIZATION
# ============================================================

st.header("Part 31 — Multi-Objective Traffic Optimization")

# Create transportation network
G31 = nx.Graph()

edges31 = [
    ("A", "B", 5, 4, 1),
    ("B", "C", 4, 3, 2),
    ("C", "D", 6, 5, 2),
    ("D", "E", 5, 4, 1),
    ("E", "F", 4, 3, 2),

    ("A", "C", 8, 6, 3),
    ("B", "D", 7, 5, 3),
    ("C", "E", 7, 5, 4),
    ("D", "F", 6, 4, 3),

    ("A", "D", 12, 9, 5),
    ("B", "E", 10, 8, 4),
    ("C", "F", 11, 8, 5)
]

for u, v, travel_time, distance, congestion in edges31:
    G31.add_edge(
        u,
        v,
        travel_time=travel_time,
        distance=distance,
        congestion=congestion
    )


# Objective weights
TIME_WEIGHT = 0.50
DISTANCE_WEIGHT = 0.30
CONGESTION_WEIGHT = 0.20


# Calculate combined road weight
for u, v, data in G31.edges(data=True):
    data["weight"] = (
        TIME_WEIGHT * data["travel_time"]
        + DISTANCE_WEIGHT * data["distance"]
        + CONGESTION_WEIGHT * data["congestion"]
    )


# Calculate multi-objective metrics
def calculate_multi_objective_metrics(graph, route):

    total_time = 0
    total_distance = 0
    total_congestion = 0

    for i in range(len(route) - 1):

        start = route[i]
        end = route[i + 1]

        try:

            shortest_path = nx.shortest_path(
                graph,
                start,
                end,
                weight="weight"
            )

            for j in range(len(shortest_path) - 1):

                u = shortest_path[j]
                v = shortest_path[j + 1]

                data = graph[u][v]

                total_time += data["travel_time"]
                total_distance += data["distance"]
                total_congestion += data["congestion"]

        except nx.NetworkXNoPath:

            return (
                float("inf"),
                float("inf"),
                float("inf"),
                float("inf")
            )


    # Combined objective
    objective_score = (
        TIME_WEIGHT * total_time
        + DISTANCE_WEIGHT * total_distance
        + CONGESTION_WEIGHT * total_congestion
    )

    return (
        total_time,
        total_distance,
        total_congestion,
        objective_score
    )


# Depot and delivery points
depot31 = "A"

delivery_points31 = [
    "B",
    "C",
    "D",
    "E",
    "F"
]


# Run QPSO
qpso31_route, qpso31_cost, qpso31_convergence = (
    qpso_vrp_optimization(
        G31,
        depot31,
        delivery_points31,
        particles=40,
        iterations=200
    )
)


# Calculate final metrics
(
    qpso31_time,
    qpso31_distance,
    qpso31_congestion,
    qpso31_objective
) = calculate_multi_objective_metrics(
    G31,
    qpso31_route
)


# Display results
st.subheader("QPSO Multi-Objective Result")

st.write(
    "Best Route:",
    " → ".join(qpso31_route)
)

st.write(
    "Travel Time:",
    qpso31_time
)

st.write(
    "Distance:",
    qpso31_distance
)

st.write(
    "Congestion Score:",
    qpso31_congestion
)

st.write(
    "Combined Objective:",
    round(qpso31_objective, 2)
)


st.success("PART 31 COMPLETE")


# ============================================================
# PART 32 — QPSO PERFORMANCE VISUALIZATION
# ============================================================

st.header("Part 32 — QPSO Performance Visualization")

# ------------------------------------------------------------
# Run QPSO
# ------------------------------------------------------------

part32_route, part32_cost, part32_convergence = (
    qpso_vrp_optimization(
        G31,
        "A",
        ["B", "C", "D", "E", "F"],
        particles=30,
        iterations=100
    )
)


# ------------------------------------------------------------
# Display optimized route
# ------------------------------------------------------------

st.subheader("Optimized Route")

st.write(
    " → ".join(part32_route)
)

st.write(
    "Best Objective Cost:",
    round(part32_cost, 2)
)


# ------------------------------------------------------------
# QPSO convergence graph
# ------------------------------------------------------------

fig32, ax32 = plt.subplots()

ax32.plot(
    range(1, len(part32_convergence) + 1),
    part32_convergence,
    label="QPSO"
)

ax32.set_title(
    "QPSO Convergence"
)

ax32.set_xlabel(
    "Iteration"
)

ax32.set_ylabel(
    "Best Objective Cost"
)

ax32.legend()

ax32.grid(True)

st.pyplot(fig32)


# ------------------------------------------------------------
# Explanation
# ------------------------------------------------------------

st.info(
    "The convergence graph shows how the best objective "
    "cost changes as QPSO performs more iterations."
)


# ============================================================
# END OF PART 32
# ============================================================

st.success("PART 32 COMPLETE")

# ============================================================
# PART 33 — QPSO CONVERGENCE METRICS
# ============================================================

st.header("Part 33 — QPSO Convergence Metrics")


# ------------------------------------------------------------
# Get convergence values from Part 32
# ------------------------------------------------------------

initial_cost33 = part32_convergence[0]

final_cost33 = part32_convergence[-1]

best_cost33 = min(
    part32_convergence
)


# ------------------------------------------------------------
# Calculate improvement percentage
# ------------------------------------------------------------

if initial_cost33 != 0:

    improvement33 = (
        (initial_cost33 - best_cost33)
        / initial_cost33
    ) * 100

else:

    improvement33 = 0.0


# ------------------------------------------------------------
# Number of iterations
# ------------------------------------------------------------

iterations33 = len(
    part32_convergence
)


# ------------------------------------------------------------
# Display metrics
# ------------------------------------------------------------

st.subheader(
    "Optimization Performance"
)

st.write(
    "Initial Objective:",
    round(initial_cost33, 2)
)

st.write(
    "Final Objective:",
    round(final_cost33, 2)
)

st.write(
    "Best Objective:",
    round(best_cost33, 2)
)

st.write(
    "Improvement:",
    round(improvement33, 2),
    "%"
)

st.write(
    "Iterations:",
    iterations33
)


# ------------------------------------------------------------
# Interpretation
# ------------------------------------------------------------

if best_cost33 < initial_cost33:

    st.success(
        "QPSO improved the objective value "
        "during the optimization process."
    )

elif best_cost33 == initial_cost33:

    st.info(
        "QPSO reached its best solution early "
        "and maintained the same objective value."
    )

else:

    st.warning(
        "The best objective value was not lower "
        "than the initial objective value."
    )


# ============================================================
# END OF PART 33
# ============================================================

st.success("PART 33 COMPLETE")

# ============================================================
# PART 34 — QPSO PERFORMANCE SUMMARY
# ============================================================

st.header("Part 34 — QPSO Performance Summary")


# ------------------------------------------------------------
# Create performance summary
# ------------------------------------------------------------

summary34 = {
    "Metric": [
        "Initial Objective",
        "Final Objective",
        "Best Objective",
        "Improvement (%)",
        "Iterations"
    ],

    "Value": [
        round(initial_cost33, 2),
        round(final_cost33, 2),
        round(best_cost33, 2),
        round(improvement33, 2),
        iterations33
    ]
}


# ------------------------------------------------------------
# Display summary table
# ------------------------------------------------------------

st.subheader("QPSO Performance Summary")

st.table(summary34)


# ------------------------------------------------------------
# Display optimized route
# ------------------------------------------------------------

st.subheader("Optimized Route")

st.write(
    " → ".join(part32_route)
)


# ------------------------------------------------------------
# Display objective cost
# ------------------------------------------------------------

st.write(
    "Best Objective Cost:",
    round(part32_cost, 2)
)


# ------------------------------------------------------------
# Explanation
# ------------------------------------------------------------

st.info(
    "This table summarizes the main performance metrics "
    "obtained during the QPSO optimization experiment."
)


# ============================================================
# END OF PART 34
# ============================================================

st.success("PART 34 COMPLETE")

# ============================================================
# PART 35 — QPSO RELIABILITY TEST
# ============================================================

st.header("Part 35 — QPSO Reliability Test")


# ------------------------------------------------------------
# Reliability experiment settings
# ------------------------------------------------------------

NUM_RELIABILITY_RUNS = 10

reliability_results35 = []

reliability_routes35 = []


# ------------------------------------------------------------
# Run QPSO multiple times
# ------------------------------------------------------------

for run in range(NUM_RELIABILITY_RUNS):

    route35, cost35, convergence35 = (
        qpso_vrp_optimization(
            G31,
            "A",
            ["B", "C", "D", "E", "F"],
            particles=30,
            iterations=100
        )
    )

    reliability_results35.append(
        cost35
    )

    reliability_routes35.append(
        route35
    )


# ------------------------------------------------------------
# Keep only valid results
# ------------------------------------------------------------

valid_results35 = [
    value
    for value in reliability_results35
    if math.isfinite(value)
]


# ------------------------------------------------------------
# Calculate statistics
# ------------------------------------------------------------

if valid_results35:

    average35 = statistics.mean(
        valid_results35
    )

    best35 = min(
        valid_results35
    )

    worst35 = max(
        valid_results35
    )

else:

    average35 = float("inf")
    best35 = float("inf")
    worst35 = float("inf")


# ------------------------------------------------------------
# Display summary
# ------------------------------------------------------------

st.subheader(
    "Reliability Summary"
)

st.write(
    "Number of Runs:",
    NUM_RELIABILITY_RUNS
)

st.write(
    "Valid Runs:",
    len(valid_results35)
)

if valid_results35:

    st.write(
        "Average Objective:",
        round(average35, 2)
    )

    st.write(
        "Best Objective:",
        round(best35, 2)
    )

    st.write(
        "Worst Objective:",
        round(worst35, 2)
    )


# ------------------------------------------------------------
# Display individual runs
# ------------------------------------------------------------

st.subheader(
    "Individual QPSO Runs"
)

for i, value in enumerate(
    reliability_results35,
    start=1
):

    if math.isfinite(value):

        st.write(
            f"Run {i}: {value:.2f}"
        )

    else:

        st.write(
            f"Run {i}: Invalid"
        )


# ------------------------------------------------------------
# Reliability interpretation
# ------------------------------------------------------------

if len(valid_results35) == NUM_RELIABILITY_RUNS:

    st.success(
        "All QPSO runs produced valid solutions."
    )

elif len(valid_results35) > 0:

    st.warning(
        "Some QPSO runs produced invalid solutions."
    )

else:

    st.error(
        "No valid QPSO solutions were produced."
    )


# ============================================================
# END OF PART 35
# ============================================================

st.success(
    "PART 35 COMPLETE"
)

# ============================================================
# PART 36 — QPSO VS CLASSICAL PSO COMPARISON
# ============================================================

st.header("Part 36 — QPSO vs Classical PSO Comparison")


# ------------------------------------------------------------
# EXPERIMENT SETTINGS
# ------------------------------------------------------------

NUM_COMPARISON_RUNS = 10
COMPARISON_PARTICLES = 30
COMPARISON_ITERATIONS = 100


qpso_comparison_results36 = []
pso_comparison_results36 = []

qpso_runtime_results36 = []
pso_runtime_results36 = []


# ------------------------------------------------------------
# RUN BOTH ALGORITHMS
# ------------------------------------------------------------

for run in range(NUM_COMPARISON_RUNS):

    # --------------------------------------------------------
    # QPSO
    # --------------------------------------------------------

    start_qpso36 = time.perf_counter()

    qpso_route36, qpso_cost36, qpso_conv36 = (
        qpso_vrp_optimization(
            G31,
            "A",
            ["B", "C", "D", "E", "F"],
            particles=COMPARISON_PARTICLES,
            iterations=COMPARISON_ITERATIONS
        )
    )

    end_qpso36 = time.perf_counter()

    qpso_runtime36 = (
        end_qpso36 - start_qpso36
    )


    # --------------------------------------------------------
    # CLASSICAL PSO-STYLE BASELINE
    # --------------------------------------------------------

    start_pso36 = time.perf_counter()

    pso_route36, pso_cost36, pso_conv36 = (
        pso_vrp_optimization(
            G31,
            "A",
            ["B", "C", "D", "E", "F"],
            particles=COMPARISON_PARTICLES,
            iterations=COMPARISON_ITERATIONS
        )
    )

    end_pso36 = time.perf_counter()

    pso_runtime36 = (
        end_pso36 - start_pso36
    )


    # --------------------------------------------------------
    # STORE VALID RESULTS
    # --------------------------------------------------------

    if math.isfinite(qpso_cost36):

        qpso_comparison_results36.append(
            qpso_cost36
        )

        qpso_runtime_results36.append(
            qpso_runtime36
        )


    if math.isfinite(pso_cost36):

        pso_comparison_results36.append(
            pso_cost36
        )

        pso_runtime_results36.append(
            pso_runtime36
        )


# ============================================================
# CALCULATE STATISTICS
# ============================================================

if (
    qpso_comparison_results36
    and pso_comparison_results36
):

    avg_qpso36 = statistics.mean(
        qpso_comparison_results36
    )

    avg_pso36 = statistics.mean(
        pso_comparison_results36
    )

    best_qpso36 = min(
        qpso_comparison_results36
    )

    best_pso36 = min(
        pso_comparison_results36
    )

    avg_qpso_runtime36 = statistics.mean(
        qpso_runtime_results36
    )

    avg_pso_runtime36 = statistics.mean(
        pso_runtime_results36
    )


    # --------------------------------------------------------
    # IMPROVEMENT
    # --------------------------------------------------------

    if avg_pso36 > 0:

        improvement36 = (
            (avg_pso36 - avg_qpso36)
            / avg_pso36
        ) * 100

    else:

        improvement36 = 0.0


    # --------------------------------------------------------
    # COMPARISON TABLE
    # --------------------------------------------------------

    st.subheader(
        "Comparison Results"
    )

    comparison_rows36 = [

        {
            "Metric": "Average Objective",
            "QPSO": f"{avg_qpso36:.4f}",
            "Classical PSO-style": f"{avg_pso36:.4f}"
        },

        {
            "Metric": "Best Objective",
            "QPSO": f"{best_qpso36:.4f}",
            "Classical PSO-style": f"{best_pso36:.4f}"
        },

        {
            "Metric": "Average Runtime (seconds)",
            "QPSO": f"{avg_qpso_runtime36:.4f}",
            "Classical PSO-style": f"{avg_pso_runtime36:.4f}"
        },

        {
            "Metric": "Improvement (%)",
            "QPSO": f"{improvement36:.2f}",
            "Classical PSO-style": "Baseline"
        }
    ]


    # Convert everything to text
    # so Streamlit does not try to mix numbers and strings.

    comparison_df36 = pd.DataFrame(
        comparison_rows36,
        dtype=str
    )

    st.dataframe(
        comparison_df36,
        width="stretch",
        hide_index=True
    )


    # --------------------------------------------------------
    # INTERPRETATION
    # --------------------------------------------------------

    if abs(improvement36) < 0.0001:

        st.info(
            "QPSO and the Classical PSO-style baseline "
            "achieved essentially the same average "
            "objective cost in this experiment."
        )

    elif improvement36 > 0:

        st.success(
            f"QPSO achieved {improvement36:.2f}% "
            "lower average objective cost than the "
            "Classical PSO-style baseline."
        )

    else:

        st.warning(
            f"QPSO produced a {abs(improvement36):.2f}% "
            "higher average objective cost than the "
            "Classical PSO-style baseline."
        )


    # --------------------------------------------------------
    # RUNTIME COMPARISON
    # --------------------------------------------------------

    st.subheader(
        "Average Runtime Comparison"
    )

    st.write(
        f"QPSO Runtime: "
        f"{avg_qpso_runtime36:.4f} seconds"
    )

    st.write(
        f"Classical PSO-style Runtime: "
        f"{avg_pso_runtime36:.4f} seconds"
    )


    # --------------------------------------------------------
    # VALID RUNS
    # --------------------------------------------------------

    st.write(
        f"Valid QPSO Runs: "
        f"{len(qpso_comparison_results36)} / "
        f"{NUM_COMPARISON_RUNS}"
    )

    st.write(
        f"Valid Classical PSO-style Runs: "
        f"{len(pso_comparison_results36)} / "
        f"{NUM_COMPARISON_RUNS}"
    )


else:

    st.error(
        "Comparison could not be completed because "
        "one or both algorithms produced no valid results."
    )


# ============================================================
# END OF PART 36
# ============================================================

st.success("PART 36 COMPLETE")

# ============================================================
# PART 37 — RUNTIME & EFFICIENCY VISUALIZATION
# ============================================================

st.header("Part 37 — Runtime & Efficiency Visualization")

st.subheader("Algorithm Runtime Comparison")


# ------------------------------------------------------------
# RUNTIME DATA
# ------------------------------------------------------------

runtime_labels37 = [
    "QPSO",
    "Classical PSO-style"
]

runtime_values37 = [
    avg_qpso_runtime36,
    avg_pso_runtime36
]


# ------------------------------------------------------------
# CREATE BAR CHART
# ------------------------------------------------------------

fig37, ax37 = plt.subplots(
    figsize=(8, 5)
)

ax37.bar(
    runtime_labels37,
    runtime_values37
)

ax37.set_title(
    "Average Runtime Comparison"
)

ax37.set_ylabel(
    "Runtime (seconds)"
)

ax37.set_xlabel(
    "Optimization Algorithm"
)

ax37.grid(
    axis="y",
    alpha=0.3
)


# ------------------------------------------------------------
# DISPLAY CHART
# ------------------------------------------------------------

st.pyplot(
    fig37
)

plt.close(
    fig37
)


# ------------------------------------------------------------
# RUNTIME VALUES
# ------------------------------------------------------------

st.subheader(
    "Runtime Results"
)

st.write(
    f"QPSO average runtime: "
    f"{avg_qpso_runtime36:.4f} seconds"
)

st.write(
    f"Classical PSO-style average runtime: "
    f"{avg_pso_runtime36:.4f} seconds"
)


# ------------------------------------------------------------
# EFFICIENCY INTERPRETATION
# ------------------------------------------------------------

if avg_qpso_runtime36 < avg_pso_runtime36:

    runtime_difference37 = (
        avg_pso_runtime36
        - avg_qpso_runtime36
    )

    runtime_percentage37 = (
        runtime_difference37
        / avg_pso_runtime36
    ) * 100

    st.success(
        f"QPSO was approximately "
        f"{runtime_percentage37:.2f}% faster "
        f"than the Classical PSO-style baseline "
        f"in this experiment."
    )

elif avg_qpso_runtime36 > avg_pso_runtime36:

    runtime_difference37 = (
        avg_qpso_runtime36
        - avg_pso_runtime36
    )

    runtime_percentage37 = (
        runtime_difference37
        / avg_qpso_runtime36
    ) * 100

    st.warning(
        f"The Classical PSO-style baseline was "
        f"approximately "
        f"{runtime_percentage37:.2f}% faster "
        f"than QPSO in this experiment."
    )

else:

    st.info(
        "Both algorithms had essentially the same "
        "runtime in this experiment."
    )


# ------------------------------------------------------------
# EXPLANATION
# ------------------------------------------------------------

st.info(
    "Runtime is measured on the same computer using "
    "the same number of particles and iterations. "
    "This provides an experimental comparison of "
    "computational efficiency."
)


# ============================================================
# END OF PART 37
# ============================================================

st.success("PART 37 COMPLETE")

# ============================================================
# PART 38 — OBJECTIVE COST COMPARISON
# ============================================================

st.header("Part 38 — Objective Cost Comparison")

st.subheader("Average and Best Objective Cost")


# ------------------------------------------------------------
# OBJECTIVE DATA
# ------------------------------------------------------------

objective_labels38 = [
    "QPSO",
    "Classical PSO-style"
]

average_objective38 = [
    avg_qpso36,
    avg_pso36
]

best_objective38 = [
    best_qpso36,
    best_pso36
]


# ------------------------------------------------------------
# CREATE AVERAGE OBJECTIVE CHART
# ------------------------------------------------------------

fig38, ax38 = plt.subplots(
    figsize=(8, 5)
)

x38 = range(
    len(objective_labels38)
)

ax38.bar(
    x38,
    average_objective38
)

ax38.set_xticks(
    list(x38)
)

ax38.set_xticklabels(
    objective_labels38
)

ax38.set_title(
    "Average Objective Cost Comparison"
)

ax38.set_xlabel(
    "Optimization Algorithm"
)

ax38.set_ylabel(
    "Average Objective Cost"
)

ax38.grid(
    axis="y",
    alpha=0.3
)


# ------------------------------------------------------------
# DISPLAY CHART
# ------------------------------------------------------------

st.pyplot(
    fig38
)

plt.close(
    fig38
)


# ------------------------------------------------------------
# NUMERICAL RESULTS
# ------------------------------------------------------------

st.subheader(
    "Objective Cost Results"
)

st.write(
    f"QPSO average objective: "
    f"{avg_qpso36:.4f}"
)

st.write(
    f"Classical PSO-style average objective: "
    f"{avg_pso36:.4f}"
)

st.write(
    f"QPSO best objective: "
    f"{best_qpso36:.4f}"
)

st.write(
    f"Classical PSO-style best objective: "
    f"{best_pso36:.4f}"
)


# ------------------------------------------------------------
# INTERPRETATION
# ------------------------------------------------------------

if avg_qpso36 < avg_pso36:

    st.success(
        "QPSO achieved a lower average objective "
        "cost than the Classical PSO-style baseline "
        "in this experiment."
    )

elif avg_qpso36 > avg_pso36:

    st.warning(
        "The Classical PSO-style baseline achieved "
        "a lower average objective cost than QPSO "
        "in this experiment."
    )

else:

    st.info(
        "QPSO and the Classical PSO-style baseline "
        "achieved the same average objective cost "
        "in this experiment."
    )


# ------------------------------------------------------------
# BEST-SOLUTION COMPARISON
# ------------------------------------------------------------

if best_qpso36 < best_pso36:

    st.success(
        "QPSO found the better best solution "
        "in this experiment."
    )

elif best_qpso36 > best_pso36:

    st.warning(
        "The Classical PSO-style baseline found "
        "the better best solution in this experiment."
    )

else:

    st.info(
        "Both algorithms found the same best "
        "objective value in this experiment."
    )


# ------------------------------------------------------------
# EXPLANATION
# ------------------------------------------------------------

st.info(
    "Objective cost represents the total route cost "
    "used by the optimization model. Lower values "
    "represent better solutions."
)


# ============================================================
# END OF PART 38
# ============================================================

st.success("PART 38 COMPLETE")

# ============================================================
# PART 39 — SCALABILITY PERFORMANCE VISUALIZATION
# ============================================================

st.header("Part 39 — Scalability Performance Visualization")

st.subheader("QPSO Scalability Analysis")

st.write(
    "This experiment evaluates how QPSO performance changes "
    "as the number of delivery locations increases."
)


# ------------------------------------------------------------
# SCALABILITY DATA
# ------------------------------------------------------------

scalability_sizes39 = [10, 15, 20, 25]

scalability_costs39 = []
scalability_runtimes39 = []


# ------------------------------------------------------------
# RUN SCALABILITY EXPERIMENT
# ------------------------------------------------------------

for size39 in scalability_sizes39:

    G39 = nx.Graph()

    nodes39 = [
        chr(65 + i)
        for i in range(size39)
    ]

    # Main road chain
    for i in range(size39 - 1):

        G39.add_edge(
            nodes39[i],
            nodes39[i + 1],
            weight=random.randint(2, 10)
        )

    # Additional roads
    for _ in range(size39 * 2):

        u39, v39 = random.sample(
            nodes39,
            2
        )

        if not G39.has_edge(u39, v39):

            G39.add_edge(
                u39,
                v39,
                weight=random.randint(2, 15)
            )

    depot39 = nodes39[0]

    delivery_points39 = nodes39[
        1:min(11, size39)
    ]

    start_time39 = time.time()

    route39, cost39, convergence39 = (
        qpso_vrp_optimization(
            G39,
            depot39,
            delivery_points39,
            particles=20,
            iterations=50
        )
    )

    runtime39 = time.time() - start_time39

    scalability_costs39.append(
        cost39
    )

    scalability_runtimes39.append(
        runtime39
    )


# ------------------------------------------------------------
# SCALABILITY TABLE
# ------------------------------------------------------------

scalability_table39 = pd.DataFrame(
    {
        "Delivery Locations": scalability_sizes39,
        "Objective Cost": scalability_costs39,
        "Runtime (seconds)": scalability_runtimes39
    }
)

st.dataframe(
    scalability_table39,
    width="stretch"
)


# ------------------------------------------------------------
# OBJECTIVE COST GRAPH
# ------------------------------------------------------------

fig39_cost, ax39_cost = plt.subplots(
    figsize=(8, 5)
)

ax39_cost.plot(
    scalability_sizes39,
    scalability_costs39,
    marker="o"
)

ax39_cost.set_title(
    "QPSO Objective Cost vs Problem Size"
)

ax39_cost.set_xlabel(
    "Number of Delivery Locations"
)

ax39_cost.set_ylabel(
    "Objective Cost"
)

ax39_cost.grid(
    True,
    alpha=0.3
)

st.pyplot(
    fig39_cost
)

plt.close(
    fig39_cost
)


# ------------------------------------------------------------
# RUNTIME GRAPH
# ------------------------------------------------------------

fig39_runtime, ax39_runtime = plt.subplots(
    figsize=(8, 5)
)

ax39_runtime.plot(
    scalability_sizes39,
    scalability_runtimes39,
    marker="o"
)

ax39_runtime.set_title(
    "QPSO Runtime vs Problem Size"
)

ax39_runtime.set_xlabel(
    "Number of Delivery Locations"
)

ax39_runtime.set_ylabel(
    "Runtime (seconds)"
)

ax39_runtime.grid(
    True,
    alpha=0.3
)

st.pyplot(
    fig39_runtime
)

plt.close(
    fig39_runtime
)


# ------------------------------------------------------------
# INTERPRETATION
# ------------------------------------------------------------

st.info(
    "As the number of delivery locations increases, "
    "the optimization problem becomes more complex. "
    "The scalability experiment measures how QPSO "
    "handles increasing problem size."
)


# ============================================================
# END OF PART 39
# ============================================================

st.success("PART 39 COMPLETE")

# ============================================================
# PART 40 — FINAL PROJECT DASHBOARD & CONCLUSION
# ============================================================

st.header("Part 40 — Final Project Dashboard")

st.subheader("Quantum-Inspired Intelligent Traffic Route Optimization")

st.write(
    "This final dashboard summarizes the complete experimental "
    "prototype developed for intelligent traffic route optimization "
    "using Quantum Particle Swarm Optimization (QPSO)."
)


# ------------------------------------------------------------
# PROJECT OVERVIEW
# ------------------------------------------------------------

st.subheader("Project Overview")

st.write(
    "The system models a transportation network as a weighted graph. "
    "Roads are represented as edges and locations as nodes. "
    "Traffic conditions are represented by changing road costs. "
    "QPSO searches for a low-cost delivery route."
)


# ------------------------------------------------------------
# MAIN FEATURES
# ------------------------------------------------------------

st.subheader("Implemented Features")

features40 = [
    "Road network graph modeling",
    "Shortest-path route calculation",
    "Traffic congestion simulation",
    "Vehicle routing optimization",
    "Quantum Particle Swarm Optimization (QPSO)",
    "Classical PSO-style baseline comparison",
    "QPSO convergence analysis",
    "Reliability testing using multiple runs",
    "Runtime benchmarking",
    "Scalability testing",
    "Multi-objective route evaluation",
    "Interactive Streamlit dashboard"
]

for feature40 in features40:
    st.write("✓", feature40)


# ------------------------------------------------------------
# FINAL OPTIMIZED ROUTE
# ------------------------------------------------------------

st.subheader("Final Optimized Route")

try:

    st.write(
        " → ".join(
            str(node)
            for node in part32_route
        )
    )

    st.metric(
        "Best Objective Cost",
        f"{part32_cost:.2f}"
    )

except Exception:

    st.info(
        "The final route result is available from the "
        "QPSO optimization experiments."
    )


# ------------------------------------------------------------
# EXPERIMENTAL RESULTS
# ------------------------------------------------------------

st.subheader("Experimental Results")

try:

    initial40 = part32_convergence[0]
    final40 = part32_convergence[-1]
    best40 = min(part32_convergence)

    if initial40 != 0:

        improvement40 = (
            (initial40 - best40)
            / initial40
        ) * 100

    else:

        improvement40 = 0

    final_results40 = pd.DataFrame(
        {
            "Metric": [
                "Initial Objective",
                "Final Objective",
                "Best Objective",
                "Improvement (%)",
                "Iterations"
            ],
            "Value": [
                round(initial40, 4),
                round(final40, 4),
                round(best40, 4),
                round(improvement40, 2),
                len(part32_convergence)
            ]
        }
    )

    st.dataframe(
        final_results40,
        width="stretch"
    )

except Exception as e:

    st.warning(
        f"Experimental summary could not be displayed: {e}"
    )


# ------------------------------------------------------------
# RELIABILITY
# ------------------------------------------------------------

st.subheader("Reliability")

try:

    st.write(
        f"QPSO reliability experiment completed with "
        f"{len(results21)} recorded optimization results."
    )

    st.write(
        "Multiple independent runs were used to examine "
        "whether QPSO can repeatedly produce valid solutions."
    )

except Exception:

    st.write(
        "Multiple independent QPSO runs were used to "
        "evaluate solution reliability."
    )


# ------------------------------------------------------------
# COMPARISON WITH CLASSICAL BASELINE
# ------------------------------------------------------------

st.subheader("Algorithm Comparison")

st.write(
    "The prototype compares QPSO with a Classical PSO-style "
    "baseline using objective cost and runtime measurements."
)

st.info(
    "The experimental results should be interpreted as "
    "benchmark results for this prototype. QPSO is not "
    "assumed to outperform the classical baseline in every "
    "experiment."
)


# ------------------------------------------------------------
# SCALABILITY
# ------------------------------------------------------------

st.subheader("Scalability")

st.write(
    "The scalability experiment evaluates QPSO on increasing "
    "numbers of delivery locations. This demonstrates how "
    "the optimization system behaves as the transportation "
    "problem becomes larger."
)


# ------------------------------------------------------------
# TECHNOLOGY STACK
# ------------------------------------------------------------

st.subheader("Technology Stack")

technology40 = pd.DataFrame(
    {
        "Component": [
            "Programming Language",
            "Optimization",
            "Graph Modeling",
            "Data Analysis",
            "Visualization",
            "Dashboard"
        ],
        "Technology": [
            "Python",
            "QPSO",
            "NetworkX",
            "Pandas",
            "Matplotlib",
            "Streamlit"
        ]
    }
)

st.dataframe(
    technology40,
    width="stretch"
)


# ------------------------------------------------------------
# PROJECT CONCLUSION
# ------------------------------------------------------------

st.subheader("Conclusion")

st.success(
    "The prototype demonstrates how a quantum-inspired "
    "optimization approach can be implemented on a classical "
    "computer for intelligent transportation route optimization."
)

st.write(
    "The system combines graph-based transportation modeling, "
    "traffic-aware route costs, QPSO optimization, convergence "
    "analysis, reliability testing, runtime benchmarking, "
    "algorithm comparison and scalability evaluation."
)

st.write(
    "The framework can be extended in future work by using "
    "real-time traffic data, larger road networks, multiple "
    "vehicles, time-window constraints and more advanced "
    "multi-objective optimization techniques."
)


# ------------------------------------------------------------
# SMART INDIA HACKATHON CONNECTION
# ------------------------------------------------------------

st.subheader("Problem Statement Alignment")

st.write(
    "This prototype addresses the main objectives of the "
    "transportation optimization problem by modeling road "
    "networks, optimizing delivery routes, incorporating "
    "traffic-related costs, analyzing convergence and "
    "benchmarking the optimization approach."
)


# ------------------------------------------------------------
# FINAL MESSAGE
# ------------------------------------------------------------

st.markdown("---")

st.success(
    "QUANTUM-INSPIRED INTELLIGENT TRAFFIC ROUTE OPTIMIZATION "
    "PROTOTYPE COMPLETE"
)

st.info(
    "The complete 40-part experimental prototype has now "
    "been implemented in Streamlit."
)


# ============================================================
# END OF PART 40
# ============================================================

st.success("PART 40 COMPLETE")

# ============================================================
# PART 41 — INTERACTIVE TRAFFIC OPTIMIZATION DASHBOARD
# ============================================================

st.divider()

st.header("🚦 Part 41 — Interactive Traffic Route Optimization")

st.write(
    "Use the controls below to simulate traffic conditions and "
    "run QPSO route optimization interactively."
)

# ------------------------------------------------------------
# USER CONTROLS
# ------------------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    traffic_level41 = st.selectbox(
        "🚦 Traffic Condition",
        ["Normal", "Moderate", "Heavy"]
    )

with col2:
    delivery_count41 = st.slider(
        "📍 Number of Delivery Locations",
        min_value=2,
        max_value=5,
        value=5
    )

st.write("")

run_optimization41 = st.button(
    "▶️ Run QPSO Optimization",
    use_container_width=True
)

# ------------------------------------------------------------
# RUN OPTIMIZATION
# ------------------------------------------------------------

if run_optimization41:

    # Create a fresh copy so previous experiments are not changed
    demo_graph41 = G31.copy()

    # Traffic multiplier
    if traffic_level41 == "Normal":
        traffic_multiplier41 = 1.0
    elif traffic_level41 == "Moderate":
        traffic_multiplier41 = 1.5
    else:
        traffic_multiplier41 = 2.5

    # Apply traffic to the road network
    for u, v, data in demo_graph41.edges(data=True):

        base_time41 = data.get("travel_time", 1)
        distance41 = data.get("distance", 1)
        congestion41 = data.get("congestion", 1)

        traffic_time41 = base_time41 * traffic_multiplier41

        data["weight"] = (
            TIME_WEIGHT * traffic_time41
            + DISTANCE_WEIGHT * distance41
            + CONGESTION_WEIGHT * congestion41
        )

    # Select delivery locations
    available_locations41 = ["B", "C", "D", "E", "F"]

    delivery_points41 = available_locations41[:delivery_count41]

    # Start timer
    start_time41 = time.time()

    # Run QPSO
    route41, cost41, convergence41 = qpso_vrp_optimization(
        demo_graph41,
        "A",
        delivery_points41,
        particles=30,
        iterations=100
    )

    runtime41 = time.time() - start_time41

    # --------------------------------------------------------
    # RESULTS
    # --------------------------------------------------------

    st.subheader("📊 Optimization Results")

    result_col1, result_col2, result_col3 = st.columns(3)

    with result_col1:
        st.metric(
            "Traffic Level",
            traffic_level41
        )

    with result_col2:
        st.metric(
            "Objective Cost",
            f"{cost41:.2f}"
        )

    with result_col3:
        st.metric(
            "Runtime",
            f"{runtime41:.4f} s"
        )

    st.write("### 🚚 Optimized Delivery Route")

    st.success(
        " → ".join(route41)
    )

    # --------------------------------------------------------
    # CONVERGENCE GRAPH
    # --------------------------------------------------------

    st.write("### 📉 QPSO Convergence")

    fig41, ax41 = plt.subplots()

    ax41.plot(
        range(1, len(convergence41) + 1),
        convergence41,
        label="QPSO"
    )

    ax41.set_xlabel("Iteration")
    ax41.set_ylabel("Objective Cost")
    ax41.set_title("QPSO Convergence Under " + traffic_level41 + " Traffic")
    ax41.grid(True)
    ax41.legend()

    st.pyplot(fig41)

    # --------------------------------------------------------
    # TRAFFIC EXPLANATION
    # --------------------------------------------------------

    if traffic_level41 == "Normal":

        st.info(
            "Normal traffic: road costs remain close to their "
            "base values, so the optimizer searches through "
            "the normal transportation network."
        )

    elif traffic_level41 == "Moderate":

        st.warning(
            "Moderate traffic: travel-time costs increase. "
            "QPSO searches for a lower-cost delivery sequence "
            "under the changed traffic conditions."
        )

    else:

        st.error(
            "Heavy traffic: travel-time costs increase significantly. "
            "The optimization problem becomes more expensive, "
            "and QPSO searches for an alternative low-cost route."
        )

    st.info(
        "This interactive experiment demonstrates how changing "
        "traffic conditions changes the optimization environment."
    )

st.success("PART 41 COMPLETE")

# ============================================================
# PART 42 — INTERACTIVE QPSO VS CLASSICAL PSO COMPARISON
# ============================================================

st.divider()

st.header("⚖️ Part 42 — Interactive Algorithm Comparison")

st.write(
    "This experiment compares QPSO with the Classical PSO-style "
    "baseline under the same traffic conditions and problem size."
)

# ------------------------------------------------------------
# USER CONTROLS
# ------------------------------------------------------------

col1_42, col2_42 = st.columns(2)

with col1_42:
    traffic_level42 = st.selectbox(
        "🚦 Traffic Condition",
        ["Normal", "Moderate", "Heavy"],
        key="traffic_level42"
    )

with col2_42:
    delivery_count42 = st.slider(
        "📍 Delivery Locations",
        min_value=2,
        max_value=5,
        value=5,
        key="delivery_count42"
    )

run_comparison42 = st.button(
    "▶️ Compare QPSO and Classical PSO",
    use_container_width=True
)

# ------------------------------------------------------------
# RUN COMPARISON
# ------------------------------------------------------------

if run_comparison42:

    # Create independent graph copies
    graph_qpso42 = G31.copy()
    graph_pso42 = G31.copy()

    # Traffic multiplier
    if traffic_level42 == "Normal":
        multiplier42 = 1.0
    elif traffic_level42 == "Moderate":
        multiplier42 = 1.5
    else:
        multiplier42 = 2.5

    # Apply the same traffic condition to both algorithms
    for graph42 in [graph_qpso42, graph_pso42]:

        for u, v, data in graph42.edges(data=True):

            travel_time42 = data.get("travel_time", 1)
            distance42 = data.get("distance", 1)
            congestion42 = data.get("congestion", 1)

            adjusted_time42 = travel_time42 * multiplier42

            data["weight"] = (
                TIME_WEIGHT * adjusted_time42
                + DISTANCE_WEIGHT * distance42
                + CONGESTION_WEIGHT * congestion42
            )

    # Delivery locations
    locations42 = ["B", "C", "D", "E", "F"]

    delivery_points42 = locations42[:delivery_count42]

    # --------------------------------------------------------
    # QPSO
    # --------------------------------------------------------

    start_qpso42 = time.time()

    qpso_route42, qpso_cost42, qpso_conv42 = qpso_vrp_optimization(
        graph_qpso42,
        "A",
        delivery_points42,
        particles=30,
        iterations=100
    )

    qpso_runtime42 = time.time() - start_qpso42

    # --------------------------------------------------------
    # CLASSICAL PSO-STYLE
    # --------------------------------------------------------

    start_pso42 = time.time()

    pso_route42, pso_cost42, pso_conv42 = pso_vrp_optimization(
        graph_pso42,
        "A",
        delivery_points42,
        particles=30,
        iterations=100
    )

    pso_runtime42 = time.time() - start_pso42

    # --------------------------------------------------------
    # RESULTS
    # --------------------------------------------------------

    st.subheader("📊 Comparison Results")

    result42 = pd.DataFrame({
        "Metric": [
            "Objective Cost",
            "Runtime (seconds)",
            "Delivery Locations"
        ],
        "QPSO": [
            round(qpso_cost42, 4),
            round(qpso_runtime42, 4),
            delivery_count42
        ],
        "Classical PSO-style": [
            round(pso_cost42, 4),
            round(pso_runtime42, 4),
            delivery_count42
        ]
    })

    st.dataframe(
        result42,
        use_container_width=True
    )

    # --------------------------------------------------------
    # ROUTES
    # --------------------------------------------------------

    st.subheader("🚚 Optimized Routes")

    route_col1, route_col2 = st.columns(2)

    with route_col1:

        st.write("### 🟣 QPSO Route")

        st.success(
            " → ".join(qpso_route42)
        )

    with route_col2:

        st.write("### 🔵 Classical PSO-style Route")

        st.info(
            " → ".join(pso_route42)
        )

    # --------------------------------------------------------
    # OBJECTIVE COST GRAPH
    # --------------------------------------------------------

    st.subheader("📈 Objective Cost Comparison")

    fig42, ax42 = plt.subplots()

    algorithms42 = [
        "QPSO",
        "Classical PSO-style"
    ]

    costs42 = [
        qpso_cost42,
        pso_cost42
    ]

    ax42.bar(
        algorithms42,
        costs42
    )

    ax42.set_ylabel("Objective Cost")
    ax42.set_title(
        "Objective Cost Under " + traffic_level42 + " Traffic"
    )

    st.pyplot(fig42)

    # --------------------------------------------------------
    # RUNTIME GRAPH
    # --------------------------------------------------------

    st.subheader("⏱️ Runtime Comparison")

    fig_runtime42, ax_runtime42 = plt.subplots()

    runtimes42 = [
        qpso_runtime42,
        pso_runtime42
    ]

    ax_runtime42.bar(
        algorithms42,
        runtimes42
    )

    ax_runtime42.set_ylabel("Runtime (seconds)")
    ax_runtime42.set_title("Computational Runtime Comparison")

    st.pyplot(fig_runtime42)

    # --------------------------------------------------------
    # CONVERGENCE COMPARISON
    # --------------------------------------------------------

    st.subheader("📉 Convergence Comparison")

    fig_conv42, ax_conv42 = plt.subplots()

    ax_conv42.plot(
        range(1, len(qpso_conv42) + 1),
        qpso_conv42,
        label="QPSO"
    )

    ax_conv42.plot(
        range(1, len(pso_conv42) + 1),
        pso_conv42,
        label="Classical PSO-style"
    )

    ax_conv42.set_xlabel("Iteration")
    ax_conv42.set_ylabel("Objective Cost")
    ax_conv42.set_title("Convergence Comparison")
    ax_conv42.grid(True)
    ax_conv42.legend()

    st.pyplot(fig_conv42)

    # --------------------------------------------------------
    # INTERPRETATION
    # --------------------------------------------------------

    if qpso_cost42 < pso_cost42:

        improvement42 = (
            (pso_cost42 - qpso_cost42)
            / pso_cost42
        ) * 100

        st.success(
            f"QPSO achieved a {improvement42:.2f}% lower "
            "objective cost than the Classical PSO-style baseline "
            "in this experiment."
        )

    elif qpso_cost42 > pso_cost42:

        difference42 = (
            (qpso_cost42 - pso_cost42)
            / pso_cost42
        ) * 100

        st.warning(
            f"The Classical PSO-style baseline achieved a "
            f"{difference42:.2f}% lower objective cost than QPSO "
            "in this experiment."
        )

    else:

        st.info(
            "Both algorithms achieved the same objective cost "
            "in this experiment."
        )

    st.info(
        "Both algorithms use the same graph, traffic condition, "
        "number of delivery locations, particles and iterations. "
        "This provides a controlled experimental comparison."
    )

st.success("PART 42 COMPLETE")

# ============================================================
# PART 43 — MULTI-RUN STATISTICAL COMPARISON
# ============================================================

st.divider()

st.header("📊 Part 43 — Multi-Run Statistical Comparison")

st.write(
    "This experiment runs QPSO and the Classical PSO-style "
    "baseline multiple times to reduce the effect of random variation."
)

# ------------------------------------------------------------
# SETTINGS
# ------------------------------------------------------------

runs43 = st.slider(
    "🔁 Number of Experimental Runs",
    min_value=5,
    max_value=20,
    value=10,
    key="runs43"
)

delivery_count43 = st.slider(
    "📍 Number of Delivery Locations",
    min_value=2,
    max_value=5,
    value=5,
    key="delivery_count43"
)

traffic_level43 = st.selectbox(
    "🚦 Traffic Condition",
    ["Normal", "Moderate", "Heavy"],
    key="traffic_level43"
)

run_part43 = st.button(
    "▶️ Run Statistical Experiment",
    use_container_width=True
)

# ------------------------------------------------------------
# EXPERIMENT
# ------------------------------------------------------------

if run_part43:

    graph43 = G31.copy()

    # Traffic multiplier
    if traffic_level43 == "Normal":
        multiplier43 = 1.0
    elif traffic_level43 == "Moderate":
        multiplier43 = 1.5
    else:
        multiplier43 = 2.5

    # Apply traffic
    for u, v, data in graph43.edges(data=True):

        travel_time43 = data.get("travel_time", 1)
        distance43 = data.get("distance", 1)
        congestion43 = data.get("congestion", 1)

        adjusted_time43 = travel_time43 * multiplier43

        data["weight"] = (
            TIME_WEIGHT * adjusted_time43
            + DISTANCE_WEIGHT * distance43
            + CONGESTION_WEIGHT * congestion43
        )

    locations43 = ["B", "C", "D", "E", "F"]

    delivery_points43 = locations43[:delivery_count43]

    qpso_costs43 = []
    pso_costs43 = []

    qpso_times43 = []
    pso_times43 = []

    valid_qpso43 = 0
    valid_pso43 = 0

    progress43 = st.progress(0)

    # --------------------------------------------------------
    # MULTIPLE RUNS
    # --------------------------------------------------------

    for run43 in range(runs43):

        # ---------------- QPSO ----------------

        start_qpso43 = time.time()

        qpso_route43, qpso_cost43, qpso_conv43 = (
            qpso_vrp_optimization(
                graph43,
                "A",
                delivery_points43,
                particles=30,
                iterations=100
            )
        )

        qpso_time43 = time.time() - start_qpso43

        if math.isfinite(qpso_cost43):

            qpso_costs43.append(qpso_cost43)
            qpso_times43.append(qpso_time43)
            valid_qpso43 += 1

        # ---------------- PSO ----------------

        start_pso43 = time.time()

        pso_route43, pso_cost43, pso_conv43 = (
            pso_vrp_optimization(
                graph43,
                "A",
                delivery_points43,
                particles=30,
                iterations=100
            )
        )

        pso_time43 = time.time() - start_pso43

        if math.isfinite(pso_cost43):

            pso_costs43.append(pso_cost43)
            pso_times43.append(pso_time43)
            valid_pso43 += 1

        progress43.progress((run43 + 1) / runs43)

    # --------------------------------------------------------
    # CHECK RESULTS
    # --------------------------------------------------------

    if len(qpso_costs43) == 0 or len(pso_costs43) == 0:

        st.error(
            "The statistical comparison could not be completed "
            "because one algorithm produced no valid results."
        )

    else:

        # ----------------------------------------------------
        # STATISTICS
        # ----------------------------------------------------

        qpso_average43 = statistics.mean(qpso_costs43)
        pso_average43 = statistics.mean(pso_costs43)

        qpso_best43 = min(qpso_costs43)
        pso_best43 = min(pso_costs43)

        qpso_worst43 = max(qpso_costs43)
        pso_worst43 = max(pso_costs43)

        qpso_runtime43 = statistics.mean(qpso_times43)
        pso_runtime43 = statistics.mean(pso_times43)

        # ----------------------------------------------------
        # IMPROVEMENT
        # ----------------------------------------------------

        if pso_average43 != 0:

            improvement43 = (
                (pso_average43 - qpso_average43)
                / pso_average43
            ) * 100

        else:

            improvement43 = 0

        # ----------------------------------------------------
        # RESULTS TABLE
        # ----------------------------------------------------

        st.subheader("📋 Statistical Results")

        statistics_table43 = pd.DataFrame({
            "Metric": [
                "Average Objective",
                "Best Objective",
                "Worst Objective",
                "Average Runtime (seconds)",
                "Valid Runs"
            ],
            "QPSO": [
                round(qpso_average43, 4),
                round(qpso_best43, 4),
                round(qpso_worst43, 4),
                round(qpso_runtime43, 4),
                valid_qpso43
            ],
            "Classical PSO-style": [
                round(pso_average43, 4),
                round(pso_best43, 4),
                round(pso_worst43, 4),
                round(pso_runtime43, 4),
                valid_pso43
            ]
        })

        st.dataframe(
            statistics_table43,
            use_container_width=True
        )

        # ----------------------------------------------------
        # COST DISTRIBUTION
        # ----------------------------------------------------

        st.subheader("📈 Objective Cost Distribution")

        fig43, ax43 = plt.subplots()

        ax43.boxplot(
            [qpso_costs43, pso_costs43],
            labels=["QPSO", "Classical PSO-style"]
        )

        ax43.set_ylabel("Objective Cost")
        ax43.set_title(
            "Objective Cost Distribution Across Multiple Runs"
        )

        st.pyplot(fig43)

        # ----------------------------------------------------
        # RUNTIME DISTRIBUTION
        # ----------------------------------------------------

        st.subheader("⏱️ Runtime Distribution")

        fig_runtime43, ax_runtime43 = plt.subplots()

        ax_runtime43.boxplot(
            [qpso_times43, pso_times43],
            labels=["QPSO", "Classical PSO-style"]
        )

        ax_runtime43.set_ylabel("Runtime (seconds)")
        ax_runtime43.set_title(
            "Runtime Distribution Across Multiple Runs"
        )

        st.pyplot(fig_runtime43)

        # ----------------------------------------------------
        # INTERPRETATION
        # ----------------------------------------------------

        if improvement43 > 0:

            st.success(
                f"Across {runs43} runs, QPSO achieved an average "
                f"objective cost {improvement43:.2f}% lower than "
                "the Classical PSO-style baseline."
            )

        elif improvement43 < 0:

            st.warning(
                f"Across {runs43} runs, the Classical PSO-style "
                f"baseline achieved an average objective cost "
                f"{abs(improvement43):.2f}% lower than QPSO."
            )

        else:

            st.info(
                f"Across {runs43} runs, both algorithms achieved "
                "the same average objective cost."
            )

        st.info(
            "Multiple independent runs provide a more reliable "
            "experimental comparison because QPSO and PSO-style "
            "optimization are stochastic methods."
        )

st.success("PART 43 COMPLETE")


# ============================================================
# PART 44 — TRAFFIC SENSITIVITY ANALYSIS
# ============================================================

st.divider()

st.header("🚦 Part 44 — Traffic Sensitivity Analysis")

st.write(
    "This experiment evaluates how changing traffic conditions "
    "affect the optimized QPSO route cost."
)

# ------------------------------------------------------------
# SETTINGS
# ------------------------------------------------------------

delivery_count44 = st.slider(
    "📍 Number of Delivery Locations",
    min_value=2,
    max_value=5,
    value=5,
    key="delivery_count44"
)

run_part44 = st.button(
    "▶️ Run Traffic Sensitivity Experiment",
    use_container_width=True
)

# ------------------------------------------------------------
# EXPERIMENT
# ------------------------------------------------------------

if run_part44:

    traffic_levels44 = [
        ("Normal", 1.0),
        ("Moderate", 1.5),
        ("Heavy", 2.5)
    ]

    locations44 = ["B", "C", "D", "E", "F"]

    delivery_points44 = locations44[:delivery_count44]

    traffic_results44 = []

    progress44 = st.progress(0)

    for index44, (traffic_name44, multiplier44) in enumerate(
        traffic_levels44
    ):

        graph44 = G31.copy()

        # Apply traffic multiplier
        for u44, v44, data44 in graph44.edges(data=True):

            travel_time44 = data44.get("travel_time", 1)
            distance44 = data44.get("distance", 1)
            congestion44 = data44.get("congestion", 1)

            adjusted_time44 = travel_time44 * multiplier44

            data44["weight"] = (
                TIME_WEIGHT * adjusted_time44
                + DISTANCE_WEIGHT * distance44
                + CONGESTION_WEIGHT * congestion44
            )

        # Run QPSO
        start44 = time.time()

        route44, cost44, convergence44 = (
            qpso_vrp_optimization(
                graph44,
                "A",
                delivery_points44,
                particles=30,
                iterations=100
            )
        )

        runtime44 = time.time() - start44

        traffic_results44.append({
            "Traffic Condition": traffic_name44,
            "Traffic Multiplier": multiplier44,
            "Objective Cost": cost44,
            "Runtime (seconds)": runtime44,
            "Route": " → ".join(route44)
        })

        progress44.progress(
            (index44 + 1) / len(traffic_levels44)
        )

    # --------------------------------------------------------
    # RESULTS TABLE
    # --------------------------------------------------------

    st.subheader("📋 Traffic Sensitivity Results")

    traffic_table44 = pd.DataFrame(
        traffic_results44
    )

    traffic_table44["Objective Cost"] = (
        traffic_table44["Objective Cost"].round(4)
    )

    traffic_table44["Runtime (seconds)"] = (
        traffic_table44["Runtime (seconds)"].round(4)
    )

    st.dataframe(
        traffic_table44,
        use_container_width=True
    )

    # --------------------------------------------------------
    # COST GRAPH
    # --------------------------------------------------------

    st.subheader("📈 Objective Cost vs Traffic")

    fig44, ax44 = plt.subplots()

    traffic_names44 = [
        row["Traffic Condition"]
        for row in traffic_results44
    ]

    traffic_costs44 = [
        row["Objective Cost"]
        for row in traffic_results44
    ]

    ax44.plot(
        traffic_names44,
        traffic_costs44,
        marker="o",
        linewidth=2
    )

    ax44.set_xlabel("Traffic Condition")
    ax44.set_ylabel("Objective Cost")
    ax44.set_title(
        "QPSO Objective Cost Under Different Traffic Conditions"
    )

    ax44.grid(True)

    st.pyplot(fig44)

    # --------------------------------------------------------
    # ROUTE RESULTS
    # --------------------------------------------------------

    st.subheader("🛣️ Route Under Different Traffic Conditions")

    for row44 in traffic_results44:

        st.write(
            f"**{row44['Traffic Condition']} Traffic:** "
            f"{row44['Route']}"
        )

    # --------------------------------------------------------
    # INTERPRETATION
    # --------------------------------------------------------

    normal_cost44 = traffic_results44[0]["Objective Cost"]
    heavy_cost44 = traffic_results44[-1]["Objective Cost"]

    if heavy_cost44 > normal_cost44:

        increase44 = (
            (heavy_cost44 - normal_cost44)
            / normal_cost44
        ) * 100

        st.warning(
            f"Heavy traffic increased the optimized objective "
            f"cost by approximately {increase44:.2f}% compared "
            "with normal traffic."
        )

    elif heavy_cost44 < normal_cost44:

        st.info(
            "The optimized route under heavy traffic produced "
            "a lower objective cost in this stochastic experiment."
        )

    else:

        st.info(
            "The objective cost remained the same between "
            "normal and heavy traffic in this experiment."
        )

    st.info(
        "Traffic sensitivity demonstrates why transportation "
        "route optimization should consider changing road "
        "conditions rather than relying only on static routes."
    )

st.success("PART 44 COMPLETE")

# ============================================================
# PART 45 — TRAFFIC IMPACT ON ROUTE COST
# ============================================================

st.divider()

st.header("🚦 Part 45 — Traffic Impact on Route Cost")

st.write(
    "This experiment measures how traffic congestion changes "
    "the optimized transportation route cost."
)

# ------------------------------------------------------------
# RUN EXPERIMENT
# ------------------------------------------------------------

run_part45 = st.button(
    "▶️ Run Traffic Impact Experiment",
    use_container_width=True
)

if run_part45:

    traffic_levels45 = [
        ("Normal", 1.0),
        ("Moderate", 1.5),
        ("Heavy", 2.5)
    ]

    delivery_points45 = ["B", "C", "D", "E", "F"]

    results45 = []

    progress45 = st.progress(0)

    # --------------------------------------------------------
    # TEST EACH TRAFFIC LEVEL
    # --------------------------------------------------------

    for index45, (traffic_name45, multiplier45) in enumerate(
        traffic_levels45
    ):

        graph45 = G31.copy()

        # Apply traffic condition
        for u45, v45, data45 in graph45.edges(data=True):

            travel_time45 = data45.get("travel_time", 1)
            distance45 = data45.get("distance", 1)
            congestion45 = data45.get("congestion", 1)

            adjusted_time45 = (
                travel_time45 * multiplier45
            )

            data45["weight"] = (
                TIME_WEIGHT * adjusted_time45
                + DISTANCE_WEIGHT * distance45
                + CONGESTION_WEIGHT * congestion45
            )

        # QPSO optimization
        start45 = time.time()

        route45, cost45, convergence45 = (
            qpso_vrp_optimization(
                graph45,
                "A",
                delivery_points45,
                particles=30,
                iterations=100
            )
        )

        runtime45 = time.time() - start45

        results45.append({
            "Traffic Condition": traffic_name45,
            "Objective Cost": cost45,
            "Runtime (seconds)": runtime45,
            "Optimized Route": " → ".join(route45)
        })

        progress45.progress(
            (index45 + 1) / len(traffic_levels45)
        )

    # --------------------------------------------------------
    # RESULTS TABLE
    # --------------------------------------------------------

    st.subheader("📋 Traffic Impact Results")

    results_table45 = pd.DataFrame(results45)

    results_table45["Objective Cost"] = (
        results_table45["Objective Cost"].round(4)
    )

    results_table45["Runtime (seconds)"] = (
        results_table45["Runtime (seconds)"].round(4)
    )

    st.dataframe(
        results_table45,
        use_container_width=True
    )

    # --------------------------------------------------------
    # COST GRAPH
    # --------------------------------------------------------

    st.subheader("📈 Traffic vs Objective Cost")

    fig45, ax45 = plt.subplots()

    traffic_names45 = [
        item["Traffic Condition"]
        for item in results45
    ]

    costs45 = [
        item["Objective Cost"]
        for item in results45
    ]

    ax45.plot(
        traffic_names45,
        costs45,
        marker="o",
        linewidth=2
    )

    ax45.set_xlabel("Traffic Condition")
    ax45.set_ylabel("Objective Cost")
    ax45.set_title(
        "Effect of Traffic on QPSO Route Cost"
    )

    ax45.grid(True)

    st.pyplot(fig45)

    # --------------------------------------------------------
    # ROUTES
    # --------------------------------------------------------

    st.subheader("🛣️ Optimized Routes")

    for item45 in results45:

        st.write(
            f"**{item45['Traffic Condition']} Traffic:** "
            f"{item45['Optimized Route']}"
        )

    # --------------------------------------------------------
    # TRAFFIC IMPACT
    # --------------------------------------------------------

    normal_cost45 = results45[0]["Objective Cost"]
    heavy_cost45 = results45[-1]["Objective Cost"]

    if normal_cost45 != 0:

        impact45 = (
            (heavy_cost45 - normal_cost45)
            / normal_cost45
        ) * 100

    else:

        impact45 = 0

    if impact45 > 0:

        st.warning(
            f"Heavy traffic increased the optimized route "
            f"objective cost by approximately {impact45:.2f}% "
            "compared with normal traffic."
        )

    elif impact45 < 0:

        st.info(
            "The optimized route cost decreased under heavy "
            "traffic in this stochastic experiment."
        )

    else:

        st.info(
            "The optimized route cost remained unchanged "
            "between normal and heavy traffic."
        )

    st.info(
        "This experiment demonstrates the importance of "
        "traffic-aware route optimization in dynamic "
        "transportation environments."
    )

st.success("PART 45 COMPLETE")

# ============================================================
# PART 46 — TRAFFIC-AWARE ROUTE VISUALIZATION
# ============================================================

st.divider()

st.header("🗺️ Part 46 — Traffic-Aware Route Visualization")

st.write(
    "This visualization shows the QPSO-optimized route under "
    "different traffic conditions."
)

# ------------------------------------------------------------
# USER CONTROL
# ------------------------------------------------------------

delivery_count46 = st.slider(
    "📍 Number of Delivery Locations",
    min_value=2,
    max_value=5,
    value=5,
    key="delivery_count46"
)

run_part46 = st.button(
    "▶️ Generate Traffic-Aware Route Map",
    use_container_width=True
)

# ------------------------------------------------------------
# GENERATE VISUALIZATION
# ------------------------------------------------------------

if run_part46:

    traffic_levels46 = [
        ("Normal", 1.0),
        ("Moderate", 1.5),
        ("Heavy", 2.5)
    ]

    delivery_locations46 = ["B", "C", "D", "E", "F"]

    delivery_points46 = delivery_locations46[
        :delivery_count46
    ]

    visualization_results46 = []

    progress46 = st.progress(0)

    # --------------------------------------------------------
    # OPTIMIZE FOR EACH TRAFFIC CONDITION
    # --------------------------------------------------------

    for index46, (
        traffic_name46,
        multiplier46
    ) in enumerate(traffic_levels46):

        graph46 = G31.copy()

        # Apply traffic condition
        for u46, v46, data46 in graph46.edges(data=True):

            travel_time46 = data46.get(
                "travel_time",
                1
            )

            distance46 = data46.get(
                "distance",
                1
            )

            congestion46 = data46.get(
                "congestion",
                1
            )

            adjusted_time46 = (
                travel_time46 * multiplier46
            )

            data46["weight"] = (
                TIME_WEIGHT * adjusted_time46
                + DISTANCE_WEIGHT * distance46
                + CONGESTION_WEIGHT * congestion46
            )

        # Run QPSO
        route46, cost46, convergence46 = (
            qpso_vrp_optimization(
                graph46,
                "A",
                delivery_points46,
                particles=30,
                iterations=100
            )
        )

        visualization_results46.append({
            "Traffic": traffic_name46,
            "Graph": graph46,
            "Route": route46,
            "Cost": cost46
        })

        progress46.progress(
            (index46 + 1) / len(traffic_levels46)
        )

    # --------------------------------------------------------
    # DISPLAY ROUTE INFORMATION
    # --------------------------------------------------------

    st.subheader("🚚 Optimized Routes")

    for result46 in visualization_results46:

        st.write(
            f"**{result46['Traffic']} Traffic:** "
            f"{' → '.join(result46['Route'])}"
        )

        st.write(
            f"Objective Cost: "
            f"**{result46['Cost']:.4f}**"
        )

    # --------------------------------------------------------
    # ROUTE MAPS
    # --------------------------------------------------------

    st.subheader("🗺️ Route Network Visualization")

    for result46 in visualization_results46:

        graph46 = result46["Graph"]
        route46 = result46["Route"]
        traffic_name46 = result46["Traffic"]

        fig46, ax46 = plt.subplots(
            figsize=(8, 5)
        )

        # Fixed node positions
        positions46 = nx.spring_layout(
            graph46,
            seed=42
        )

        # Draw complete road network
        nx.draw_networkx_nodes(
            graph46,
            positions46,
            node_size=700,
            ax=ax46
        )

        nx.draw_networkx_edges(
            graph46,
            positions46,
            width=1.5,
            ax=ax46
        )

        nx.draw_networkx_labels(
            graph46,
            positions46,
            font_size=10,
            ax=ax46
        )

        # ----------------------------------------------------
        # DRAW OPTIMIZED ROUTE
        # ----------------------------------------------------

        route_edges46 = []

        for i46 in range(
            len(route46) - 1
        ):

            start46 = route46[i46]
            end46 = route46[i46 + 1]

            try:

                shortest_path46 = nx.shortest_path(
                    graph46,
                    start46,
                    end46,
                    weight="weight"
                )

                for j46 in range(
                    len(shortest_path46) - 1
                ):

                    route_edges46.append(
                        (
                            shortest_path46[j46],
                            shortest_path46[j46 + 1]
                        )
                    )

            except nx.NetworkXNoPath:

                pass

        # Draw optimized route
        nx.draw_networkx_edges(
            graph46,
            positions46,
            edgelist=route_edges46,
            width=4,
            ax=ax46
        )

        ax46.set_title(
            f"QPSO Route — {traffic_name46} Traffic"
        )

        ax46.axis("off")

        st.pyplot(fig46)

    # --------------------------------------------------------
    # EXPLANATION
    # --------------------------------------------------------

    st.info(
        "The map shows the complete road network together "
        "with the route selected by QPSO. Changing traffic "
        "conditions changes road costs and can cause the "
        "optimization process to select a different route."
    )

st.success("PART 46 COMPLETE")

# ============================================================
# PART 47 — TRAFFIC CONDITION COMPARISON
# ============================================================

st.divider()

st.header("📊 Part 47 — Traffic Condition Comparison")

st.write(
    "This experiment compares the optimized QPSO route cost "
    "under different traffic conditions."
)

run_part47 = st.button(
    "▶️ Run Traffic Comparison",
    use_container_width=True
)

if run_part47:

    traffic_conditions47 = [
        ("Normal", 1.0),
        ("Moderate", 1.5),
        ("Heavy", 2.5)
    ]

    delivery_points47 = ["B", "C", "D", "E", "F"]

    results47 = []

    progress47 = st.progress(0)

    for index47, (
        traffic_name47,
        multiplier47
    ) in enumerate(traffic_conditions47):

        graph47 = G31.copy()

        for u47, v47, data47 in graph47.edges(data=True):

            travel_time47 = data47.get(
                "travel_time",
                1
            )

            distance47 = data47.get(
                "distance",
                1
            )

            congestion47 = data47.get(
                "congestion",
                1
            )

            adjusted_time47 = (
                travel_time47 * multiplier47
            )

            data47["weight"] = (
                TIME_WEIGHT * adjusted_time47
                + DISTANCE_WEIGHT * distance47
                + CONGESTION_WEIGHT * congestion47
            )

        route47, cost47, convergence47 = (
            qpso_vrp_optimization(
                graph47,
                "A",
                delivery_points47,
                particles=30,
                iterations=100
            )
        )

        results47.append({
            "Traffic Condition": traffic_name47,
            "Route": " → ".join(route47),
            "Objective Cost": cost47
        })

        progress47.progress(
            (index47 + 1) / len(traffic_conditions47)
        )

    # --------------------------------------------------------
    # RESULTS TABLE
    # --------------------------------------------------------

    st.subheader("Traffic Comparison Results")

    st.dataframe(
        results47,
        use_container_width=True
    )

    # --------------------------------------------------------
    # COST GRAPH
    # --------------------------------------------------------

    traffic_names47 = [
        item["Traffic Condition"]
        for item in results47
    ]

    traffic_costs47 = [
        item["Objective Cost"]
        for item in results47
    ]

    fig47, ax47 = plt.subplots(
        figsize=(8, 5)
    )

    ax47.bar(
        traffic_names47,
        traffic_costs47
    )

    ax47.set_title(
        "QPSO Objective Cost Under Different Traffic Conditions"
    )

    ax47.set_xlabel(
        "Traffic Condition"
    )

    ax47.set_ylabel(
        "Objective Cost"
    )

    st.pyplot(fig47)

    # --------------------------------------------------------
    # EXPLANATION
    # --------------------------------------------------------

    st.info(
        "As traffic congestion increases, road travel-time "
        "costs increase. QPSO evaluates the changed network "
        "and searches for a low-cost delivery route."
    )

st.success("PART 47 COMPLETE")

# ============================================================
# PART 48 — MULTI-RUN STATISTICAL TRAFFIC ANALYSIS
# ============================================================

st.divider()

st.header("📈 Part 48 — Multi-Run Statistical Traffic Analysis")

st.write(
    "This experiment performs multiple QPSO runs under "
    "different traffic conditions and calculates statistical "
    "performance measures."
)

runs48 = st.slider(
    "Number of QPSO Runs",
    min_value=5,
    max_value=30,
    value=10,
    step=5
)

run_part48 = st.button(
    "▶️ Run Statistical Experiment",
    use_container_width=True,
    key="part48_statistical_experiment"
)

if run_part48:

    traffic_conditions48 = [
        ("Normal", 1.0),
        ("Moderate", 1.5),
        ("Heavy", 2.5)
    ]

    delivery_points48 = ["B", "C", "D", "E", "F"]

    statistical_results48 = []

    progress48 = st.progress(0)

    for condition_index48, (
        condition_name48,
        multiplier48
    ) in enumerate(traffic_conditions48):

        costs48 = []

        for run_index48 in range(runs48):

            graph48 = G31.copy()

            for u48, v48, data48 in graph48.edges(data=True):

                travel_time48 = data48.get(
                    "travel_time",
                    1
                )

                distance48 = data48.get(
                    "distance",
                    1
                )

                congestion48 = data48.get(
                    "congestion",
                    1
                )

                adjusted_time48 = (
                    travel_time48 * multiplier48
                )

                data48["weight"] = (
                    TIME_WEIGHT * adjusted_time48
                    + DISTANCE_WEIGHT * distance48
                    + CONGESTION_WEIGHT * congestion48
                )

            route48, cost48, convergence48 = (
                qpso_vrp_optimization(
                    graph48,
                    "A",
                    delivery_points48,
                    particles=30,
                    iterations=100
                )
            )

            costs48.append(cost48)

        average48 = statistics.mean(costs48)
        best48 = min(costs48)
        worst48 = max(costs48)

        if len(costs48) > 1:
            std48 = statistics.stdev(costs48)
        else:
            std48 = 0

        statistical_results48.append({
            "Traffic Condition": condition_name48,
            "Average Cost": round(average48, 3),
            "Best Cost": round(best48, 3),
            "Worst Cost": round(worst48, 3),
            "Std. Deviation": round(std48, 3)
        })

        progress48.progress(
            (condition_index48 + 1)
            / len(traffic_conditions48)
        )

    # --------------------------------------------------------
    # RESULTS TABLE
    # --------------------------------------------------------

    st.subheader("Statistical Results")

    st.dataframe(
        statistical_results48,
        use_container_width=True
    )

    # --------------------------------------------------------
    # AVERAGE COST GRAPH
    # --------------------------------------------------------

    condition_names48 = [
        item["Traffic Condition"]
        for item in statistical_results48
    ]

    average_costs48 = [
        item["Average Cost"]
        for item in statistical_results48
    ]

    fig48, ax48 = plt.subplots(
        figsize=(8, 5)
    )

    ax48.bar(
        condition_names48,
        average_costs48
    )

    ax48.set_title(
        "Average QPSO Objective Cost Across Traffic Conditions"
    )

    ax48.set_xlabel(
        "Traffic Condition"
    )

    ax48.set_ylabel(
        "Average Objective Cost"
    )

    st.pyplot(fig48)

    # --------------------------------------------------------
    # STATISTICAL INTERPRETATION
    # --------------------------------------------------------

    st.info(
        "The experiment shows how QPSO behaves statistically "
        "when traffic conditions change. Average, best, worst "
        "and standard deviation values help evaluate the "
        "stability and reliability of the optimization process."
    )

st.success("PART 48 COMPLETE")


# ============================================================
# PART 49 - QPSO CONVERGENCE STABILITY ANALYSIS
# ============================================================

st.divider()

st.header("📉 Part 49 — QPSO Convergence Stability Analysis")

st.write(
    "This experiment analyzes how the QPSO objective cost changes "
    "during optimization iterations under different traffic conditions."
)

# ------------------------------------------------------------
# 1. USER CONTROLS
# ------------------------------------------------------------

runs49 = st.slider(
    "Number of QPSO Runs",
    min_value=3,
    max_value=15,
    value=5,
    key="part49_runs"
)

iterations49 = st.slider(
    "Number of Optimization Iterations",
    min_value=50,
    max_value=200,
    value=100,
    step=10,
    key="part49_iterations"
)

run_part49 = st.checkbox(
    "Run Convergence Stability Analysis",
    key="part49_run_button"
)


# ------------------------------------------------------------
# 2. CREATE BASE NETWORK
# ------------------------------------------------------------

G49_base = nx.Graph()

edges49 = [
    ("A", "B", 5),
    ("B", "C", 4),
    ("C", "D", 6),
    ("D", "E", 5),
    ("E", "F", 4),

    ("A", "C", 8),
    ("B", "D", 7),
    ("C", "E", 7),
    ("D", "F", 6),

    ("A", "D", 12),
    ("B", "E", 10),
    ("C", "F", 11)
]

for u, v, weight in edges49:
    G49_base.add_edge(
        u,
        v,
        weight=float(weight)
    )


# ------------------------------------------------------------
# 3. TRAFFIC CONDITIONS
# ------------------------------------------------------------

traffic_levels49 = {
    "Normal": 1.0,
    "Moderate": 1.5,
    "Heavy": 2.0
}

depot49 = "A"

delivery_points49 = [
    "B",
    "C",
    "D",
    "E",
    "F"
]


# ------------------------------------------------------------
# 4. RUN EXPERIMENT
# ------------------------------------------------------------

if run_part49:

    st.info(
        "QPSO is executed multiple times for each traffic condition. "
        "The convergence curves show how the best objective cost "
        "changes as the number of iterations increases."
    )

    average_convergence49 = {}

    for traffic_name49, multiplier49 in traffic_levels49.items():

        all_convergence49 = []

        # Create traffic-specific graph
        G49 = G49_base.copy()

        for u, v, data in G49.edges(data=True):
            data["weight"] = (
                G49_base[u][v]["weight"] * multiplier49
            )

        # --------------------------------------------
        # Multiple QPSO runs
        # --------------------------------------------

        for run49 in range(runs49):

            route49, cost49, convergence49 = (
                qpso_vrp_optimization(
                    G49,
                    depot49,
                    delivery_points49,
                    particles=30,
                    iterations=iterations49
                )
            )

            if len(convergence49) > 0:
                all_convergence49.append(
                    convergence49
                )

        # --------------------------------------------
        # Average convergence
        # --------------------------------------------

        if len(all_convergence49) > 0:

            minimum_length49 = min(
                len(x) for x in all_convergence49
            )

            trimmed_convergence49 = [
                x[:minimum_length49]
                for x in all_convergence49
            ]

            avg_curve49 = []

            for i49 in range(minimum_length49):

                values49 = [
                    curve49[i49]
                    for curve49 in trimmed_convergence49
                ]

                avg_curve49.append(
                    statistics.mean(values49)
                )

            average_convergence49[
                traffic_name49
            ] = avg_curve49


    # --------------------------------------------------------
    # 5. DISPLAY CONVERGENCE GRAPH
    # --------------------------------------------------------

    if len(average_convergence49) > 0:

        fig49, ax49 = plt.subplots(
            figsize=(10, 5)
        )

        for traffic_name49, curve49 in (
            average_convergence49.items()
        ):

            ax49.plot(
                range(
                    1,
                    len(curve49) + 1
                ),
                curve49,
                label=traffic_name49
            )

        ax49.set_title(
            "QPSO Convergence Stability Under Traffic Conditions"
        )

        ax49.set_xlabel(
            "Optimization Iteration"
        )

        ax49.set_ylabel(
            "Average Best Objective Cost"
        )

        ax49.legend()

        ax49.grid(True, alpha=0.3)

        st.pyplot(fig49)

        plt.close(fig49)


        # ----------------------------------------------------
        # 6. CONVERGENCE SUMMARY
        # ----------------------------------------------------

        summary49 = []

        for traffic_name49, curve49 in (
            average_convergence49.items()
        ):

            initial49 = curve49[0]
            final49 = curve49[-1]
            improvement49 = 0

            if initial49 != 0:
                improvement49 = (
                    (initial49 - final49)
                    / initial49
                ) * 100

            summary49.append({
                "Traffic Condition": traffic_name49,
                "Initial Cost": round(
                    initial49, 2
                ),
                "Final Cost": round(
                    final49, 2
                ),
                "Improvement (%)": round(
                    improvement49, 2
                ),
                "Iterations": len(curve49)
            })


        st.subheader(
            "Convergence Stability Summary"
        )

        st.dataframe(
            summary49,
            use_container_width=True
        )


        # ----------------------------------------------------
        # 7. INTERPRETATION
        # ----------------------------------------------------

        st.info(
            "A decreasing convergence curve indicates that QPSO "
            "is improving the route objective during optimization. "
            "When the curve becomes nearly flat, the algorithm "
            "has reached a stable region of the search space."
        )


st.success("PART 49 COMPLETE")



# ============================================================
# PART 50 - QPSO VS CLASSICAL PSO CONVERGENCE COMPARISON
# ============================================================

st.divider()

st.header("⚖️ Part 50 — QPSO vs Classical PSO Convergence Comparison")

st.write(
    "This experiment compares the convergence behavior of "
    "QPSO and the Classical PSO-style baseline under the "
    "same traffic conditions."
)

# ------------------------------------------------------------
# 1. USER CONTROLS
# ------------------------------------------------------------

traffic_condition50 = st.selectbox(
    "Traffic Condition",
    ["Normal", "Moderate", "Heavy"],
    key="part50_traffic_condition"
)

iterations50 = st.slider(
    "Number of Optimization Iterations",
    min_value=50,
    max_value=200,
    value=100,
    step=10,
    key="part50_iterations"
)

particles50 = st.slider(
    "Number of Particles",
    min_value=10,
    max_value=50,
    value=30,
    step=5,
    key="part50_particles"
)

run_part50 = st.checkbox(
    "Run QPSO and Classical PSO Comparison",
    key="part50_run_comparison"
)


# ------------------------------------------------------------
# 2. CREATE TEST NETWORK
# ------------------------------------------------------------

G50_base = nx.Graph()

edges50 = [
    ("A", "B", 5),
    ("B", "C", 4),
    ("C", "D", 6),
    ("D", "E", 5),
    ("E", "F", 4),

    ("A", "C", 8),
    ("B", "D", 7),
    ("C", "E", 7),
    ("D", "F", 6),

    ("A", "D", 12),
    ("B", "E", 10),
    ("C", "F", 11)
]

for u50, v50, weight50 in edges50:
    G50_base.add_edge(
        u50,
        v50,
        weight=float(weight50)
    )


# ------------------------------------------------------------
# 3. TRAFFIC MULTIPLIERS
# ------------------------------------------------------------

traffic_multipliers50 = {
    "Normal": 1.0,
    "Moderate": 1.5,
    "Heavy": 2.0
}


# ------------------------------------------------------------
# 4. RUN COMPARISON
# ------------------------------------------------------------

if run_part50:

    # Create traffic-specific graph
    G50 = G50_base.copy()

    multiplier50 = traffic_multipliers50[
        traffic_condition50
    ]

    for u50, v50, data50 in G50.edges(data=True):
        data50["weight"] = (
            G50_base[u50][v50]["weight"]
            * multiplier50
        )

    depot50 = "A"

    delivery_points50 = [
        "B",
        "C",
        "D",
        "E",
        "F"
    ]

    st.info(
        f"Running both algorithms under "
        f"{traffic_condition50.lower()} traffic..."
    )

    # --------------------------------------------------------
    # 5. QPSO
    # --------------------------------------------------------

    start_qpso50 = time.perf_counter()

    qpso_route50, qpso_cost50, qpso_convergence50 = (
        qpso_vrp_optimization(
            G50,
            depot50,
            delivery_points50,
            particles=particles50,
            iterations=iterations50
        )
    )

    qpso_runtime50 = (
        time.perf_counter() - start_qpso50
    )


    # --------------------------------------------------------
    # 6. CLASSICAL PSO-STYLE BASELINE
    # --------------------------------------------------------

    start_pso50 = time.perf_counter()

    pso_route50, pso_cost50, pso_convergence50 = (
        pso_vrp_optimization(
            G50,
            depot50,
            delivery_points50,
            particles=particles50,
            iterations=iterations50
        )
    )

    pso_runtime50 = (
        time.perf_counter() - start_pso50
    )


    # --------------------------------------------------------
    # 7. DISPLAY ROUTES AND COSTS
    # --------------------------------------------------------

    st.subheader("Algorithm Results")

    comparison50 = [
        {
            "Algorithm": "QPSO",
            "Route": " → ".join(
                map(str, qpso_route50)
            ),
            "Objective Cost": round(
                qpso_cost50, 2
            ),
            "Runtime (seconds)": round(
                qpso_runtime50, 4
            )
        },
        {
            "Algorithm": "Classical PSO-style",
            "Route": " → ".join(
                map(str, pso_route50)
            ),
            "Objective Cost": round(
                pso_cost50, 2
            ),
            "Runtime (seconds)": round(
                pso_runtime50, 4
            )
        }
    ]

    st.dataframe(
        comparison50,
        use_container_width=True
    )


    # --------------------------------------------------------
    # 8. CONVERGENCE GRAPH
    # --------------------------------------------------------

    st.subheader("Convergence Comparison")

    fig50, ax50 = plt.subplots(
        figsize=(10, 5)
    )

    if len(qpso_convergence50) > 0:
        ax50.plot(
            range(
                1,
                len(qpso_convergence50) + 1
            ),
            qpso_convergence50,
            label="QPSO"
        )

    if len(pso_convergence50) > 0:
        ax50.plot(
            range(
                1,
                len(pso_convergence50) + 1
            ),
            pso_convergence50,
            label="Classical PSO-style"
        )

    ax50.set_title(
        "QPSO vs Classical PSO Convergence"
    )

    ax50.set_xlabel(
        "Optimization Iteration"
    )

    ax50.set_ylabel(
        "Best Objective Cost"
    )

    ax50.legend()

    ax50.grid(
        True,
        alpha=0.3
    )

    st.pyplot(fig50)

    plt.close(fig50)


    # --------------------------------------------------------
    # 9. PERFORMANCE DIFFERENCE
    # --------------------------------------------------------

    cost_difference50 = (
        pso_cost50 - qpso_cost50
    )

    if pso_cost50 != 0:
        cost_difference_percent50 = (
            cost_difference50
            / pso_cost50
        ) * 100
    else:
        cost_difference_percent50 = 0


    runtime_difference50 = (
        pso_runtime50 - qpso_runtime50
    )

    if pso_runtime50 != 0:
        runtime_difference_percent50 = (
            runtime_difference50
            / pso_runtime50
        ) * 100
    else:
        runtime_difference_percent50 = 0


    st.subheader(
        "Performance Comparison"
    )

    metrics50 = [
        {
            "Metric": "QPSO Objective Cost",
            "Value": round(
                qpso_cost50, 2
            )
        },
        {
            "Metric": "Classical PSO Objective Cost",
            "Value": round(
                pso_cost50, 2
            )
        },
        {
            "Metric": "Cost Difference (%)",
            "Value": round(
                cost_difference_percent50, 2
            )
        },
        {
            "Metric": "QPSO Runtime (seconds)",
            "Value": round(
                qpso_runtime50, 4
            )
        },
        {
            "Metric": "PSO Runtime (seconds)",
            "Value": round(
                pso_runtime50, 4
            )
        },
        {
            "Metric": "Runtime Difference (%)",
            "Value": round(
                runtime_difference_percent50, 2
            )
        }
    ]

    st.dataframe(
        metrics50,
        use_container_width=True
    )


    # --------------------------------------------------------
    # 10. INTERPRETATION
    # --------------------------------------------------------

    if qpso_cost50 < pso_cost50:

        st.success(
            "For this experiment, QPSO found a lower-cost "
            "route than the Classical PSO-style baseline."
        )

    elif qpso_cost50 > pso_cost50:

        st.warning(
            "For this experiment, the Classical PSO-style "
            "baseline found a lower-cost route than QPSO."
        )

    else:

        st.info(
            "For this experiment, both algorithms found "
            "the same objective cost."
        )

    st.info(
        "The comparison uses the same road network, "
        "traffic condition, delivery locations, particle "
        "count and iteration count for both algorithms. "
        "This makes the comparison more consistent."
    )


st.success("PART 50 COMPLETE")

# ============================================================
# PART 51 - MULTI-RUN RUNTIME PERFORMANCE ANALYSIS
# ============================================================

st.markdown("---")

st.header("⏱️ Part 51 — Multi-Run Runtime Performance Analysis")

st.write(
    "This experiment runs QPSO and the Classical PSO-style baseline "
    "multiple times under the same traffic conditions and compares "
    "their average computational runtime."
)

# ------------------------------------------------------------
# USER CONTROLS
# ------------------------------------------------------------

runs51 = st.slider(
    "Number of Benchmark Runs",
    min_value=3,
    max_value=30,
    value=10,
    step=1,
    key="part51_runs"
)

iterations51 = st.slider(
    "Number of Optimization Iterations",
    min_value=50,
    max_value=200,
    value=100,
    step=10,
    key="part51_iterations"
)

particles51 = st.slider(
    "Number of Particles",
    min_value=10,
    max_value=50,
    value=30,
    step=5,
    key="part51_particles"
)

run_part51 = st.button(
    "⏱️ Run Runtime Performance Analysis",
    key="part51_button"
)


# ------------------------------------------------------------
# RUN EXPERIMENT
# ------------------------------------------------------------

if run_part51:

    with st.spinner("Running QPSO and Classical PSO-style benchmarks..."):

        qpso_times51 = []
        pso_times51 = []

        qpso_costs51 = []
        pso_costs51 = []

        for run in range(runs51):

            # ------------------------------------------------
            # QPSO
            # ------------------------------------------------

            start_qpso51 = time.perf_counter()

            qpso_route51, qpso_cost51, qpso_convergence51 = (
                qpso_vrp_optimization(
                    G31,
                    "A",
                    ["B", "C", "D", "E", "F"],
                    particles=particles51,
                    iterations=iterations51
                )
            )

            end_qpso51 = time.perf_counter()

            qpso_runtime51 = end_qpso51 - start_qpso51

            qpso_times51.append(qpso_runtime51)
            qpso_costs51.append(qpso_cost51)


            # ------------------------------------------------
            # CLASSICAL PSO-STYLE BASELINE
            # ------------------------------------------------

            start_pso51 = time.perf_counter()

            pso_route51, pso_cost51, pso_convergence51 = (
                pso_vrp_optimization(
                    G31,
                    "A",
                    ["B", "C", "D", "E", "F"],
                    particles=particles51,
                    iterations=iterations51
                )
            )

            end_pso51 = time.perf_counter()

            pso_runtime51 = end_pso51 - start_pso51

            pso_times51.append(pso_runtime51)
            pso_costs51.append(pso_cost51)


        # ----------------------------------------------------
        # STATISTICS
        # ----------------------------------------------------

        avg_qpso_time51 = statistics.mean(qpso_times51)
        avg_pso_time51 = statistics.mean(pso_times51)

        best_qpso_time51 = min(qpso_times51)
        best_pso_time51 = min(pso_times51)

        worst_qpso_time51 = max(qpso_times51)
        worst_pso_time51 = max(pso_times51)

        avg_qpso_cost51 = statistics.mean(qpso_costs51)
        avg_pso_cost51 = statistics.mean(pso_costs51)

        if avg_pso_time51 > 0:
            runtime_difference51 = (
                (avg_pso_time51 - avg_qpso_time51)
                / avg_pso_time51
            ) * 100
        else:
            runtime_difference51 = 0


        # ----------------------------------------------------
        # RESULTS TABLE
        # ----------------------------------------------------

        st.success("Runtime experiment completed successfully.")

        st.subheader("Runtime Performance Results")

        runtime_table51 = {
            "Metric": [
                "Average Runtime (seconds)",
                "Best Runtime (seconds)",
                "Worst Runtime (seconds)",
                "Average Objective Cost"
            ],
            "QPSO": [
                round(avg_qpso_time51, 6),
                round(best_qpso_time51, 6),
                round(worst_qpso_time51, 6),
                round(avg_qpso_cost51, 4)
            ],
            "Classical PSO-style": [
                round(avg_pso_time51, 6),
                round(best_pso_time51, 6),
                round(worst_pso_time51, 6),
                round(avg_pso_cost51, 4)
            ]
        }

        st.table(runtime_table51)


        # ----------------------------------------------------
        # RUNTIME DIFFERENCE
        # ----------------------------------------------------

        st.subheader("Average Runtime Comparison")

        if runtime_difference51 > 0:

            st.info(
                f"QPSO used approximately "
                f"{runtime_difference51:.2f}% less runtime than "
                f"the Classical PSO-style baseline in this experiment."
            )

        elif runtime_difference51 < 0:

            st.info(
                f"QPSO used approximately "
                f"{abs(runtime_difference51):.2f}% more runtime than "
                f"the Classical PSO-style baseline in this experiment."
            )

        else:

            st.info(
                "Both algorithms had approximately the same average runtime "
                "in this experiment."
            )


        # ----------------------------------------------------
        # BAR CHART
        # ----------------------------------------------------

        st.subheader("Average Runtime Chart")

        fig51, ax51 = plt.subplots(figsize=(8, 5))

        algorithms51 = [
            "QPSO",
            "Classical PSO-style"
        ]

        runtimes51 = [
            avg_qpso_time51,
            avg_pso_time51
        ]

        ax51.bar(
            algorithms51,
            runtimes51
        )

        ax51.set_title(
            "Average Runtime: QPSO vs Classical PSO-style"
        )

        ax51.set_ylabel(
            "Runtime (seconds)"
        )

        ax51.grid(
            axis="y",
            alpha=0.3
        )

        st.pyplot(fig51)

        plt.close(fig51)


        # ----------------------------------------------------
        # EXPERIMENT INFORMATION
        # ----------------------------------------------------

        st.subheader("Experiment Configuration")

        st.write(
            f"Number of benchmark runs: **{runs51}**"
        )

        st.write(
            f"Particles per run: **{particles51}**"
        )

        st.write(
            f"Optimization iterations per run: **{iterations51}**"
        )

        st.write(
            "Both algorithms were tested on the same road network, "
            "depot, delivery locations and optimization settings."
        )


        # ----------------------------------------------------
        # EXPLANATION
        # ----------------------------------------------------

        st.info(
            "Runtime analysis measures computational efficiency. "
            "A lower runtime means the algorithm completed the optimization "
            "faster under the tested configuration. The objective-cost results "
            "should also be considered together with runtime when evaluating "
            "overall algorithm performance."
        )


st.success("PART 51 COMPLETE")

# ============================================================
# PART 52 - QPSO SCALABILITY ANALYSIS
# ============================================================

st.markdown("---")

st.header("📈 Part 52 — QPSO Scalability Analysis")

st.write(
    "This experiment evaluates how QPSO performs as the number of "
    "delivery locations increases. Objective cost and computation "
    "time are measured for different problem sizes."
)


# ------------------------------------------------------------
# USER CONTROLS
# ------------------------------------------------------------

max_locations52 = st.slider(
    "Maximum Number of Delivery Locations",
    min_value=10,
    max_value=25,
    value=20,
    step=5,
    key="part52_max_locations"
)

particles52 = st.slider(
    "Number of QPSO Particles",
    min_value=10,
    max_value=40,
    value=20,
    step=5,
    key="part52_particles"
)

iterations52 = st.slider(
    "Number of Optimization Iterations",
    min_value=30,
    max_value=100,
    value=60,
    step=10,
    key="part52_iterations"
)

run_part52 = st.button(
    "📈 Run QPSO Scalability Analysis",
    key="part52_button"
)


# ------------------------------------------------------------
# RUN SCALABILITY EXPERIMENT
# ------------------------------------------------------------

if run_part52:

    with st.spinner(
        "Testing QPSO with increasing numbers of delivery locations..."
    ):

        random.seed(52)

        location_sizes52 = [
            size for size in [5, 10, 15, 20, 25]
            if size <= max_locations52
        ]

        scalability_results52 = []

        for delivery_count52 in location_sizes52:

            # ------------------------------------------------
            # CREATE TEST ROAD NETWORK
            # ------------------------------------------------

            G52 = nx.Graph()

            nodes52 = [
                f"N{i}"
                for i in range(delivery_count52 + 1)
            ]

            depot52 = nodes52[0]

            G52.add_nodes_from(nodes52)

            # Guaranteed connected backbone
            for i in range(len(nodes52) - 1):

                u52 = nodes52[i]
                v52 = nodes52[i + 1]

                G52.add_edge(
                    u52,
                    v52,
                    weight=random.randint(3, 15)
                )

            # Additional roads
            for i in range(len(nodes52)):

                for j in range(i + 2, len(nodes52)):

                    if random.random() < 0.20:

                        G52.add_edge(
                            nodes52[i],
                            nodes52[j],
                            weight=random.randint(3, 20)
                        )


            # ------------------------------------------------
            # DELIVERY LOCATIONS
            # ------------------------------------------------

            delivery_points52 = nodes52[1:]


            # ------------------------------------------------
            # RUN QPSO
            # ------------------------------------------------

            start_time52 = time.perf_counter()

            route52, cost52, convergence52 = (
                qpso_vrp_optimization(
                    G52,
                    depot52,
                    delivery_points52,
                    particles=particles52,
                    iterations=iterations52
                )
            )

            end_time52 = time.perf_counter()

            runtime52 = end_time52 - start_time52


            # ------------------------------------------------
            # STORE RESULTS
            # ------------------------------------------------

            scalability_results52.append({
                "Delivery Locations": delivery_count52,
                "Objective Cost": round(cost52, 4),
                "Runtime (seconds)": round(runtime52, 6),
                "Iterations": len(convergence52)
            })


        # ----------------------------------------------------
        # DISPLAY RESULTS
        # ----------------------------------------------------

        st.success(
            "QPSO scalability experiment completed successfully."
        )

        st.subheader("Scalability Results")

        st.table(scalability_results52)


        # ----------------------------------------------------
        # PREPARE DATA
        # ----------------------------------------------------

        sizes52 = [
            row["Delivery Locations"]
            for row in scalability_results52
        ]

        costs52 = [
            row["Objective Cost"]
            for row in scalability_results52
        ]

        runtimes52 = [
            row["Runtime (seconds)"]
            for row in scalability_results52
        ]


        # ----------------------------------------------------
        # OBJECTIVE COST GRAPH
        # ----------------------------------------------------

        st.subheader("Objective Cost vs Delivery Locations")

        fig52_cost, ax52_cost = plt.subplots(
            figsize=(8, 5)
        )

        ax52_cost.plot(
            sizes52,
            costs52,
            marker="o",
            linewidth=2
        )

        ax52_cost.set_title(
            "QPSO Objective Cost vs Delivery Locations"
        )

        ax52_cost.set_xlabel(
            "Number of Delivery Locations"
        )

        ax52_cost.set_ylabel(
            "Objective Cost"
        )

        ax52_cost.grid(
            True,
            alpha=0.3
        )

        st.pyplot(fig52_cost)

        plt.close(fig52_cost)


        # ----------------------------------------------------
        # RUNTIME GRAPH
        # ----------------------------------------------------

        st.subheader("Runtime vs Delivery Locations")

        fig52_runtime, ax52_runtime = plt.subplots(
            figsize=(8, 5)
        )

        ax52_runtime.plot(
            sizes52,
            runtimes52,
            marker="o",
            linewidth=2
        )

        ax52_runtime.set_title(
            "QPSO Runtime vs Delivery Locations"
        )

        ax52_runtime.set_xlabel(
            "Number of Delivery Locations"
        )

        ax52_runtime.set_ylabel(
            "Runtime (seconds)"
        )

        ax52_runtime.grid(
            True,
            alpha=0.3
        )

        st.pyplot(fig52_runtime)

        plt.close(fig52_runtime)


        # ----------------------------------------------------
        # FINAL OBSERVATION
        # ----------------------------------------------------

        st.subheader("Scalability Observation")

        st.info(
            "As the number of delivery locations increases, the "
            "routing problem becomes more complex. QPSO is tested "
            "on progressively larger problem sizes to observe how "
            "objective cost and computation time change."
        )


        # ----------------------------------------------------
        # EXPERIMENT CONFIGURATION
        # ----------------------------------------------------

        st.subheader("Experiment Configuration")

        st.write(
            f"Maximum delivery locations: **{max_locations52}**"
        )

        st.write(
            f"QPSO particles: **{particles52}**"
        )

        st.write(
            f"Optimization iterations: **{iterations52}**"
        )

        st.write(
            "Each test uses a connected simulated road network "
            "with randomly generated road costs."
        )


st.success("PART 52 COMPLETE")

# ============================================================
# PART 53 - QPSO VS CLASSICAL PSO SCALABILITY COMPARISON
# ============================================================

st.markdown("---")

st.header("📊 Part 53 — QPSO vs Classical PSO Scalability Comparison")

st.write(
    "This experiment compares QPSO and the Classical PSO-style "
    "baseline as the number of delivery locations increases."
)


# ------------------------------------------------------------
# USER CONTROLS
# ------------------------------------------------------------

runs53 = st.slider(
    "Number of Runs for Each Problem Size",
    min_value=1,
    max_value=10,
    value=3,
    step=1,
    key="part53_runs"
)

particles53 = st.slider(
    "Number of Particles",
    min_value=10,
    max_value=40,
    value=20,
    step=5,
    key="part53_particles"
)

iterations53 = st.slider(
    "Number of Optimization Iterations",
    min_value=30,
    max_value=100,
    value=60,
    step=10,
    key="part53_iterations"
)

run_part53 = st.button(
    "📊 Run Scalability Comparison",
    key="part53_button"
)


# ------------------------------------------------------------
# RUN EXPERIMENT
# ------------------------------------------------------------

if run_part53:

    with st.spinner(
        "Comparing QPSO and Classical PSO-style scalability..."
    ):

        random.seed(53)

        problem_sizes53 = [5, 10, 15, 20]

        qpso_costs53 = []
        pso_costs53 = []

        qpso_times53 = []
        pso_times53 = []

        comparison_rows53 = []


        # ----------------------------------------------------
        # TEST EACH PROBLEM SIZE
        # ----------------------------------------------------

        for delivery_count53 in problem_sizes53:

            qpso_cost_list53 = []
            pso_cost_list53 = []

            qpso_time_list53 = []
            pso_time_list53 = []


            # ------------------------------------------------
            # MULTIPLE RUNS
            # ------------------------------------------------

            for run53 in range(runs53):

                # --------------------------------------------
                # CREATE CONNECTED TEST NETWORK
                # --------------------------------------------

                G53 = nx.Graph()

                nodes53 = [
                    f"N{i}"
                    for i in range(delivery_count53 + 1)
                ]

                depot53 = nodes53[0]

                G53.add_nodes_from(nodes53)


                # Guaranteed connected backbone
                for i in range(len(nodes53) - 1):

                    u53 = nodes53[i]
                    v53 = nodes53[i + 1]

                    G53.add_edge(
                        u53,
                        v53,
                        weight=random.randint(3, 15)
                    )


                # Additional roads
                for i in range(len(nodes53)):

                    for j in range(i + 2, len(nodes53)):

                        if random.random() < 0.20:

                            G53.add_edge(
                                nodes53[i],
                                nodes53[j],
                                weight=random.randint(3, 20)
                            )


                delivery_points53 = nodes53[1:]


                # --------------------------------------------
                # QPSO
                # --------------------------------------------

                start_qpso53 = time.perf_counter()

                (
                    qpso_route53,
                    qpso_cost53,
                    qpso_convergence53
                ) = qpso_vrp_optimization(
                    G53,
                    depot53,
                    delivery_points53,
                    particles=particles53,
                    iterations=iterations53
                )

                end_qpso53 = time.perf_counter()

                qpso_runtime53 = (
                    end_qpso53 - start_qpso53
                )

                qpso_cost_list53.append(qpso_cost53)
                qpso_time_list53.append(qpso_runtime53)


                # --------------------------------------------
                # CLASSICAL PSO-STYLE
                # --------------------------------------------

                start_pso53 = time.perf_counter()

                (
                    pso_route53,
                    pso_cost53,
                    pso_convergence53
                ) = pso_vrp_optimization(
                    G53,
                    depot53,
                    delivery_points53,
                    particles=particles53,
                    iterations=iterations53
                )

                end_pso53 = time.perf_counter()

                pso_runtime53 = (
                    end_pso53 - start_pso53
                )

                pso_cost_list53.append(pso_cost53)
                pso_time_list53.append(pso_runtime53)


            # ------------------------------------------------
            # AVERAGES
            # ------------------------------------------------

            avg_qpso_cost53 = statistics.mean(
                qpso_cost_list53
            )

            avg_pso_cost53 = statistics.mean(
                pso_cost_list53
            )

            avg_qpso_time53 = statistics.mean(
                qpso_time_list53
            )

            avg_pso_time53 = statistics.mean(
                pso_time_list53
            )


            # ------------------------------------------------
            # STORE
            # ------------------------------------------------

            qpso_costs53.append(avg_qpso_cost53)
            pso_costs53.append(avg_pso_cost53)

            qpso_times53.append(avg_qpso_time53)
            pso_times53.append(avg_pso_time53)


            comparison_rows53.append({
                "Delivery Locations": delivery_count53,
                "QPSO Avg Cost": round(
                    avg_qpso_cost53, 4
                ),
                "PSO Avg Cost": round(
                    avg_pso_cost53, 4
                ),
                "QPSO Avg Runtime (s)": round(
                    avg_qpso_time53, 6
                ),
                "PSO Avg Runtime (s)": round(
                    avg_pso_time53, 6
                )
            })


        # ----------------------------------------------------
        # RESULTS
        # ----------------------------------------------------

        st.success(
            "Scalability comparison completed successfully."
        )

        st.subheader(
            "QPSO vs Classical PSO-style Results"
        )

        st.table(comparison_rows53)


        # ----------------------------------------------------
        # COST COMPARISON GRAPH
        # ----------------------------------------------------

        st.subheader(
            "Objective Cost vs Delivery Locations"
        )

        fig53_cost, ax53_cost = plt.subplots(
            figsize=(8, 5)
        )

        ax53_cost.plot(
            problem_sizes53,
            qpso_costs53,
            marker="o",
            linewidth=2,
            label="QPSO"
        )

        ax53_cost.plot(
            problem_sizes53,
            pso_costs53,
            marker="o",
            linewidth=2,
            label="Classical PSO-style"
        )

        ax53_cost.set_title(
            "QPSO vs Classical PSO-style: Objective Cost"
        )

        ax53_cost.set_xlabel(
            "Number of Delivery Locations"
        )

        ax53_cost.set_ylabel(
            "Average Objective Cost"
        )

        ax53_cost.legend()

        ax53_cost.grid(
            True,
            alpha=0.3
        )

        st.pyplot(fig53_cost)

        plt.close(fig53_cost)


        # ----------------------------------------------------
        # RUNTIME COMPARISON GRAPH
        # ----------------------------------------------------

        st.subheader(
            "Runtime vs Delivery Locations"
        )

        fig53_runtime, ax53_runtime = plt.subplots(
            figsize=(8, 5)
        )

        ax53_runtime.plot(
            problem_sizes53,
            qpso_times53,
            marker="o",
            linewidth=2,
            label="QPSO"
        )

        ax53_runtime.plot(
            problem_sizes53,
            pso_times53,
            marker="o",
            linewidth=2,
            label="Classical PSO-style"
        )

        ax53_runtime.set_title(
            "QPSO vs Classical PSO-style: Runtime"
        )

        ax53_runtime.set_xlabel(
            "Number of Delivery Locations"
        )

        ax53_runtime.set_ylabel(
            "Average Runtime (seconds)"
        )

        ax53_runtime.legend()

        ax53_runtime.grid(
            True,
            alpha=0.3
        )

        st.pyplot(fig53_runtime)

        plt.close(fig53_runtime)


        # ----------------------------------------------------
        # INTERPRETATION
        # ----------------------------------------------------

        st.subheader("Scalability Interpretation")

        st.info(
            "As the number of delivery locations increases, the "
            "vehicle routing problem becomes more computationally "
            "complex. This experiment compares how QPSO and the "
            "Classical PSO-style baseline behave under increasing "
            "problem sizes."
        )


        # ----------------------------------------------------
        # CONFIGURATION
        # ----------------------------------------------------

        st.subheader("Experiment Configuration")

        st.write(
            f"Problem sizes tested: **{problem_sizes53}**"
        )

        st.write(
            f"Runs per problem size: **{runs53}**"
        )

        st.write(
            f"Particles: **{particles53}**"
        )

        st.write(
            f"Iterations: **{iterations53}**"
        )

        st.write(
            "Both algorithms use the same network, delivery "
            "locations and optimization settings for each test."
        )


st.success("PART 53 COMPLETE")

# ============================================================
# PART 54 - QPSO PARAMETER SENSITIVITY ANALYSIS
# ============================================================

st.markdown("---")

st.header("⚙️ Part 54 — QPSO Parameter Sensitivity Analysis")

st.write(
    "This experiment studies how the number of QPSO particles "
    "affects optimization quality and computational runtime."
)


# ------------------------------------------------------------
# USER CONTROLS
# ------------------------------------------------------------

runs54 = st.slider(
    "Number of Runs",
    min_value=1,
    max_value=10,
    value=3,
    step=1,
    key="part54_runs"
)

iterations54 = st.slider(
    "Number of Optimization Iterations",
    min_value=30,
    max_value=150,
    value=60,
    step=10,
    key="part54_iterations"
)

run_part54 = st.button(
    "⚙️ Run Parameter Sensitivity Analysis",
    key="part54_button"
)


# ------------------------------------------------------------
# RUN EXPERIMENT
# ------------------------------------------------------------

if run_part54:

    with st.spinner(
        "Testing QPSO with different particle populations..."
    ):

        random.seed(54)

        particle_values54 = [10, 20, 30, 40]

        cost_results54 = []
        runtime_results54 = []

        rows54 = []


        # ----------------------------------------------------
        # TEST DIFFERENT PARTICLE COUNTS
        # ----------------------------------------------------

        for particles54 in particle_values54:

            cost_list54 = []
            runtime_list54 = []


            # ------------------------------------------------
            # MULTIPLE RUNS
            # ------------------------------------------------

            for run54 in range(runs54):

                start54 = time.perf_counter()


                route54, cost54, convergence54 = (
                    qpso_vrp_optimization(
                        G31,
                        "A",
                        ["B", "C", "D", "E", "F"],
                        particles=particles54,
                        iterations=iterations54
                    )
                )


                end54 = time.perf_counter()

                runtime54 = end54 - start54

                cost_list54.append(cost54)
                runtime_list54.append(runtime54)


            # ------------------------------------------------
            # STATISTICS
            # ------------------------------------------------

            average_cost54 = statistics.mean(
                cost_list54
            )

            best_cost54 = min(
                cost_list54
            )

            average_runtime54 = statistics.mean(
                runtime_list54
            )


            # ------------------------------------------------
            # STORE RESULTS
            # ------------------------------------------------

            cost_results54.append(
                average_cost54
            )

            runtime_results54.append(
                average_runtime54
            )


            rows54.append({
                "QPSO Particles": particles54,
                "Average Cost": round(
                    average_cost54,
                    4
                ),
                "Best Cost": round(
                    best_cost54,
                    4
                ),
                "Average Runtime (s)": round(
                    average_runtime54,
                    6
                )
            })


        # ----------------------------------------------------
        # RESULTS TABLE
        # ----------------------------------------------------

        st.success(
            "QPSO parameter sensitivity experiment completed successfully."
        )

        st.subheader(
            "Parameter Sensitivity Results"
        )

        st.table(rows54)


        # ----------------------------------------------------
        # OBJECTIVE COST GRAPH
        # ----------------------------------------------------

        st.subheader(
            "Objective Cost vs Number of QPSO Particles"
        )

        fig54_cost, ax54_cost = plt.subplots(
            figsize=(8, 5)
        )

        ax54_cost.plot(
            particle_values54,
            cost_results54,
            marker="o",
            linewidth=2
        )

        ax54_cost.set_title(
            "QPSO Objective Cost vs Number of Particles"
        )

        ax54_cost.set_xlabel(
            "Number of QPSO Particles"
        )

        ax54_cost.set_ylabel(
            "Average Objective Cost"
        )

        ax54_cost.grid(
            True,
            alpha=0.3
        )

        st.pyplot(fig54_cost)

        plt.close(fig54_cost)


        # ----------------------------------------------------
        # RUNTIME GRAPH
        # ----------------------------------------------------

        st.subheader(
            "Runtime vs Number of QPSO Particles"
        )

        fig54_runtime, ax54_runtime = plt.subplots(
            figsize=(8, 5)
        )

        ax54_runtime.plot(
            particle_values54,
            runtime_results54,
            marker="o",
            linewidth=2
        )

        ax54_runtime.set_title(
            "QPSO Runtime vs Number of Particles"
        )

        ax54_runtime.set_xlabel(
            "Number of QPSO Particles"
        )

        ax54_runtime.set_ylabel(
            "Average Runtime (seconds)"
        )

        ax54_runtime.grid(
            True,
            alpha=0.3
        )

        st.pyplot(fig54_runtime)

        plt.close(fig54_runtime)


        # ----------------------------------------------------
        # INTERPRETATION
        # ----------------------------------------------------

        st.subheader(
            "Parameter Sensitivity Observation"
        )

        st.info(
            "Increasing the number of particles gives QPSO more "
            "candidate solutions to explore. However, a larger "
            "particle population also increases computational "
            "work per optimization iteration."
        )


        # ----------------------------------------------------
        # EXPERIMENT CONFIGURATION
        # ----------------------------------------------------

        st.subheader(
            "Experiment Configuration"
        )

        st.write(
            "Particle values tested: **[10, 20, 30, 40]**"
        )

        st.write(
            f"Runs for each particle setting: **{runs54}**"
        )

        st.write(
            f"Optimization iterations: **{iterations54}**"
        )

        st.write(
            "The same road network, depot and delivery locations "
            "were used for every particle configuration."
        )


st.success("PART 54 COMPLETE")

# ============================================================
# PART 55 - QPSO ITERATION SENSITIVITY ANALYSIS
# ============================================================

st.markdown("---")

st.header("🔄 Part 55 — QPSO Iteration Sensitivity Analysis")

st.write(
    "This experiment studies how the number of optimization "
    "iterations affects QPSO solution quality and computational runtime."
)


# ------------------------------------------------------------
# USER CONTROLS
# ------------------------------------------------------------

runs55 = st.slider(
    "Number of Runs",
    min_value=1,
    max_value=10,
    value=3,
    step=1,
    key="part55_runs"
)

particles55 = st.slider(
    "Number of QPSO Particles",
    min_value=10,
    max_value=50,
    value=30,
    step=10,
    key="part55_particles"
)

run_part55 = st.button(
    "🔄 Run Iteration Sensitivity Analysis",
    key="part55_button"
)


# ------------------------------------------------------------
# RUN EXPERIMENT
# ------------------------------------------------------------

if run_part55:

    with st.spinner(
        "Testing QPSO with different numbers of iterations..."
    ):

        random.seed(55)

        iteration_values55 = [20, 40, 60, 80, 100]

        cost_results55 = []
        runtime_results55 = []

        rows55 = []


        # ----------------------------------------------------
        # TEST DIFFERENT ITERATION COUNTS
        # ----------------------------------------------------

        for iterations_test55 in iteration_values55:

            cost_list55 = []
            runtime_list55 = []


            # ------------------------------------------------
            # MULTIPLE RUNS
            # ------------------------------------------------

            for run55 in range(runs55):

                start55 = time.perf_counter()


                route55, cost55, convergence55 = (
                    qpso_vrp_optimization(
                        G31,
                        "A",
                        ["B", "C", "D", "E", "F"],
                        particles=particles55,
                        iterations=iterations_test55
                    )
                )


                end55 = time.perf_counter()

                runtime55 = end55 - start55

                cost_list55.append(cost55)
                runtime_list55.append(runtime55)


            # ------------------------------------------------
            # CALCULATE STATISTICS
            # ------------------------------------------------

            average_cost55 = statistics.mean(
                cost_list55
            )

            best_cost55 = min(
                cost_list55
            )

            average_runtime55 = statistics.mean(
                runtime_list55
            )


            # ------------------------------------------------
            # STORE RESULTS
            # ------------------------------------------------

            cost_results55.append(
                average_cost55
            )

            runtime_results55.append(
                average_runtime55
            )


            rows55.append({
                "Optimization Iterations": iterations_test55,
                "Average Cost": round(
                    average_cost55,
                    4
                ),
                "Best Cost": round(
                    best_cost55,
                    4
                ),
                "Average Runtime (s)": round(
                    average_runtime55,
                    6
                )
            })


        # ----------------------------------------------------
        # RESULTS TABLE
        # ----------------------------------------------------

        st.success(
            "QPSO iteration sensitivity experiment completed successfully."
        )

        st.subheader(
            "Iteration Sensitivity Results"
        )

        st.table(rows55)


        # ----------------------------------------------------
        # OBJECTIVE COST GRAPH
        # ----------------------------------------------------

        st.subheader(
            "Objective Cost vs Optimization Iterations"
        )

        fig55_cost, ax55_cost = plt.subplots(
            figsize=(8, 5)
        )

        ax55_cost.plot(
            iteration_values55,
            cost_results55,
            marker="o",
            linewidth=2
        )

        ax55_cost.set_title(
            "QPSO Objective Cost vs Optimization Iterations"
        )

        ax55_cost.set_xlabel(
            "Number of Optimization Iterations"
        )

        ax55_cost.set_ylabel(
            "Average Objective Cost"
        )

        ax55_cost.grid(
            True,
            alpha=0.3
        )

        st.pyplot(fig55_cost)

        plt.close(fig55_cost)


        # ----------------------------------------------------
        # RUNTIME GRAPH
        # ----------------------------------------------------

        st.subheader(
            "Runtime vs Optimization Iterations"
        )

        fig55_runtime, ax55_runtime = plt.subplots(
            figsize=(8, 5)
        )

        ax55_runtime.plot(
            iteration_values55,
            runtime_results55,
            marker="o",
            linewidth=2
        )

        ax55_runtime.set_title(
            "QPSO Runtime vs Optimization Iterations"
        )

        ax55_runtime.set_xlabel(
            "Number of Optimization Iterations"
        )

        ax55_runtime.set_ylabel(
            "Average Runtime (seconds)"
        )

        ax55_runtime.grid(
            True,
            alpha=0.3
        )

        st.pyplot(fig55_runtime)

        plt.close(fig55_runtime)


        # ----------------------------------------------------
        # INTERPRETATION
        # ----------------------------------------------------

        st.subheader(
            "Iteration Sensitivity Observation"
        )

        st.info(
            "Increasing the number of optimization iterations gives "
            "QPSO more opportunities to improve the candidate solution. "
            "However, additional iterations also increase computational "
            "runtime. The experiment helps identify a practical balance "
            "between optimization quality and computation time."
        )


        # ----------------------------------------------------
        # EXPERIMENT CONFIGURATION
        # ----------------------------------------------------

        st.subheader(
            "Experiment Configuration"
        )

        st.write(
            "Iteration values tested: **[20, 40, 60, 80, 100]**"
        )

        st.write(
            f"QPSO particles: **{particles55}**"
        )

        st.write(
            f"Runs for each iteration setting: **{runs55}**"
        )

        st.write(
            "The same road network, depot and delivery locations "
            "were used for every test."
        )


st.success("PART 55 COMPLETE")

# ============================================================
# PART 56 - FINAL TRAFFIC CONDITION PERFORMANCE COMPARISON
# ============================================================

print()
print("=" * 70)
print("PART 56 - FINAL TRAFFIC CONDITION PERFORMANCE COMPARISON")
print("=" * 70)

st.header("📊 Part 56 — Final Traffic Condition Performance Comparison")

st.write(
    "This experiment compares QPSO performance under normal, "
    "moderate and heavy traffic conditions."
)

# ------------------------------------------------------------
# 1. CREATE THREE TRAFFIC CONDITIONS
# ------------------------------------------------------------

G56_normal = G17.copy()

G56_moderate = G17.copy()

G56_heavy = G17.copy()


# ------------------------------------------------------------
# 2. APPLY MODERATE TRAFFIC
# ------------------------------------------------------------

traffic_edges56 = [
    ("A", "C"),
    ("C", "E"),
    ("E", "G"),
    ("G", "I")
]

for u, v in traffic_edges56:

    if G56_moderate.has_edge(u, v):
        G56_moderate[u][v]["weight"] *= 2


# ------------------------------------------------------------
# 3. APPLY HEAVY TRAFFIC
# ------------------------------------------------------------

for u, v in traffic_edges56:

    if G56_heavy.has_edge(u, v):
        G56_heavy[u][v]["weight"] *= 4


# ------------------------------------------------------------
# 4. RUN QPSO FOR EACH CONDITION
# ------------------------------------------------------------

conditions56 = {
    "Normal": G56_normal,
    "Moderate": G56_moderate,
    "Heavy": G56_heavy
}

results56 = []

for condition_name, graph56 in conditions56.items():

    start_time56 = time.time()

    route56, cost56, convergence56 = qpso_vrp_optimization(
        graph56,
        "A",
        delivery_points14,
        particles=30,
        iterations=100
    )

    runtime56 = time.time() - start_time56

    results56.append({
        "Traffic Condition": condition_name,
        "Objective Cost": round(cost56, 4),
        "Runtime (seconds)": round(runtime56, 4),
        "Iterations": len(convergence56),
        "Route": " → ".join(route56)
    })


# ------------------------------------------------------------
# 5. DISPLAY RESULTS
# ------------------------------------------------------------

st.success(
    "Final traffic condition comparison completed successfully."
)

st.subheader("Traffic Condition Results")

st.table(results56)


# ------------------------------------------------------------
# 6. EXTRACT VALUES FOR GRAPH
# ------------------------------------------------------------

condition_names56 = [
    row["Traffic Condition"]
    for row in results56
]

cost_values56 = [
    row["Objective Cost"]
    for row in results56
]

runtime_values56 = [
    row["Runtime (seconds)"]
    for row in results56
]


# ------------------------------------------------------------
# 7. OBJECTIVE COST GRAPH
# ------------------------------------------------------------

st.subheader("Objective Cost vs Traffic Condition")

fig56_cost, ax56_cost = plt.subplots(figsize=(10, 5))

ax56_cost.bar(
    condition_names56,
    cost_values56
)

ax56_cost.set_title(
    "QPSO Objective Cost Under Different Traffic Conditions"
)

ax56_cost.set_xlabel("Traffic Condition")

ax56_cost.set_ylabel("Objective Cost")

ax56_cost.grid(axis="y", alpha=0.3)

st.pyplot(fig56_cost)

plt.close(fig56_cost)


# ------------------------------------------------------------
# 8. RUNTIME GRAPH
# ------------------------------------------------------------

st.subheader("QPSO Runtime vs Traffic Condition")

fig56_runtime, ax56_runtime = plt.subplots(figsize=(10, 5))

ax56_runtime.plot(
    condition_names56,
    runtime_values56,
    marker="o",
    linewidth=2
)

ax56_runtime.set_title(
    "QPSO Runtime Under Different Traffic Conditions"
)

ax56_runtime.set_xlabel("Traffic Condition")

ax56_runtime.set_ylabel("Runtime (seconds)")

ax56_runtime.grid(True, alpha=0.3)

st.pyplot(fig56_runtime)

plt.close(fig56_runtime)


# ------------------------------------------------------------
# 9. INTERPRETATION
# ------------------------------------------------------------

st.subheader("Traffic Performance Interpretation")

st.info(
    "As traffic becomes more congested, the objective cost can increase "
    "because affected roads become more expensive to use. QPSO evaluates "
    "the modified traffic-weighted network and searches for a suitable "
    "vehicle route under each traffic condition."
)


# ------------------------------------------------------------
# 10. EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

st.subheader("Experiment Configuration")

st.write("Traffic conditions tested: Normal, Moderate, Heavy")

st.write("QPSO particles: 30")

st.write("Optimization iterations: 100")

st.write(
    "The same depot and delivery locations were used for all traffic conditions."
)


# ------------------------------------------------------------
# 11. COMPLETION
# ------------------------------------------------------------

st.success("PART 56 COMPLETE")

print("PART 56 COMPLETE")


# ============================================================
# PART 57 - TRAFFIC REROUTING EFFECTIVENESS ANALYSIS
# ============================================================

print()
print("=" * 70)
print("PART 57 - TRAFFIC REROUTING EFFECTIVENESS ANALYSIS")
print("=" * 70)

st.header("🚦 Part 57 — Traffic Rerouting Effectiveness Analysis")

st.write(
    "This experiment studies how increasing traffic on selected roads "
    "can change the shortest route between two locations."
)

# ------------------------------------------------------------
# 1. CREATE TRAFFIC NETWORKS
# ------------------------------------------------------------

G57_normal = G17.copy()
G57_moderate = G17.copy()
G57_heavy = G17.copy()


# ------------------------------------------------------------
# 2. SELECT TRAFFIC-AFFECTED ROADS
# ------------------------------------------------------------

traffic_edges57 = [
    ("A", "C"),
    ("C", "E"),
    ("E", "G"),
    ("G", "I")
]


# ------------------------------------------------------------
# 3. APPLY MODERATE TRAFFIC
# ------------------------------------------------------------

for u, v in traffic_edges57:

    if G57_moderate.has_edge(u, v):
        G57_moderate[u][v]["weight"] *= 2


# ------------------------------------------------------------
# 4. APPLY HEAVY TRAFFIC
# ------------------------------------------------------------

for u, v in traffic_edges57:

    if G57_heavy.has_edge(u, v):
        G57_heavy[u][v]["weight"] *= 4


# ------------------------------------------------------------
# 5. DEFINE ORIGIN AND DESTINATION
# ------------------------------------------------------------

origin57 = "A"
destination57 = "I"


# ------------------------------------------------------------
# 6. CALCULATE SHORTEST ROUTES
# ------------------------------------------------------------

traffic_graphs57 = {
    "Normal": G57_normal,
    "Moderate": G57_moderate,
    "Heavy": G57_heavy
}

rerouting_results57 = []

for condition57, graph57 in traffic_graphs57.items():

    try:

        route57 = nx.shortest_path(
            graph57,
            origin57,
            destination57,
            weight="weight"
        )

        cost57 = nx.shortest_path_length(
            graph57,
            origin57,
            destination57,
            weight="weight"
        )

        rerouting_results57.append({
            "Traffic Condition": condition57,
            "Route": " → ".join(route57),
            "Route Cost": round(cost57, 4)
        })

    except nx.NetworkXNoPath:

        rerouting_results57.append({
            "Traffic Condition": condition57,
            "Route": "No valid route",
            "Route Cost": float("inf")
        })


# ------------------------------------------------------------
# 7. DISPLAY RESULTS
# ------------------------------------------------------------

st.success(
    "Traffic rerouting experiment completed successfully."
)

st.subheader("Rerouting Results")

st.table(rerouting_results57)


# ------------------------------------------------------------
# 8. CHECK WHETHER ROUTE CHANGED
# ------------------------------------------------------------

normal_route57 = rerouting_results57[0]["Route"]
moderate_route57 = rerouting_results57[1]["Route"]
heavy_route57 = rerouting_results57[2]["Route"]

route_changed57 = (
    normal_route57 != moderate_route57
    or normal_route57 != heavy_route57
)


if route_changed57:

    st.success(
        "Traffic caused the shortest route to change. "
        "This demonstrates dynamic rerouting."
    )

else:

    st.info(
        "The shortest route did not change for this network configuration. "
        "The experiment still confirms that traffic-weighted routing "
        "was evaluated under three conditions."
    )


# ------------------------------------------------------------
# 9. ROUTE COST GRAPH
# ------------------------------------------------------------

st.subheader("Route Cost Under Traffic Conditions")

condition_labels57 = [
    row["Traffic Condition"]
    for row in rerouting_results57
]

cost_labels57 = [
    row["Route Cost"]
    for row in rerouting_results57
]

fig57, ax57 = plt.subplots(figsize=(10, 5))

ax57.plot(
    condition_labels57,
    cost_labels57,
    marker="o",
    linewidth=2
)

ax57.set_title(
    "Shortest Route Cost Under Different Traffic Conditions"
)

ax57.set_xlabel("Traffic Condition")

ax57.set_ylabel("Route Cost")

ax57.grid(True, alpha=0.3)

st.pyplot(fig57)

plt.close(fig57)


# ------------------------------------------------------------
# 10. ROUTE COMPARISON
# ------------------------------------------------------------

st.subheader("Route Comparison")

st.write(
    f"Origin: {origin57}"
)

st.write(
    f"Destination: {destination57}"
)

st.write(
    f"Normal traffic route: {normal_route57}"
)

st.write(
    f"Moderate traffic route: {moderate_route57}"
)

st.write(
    f"Heavy traffic route: {heavy_route57}"
)


# ------------------------------------------------------------
# 11. INTERPRETATION
# ------------------------------------------------------------

st.subheader("Rerouting Interpretation")

st.info(
    "When traffic increases, the weights of affected roads increase. "
    "The routing system therefore evaluates alternative paths. "
    "If an alternative path becomes cheaper, the route is changed "
    "to avoid the congested roads."
)


# ------------------------------------------------------------
# 12. EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

st.subheader("Experiment Configuration")

st.write(
    "Origin: A"
)

st.write(
    "Destination: I"
)

st.write(
    "Traffic conditions: Normal, Moderate, Heavy"
)

st.write(
    "Moderate traffic multiplier: 2×"
)

st.write(
    "Heavy traffic multiplier: 4×"
)

st.write(
    "Routing method: Weighted shortest-path analysis"
)


# ------------------------------------------------------------
# 13. COMPLETION
# ------------------------------------------------------------

st.success("PART 57 COMPLETE")

print("PART 57 COMPLETE")

# ============================================================
# PART 58 - QPSO TRAFFIC STRESS TEST
# ============================================================

print()
print("=" * 70)
print("PART 58 - QPSO TRAFFIC STRESS TEST")
print("=" * 70)

st.header("🚦 Part 58 — QPSO Traffic Stress Test")

st.write(
    "This experiment tests the robustness of QPSO when different "
    "traffic disturbances are introduced into the road network."
)


# ------------------------------------------------------------
# 1. EXPERIMENT SETTINGS
# ------------------------------------------------------------

NUM_SCENARIOS58 = 5
PARTICLES58 = 30
ITERATIONS58 = 100

random.seed(58)


# ------------------------------------------------------------
# 2. CREATE TRAFFIC SCENARIOS
# ------------------------------------------------------------

traffic_scenarios58 = []

base_edges58 = list(G17.edges())

for scenario_index58 in range(1, NUM_SCENARIOS58 + 1):

    graph58 = G17.copy()

    # Select several roads for traffic disturbance
    number_of_affected_edges58 = min(
        3,
        len(base_edges58)
    )

    selected_edges58 = random.sample(
        base_edges58,
        number_of_affected_edges58
    )

    affected_roads58 = []

    for u58, v58 in selected_edges58:

        multiplier58 = random.uniform(1.5, 3.0)

        graph58[u58][v58]["weight"] *= multiplier58

        affected_roads58.append(
            f"{u58}-{v58}"
        )

    traffic_scenarios58.append(
        (
            f"Scenario {scenario_index58}",
            graph58,
            affected_roads58
        )
    )


# ------------------------------------------------------------
# 3. RUN QPSO ON EACH SCENARIO
# ------------------------------------------------------------

stress_results58 = []

for scenario_name58, graph58, affected_roads58 in traffic_scenarios58:

    start_time58 = time.time()

    route58, cost58, convergence58 = qpso_vrp_optimization(
        graph58,
        "A",
        delivery_points14,
        particles=PARTICLES58,
        iterations=ITERATIONS58
    )

    runtime58 = time.time() - start_time58

    stress_results58.append({
        "Scenario": scenario_name58,
        "Affected Roads": ", ".join(affected_roads58),
        "Objective Cost": round(cost58, 4),
        "Runtime (seconds)": round(runtime58, 4),
        "Iterations": len(convergence58),
        "Route": " → ".join(route58)
    })


# ------------------------------------------------------------
# 4. DISPLAY RESULTS
# ------------------------------------------------------------

st.success(
    "QPSO traffic stress test completed successfully."
)

st.subheader("Traffic Stress Test Results")

st.table(stress_results58)


# ------------------------------------------------------------
# 5. CALCULATE STATISTICS
# ------------------------------------------------------------

stress_costs58 = [
    row["Objective Cost"]
    for row in stress_results58
]

stress_runtimes58 = [
    row["Runtime (seconds)"]
    for row in stress_results58
]

average_cost58 = statistics.mean(
    stress_costs58
)

best_cost58 = min(
    stress_costs58
)

worst_cost58 = max(
    stress_costs58
)

cost_std58 = (
    statistics.stdev(stress_costs58)
    if len(stress_costs58) > 1
    else 0
)

average_runtime58 = statistics.mean(
    stress_runtimes58
)


# ------------------------------------------------------------
# 6. STATISTICAL SUMMARY
# ------------------------------------------------------------

st.subheader("Stress Test Statistical Summary")

summary58 = [
    {
        "Metric": "Average Objective Cost",
        "Value": round(average_cost58, 4)
    },
    {
        "Metric": "Best Objective Cost",
        "Value": round(best_cost58, 4)
    },
    {
        "Metric": "Worst Objective Cost",
        "Value": round(worst_cost58, 4)
    },
    {
        "Metric": "Standard Deviation",
        "Value": round(cost_std58, 4)
    },
    {
        "Metric": "Average Runtime (seconds)",
        "Value": round(average_runtime58, 4)
    }
]

st.table(summary58)


# ------------------------------------------------------------
# 7. OBJECTIVE COST GRAPH
# ------------------------------------------------------------

st.subheader("Objective Cost Across Traffic Scenarios")

scenario_labels58 = [
    row["Scenario"]
    for row in stress_results58
]

fig58_cost, ax58_cost = plt.subplots(
    figsize=(10, 5)
)

ax58_cost.plot(
    scenario_labels58,
    stress_costs58,
    marker="o",
    linewidth=2
)

ax58_cost.set_title(
    "QPSO Objective Cost Across Traffic Stress Scenarios"
)

ax58_cost.set_xlabel(
    "Traffic Scenario"
)

ax58_cost.set_ylabel(
    "Objective Cost"
)

ax58_cost.grid(
    True,
    alpha=0.3
)

st.pyplot(fig58_cost)

plt.close(fig58_cost)


# ------------------------------------------------------------
# 8. RUNTIME GRAPH
# ------------------------------------------------------------

st.subheader("Runtime Across Traffic Scenarios")

fig58_runtime, ax58_runtime = plt.subplots(
    figsize=(10, 5)
)

ax58_runtime.plot(
    scenario_labels58,
    stress_runtimes58,
    marker="o",
    linewidth=2
)

ax58_runtime.set_title(
    "QPSO Runtime Across Traffic Stress Scenarios"
)

ax58_runtime.set_xlabel(
    "Traffic Scenario"
)

ax58_runtime.set_ylabel(
    "Runtime (seconds)"
)

ax58_runtime.grid(
    True,
    alpha=0.3
)

st.pyplot(fig58_runtime)

plt.close(fig58_runtime)


# ------------------------------------------------------------
# 9. ROBUSTNESS INTERPRETATION
# ------------------------------------------------------------

st.subheader("Robustness Interpretation")

st.info(
    "The stress test introduces different traffic disturbances into "
    "the same road network. QPSO is then executed independently for "
    "each scenario. Comparing the objective cost, runtime and standard "
    "deviation helps evaluate the robustness of the optimization process."
)


# ------------------------------------------------------------
# 10. EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

st.subheader("Experiment Configuration")

st.write(
    f"Number of traffic scenarios: {NUM_SCENARIOS58}"
)

st.write(
    f"QPSO particles: {PARTICLES58}"
)

st.write(
    f"Optimization iterations: {ITERATIONS58}"
)

st.write(
    "Traffic multiplier range: 1.5× to 3.0×"
)

st.write(
    "The same depot and delivery locations were used in every scenario."
)


# ------------------------------------------------------------
# 11. COMPLETION
# ------------------------------------------------------------

st.success("PART 58 COMPLETE")

print("PART 58 COMPLETE")

# ============================================================
# PART 59 - QPSO TRAFFIC ROBUSTNESS ANALYSIS
# ============================================================

print()
print("=" * 70)
print("PART 59 - QPSO TRAFFIC ROBUSTNESS ANALYSIS")
print("=" * 70)

st.header("🛡️ Part 59 — QPSO Traffic Robustness Analysis")

st.write(
    "This experiment evaluates the stability of QPSO across "
    "different traffic stress scenarios using the results obtained "
    "in Part 58."
)


# ------------------------------------------------------------
# 1. USE RESULTS FROM PART 58
# ------------------------------------------------------------

costs59 = [
    row["Objective Cost"]
    for row in stress_results58
]

runtimes59 = [
    row["Runtime (seconds)"]
    for row in stress_results58
]

scenario_names59 = [
    row["Scenario"]
    for row in stress_results58
]


# ------------------------------------------------------------
# 2. BASIC ROBUSTNESS METRICS
# ------------------------------------------------------------

average_cost59 = statistics.mean(costs59)

minimum_cost59 = min(costs59)

maximum_cost59 = max(costs59)

cost_range59 = maximum_cost59 - minimum_cost59

if average_cost59 != 0:
    variation_percentage59 = (
        cost_range59 / average_cost59
    ) * 100
else:
    variation_percentage59 = 0


average_runtime59 = statistics.mean(runtimes59)

minimum_runtime59 = min(runtimes59)

maximum_runtime59 = max(runtimes59)


# ------------------------------------------------------------
# 3. STANDARD DEVIATION
# ------------------------------------------------------------

if len(costs59) > 1:
    cost_std59 = statistics.stdev(costs59)
else:
    cost_std59 = 0


# ------------------------------------------------------------
# 4. ROBUSTNESS TABLE
# ------------------------------------------------------------

robustness_metrics59 = [
    {
        "Metric": "Average Objective Cost",
        "Value": round(average_cost59, 4)
    },
    {
        "Metric": "Minimum Objective Cost",
        "Value": round(minimum_cost59, 4)
    },
    {
        "Metric": "Maximum Objective Cost",
        "Value": round(maximum_cost59, 4)
    },
    {
        "Metric": "Objective Cost Range",
        "Value": round(cost_range59, 4)
    },
    {
        "Metric": "Cost Variation (%)",
        "Value": round(variation_percentage59, 2)
    },
    {
        "Metric": "Cost Standard Deviation",
        "Value": round(cost_std59, 4)
    },
    {
        "Metric": "Average Runtime (seconds)",
        "Value": round(average_runtime59, 4)
    },
    {
        "Metric": "Minimum Runtime (seconds)",
        "Value": round(minimum_runtime59, 4)
    },
    {
        "Metric": "Maximum Runtime (seconds)",
        "Value": round(maximum_runtime59, 4)
    }
]


st.subheader("Robustness Metrics")

st.table(robustness_metrics59)


# ------------------------------------------------------------
# 5. COST STABILITY GRAPH
# ------------------------------------------------------------

st.subheader("Objective Cost Stability")

fig59_cost, ax59_cost = plt.subplots(
    figsize=(10, 5)
)

ax59_cost.plot(
    scenario_names59,
    costs59,
    marker="o",
    linewidth=2,
    label="QPSO Objective Cost"
)

ax59_cost.axhline(
    average_cost59,
    linestyle="--",
    linewidth=2,
    label="Average Cost"
)

ax59_cost.set_title(
    "QPSO Objective Cost Stability Across Traffic Scenarios"
)

ax59_cost.set_xlabel(
    "Traffic Scenario"
)

ax59_cost.set_ylabel(
    "Objective Cost"
)

ax59_cost.legend()

ax59_cost.grid(
    True,
    alpha=0.3
)

st.pyplot(fig59_cost)

plt.close(fig59_cost)


# ------------------------------------------------------------
# 6. RUNTIME STABILITY GRAPH
# ------------------------------------------------------------

st.subheader("Computational Runtime Stability")

fig59_runtime, ax59_runtime = plt.subplots(
    figsize=(10, 5)
)

ax59_runtime.plot(
    scenario_names59,
    runtimes59,
    marker="o",
    linewidth=2,
    label="QPSO Runtime"
)

ax59_runtime.axhline(
    average_runtime59,
    linestyle="--",
    linewidth=2,
    label="Average Runtime"
)

ax59_runtime.set_title(
    "QPSO Runtime Stability Across Traffic Scenarios"
)

ax59_runtime.set_xlabel(
    "Traffic Scenario"
)

ax59_runtime.set_ylabel(
    "Runtime (seconds)"
)

ax59_runtime.legend()

ax59_runtime.grid(
    True,
    alpha=0.3
)

st.pyplot(fig59_runtime)

plt.close(fig59_runtime)


# ------------------------------------------------------------
# 7. ROBUSTNESS INTERPRETATION
# ------------------------------------------------------------

st.subheader("Robustness Interpretation")

if variation_percentage59 < 10:

    interpretation59 = (
        "The objective cost shows relatively low variation across "
        "the tested traffic scenarios, indicating stable behavior "
        "under the tested disturbances."
    )

elif variation_percentage59 < 25:

    interpretation59 = (
        "The objective cost shows moderate variation across the "
        "traffic scenarios. QPSO remains operational, but traffic "
        "disturbances have a measurable effect on solution cost."
    )

else:

    interpretation59 = (
        "The objective cost shows substantial variation across "
        "the tested traffic scenarios. This indicates that traffic "
        "conditions have a significant effect on routing performance."
    )


st.info(interpretation59)


# ------------------------------------------------------------
# 8. IMPORTANT SCIENTIFIC NOTE
# ------------------------------------------------------------

st.warning(
    "Robustness is evaluated only for the traffic scenarios tested "
    "in this experiment. These results should not be interpreted as "
    "a guarantee of performance under every possible real-world "
    "traffic condition."
)


# ------------------------------------------------------------
# 9. EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

st.subheader("Experiment Configuration")

st.write(
    f"Traffic scenarios analyzed: {len(stress_results58)}"
)

st.write(
    f"QPSO particles: {PARTICLES58}"
)

st.write(
    f"Optimization iterations: {ITERATIONS58}"
)

st.write(
    "Results source: Part 58 traffic stress test"
)

st.write(
    "Robustness metrics: cost range, variation, standard deviation and runtime"
)


# ------------------------------------------------------------
# 10. COMPLETION
# ------------------------------------------------------------

st.success("PART 59 COMPLETE")

print("PART 59 COMPLETE")

# ============================================================
# PART 60 - FINAL QPSO PERFORMANCE SUMMARY
# ============================================================

print()
print("=" * 70)
print("PART 60 - FINAL QPSO PERFORMANCE SUMMARY")
print("=" * 70)

st.header("🏆 Part 60 — Final QPSO Performance Summary")

st.write(
    "This section provides a consolidated summary of the "
    "QPSO traffic route optimization experiments performed "
    "throughout the project."
)


# ------------------------------------------------------------
# 1. FINAL TRAFFIC ROBUSTNESS VALUES
# ------------------------------------------------------------

final_average_cost60 = average_cost59
final_minimum_cost60 = minimum_cost59
final_maximum_cost60 = maximum_cost59
final_variation60 = variation_percentage59
final_std60 = cost_std59
final_average_runtime60 = average_runtime59


# ------------------------------------------------------------
# 2. PERFORMANCE SUMMARY TABLE
# ------------------------------------------------------------

final_summary60 = [
    {
        "Performance Metric": "Average Objective Cost",
        "Result": round(final_average_cost60, 4)
    },
    {
        "Performance Metric": "Best Objective Cost",
        "Result": round(final_minimum_cost60, 4)
    },
    {
        "Performance Metric": "Worst Objective Cost",
        "Result": round(final_maximum_cost60, 4)
    },
    {
        "Performance Metric": "Objective Cost Variation (%)",
        "Result": round(final_variation60, 2)
    },
    {
        "Performance Metric": "Objective Cost Standard Deviation",
        "Result": round(final_std60, 4)
    },
    {
        "Performance Metric": "Average Runtime (seconds)",
        "Result": round(final_average_runtime60, 4)
    },
    {
        "Performance Metric": "Traffic Scenarios Tested",
        "Result": len(stress_results58)
    },
    {
        "Performance Metric": "QPSO Particles",
        "Result": PARTICLES58
    },
    {
        "Performance Metric": "Optimization Iterations",
        "Result": ITERATIONS58
    }
]


st.subheader("Final Performance Summary")

st.table(final_summary60)


# ------------------------------------------------------------
# 3. PERFORMANCE INDICATORS
# ------------------------------------------------------------

st.subheader("Performance Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Best Objective Cost",
        f"{final_minimum_cost60:.2f}"
    )

with col2:
    st.metric(
        "Cost Variation",
        f"{final_variation60:.2f}%"
    )

with col3:
    st.metric(
        "Average Runtime",
        f"{final_average_runtime60:.4f} s"
    )


# ------------------------------------------------------------
# 4. COST RANGE VISUALIZATION
# ------------------------------------------------------------

st.subheader("Best vs Average vs Worst Objective Cost")

cost_labels60 = [
    "Best",
    "Average",
    "Worst"
]

cost_values60 = [
    final_minimum_cost60,
    final_average_cost60,
    final_maximum_cost60
]

fig60_cost, ax60_cost = plt.subplots(
    figsize=(9, 5)
)

ax60_cost.bar(
    cost_labels60,
    cost_values60
)

ax60_cost.set_title(
    "QPSO Objective Cost Summary"
)

ax60_cost.set_xlabel(
    "Performance Measure"
)

ax60_cost.set_ylabel(
    "Objective Cost"
)

ax60_cost.grid(
    axis="y",
    alpha=0.3
)

st.pyplot(fig60_cost)

plt.close(fig60_cost)


# ------------------------------------------------------------
# 5. FINAL INTERPRETATION
# ------------------------------------------------------------

st.subheader("Final Performance Interpretation")

if final_variation60 < 10:

    stability_text60 = (
        "The tested traffic scenarios produced relatively low "
        "objective-cost variation. This indicates that QPSO "
        "maintained stable performance across the evaluated "
        "traffic disturbances."
    )

elif final_variation60 < 25:

    stability_text60 = (
        "The tested traffic scenarios produced moderate "
        "objective-cost variation. QPSO remained functional, "
        "although traffic disturbances affected the optimization "
        "cost."
    )

else:

    stability_text60 = (
        "The tested traffic scenarios produced relatively high "
        "objective-cost variation. Traffic disturbances had a "
        "substantial influence on the optimization cost."
    )


st.info(stability_text60)


# ------------------------------------------------------------
# 6. PROJECT CONTRIBUTION
# ------------------------------------------------------------

st.subheader("Project Contribution")

st.write(
    "The developed prototype demonstrates a classical-computer "
    "implementation of Quantum Particle Swarm Optimization for "
    "traffic-aware vehicle routing. The system models a road "
    "network as a weighted graph, evaluates route costs, "
    "simulates traffic disturbances, and measures optimization "
    "quality and computational runtime."
)

st.write(
    "The experiments additionally evaluate convergence, "
    "scalability, parameter sensitivity, traffic robustness, "
    "and comparison with a Classical PSO-style baseline."
)


# ------------------------------------------------------------
# 7. SCIENTIFIC LIMITATION
# ------------------------------------------------------------

st.warning(
    "The reported performance is based on the simulated road "
    "networks and traffic scenarios used in this prototype. "
    "Further validation with larger real-world road networks, "
    "real traffic datasets and additional optimization "
    "baselines would be required before deployment."
)


# ------------------------------------------------------------
# 8. FINAL EXP

# ============================================================
# PART 61 - FINAL ROUTE OPTIMIZATION DEMONSTRATION
# ============================================================

print()
print("=" * 70)
print("PART 61 - FINAL ROUTE OPTIMIZATION DEMONSTRATION")
print("=" * 70)

st.header("🚗 Part 61 — Final Route Optimization Demonstration")

st.write(
    "This demonstration shows how QPSO can optimize a vehicle "
    "route on a traffic-weighted road network."
)


# ------------------------------------------------------------
# 1. CREATE DEMONSTRATION NETWORK
# ------------------------------------------------------------

G61 = nx.Graph()

edges61 = [
    ("A", "B", 5),
    ("B", "C", 4),
    ("C", "D", 5),
    ("D", "E", 6),
    ("E", "F", 4),
    ("F", "G", 5),

    ("A", "C", 8),
    ("B", "D", 7),
    ("C", "E", 8),
    ("D", "F", 7),
    ("E", "G", 8),

    ("A", "D", 12),
    ("B", "E", 11),
    ("C", "F", 10),
    ("D", "G", 11)
]

for u61, v61, w61 in edges61:
    G61.add_edge(
        u61,
        v61,
        weight=w61
    )


# ------------------------------------------------------------
# 2. DEFINE ROUTING PROBLEM
# ------------------------------------------------------------

depot61 = "A"

delivery_points61 = [
    "B",
    "C",
    "D",
    "E",
    "F",
    "G"
]


# ------------------------------------------------------------
# 3. NORMAL TRAFFIC QPSO
# ------------------------------------------------------------

start61_normal = time.perf_counter()

normal_route61, normal_cost61, normal_convergence61 = (
    qpso_vrp_optimization(
        G61,
        depot61,
        delivery_points61,
        particles=30,
        iterations=100
    )
)

normal_runtime61 = (
    time.perf_counter() - start61_normal
)


# ------------------------------------------------------------
# 4. CREATE TRAFFIC DISTURBANCE
# ------------------------------------------------------------

G61_traffic = G61.copy()

congested_edges61 = [
    ("A", "B"),
    ("B", "C"),
    ("C", "D")
]

for u61, v61 in congested_edges61:

    if G61_traffic.has_edge(u61, v61):

        G61_traffic[u61][v61]["weight"] *= 4


# ------------------------------------------------------------
# 5. TRAFFIC-AWARE QPSO
# ------------------------------------------------------------

start61_traffic = time.perf_counter()

traffic_route61, traffic_cost61, traffic_convergence61 = (
    qpso_vrp_optimization(
        G61_traffic,
        depot61,
        delivery_points61,
        particles=30,
        iterations=100
    )
)

traffic_runtime61 = (
    time.perf_counter() - start61_traffic
)


# ------------------------------------------------------------
# 6. DISPLAY NORMAL TRAFFIC RESULT
# ------------------------------------------------------------

st.subheader("Normal Traffic Result")

normal_result61 = [
    {
        "Metric": "Route",
        "Value": " → ".join(map(str, normal_route61))
    },
    {
        "Metric": "Objective Cost",
        "Value": round(normal_cost61, 4)
    },
    {
        "Metric": "Runtime (seconds)",
        "Value": round(normal_runtime61, 4)
    }
]

st.table(normal_result61)


# ------------------------------------------------------------
# 7. DISPLAY TRAFFIC-AWARE RESULT
# ------------------------------------------------------------

st.subheader("Traffic-Disturbed Result")

traffic_result61 = [
    {
        "Metric": "Route",
        "Value": " → ".join(map(str, traffic_route61))
    },
    {
        "Metric": "Objective Cost",
        "Value": round(traffic_cost61, 4)
    },
    {
        "Metric": "Runtime (seconds)",
        "Value": round(traffic_runtime61, 4)
    }
]

st.table(traffic_result61)


# ------------------------------------------------------------
# 8. COST COMPARISON
# ------------------------------------------------------------

st.subheader("Route Cost Comparison")

comparison_labels61 = [
    "Normal Traffic",
    "Traffic Disturbed"
]

comparison_values61 = [
    normal_cost61,
    traffic_cost61
]

fig61_cost, ax61_cost = plt.subplots(
    figsize=(9, 5)
)

ax61_cost.bar(
    comparison_labels61,
    comparison_values61
)

ax61_cost.set_title(
    "QPSO Route Cost: Normal vs Traffic-Disturbed"
)

ax61_cost.set_xlabel(
    "Traffic Condition"
)

ax61_cost.set_ylabel(
    "Objective Cost"
)

ax61_cost.grid(
    axis="y",
    alpha=0.3
)

st.pyplot(fig61_cost)

plt.close(fig61_cost)


# ------------------------------------------------------------
# 9. CONVERGENCE COMPARISON
# ------------------------------------------------------------

st.subheader("QPSO Convergence Comparison")

fig61_conv, ax61_conv = plt.subplots(
    figsize=(10, 5)
)

ax61_conv.plot(
    range(1, len(normal_convergence61) + 1),
    normal_convergence61,
    label="Normal Traffic"
)

ax61_conv.plot(
    range(1, len(traffic_convergence61) + 1),
    traffic_convergence61,
    label="Traffic Disturbed"
)

ax61_conv.set_title(
    "QPSO Convergence Under Different Traffic Conditions"
)

ax61_conv.set_xlabel(
    "Optimization Iteration"
)

ax61_conv.set_ylabel(
    "Objective Cost"
)

ax61_conv.legend()

ax61_conv.grid(
    True,
    alpha=0.3
)

st.pyplot(fig61_conv)

plt.close(fig61_conv)


# ------------------------------------------------------------
# 10. ROUTE CHANGE CHECK
# ------------------------------------------------------------

st.subheader("Rerouting Analysis")

if normal_route61 != traffic_route61:

    st.success(
        "QPSO selected a different route after the traffic "
        "disturbance. This demonstrates traffic-aware rerouting."
    )

else:

    st.info(
        "The selected route remained unchanged for this network "
        "configuration. The traffic disturbance was evaluated, "
        "but the same route remained the best solution."
    )


# ------------------------------------------------------------
# 11. TRAFFIC DISTURBANCE INFORMATION
# ------------------------------------------------------------

st.subheader("Traffic Disturbance")

st.write(
    "The following roads were given increased weights to "
    "simulate congestion:"
)

for edge61 in congested_edges61:

    st.write(
        f"• {edge61[0]} → {edge61[1]} : "
        f"traffic weight increased by 4×"
    )


# ------------------------------------------------------------
# 12. EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

st.subheader("Experiment Configuration")

st.write(
    "Optimization method: Quantum Particle Swarm Optimization"
)

st.write(
    "Depot: A"
)

st.write(
    f"Delivery locations: {len(delivery_points61)}"
)

st.write(
    "QPSO particles: 30"
)

st.write(
    "Optimization iterations: 100"
)

st.write(
    "Traffic disturbance multiplier: 4×"
)


# ------------------------------------------------------------
# 13. SCIENTIFIC NOTE
# ------------------------------------------------------------

st.warning(
    "This demonstration uses a simulated road network and "
    "artificial traffic-weight changes. It demonstrates the "
    "routing mechanism rather than claiming real-world traffic "
    "prediction accuracy."
)


# ------------------------------------------------------------
# 14. COMPLETION
# ------------------------------------------------------------

st.success("PART 61 COMPLETE")

print("PART 61 COMPLETE")

# ============================================================
# PART 62 - FINAL ROUTE VISUALIZATION
# ============================================================

print()
print("=" * 70)
print("PART 62 - FINAL ROUTE VISUALIZATION")
print("=" * 70)

st.header("🗺️ Part 62 — Final QPSO Route Visualization")

st.write(
    "This visualization shows the routes selected by QPSO "
    "before and after the traffic disturbance."
)


# ------------------------------------------------------------
# 1. FUNCTION TO EXPAND ROUTE INTO ROAD SEGMENTS
# ------------------------------------------------------------

def expand_route62(graph, route):

    expanded_path62 = []

    for i62 in range(len(route) - 1):

        start_node62 = route[i62]
        end_node62 = route[i62 + 1]

        try:

            shortest_path62 = nx.shortest_path(
                graph,
                start_node62,
                end_node62,
                weight="weight"
            )

            if i62 == 0:

                expanded_path62.extend(
                    shortest_path62
                )

            else:

                expanded_path62.extend(
                    shortest_path62[1:]
                )

        except nx.NetworkXNoPath:

            return []

    return expanded_path62


# ------------------------------------------------------------
# 2. EXPAND NORMAL TRAFFIC ROUTE
# ------------------------------------------------------------

normal_expanded62 = expand_route62(
    G61,
    normal_route61
)


# ------------------------------------------------------------
# 3. EXPAND TRAFFIC-DISTURBED ROUTE
# ------------------------------------------------------------

traffic_expanded62 = expand_route62(
    G61_traffic,
    traffic_route61
)


# ------------------------------------------------------------
# 4. DISPLAY NORMAL TRAFFIC ROUTE
# ------------------------------------------------------------

st.subheader("Normal Traffic Route")

st.write(
    " → ".join(
        map(str, normal_expanded62)
    )
)


# ------------------------------------------------------------
# 5. DISPLAY TRAFFIC-DISTURBED ROUTE
# ------------------------------------------------------------

st.subheader("Traffic-Disturbed Route")

st.write(
    " → ".join(
        map(str, traffic_expanded62)
    )
)


# ------------------------------------------------------------
# 6. CREATE NORMAL TRAFFIC VISUALIZATION
# ------------------------------------------------------------

st.subheader("Normal Traffic Network")

fig62_normal, ax62_normal = plt.subplots(
    figsize=(10, 7)
)

pos62 = nx.spring_layout(
    G61,
    seed=42
)

# Draw complete network
nx.draw_networkx_edges(
    G61,
    pos62,
    ax=ax62_normal,
    width=1.5,
    alpha=0.4
)

# Draw nodes
nx.draw_networkx_nodes(
    G61,
    pos62,
    ax=ax62_normal,
    node_size=800
)

# Draw labels
nx.draw_networkx_labels(
    G61,
    pos62,
    ax=ax62_normal,
    font_size=11,
    font_weight="bold"
)


# ------------------------------------------------------------
# 7. HIGHLIGHT NORMAL ROUTE
# ------------------------------------------------------------

normal_route_edges62 = []

for i62 in range(len(normal_expanded62) - 1):

    normal_route_edges62.append(
        (
            normal_expanded62[i62],
            normal_expanded62[i62 + 1]
        )
    )


nx.draw_networkx_edges(
    G61,
    pos62,
    edgelist=normal_route_edges62,
    ax=ax62_normal,
    width=4
)


ax62_normal.set_title(
    "QPSO Route Under Normal Traffic"
)

ax62_normal.axis("off")

st.pyplot(fig62_normal)

plt.close(fig62_normal)


# ------------------------------------------------------------
# 8. CREATE TRAFFIC-DISTURBED VISUALIZATION
# ------------------------------------------------------------

st.subheader("Traffic-Disturbed Network")

fig62_traffic, ax62_traffic = plt.subplots(
    figsize=(10, 7)
)

pos62_traffic = pos62


# Draw complete traffic network
nx.draw_networkx_edges(
    G61_traffic,
    pos62_traffic,
    ax=ax62_traffic,
    width=1.5,
    alpha=0.4
)

# Draw nodes
nx.draw_networkx_nodes(
    G61_traffic,
    pos62_traffic,
    ax=ax62_traffic,
    node_size=800
)

# Draw labels
nx.draw_networkx_labels(
    G61_traffic,
    pos62_traffic,
    ax=ax62_traffic,
    font_size=11,
    font_weight="bold"
)


# ------------------------------------------------------------
# 9. HIGHLIGHT CONGESTED ROADS
# ------------------------------------------------------------

nx.draw_networkx_edges(
    G61_traffic,
    pos62_traffic,
    edgelist=congested_edges61,
    ax=ax62_traffic,
    width=3,
    style="dashed",
    alpha=0.8
)


# ------------------------------------------------------------
# 10. HIGHLIGHT TRAFFIC-AWARE ROUTE
# ------------------------------------------------------------

traffic_route_edges62 = []

for i62 in range(len(traffic_expanded62) - 1):

    traffic_route_edges62.append(
        (
            traffic_expanded62[i62],
            traffic_expanded62[i62 + 1]
        )
    )


nx.draw_networkx_edges(
    G61_traffic,
    pos62_traffic,
    edgelist=traffic_route_edges62,
    ax=ax62_traffic,
    width=4
)


ax62_traffic.set_title(
    "QPSO Route Under Traffic Disturbance"
)

ax62_traffic.axis("off")

st.pyplot(fig62_traffic)

plt.close(fig62_traffic)


# ------------------------------------------------------------
# 11. ROUTE CHANGE STATUS
# ------------------------------------------------------------

st.subheader("Route Change Analysis")

if normal_expanded62 != traffic_expanded62:

    st.success(
        "The final road-level route changed after the "
        "traffic disturbance."
    )

    st.write(
        "This demonstrates how the QPSO-based routing system "
        "can evaluate a modified traffic-weighted network "
        "and select an alternative route."
    )

else:

    st.info(
        "The final road-level route remained unchanged under "
        "the tested traffic disturbance."
    )

    st.write(
        "The system still evaluated the traffic-weighted "
        "network and confirmed that the original route "
        "remained the best solution."
    )


# ------------------------------------------------------------
# 12. CONGESTED ROAD INFORMATION
# ------------------------------------------------------------

st.subheader("Congested Roads")

for edge62 in congested_edges61:

    st.write(
        f"• {edge62[0]} → {edge62[1]} : "
        "4× traffic weight"
    )


# ------------------------------------------------------------
# 13. FINAL EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

st.subheader("Experiment Configuration")

st.write(
    "Routing algorithm: Quantum Particle Swarm Optimization"
)

st.write(
    "Network type: Simulated weighted road network"
)

st.write(
    f"Number of delivery locations: "
    f"{len(delivery_points61)}"
)

st.write(
    "QPSO particles: 30"
)

st.write(
    "Optimization iterations: 100"
)

st.write(
    "Traffic disturbance multiplier: 4×"
)


# ------------------------------------------------------------
# 14. SCIENTIFIC NOTE
# ------------------------------------------------------------

st.warning(
    "The visualization uses a simulated network. "
    "The highlighted route demonstrates the optimization "
    "and rerouting mechanism and should not be interpreted "
    "as a real-world map or real-time traffic prediction."
)


# ------------------------------------------------------------
# 15. COMPLETION
# ------------------------------------------------------------

st.success("PART 62 COMPLETE")

print("PART 62 COMPLETE")

# ============================================================
# PART 63 - QPSO VS CLASSICAL PSO FINAL COMPARISON
# ============================================================

print()
print("=" * 70)
print("PART 63 - QPSO VS CLASSICAL PSO FINAL COMPARISON")
print("=" * 70)

st.header("⚖️ Part 63 — QPSO vs Classical PSO Final Comparison")

st.write(
    "This experiment compares the QPSO solution with the "
    "Classical PSO-style baseline using the same road network, "
    "depot, delivery locations and optimization settings."
)


# ------------------------------------------------------------
# 1. RUN QPSO
# ------------------------------------------------------------

start63_qpso = time.perf_counter()

qpso_route63, qpso_cost63, qpso_convergence63 = (
    qpso_vrp_optimization(
        G61,
        depot61,
        delivery_points61,
        particles=30,
        iterations=100
    )
)

qpso_runtime63 = (
    time.perf_counter() - start63_qpso
)


# ------------------------------------------------------------
# 2. RUN CLASSICAL PSO-STYLE BASELINE
# ------------------------------------------------------------

start63_pso = time.perf_counter()

pso_route63, pso_cost63, pso_convergence63 = (
    pso_vrp_optimization(
        G61,
        depot61,
        delivery_points61,
        particles=30,
        iterations=100
    )
)

pso_runtime63 = (
    time.perf_counter() - start63_pso
)


# ------------------------------------------------------------
# 3. DISPLAY ROUTES
# ------------------------------------------------------------

st.subheader("Route Comparison")

route_comparison63 = [
    {
        "Algorithm": "QPSO",
        "Route": " → ".join(
            map(str, qpso_route63)
        ),
        "Objective Cost": round(
            qpso_cost63, 4
        ),
        "Runtime (seconds)": round(
            qpso_runtime63, 4
        )
    },
    {
        "Algorithm": "Classical PSO-style",
        "Route": " → ".join(
            map(str, pso_route63)
        ),
        "Objective Cost": round(
            pso_cost63, 4
        ),
        "Runtime (seconds)": round(
            pso_runtime63, 4
        )
    }
]

st.table(route_comparison63)


# ------------------------------------------------------------
# 4. CALCULATE COST DIFFERENCE
# ------------------------------------------------------------

if pso_cost63 != 0:

    cost_difference63 = (
        (pso_cost63 - qpso_cost63)
        / pso_cost63
    ) * 100

else:

    cost_difference63 = 0


# ------------------------------------------------------------
# 5. CALCULATE RUNTIME DIFFERENCE
# ------------------------------------------------------------

if pso_runtime63 != 0:

    runtime_difference63 = (
        (pso_runtime63 - qpso_runtime63)
        / pso_runtime63
    ) * 100

else:

    runtime_difference63 = 0


# ------------------------------------------------------------
# 6. PERFORMANCE INTERPRETATION
# ------------------------------------------------------------

st.subheader("Performance Interpretation")

if qpso_cost63 < pso_cost63:

    st.success(
        f"QPSO produced a lower objective cost than the "
        f"Classical PSO-style baseline by "
        f"{cost_difference63:.2f}%."
    )

elif qpso_cost63 > pso_cost63:

    st.info(
        f"The Classical PSO-style baseline produced a lower "
        f"objective cost in this run by "
        f"{abs(cost_difference63):.2f}%."
    )

else:

    st.info(
        "Both algorithms produced the same objective cost "
        "in this run."
    )


if qpso_runtime63 < pso_runtime63:

    st.write(
        f"QPSO runtime was lower by "
        f"{runtime_difference63:.2f}% in this run."
    )

elif qpso_runtime63 > pso_runtime63:

    st.write(
        f"Classical PSO-style runtime was lower by "
        f"{abs(runtime_difference63):.2f}% in this run."
    )

else:

    st.write(
        "Both algorithms required approximately the same "
        "runtime in this run."
    )


# ------------------------------------------------------------
# 7. OBJECTIVE COST GRAPH
# ------------------------------------------------------------

st.subheader("Objective Cost Comparison")

algorithm_labels63 = [
    "QPSO",
    "Classical PSO-style"
]

objective_values63 = [
    qpso_cost63,
    pso_cost63
]

fig63_cost, ax63_cost = plt.subplots(
    figsize=(9, 5)
)

ax63_cost.bar(
    algorithm_labels63,
    objective_values63
)

ax63_cost.set_title(
    "QPSO vs Classical PSO-style: Objective Cost"
)

ax63_cost.set_xlabel(
    "Optimization Method"
)

ax63_cost.set_ylabel(
    "Objective Cost"
)

ax63_cost.grid(
    axis="y",
    alpha=0.3
)

st.pyplot(fig63_cost)

plt.close(fig63_cost)


# ------------------------------------------------------------
# 8. RUNTIME GRAPH
# ------------------------------------------------------------

st.subheader("Runtime Comparison")

runtime_values63 = [
    qpso_runtime63,
    pso_runtime63
]

fig63_runtime, ax63_runtime = plt.subplots(
    figsize=(9, 5)
)

ax63_runtime.bar(
    algorithm_labels63,
    runtime_values63
)

ax63_runtime.set_title(
    "QPSO vs Classical PSO-style: Runtime"
)

ax63_runtime.set_xlabel(
    "Optimization Method"
)

ax63_runtime.set_ylabel(
    "Runtime (seconds)"
)

ax63_runtime.grid(
    axis="y",
    alpha=0.3
)

st.pyplot(fig63_runtime)

plt.close(fig63_runtime)


# ------------------------------------------------------------
# 9. CONVERGENCE COMPARISON
# ------------------------------------------------------------

st.subheader("Convergence Comparison")

fig63_conv, ax63_conv = plt.subplots(
    figsize=(10, 5)
)

ax63_conv.plot(
    range(1, len(qpso_convergence63) + 1),
    qpso_convergence63,
    label="QPSO"
)

ax63_conv.plot(
    range(1, len(pso_convergence63) + 1),
    pso_convergence63,
    label="Classical PSO-style"
)

ax63_conv.set_title(
    "QPSO vs Classical PSO-style Convergence"
)

ax63_conv.set_xlabel(
    "Optimization Iteration"
)

ax63_conv.set_ylabel(
    "Best Objective Cost"
)

ax63_conv.legend()

ax63_conv.grid(
    True,
    alpha=0.3
)

st.pyplot(fig63_conv)

plt.close(fig63_conv)


# ------------------------------------------------------------
# 10. FAIR COMPARISON NOTE
# ------------------------------------------------------------

st.subheader("Fair Comparison")

st.info(
    "Both methods use the same road network, depot, delivery "
    "locations, number of particles and number of iterations. "
    "The comparison is therefore based on the same experimental "
    "conditions."
)


# ------------------------------------------------------------
# 11. SCIENTIFIC NOTE
# ------------------------------------------------------------

st.warning(
    "The Classical PSO-style method is used as a baseline for "
    "experimental comparison. A single run does not establish "
    "statistical superiority. Multiple independent runs are "
    "required for stronger performance conclusions."
)


# ------------------------------------------------------------
# 12. EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

st.subheader("Experiment Configuration")

st.write(
    "QPSO particles: 30"
)

st.write(
    "Classical PSO-style particles: 30"
)

st.write(
    "Optimization iterations: 100"
)

st.write(
    f"Delivery locations: {len(delivery_points61)}"
)

st.write(
    "Same road network and routing problem used for both methods."
)


# ------------------------------------------------------------
# 13. COMPLETION
# ------------------------------------------------------------

st.success("PART 63 COMPLETE")

print("PART 63 COMPLETE")

# ============================================================
# PART 64 - MULTIPLE-RUN STATISTICAL COMPARISON
# ============================================================

print()
print("=" * 70)
print("PART 64 - MULTIPLE-RUN STATISTICAL COMPARISON")
print("=" * 70)

st.header("📊 Part 64 — Multiple-Run Statistical Comparison")

st.write(
    "This experiment performs multiple independent runs of "
    "QPSO and the Classical PSO-style baseline under the "
    "same routing conditions."
)


# ------------------------------------------------------------
# 1. EXPERIMENT SETTINGS
# ------------------------------------------------------------

NUM_RUNS64 = 10
PARTICLES64 = 30
ITERATIONS64 = 100


# ------------------------------------------------------------
# 2. RESULT STORAGE
# ------------------------------------------------------------

qpso_costs64 = []
pso_costs64 = []

qpso_runtimes64 = []
pso_runtimes64 = []


# ------------------------------------------------------------
# 3. RUN MULTIPLE EXPERIMENTS
# ------------------------------------------------------------

progress64 = st.progress(0)

for run64 in range(NUM_RUNS64):

    # --------------------------------------------------------
    # QPSO
    # --------------------------------------------------------

    start64_qpso = time.perf_counter()

    route_qpso64, cost_qpso64, convergence_qpso64 = (
        qpso_vrp_optimization(
            G61,
            depot61,
            delivery_points61,
            particles=PARTICLES64,
            iterations=ITERATIONS64
        )
    )

    runtime_qpso64 = (
        time.perf_counter() - start64_qpso
    )

    qpso_costs64.append(cost_qpso64)
    qpso_runtimes64.append(runtime_qpso64)


    # --------------------------------------------------------
    # CLASSICAL PSO-STYLE BASELINE
    # --------------------------------------------------------

    start64_pso = time.perf_counter()

    route_pso64, cost_pso64, convergence_pso64 = (
        pso_vrp_optimization(
            G61,
            depot61,
            delivery_points61,
            particles=PARTICLES64,
            iterations=ITERATIONS64
        )
    )

    runtime_pso64 = (
        time.perf_counter() - start64_pso
    )

    pso_costs64.append(cost_pso64)
    pso_runtimes64.append(runtime_pso64)


    progress64.progress(
        (run64 + 1) / NUM_RUNS64
    )


# ------------------------------------------------------------
# 4. CALCULATE STATISTICS
# ------------------------------------------------------------

qpso_average_cost64 = statistics.mean(
    qpso_costs64
)

qpso_best_cost64 = min(
    qpso_costs64
)

qpso_worst_cost64 = max(
    qpso_costs64
)

qpso_std64 = (
    statistics.stdev(qpso_costs64)
    if len(qpso_costs64) > 1
    else 0
)

qpso_average_runtime64 = statistics.mean(
    qpso_runtimes64
)


pso_average_cost64 = statistics.mean(
    pso_costs64
)

pso_best_cost64 = min(
    pso_costs64
)

pso_worst_cost64 = max(
    pso_costs64
)

pso_std64 = (
    statistics.stdev(pso_costs64)
    if len(pso_costs64) > 1
    else 0
)

pso_average_runtime64 = statistics.mean(
    pso_runtimes64
)


# ------------------------------------------------------------
# 5. DISPLAY STATISTICAL TABLE
# ------------------------------------------------------------

st.subheader("Statistical Performance Summary")

statistics_table64 = [
    {
        "Metric": "Average Objective Cost",
        "QPSO": round(qpso_average_cost64, 4),
        "Classical PSO-style": round(
            pso_average_cost64, 4
        )
    },
    {
        "Metric": "Best Objective Cost",
        "QPSO": round(qpso_best_cost64, 4),
        "Classical PSO-style": round(
            pso_best_cost64, 4
        )
    },
    {
        "Metric": "Worst Objective Cost",
        "QPSO": round(qpso_worst_cost64, 4),
        "Classical PSO-style": round(
            pso_worst_cost64, 4
        )
    },
    {
        "Metric": "Standard Deviation",
        "QPSO": round(qpso_std64, 4),
        "Classical PSO-style": round(
            pso_std64, 4
        )
    },
    {
        "Metric": "Average Runtime (seconds)",
        "QPSO": round(
            qpso_average_runtime64, 4
        ),
        "Classical PSO-style": round(
            pso_average_runtime64, 4
        )
    }
]

st.table(statistics_table64)


# ------------------------------------------------------------
# 6. AVERAGE COST COMPARISON
# ------------------------------------------------------------

st.subheader("Average Objective Cost Comparison")

average_cost_labels64 = [
    "QPSO",
    "Classical PSO-style"
]

average_cost_values64 = [
    qpso_average_cost64,
    pso_average_cost64
]

fig64_cost, ax64_cost = plt.subplots(
    figsize=(9, 5)
)

ax64_cost.bar(
    average_cost_labels64,
    average_cost_values64
)

ax64_cost.set_title(
    "Average Objective Cost Across Multiple Runs"
)

ax64_cost.set_xlabel(
    "Optimization Method"
)

ax64_cost.set_ylabel(
    "Average Objective Cost"
)

ax64_cost.grid(
    axis="y",
    alpha=0.3
)

st.pyplot(fig64_cost)

plt.close(fig64_cost)


# ------------------------------------------------------------
# 7. RUNTIME COMPARISON
# ------------------------------------------------------------

st.subheader("Average Runtime Comparison")

runtime_labels64 = [
    "QPSO",
    "Classical PSO-style"
]

runtime_values64 = [
    qpso_average_runtime64,
    pso_average_runtime64
]

fig64_runtime, ax64_runtime = plt.subplots(
    figsize=(9, 5)
)

ax64_runtime.bar(
    runtime_labels64,
    runtime_values64
)

ax64_runtime.set_title(
    "Average Runtime Across Multiple Runs"
)

ax64_runtime.set_xlabel(
    "Optimization Method"
)

ax64_runtime.set_ylabel(
    "Average Runtime (seconds)"
)

ax64_runtime.grid(
    axis="y",
    alpha=0.3
)

st.pyplot(fig64_runtime)

plt.close(fig64_runtime)


# ------------------------------------------------------------
# 8. COST VARIABILITY COMPARISON
# ------------------------------------------------------------

st.subheader("Objective Cost Variability")

fig64_std, ax64_std = plt.subplots(
    figsize=(9, 5)
)

ax64_std.bar(
    ["QPSO", "Classical PSO-style"],
    [qpso_std64, pso_std64]
)

ax64_std.set_title(
    "Objective Cost Standard Deviation"
)

ax64_std.set_xlabel(
    "Optimization Method"
)

ax64_std.set_ylabel(
    "Standard Deviation"
)

ax64_std.grid(
    axis="y",
    alpha=0.3
)

st.pyplot(fig64_std)

plt.close(fig64_std)


# ------------------------------------------------------------
# 9. RUN-BY-RUN COST COMPARISON
# ------------------------------------------------------------

st.subheader("Run-by-Run Objective Cost")

run_numbers64 = list(
    range(1, NUM_RUNS64 + 1)
)

fig64_runs, ax64_runs = plt.subplots(
    figsize=(10, 5)
)

ax64_runs.plot(
    run_numbers64,
    qpso_costs64,
    marker="o",
    label="QPSO"
)

ax64_runs.plot(
    run_numbers64,
    pso_costs64,
    marker="o",
    label="Classical PSO-style"
)

ax64_runs.set_title(
    "Objective Cost Across Independent Runs"
)

ax64_runs.set_xlabel(
    "Run Number"
)

ax64_runs.set_ylabel(
    "Objective Cost"
)

ax64_runs.legend()

ax64_runs.grid(
    True,
    alpha=0.3
)

st.pyplot(fig64_runs)

plt.close(fig64_runs)


# ------------------------------------------------------------
# 10. PERFORMANCE INTERPRETATION
# ------------------------------------------------------------

st.subheader("Statistical Interpretation")

if qpso_average_cost64 < pso_average_cost64:

    st.success(
        "Across the tested runs, QPSO achieved a lower "
        "average objective cost than the Classical "
        "PSO-style baseline."
    )

elif qpso_average_cost64 > pso_average_cost64:

    st.info(
        "Across the tested runs, the Classical PSO-style "
        "baseline achieved a lower average objective cost "
        "than QPSO."
    )

else:

    st.info(
        "Both methods achieved the same average objective "
        "cost across the tested runs."
    )


if qpso_std64 < pso_std64:

    st.write(
        "QPSO showed lower objective-cost variation across "
        "the tested runs."
    )

elif qpso_std64 > pso_std64:

    st.write(
        "The Classical PSO-style baseline showed lower "
        "objective-cost variation across the tested runs."
    )

else:

    st.write(
        "Both methods showed the same objective-cost "
        "variation."
    )


# ------------------------------------------------------------
# 11. SCIENTIFIC NOTE
# ------------------------------------------------------------

st.warning(
    "The results describe performance on the simulated "
    "network used in this experiment. They should not be "
    "interpreted as proof that one optimization method is "
    "universally superior."
)


# ------------------------------------------------------------
# 12. EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

st.subheader("Experiment Configuration")

st.write(
    f"Independent runs: {NUM_RUNS64}"
)

st.write(
    f"QPSO particles: {PARTICLES64}"
)

st.write(
    f"Classical PSO-style particles: {PARTICLES64}"
)

st.write(
    f"Optimization iterations: {ITERATIONS64}"
)

st.write(
    f"Delivery locations: {len(delivery_points61)}"
)

st.write(
    "Same road network and routing problem used for both methods."
)


# ------------------------------------------------------------
# 13. COMPLETION
# ------------------------------------------------------------

st.success("PART 64 COMPLETE")

print("PART 64 COMPLETE")

# ============================================================
# PART 65 - QPSO PERFORMANCE DIFFERENCE ANALYSIS
# ============================================================

print()
print("=" * 70)
print("PART 65 - QPSO PERFORMANCE DIFFERENCE ANALYSIS")
print("=" * 70)

st.header("📈 Part 65 — QPSO Performance Difference Analysis")

st.write(
    "This analysis calculates the relative difference between "
    "QPSO and the Classical PSO-style baseline using the "
    "multiple-run results obtained in Part 64."
)


# ------------------------------------------------------------
# 1. OBJECTIVE COST DIFFERENCE
# ------------------------------------------------------------

cost_difference65 = (
    pso_average_cost64 - qpso_average_cost64
)


if pso_average_cost64 != 0:

    cost_difference_percent65 = (
        cost_difference65 /
        pso_average_cost64
    ) * 100

else:

    cost_difference_percent65 = 0


# ------------------------------------------------------------
# 2. RUNTIME DIFFERENCE
# ------------------------------------------------------------

runtime_difference65 = (
    pso_average_runtime64 -
    qpso_average_runtime64
)


if pso_average_runtime64 != 0:

    runtime_difference_percent65 = (
        runtime_difference65 /
        pso_average_runtime64
    ) * 100

else:

    runtime_difference_percent65 = 0


# ------------------------------------------------------------
# 3. VARIABILITY DIFFERENCE
# ------------------------------------------------------------

std_difference65 = (
    pso_std64 - qpso_std64
)


# ------------------------------------------------------------
# 4. DISPLAY PERFORMANCE METRICS
# ------------------------------------------------------------

st.subheader("Performance Difference")

difference_table65 = [
    {
        "Performance Measure": "Average Objective Cost",
        "QPSO": round(qpso_average_cost64, 4),
        "Classical PSO-style": round(
            pso_average_cost64, 4
        ),
        "Difference": round(
            cost_difference65, 4
        )
    },
    {
        "Performance Measure": "Average Runtime (seconds)",
        "QPSO": round(
            qpso_average_runtime64, 4
        ),
        "Classical PSO-style": round(
            pso_average_runtime64, 4
        ),
        "Difference": round(
            runtime_difference65, 4
        )
    },
    {
        "Performance Measure": "Standard Deviation",
        "QPSO": round(qpso_std64, 4),
        "Classical PSO-style": round(
            pso_std64, 4
        ),
        "Difference": round(
            std_difference65, 4
        )
    }
]

st.table(difference_table65)


# ------------------------------------------------------------
# 5. RELATIVE COST DIFFERENCE
# ------------------------------------------------------------

st.subheader("Relative Objective-Cost Difference")

st.metric(
    "QPSO vs Classical PSO-style",
    f"{cost_difference_percent65:.2f}%"
)


if cost_difference_percent65 > 0:

    st.success(
        f"QPSO achieved an average objective cost "
        f"{cost_difference_percent65:.2f}% lower than "
        f"the Classical PSO-style baseline in this experiment."
    )

elif cost_difference_percent65 < 0:

    st.info(
        f"QPSO achieved an average objective cost "
        f"{abs(cost_difference_percent65):.2f}% higher than "
        f"the Classical PSO-style baseline in this experiment."
    )

else:

    st.info(
        "QPSO and the Classical PSO-style baseline achieved "
        "the same average objective cost in this experiment."
    )


# ------------------------------------------------------------
# 6. RELATIVE RUNTIME DIFFERENCE
# ------------------------------------------------------------

st.subheader("Relative Runtime Difference")

st.metric(
    "Runtime Difference",
    f"{runtime_difference_percent65:.2f}%"
)


if runtime_difference_percent65 > 0:

    st.success(
        f"QPSO required approximately "
        f"{runtime_difference_percent65:.2f}% less runtime "
        f"than the Classical PSO-style baseline in this experiment."
    )

elif runtime_difference_percent65 < 0:

    st.info(
        f"QPSO required approximately "
        f"{abs(runtime_difference_percent65):.2f}% more runtime "
        f"than the Classical PSO-style baseline in this experiment."
    )

else:

    st.info(
        "Both methods required approximately the same "
        "average runtime in this experiment."
    )


# ------------------------------------------------------------
# 7. PERFORMANCE COMPARISON GRAPH
# ------------------------------------------------------------

st.subheader("Performance Comparison")

performance_labels65 = [
    "Average Cost",
    "Average Runtime"
]

qpso_performance65 = [
    qpso_average_cost64,
    qpso_average_runtime64
]

pso_performance65 = [
    pso_average_cost64,
    pso_average_runtime64
]


fig65, ax65 = plt.subplots(
    figsize=(10, 5)
)

x65 = range(len(performance_labels65))

width65 = 0.35

ax65.bar(
    [i - width65 / 2 for i in x65],
    qpso_performance65,
    width=width65,
    label="QPSO"
)

ax65.bar(
    [i + width65 / 2 for i in x65],
    pso_performance65,
    width=width65,
    label="Classical PSO-style"
)

ax65.set_title(
    "QPSO vs Classical PSO-style Performance"
)

ax65.set_xlabel(
    "Performance Measure"
)

ax65.set_ylabel(
    "Measured Value"
)

ax65.set_xticks(
    list(x65)
)

ax65.set_xticklabels(
    performance_labels65
)

ax65.legend()

ax65.grid(
    axis="y",
    alpha=0.3
)

st.pyplot(fig65)

plt.close(fig65)


# ------------------------------------------------------------
# 8. BEST AND WORST SOLUTION COMPARISON
# ------------------------------------------------------------

st.subheader("Best and Worst Objective Cost")

best_worst_table65 = [
    {
        "Metric": "Best Objective Cost",
        "QPSO": round(qpso_best_cost64, 4),
        "Classical PSO-style": round(
            pso_best_cost64, 4
        )
    },
    {
        "Metric": "Worst Objective Cost",
        "QPSO": round(qpso_worst_cost64, 4),
        "Classical PSO-style": round(
            pso_worst_cost64, 4
        )
    }
]

st.table(best_worst_table65)


# ------------------------------------------------------------
# 9. EXPERIMENT INTERPRETATION
# ------------------------------------------------------------

st.subheader("Performance Interpretation")

st.write(
    "The comparison shows how the two optimization methods "
    "behaved under identical experimental conditions."
)

st.write(
    "Lower objective cost indicates a better routing solution, "
    "while lower runtime indicates lower computational time."
)

st.write(
    "Standard deviation is used to evaluate how consistently "
    "each method produced similar objective-cost values "
    "across independent runs."
)


# ------------------------------------------------------------
# 10. SCIENTIFIC NOTE
# ------------------------------------------------------------

st.warning(
    "The percentage differences are specific to the simulated "
    "network and experimental configuration used here. "
    "They should not be interpreted as universal performance "
    "advantages of QPSO."
)


# ------------------------------------------------------------
# 11. EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

st.subheader("Experiment Configuration")

st.write(
    f"Independent runs analyzed: {NUM_RUNS64}"
)

st.write(
    f"QPSO particles: {PARTICLES64}"
)

st.write(
    f"Classical PSO-style particles: {PARTICLES64}"
)

st.write(
    f"Optimization iterations: {ITERATIONS64}"
)

st.write(
    f"Delivery locations: {len(delivery_points61)}"
)

st.write(
    "Both methods used the same road network and routing problem."
)


# ------------------------------------------------------------
# 12. COMPLETION
# ------------------------------------------------------------

st.success("PART 65 COMPLETE")

print("PART 65 COMPLETE")

# ============================================================
# PART 66 - QPSO VS CLASSICAL PSO CONVERGENCE COMPARISON
# ============================================================

print()
print("=" * 70)
print("PART 66 - QPSO VS CLASSICAL PSO CONVERGENCE COMPARISON")
print("=" * 70)

st.header("📉 Part 66 — QPSO vs Classical PSO Convergence Comparison")

st.write(
    "This experiment compares the convergence behavior of "
    "QPSO and the Classical PSO-style baseline under the "
    "same road network and optimization conditions."
)


# ------------------------------------------------------------
# 1. RUN ONE REPRESENTATIVE QPSO EXPERIMENT
# ------------------------------------------------------------

start66_qpso = time.perf_counter()

route66_qpso, cost66_qpso, convergence66_qpso = (
    qpso_vrp_optimization(
        G61,
        depot61,
        delivery_points61,
        particles=30,
        iterations=100
    )
)

runtime66_qpso = (
    time.perf_counter() - start66_qpso
)


# ------------------------------------------------------------
# 2. RUN ONE REPRESENTATIVE CLASSICAL PSO EXPERIMENT
# ------------------------------------------------------------

start66_pso = time.perf_counter()

route66_pso, cost66_pso, convergence66_pso = (
    pso_vrp_optimization(
        G61,
        depot61,
        delivery_points61,
        particles=30,
        iterations=100
    )
)

runtime66_pso = (
    time.perf_counter() - start66_pso
)


# ------------------------------------------------------------
# 3. DISPLAY FINAL RESULTS
# ------------------------------------------------------------

st.subheader("Final Optimization Results")

results66 = [
    {
        "Metric": "QPSO Final Cost",
        "Value": round(cost66_qpso, 4)
    },
    {
        "Metric": "Classical PSO-style Final Cost",
        "Value": round(cost66_pso, 4)
    },
    {
        "Metric": "QPSO Runtime (seconds)",
        "Value": round(runtime66_qpso, 4)
    },
    {
        "Metric": "Classical PSO-style Runtime (seconds)",
        "Value": round(runtime66_pso, 4)
    }
]

st.table(results66)


# ------------------------------------------------------------
# 4. CONVERGENCE GRAPH
# ------------------------------------------------------------

st.subheader("Convergence Comparison")

fig66, ax66 = plt.subplots(
    figsize=(10, 5)
)

ax66.plot(
    range(1, len(convergence66_qpso) + 1),
    convergence66_qpso,
    label="QPSO"
)

ax66.plot(
    range(1, len(convergence66_pso) + 1),
    convergence66_pso,
    label="Classical PSO-style"
)

ax66.set_title(
    "QPSO vs Classical PSO-style Convergence"
)

ax66.set_xlabel(
    "Optimization Iteration"
)

ax66.set_ylabel(
    "Best Objective Cost"
)

ax66.legend()

ax66.grid(
    True,
    alpha=0.3
)

st.pyplot(fig66)

plt.close(fig66)


# ------------------------------------------------------------
# 5. INITIAL VS FINAL COST
# ------------------------------------------------------------

initial_qpso66 = convergence66_qpso[0]
final_qpso66 = convergence66_qpso[-1]

initial_pso66 = convergence66_pso[0]
final_pso66 = convergence66_pso[-1]


# ------------------------------------------------------------
# 6. CALCULATE IMPROVEMENT
# ------------------------------------------------------------

if initial_qpso66 != 0:

    qpso_improvement66 = (
        (initial_qpso66 - final_qpso66)
        / initial_qpso66
    ) * 100

else:

    qpso_improvement66 = 0


if initial_pso66 != 0:

    pso_improvement66 = (
        (initial_pso66 - final_pso66)
        / initial_pso66
    ) * 100

else:

    pso_improvement66 = 0


# ------------------------------------------------------------
# 7. IMPROVEMENT TABLE
# ------------------------------------------------------------

st.subheader("Optimization Improvement")

improvement_table66 = [
    {
        "Method": "QPSO",
        "Initial Cost": round(
            initial_qpso66, 4
        ),
        "Final Cost": round(
            final_qpso66, 4
        ),
        "Improvement (%)": round(
            qpso_improvement66, 2
        )
    },
    {
        "Method": "Classical PSO-style",
        "Initial Cost": round(
            initial_pso66, 4
        ),
        "Final Cost": round(
            final_pso66, 4
        ),
        "Improvement (%)": round(
            pso_improvement66, 2
        )
    }
]

st.table(improvement_table66)


# ------------------------------------------------------------
# 8. ROUTE COMPARISON
# ------------------------------------------------------------

st.subheader("Optimized Route Comparison")

route_table66 = [
    {
        "Method": "QPSO",
        "Route": " → ".join(
            map(str, route66_qpso)
        ),
        "Objective Cost": round(
            cost66_qpso, 4
        )
    },
    {
        "Method": "Classical PSO-style",
        "Route": " → ".join(
            map(str, route66_pso)
        ),
        "Objective Cost": round(
            cost66_pso, 4
        )
    }
]

st.table(route_table66)


# ------------------------------------------------------------
# 9. CONVERGENCE INTERPRETATION
# ------------------------------------------------------------

st.subheader("Convergence Interpretation")

if qpso_improvement66 > pso_improvement66:

    st.success(
        "In this representative run, QPSO achieved a larger "
        "reduction from its initial objective cost than the "
        "Classical PSO-style baseline."
    )

elif qpso_improvement66 < pso_improvement66:

    st.info(
        "In this representative run, the Classical PSO-style "
        "baseline achieved a larger reduction from its initial "
        "objective cost than QPSO."
    )

else:

    st.info(
        "Both methods achieved the same percentage improvement "
        "from their initial objective cost in this representative run."
    )


# ------------------------------------------------------------
# 10. FINAL COST INTERPRETATION
# ------------------------------------------------------------

if cost66_qpso < cost66_pso:

    st.write(
        "QPSO produced the lower final objective cost in this "
        "representative run."
    )

elif cost66_qpso > cost66_pso:

    st.write(
        "The Classical PSO-style baseline produced the lower "
        "final objective cost in this representative run."
    )

else:

    st.write(
        "Both methods produced the same final objective cost "
        "in this representative run."
    )


# ------------------------------------------------------------
# 11. SCIENTIFIC NOTE
# ------------------------------------------------------------

st.warning(
    "Convergence behavior can vary between independent runs "
    "because metaheuristic optimization uses stochastic "
    "search. This single-run convergence graph is therefore "
    "illustrative and should be considered together with the "
    "multiple-run statistical analysis from Part 64."
)


# ------------------------------------------------------------
# 12. EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

st.subheader("Experiment Configuration")

st.write(
    "QPSO particles: 30"
)

st.write(
    "Classical PSO-style particles: 30"
)

st.write(
    "Optimization iterations: 100"
)

st.write(
    f"Delivery locations: {len(delivery_points61)}"
)

st.write(
    "Same road network used for both methods."
)

st.write(
    "Same depot and delivery locations used for both methods."
)


# ------------------------------------------------------------
# 13. COMPLETION
# ------------------------------------------------------------

st.success("PART 66 COMPLETE")

print("PART 66 COMPLETE")
# ============================================================
# PART 67 - MULTI-RUN CONVERGENCE STABILITY ANALYSIS
# ============================================================

print()
print("=" * 70)
print("PART 67 - MULTI-RUN CONVERGENCE STABILITY ANALYSIS")
print("=" * 70)

st.header("📊 Part 67 — Multi-Run Convergence Stability Analysis")

st.write(
    "This experiment evaluates the stability of QPSO convergence "
    "across multiple independent optimization runs."
)


# ------------------------------------------------------------
# 1. EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

NUM_RUNS67 = 10
PARTICLES67 = 30
ITERATIONS67 = 100


# ------------------------------------------------------------
# 2. STORAGE
# ------------------------------------------------------------

all_convergence67 = []
final_costs67 = []
runtimes67 = []


# ------------------------------------------------------------
# 3. RUN QPSO MULTIPLE TIMES
# ------------------------------------------------------------

for run67 in range(NUM_RUNS67):

    start67 = time.perf_counter()

    route67, cost67, convergence67 = (
        qpso_vrp_optimization(
            G61,
            depot61,
            delivery_points61,
            particles=PARTICLES67,
            iterations=ITERATIONS67
        )
    )

    runtime67 = time.perf_counter() - start67

    all_convergence67.append(convergence67)
    final_costs67.append(cost67)
    runtimes67.append(runtime67)


# ------------------------------------------------------------
# 4. CALCULATE AVERAGE CONVERGENCE
# ------------------------------------------------------------

average_convergence67 = []

for iteration67 in range(ITERATIONS67):

    values67 = [
        convergence67[iteration67]
        for convergence67 in all_convergence67
    ]

    average_convergence67.append(
        statistics.mean(values67)
    )


# ------------------------------------------------------------
# 5. CALCULATE CONVERGENCE STANDARD DEVIATION
# ------------------------------------------------------------

convergence_std67 = []

for iteration67 in range(ITERATIONS67):

    values67 = [
        convergence67[iteration67]
        for convergence67 in all_convergence67
    ]

    if len(values67) > 1:

        convergence_std67.append(
            statistics.stdev(values67)
        )

    else:

        convergence_std67.append(0)


# ------------------------------------------------------------
# 6. FINAL STATISTICS
# ------------------------------------------------------------

average_cost67 = statistics.mean(final_costs67)

best_cost67 = min(final_costs67)

worst_cost67 = max(final_costs67)

cost_std67 = (
    statistics.stdev(final_costs67)
    if len(final_costs67) > 1
    else 0
)

average_runtime67 = statistics.mean(runtimes67)


# ------------------------------------------------------------
# 7. DISPLAY STATISTICAL SUMMARY
# ------------------------------------------------------------

st.subheader("Multi-Run Statistical Summary")

summary67 = [
    {
        "Metric": "Independent Runs",
        "Value": NUM_RUNS67
    },
    {
        "Metric": "Average Final Objective Cost",
        "Value": round(average_cost67, 4)
    },
    {
        "Metric": "Best Final Objective Cost",
        "Value": round(best_cost67, 4)
    },
    {
        "Metric": "Worst Final Objective Cost",
        "Value": round(worst_cost67, 4)
    },
    {
        "Metric": "Cost Standard Deviation",
        "Value": round(cost_std67, 4)
    },
    {
        "Metric": "Average Runtime (seconds)",
        "Value": round(average_runtime67, 4)
    }
]

st.table(summary67)


# ------------------------------------------------------------
# 8. AVERAGE CONVERGENCE GRAPH
# ------------------------------------------------------------

st.subheader("Average QPSO Convergence")

fig67, ax67 = plt.subplots(
    figsize=(10, 5)
)

ax67.plot(
    range(1, ITERATIONS67 + 1),
    average_convergence67,
    label="Average QPSO Convergence"
)

ax67.set_title(
    "Average QPSO Convergence Across Independent Runs"
)

ax67.set_xlabel(
    "Optimization Iteration"
)

ax67.set_ylabel(
    "Average Best Objective Cost"
)

ax67.legend()

ax67.grid(
    True,
    alpha=0.3
)

st.pyplot(fig67)

plt.close(fig67)


# ------------------------------------------------------------
# 9. CONVERGENCE VARIATION GRAPH
# ------------------------------------------------------------

st.subheader("Convergence Standard Deviation")

fig67_std, ax67_std = plt.subplots(
    figsize=(10, 5)
)

ax67_std.plot(
    range(1, ITERATIONS67 + 1),
    convergence_std67,
    label="Convergence Standard Deviation"
)

ax67_std.set_title(
    "QPSO Convergence Variation Across Runs"
)

ax67_std.set_xlabel(
    "Optimization Iteration"
)

ax67_std.set_ylabel(
    "Standard Deviation"
)

ax67_std.legend()

ax67_std.grid(
    True,
    alpha=0.3
)

st.pyplot(fig67_std)

plt.close(fig67_std)


# ------------------------------------------------------------
# 10. FINAL COST DISTRIBUTION
# ------------------------------------------------------------

st.subheader("Final Objective Cost Across Runs")

fig67_cost, ax67_cost = plt.subplots(
    figsize=(10, 5)
)

run_numbers67 = list(
    range(1, NUM_RUNS67 + 1)
)

ax67_cost.plot(
    run_numbers67,
    final_costs67,
    marker="o",
    label="Final Objective Cost"
)

ax67_cost.axhline(
    average_cost67,
    linestyle="--",
    label="Average Cost"
)

ax67_cost.set_title(
    "QPSO Final Objective Cost Across Independent Runs"
)

ax67_cost.set_xlabel(
    "Run Number"
)

ax67_cost.set_ylabel(
    "Final Objective Cost"
)

ax67_cost.legend()

ax67_cost.grid(
    True,
    alpha=0.3
)

st.pyplot(fig67_cost)

plt.close(fig67_cost)


# ------------------------------------------------------------
# 11. STABILITY INTERPRETATION
# ------------------------------------------------------------

st.subheader("Stability Interpretation")

if cost_std67 == 0:

    st.info(
        "All independent QPSO runs produced the same final "
        "objective cost in this experiment."
    )

elif cost_std67 < average_cost67 * 0.05:

    st.success(
        "The final objective cost shows relatively low variation "
        "across the independent QPSO runs, indicating stable "
        "behavior under the tested conditions."
    )

else:

    st.info(
        "The final objective cost shows noticeable variation "
        "across independent runs. This reflects the stochastic "
        "nature of metaheuristic optimization."
    )


# ------------------------------------------------------------
# 12. BEST AND WORST RUN
# ------------------------------------------------------------

best_run67 = (
    final_costs67.index(best_cost67) + 1
)

worst_run67 = (
    final_costs67.index(worst_cost67) + 1
)

st.subheader("Best and Worst Run")

st.write(
    f"Best run: Run {best_run67} "
    f"with objective cost {best_cost67:.4f}"
)

st.write(
    f"Worst run: Run {worst_run67} "
    f"with objective cost {worst_cost67:.4f}"
)


# ------------------------------------------------------------
# 13. SCIENTIFIC NOTE
# ------------------------------------------------------------

st.warning(
    "This stability analysis is based on 10 independent runs "
    "using the simulated road network. The results characterize "
    "behavior under the tested experimental conditions and "
    "should not be interpreted as a guarantee of performance "
    "on all real-world traffic networks."
)


# ------------------------------------------------------------
# 14. EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

st.subheader("Experiment Configuration")

st.write(
    f"Independent QPSO runs: {NUM_RUNS67}"
)

st.write(
    f"QPSO particles per run: {PARTICLES67}"
)

st.write(
    f"Optimization iterations per run: {ITERATIONS67}"
)

st.write(
    f"Delivery locations: {len(delivery_points61)}"
)

st.write(
    "The same road network, depot and delivery locations "
    "were used for every independent run."
)


# ------------------------------------------------------------
# 15. COMPLETION
# ------------------------------------------------------------

st.success("PART 67 COMPLETE")

print("PART 67 COMPLETE")

# ============================================================
# PART 68 - QPSO PARAMETER SENSITIVITY ANALYSIS
# ============================================================

print()
print("=" * 70)
print("PART 68 - QPSO PARAMETER SENSITIVITY ANALYSIS")
print("=" * 70)

st.header("⚙️ Part 68 — QPSO Parameter Sensitivity Analysis")

st.write(
    "This experiment studies how the number of QPSO particles "
    "affects optimization performance and computational runtime."
)


# ------------------------------------------------------------
# 1. PARTICLE SETTINGS
# ------------------------------------------------------------

particle_settings68 = [
    10,
    20,
    30,
    40
]

iterations68 = 100


# ------------------------------------------------------------
# 2. STORAGE
# ------------------------------------------------------------

sensitivity_results68 = []


# ------------------------------------------------------------
# 3. TEST DIFFERENT PARTICLE COUNTS
# ------------------------------------------------------------

for particles68 in particle_settings68:

    start68 = time.perf_counter()

    route68, cost68, convergence68 = (
        qpso_vrp_optimization(
            G61,
            depot61,
            delivery_points61,
            particles=particles68,
            iterations=iterations68
        )
    )

    runtime68 = time.perf_counter() - start68

    sensitivity_results68.append(
        {
            "Particles": particles68,
            "Objective Cost": cost68,
            "Runtime (seconds)": runtime68
        }
    )


# ------------------------------------------------------------
# 4. DISPLAY RESULTS
# ------------------------------------------------------------

st.subheader("Parameter Sensitivity Results")

display_results68 = []

for result68 in sensitivity_results68:

    display_results68.append(
        {
            "QPSO Particles": result68["Particles"],
            "Objective Cost": round(
                result68["Objective Cost"], 4
            ),
            "Runtime (seconds)": round(
                result68["Runtime (seconds)"], 4
            )
        }
    )

st.table(display_results68)


# ------------------------------------------------------------
# 5. EXTRACT VALUES
# ------------------------------------------------------------

particle_values68 = [
    result68["Particles"]
    for result68 in sensitivity_results68
]

cost_values68 = [
    result68["Objective Cost"]
    for result68 in sensitivity_results68
]

runtime_values68 = [
    result68["Runtime (seconds)"]
    for result68 in sensitivity_results68
]


# ------------------------------------------------------------
# 6. OBJECTIVE COST GRAPH
# ------------------------------------------------------------

st.subheader("Objective Cost vs Number of Particles")

fig68_cost, ax68_cost = plt.subplots(
    figsize=(10, 5)
)

ax68_cost.plot(
    particle_values68,
    cost_values68,
    marker="o",
    label="Objective Cost"
)

ax68_cost.set_title(
    "QPSO Objective Cost vs Particle Count"
)

ax68_cost.set_xlabel(
    "Number of QPSO Particles"
)

ax68_cost.set_ylabel(
    "Objective Cost"
)

ax68_cost.legend()

ax68_cost.grid(
    True,
    alpha=0.3
)

st.pyplot(fig68_cost)

plt.close(fig68_cost)


# ------------------------------------------------------------
# 7. RUNTIME GRAPH
# ------------------------------------------------------------

st.subheader("Runtime vs Number of Particles")

fig68_runtime, ax68_runtime = plt.subplots(
    figsize=(10, 5)
)

ax68_runtime.plot(
    particle_values68,
    runtime_values68,
    marker="o",
    label="Runtime"
)

ax68_runtime.set_title(
    "QPSO Runtime vs Particle Count"
)

ax68_runtime.set_xlabel(
    "Number of QPSO Particles"
)

ax68_runtime.set_ylabel(
    "Runtime (seconds)"
)

ax68_runtime.legend()

ax68_runtime.grid(
    True,
    alpha=0.3
)

st.pyplot(fig68_runtime)

plt.close(fig68_runtime)


# ------------------------------------------------------------
# 8. BEST CONFIGURATION
# ------------------------------------------------------------

best_index68 = cost_values68.index(
    min(cost_values68)
)

best_particles68 = particle_values68[
    best_index68
]

best_cost68 = cost_values68[
    best_index68
]

best_runtime68 = runtime_values68[
    best_index68
]


# ------------------------------------------------------------
# 9. DISPLAY BEST CONFIGURATION
# ------------------------------------------------------------

st.subheader("Best Tested Configuration")

st.write(
    f"Particle count with lowest objective cost: "
    f"{best_particles68}"
)

st.write(
    f"Best objective cost: {best_cost68:.4f}"
)

st.write(
    f"Runtime for this configuration: "
    f"{best_runtime68:.4f} seconds"
)


# ------------------------------------------------------------
# 10. INTERPRETATION
# ------------------------------------------------------------

st.subheader("Parameter Sensitivity Interpretation")

st.info(
    "Increasing the number of particles changes the search "
    "population available to QPSO. A larger population can "
    "provide more candidate solutions, while also increasing "
    "computational work. The experiment therefore evaluates "
    "the trade-off between solution quality and runtime."
)


# ------------------------------------------------------------
# 11. SCIENTIFIC NOTE
# ------------------------------------------------------------

st.warning(
    "The tested particle counts and results are specific to "
    "the simulated network and experimental configuration. "
    "They should not be interpreted as a universal optimal "
    "particle count for all traffic-routing problems."
)


# ------------------------------------------------------------
# 12. EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

st.subheader("Experiment Configuration")

st.write(
    "Optimization method: Quantum Particle Swarm Optimization"
)

st.write(
    f"Particle counts tested: {particle_settings68}"
)

st.write(
    f"Optimization iterations: {iterations68}"
)

st.write(
    f"Delivery locations: {len(delivery_points61)}"
)

st.write(
    "Same road network and routing problem used for every test."
)


# ------------------------------------------------------------
# 13. COMPLETION
# ------------------------------------------------------------

st.success("PART 68 COMPLETE")

print("PART 68 COMPLETE")


# ============================================================
# PART 69 - FINAL ALGORITHM BENCHMARK
# ============================================================

print()
print("=" * 70)
print("PART 69 - FINAL ALGORITHM BENCHMARK")
print("=" * 70)

st.header("📊 Part 69 — Final Algorithm Benchmark")

st.write(
    "This experiment performs a final comparison between "
    "QPSO and the Classical PSO-style baseline under the "
    "same traffic-routing conditions."
)


# ------------------------------------------------------------
# 1. CREATE FINAL BENCHMARK NETWORK
# ------------------------------------------------------------

G69 = nx.Graph()

edges69 = [
    ("A", "B", 5),
    ("B", "C", 4),
    ("C", "D", 5),
    ("D", "E", 6),
    ("E", "F", 4),
    ("F", "G", 5),

    ("A", "C", 8),
    ("B", "D", 7),
    ("C", "E", 8),
    ("D", "F", 7),
    ("E", "G", 8),

    ("A", "D", 12),
    ("B", "E", 11),
    ("C", "F", 10),
    ("D", "G", 11)
]

for u69, v69, w69 in edges69:
    G69.add_edge(
        u69,
        v69,
        weight=w69
    )


# ------------------------------------------------------------
# 2. APPLY TRAFFIC DISTURBANCE
# ------------------------------------------------------------

traffic_edges69 = [
    ("A", "B"),
    ("B", "C"),
    ("C", "D")
]

for u69, v69 in traffic_edges69:

    if G69.has_edge(u69, v69):

        G69[u69][v69]["weight"] *= 4


# ------------------------------------------------------------
# 3. ROUTING CONFIGURATION
# ------------------------------------------------------------

depot69 = "A"

delivery_points69 = [
    "B",
    "C",
    "D",
    "E",
    "F",
    "G"
]

benchmark_runs69 = 10
particles69 = 30
iterations69 = 100


# ------------------------------------------------------------
# 4. RUN QPSO AND CLASSICAL PSO
# ------------------------------------------------------------

qpso_results69 = []
pso_results69 = []

qpso_runtimes69 = []
pso_runtimes69 = []

qpso_convergence69 = []
pso_convergence69 = []


for run69 in range(benchmark_runs69):

    # -------------------------
    # QPSO
    # -------------------------

    start_qpso69 = time.perf_counter()

    route_q69, cost_q69, convergence_q69 = (
        qpso_vrp_optimization(
            G69,
            depot69,
            delivery_points69,
            particles=particles69,
            iterations=iterations69
        )
    )

    runtime_q69 = time.perf_counter() - start_qpso69

    qpso_results69.append(cost_q69)
    qpso_runtimes69.append(runtime_q69)

    if run69 == 0:
        qpso_convergence69 = convergence_q69


    # -------------------------
    # Classical PSO-style
    # -------------------------

    start_pso69 = time.perf_counter()

    route_p69, cost_p69, convergence_p69 = (
        pso_vrp_optimization(
            G69,
            depot69,
            delivery_points69,
            particles=particles69,
            iterations=iterations69
        )
    )

    runtime_p69 = time.perf_counter() - start_pso69

    pso_results69.append(cost_p69)
    pso_runtimes69.append(runtime_p69)

    if run69 == 0:
        pso_convergence69 = convergence_p69


# ------------------------------------------------------------
# 5. CALCULATE FINAL STATISTICS
# ------------------------------------------------------------

qpso_average69 = statistics.mean(qpso_results69)
pso_average69 = statistics.mean(pso_results69)

qpso_best69 = min(qpso_results69)
pso_best69 = min(pso_results69)

qpso_worst69 = max(qpso_results69)
pso_worst69 = max(pso_results69)

qpso_std69 = (
    statistics.stdev(qpso_results69)
    if len(qpso_results69) > 1
    else 0
)

pso_std69 = (
    statistics.stdev(pso_results69)
    if len(pso_results69) > 1
    else 0
)

qpso_runtime_average69 = statistics.mean(qpso_runtimes69)
pso_runtime_average69 = statistics.mean(pso_runtimes69)


# ------------------------------------------------------------
# 6. RELATIVE DIFFERENCE
# ------------------------------------------------------------

if pso_average69 != 0:

    objective_difference69 = (
        (pso_average69 - qpso_average69)
        / pso_average69
    ) * 100

else:

    objective_difference69 = 0


if pso_runtime_average69 != 0:

    runtime_difference69 = (
        (pso_runtime_average69 - qpso_runtime_average69)
        / pso_runtime_average69
    ) * 100

else:

    runtime_difference69 = 0


# ------------------------------------------------------------
# 7. DISPLAY STATISTICAL COMPARISON
# ------------------------------------------------------------

st.subheader("Final Statistical Comparison")

comparison_table69 = [
    {
        "Metric": "Average Objective Cost",
        "QPSO": round(qpso_average69, 4),
        "Classical PSO-style": round(pso_average69, 4)
    },
    {
        "Metric": "Best Objective Cost",
        "QPSO": round(qpso_best69, 4),
        "Classical PSO-style": round(pso_best69, 4)
    },
    {
        "Metric": "Worst Objective Cost",
        "QPSO": round(qpso_worst69, 4),
        "Classical PSO-style": round(pso_worst69, 4)
    },
    {
        "Metric": "Standard Deviation",
        "QPSO": round(qpso_std69, 4),
        "Classical PSO-style": round(pso_std69, 4)
    },
    {
        "Metric": "Average Runtime (seconds)",
        "QPSO": round(qpso_runtime_average69, 4),
        "Classical PSO-style": round(pso_runtime_average69, 4)
    }
]

st.table(comparison_table69)


# ------------------------------------------------------------
# 8. OBJECTIVE COST GRAPH
# ------------------------------------------------------------

st.subheader("Average Objective Cost")

fig69_cost, ax69_cost = plt.subplots(
    figsize=(9, 5)
)

ax69_cost.bar(
    ["QPSO", "Classical PSO-style"],
    [
        qpso_average69,
        pso_average69
    ]
)

ax69_cost.set_title(
    "Average Objective Cost Comparison"
)

ax69_cost.set_xlabel(
    "Optimization Method"
)

ax69_cost.set_ylabel(
    "Average Objective Cost"
)

ax69_cost.grid(
    axis="y",
    alpha=0.3
)

st.pyplot(fig69_cost)

plt.close(fig69_cost)


# ------------------------------------------------------------
# 9. RUNTIME GRAPH
# ------------------------------------------------------------

st.subheader("Average Runtime")

fig69_runtime, ax69_runtime = plt.subplots(
    figsize=(9, 5)
)

ax69_runtime.bar(
    ["QPSO", "Classical PSO-style"],
    [
        qpso_runtime_average69,
        pso_runtime_average69
    ]
)

ax69_runtime.set_title(
    "Average Computational Runtime Comparison"
)

ax69_runtime.set_xlabel(
    "Optimization Method"
)

ax69_runtime.set_ylabel(
    "Runtime (seconds)"
)

ax69_runtime.grid(
    axis="y",
    alpha=0.3
)

st.pyplot(fig69_runtime)

plt.close(fig69_runtime)


# ------------------------------------------------------------
# 10. CONVERGENCE COMPARISON
# ------------------------------------------------------------

st.subheader("Convergence Comparison")

if len(qpso_convergence69) > 0 and len(pso_convergence69) > 0:

    fig69_conv, ax69_conv = plt.subplots(
        figsize=(10, 5)
    )

    ax69_conv.plot(
        range(1, len(qpso_convergence69) + 1),
        qpso_convergence69,
        label="QPSO"
    )

    ax69_conv.plot(
        range(1, len(pso_convergence69) + 1),
        pso_convergence69,
        label="Classical PSO-style"
    )

    ax69_conv.set_title(
        "QPSO vs Classical PSO-style Convergence"
    )

    ax69_conv.set_xlabel(
        "Optimization Iteration"
    )

    ax69_conv.set_ylabel(
        "Best Objective Cost"
    )

    ax69_conv.legend()

    ax69_conv.grid(
        True,
        alpha=0.3
    )

    st.pyplot(fig69_conv)

    plt.close(fig69_conv)


# ------------------------------------------------------------
# 11. PERFORMANCE INTERPRETATION
# ------------------------------------------------------------

st.subheader("Performance Interpretation")

if objective_difference69 > 0:

    st.success(
        f"QPSO achieved a lower average objective cost than "
        f"the Classical PSO-style baseline by approximately "
        f"{objective_difference69:.2f}% in this experiment."
    )

elif objective_difference69 < 0:

    st.info(
        f"The Classical PSO-style baseline achieved a lower "
        f"average objective cost by approximately "
        f"{abs(objective_difference69):.2f}% in this experiment."
    )

else:

    st.info(
        "Both methods achieved the same average objective "
        "cost in this experiment."
    )


if runtime_difference69 > 0:

    st.write(
        f"QPSO required approximately "
        f"{runtime_difference69:.2f}% less computational time "
        f"than the Classical PSO-style baseline."
    )

elif runtime_difference69 < 0:

    st.write(
        f"The Classical PSO-style baseline required approximately "
        f"{abs(runtime_difference69):.2f}% less computational "
        f"time than QPSO."
    )

else:

    st.write(
        "Both methods required approximately the same "
        "computational time."
    )


# ------------------------------------------------------------
# 12. EXPERIMENT CONFIGURATION
# ------------------------------------------------------------

st.subheader("Experiment Configuration")

st.write(
    f"Independent benchmark runs: {benchmark_runs69}"
)

st.write(
    f"QPSO particles: {particles69}"
)

st.write(
    f"Classical PSO-style particles: {particles69}"
)

st.write(
    f"Optimization iterations: {iterations69}"
)

st.write(
    f"Delivery locations: {len(delivery_points69)}"
)

st.write(
    "Same road network and routing problem used for both methods."
)

st.write(
    "Traffic disturbance applied before benchmarking."
)


# ------------------------------------------------------------
# 13. SCIENTIFIC NOTE
# ------------------------------------------------------------

st.warning(
    "The benchmark results are specific to the simulated road "
    "network, traffic configuration and algorithm parameters "
    "used in this prototype. They should not be interpreted as "
    "universal evidence that one method always outperforms the other."
)


# ------------------------------------------------------------
# 14. COMPLETION
# ------------------------------------------------------------

st.success("PART 69 COMPLETE")

print("PART 69 COMPLETE")


# ============================================================
# PART 70 - FINAL PROJECT CONCLUSION AND DASHBOARD
# ============================================================

print()
print("=" * 70)
print("PART 70 - FINAL PROJECT CONCLUSION AND DASHBOARD")
print("=" * 70)

st.header("🏁 Part 70 — Final Project Conclusion & Dashboard")

st.write(
    "This final section summarizes the complete QuantumRoute "
    "prototype and the experimental findings obtained throughout "
    "the project."
)


# ------------------------------------------------------------
# 1. PROJECT TITLE
# ------------------------------------------------------------

st.subheader("🚦 QuantumRoute")

st.markdown(
    """
    **Quantum-Inspired Intelligent Traffic Route Optimization
    in Transportation Systems Using Metaheuristic Optimization**
    """
)


# ------------------------------------------------------------
# 2. PROJECT OBJECTIVE
# ------------------------------------------------------------

st.subheader("🎯 Project Objective")

st.write(
    "The objective of this prototype is to investigate the use "
    "of Quantum Particle Swarm Optimization (QPSO) for vehicle "
    "route optimization on a traffic-weighted road network."
)

st.write(
    "The system models roads as a weighted graph and searches "
    "for efficient routes while considering changing traffic "
    "conditions."
)


# ------------------------------------------------------------
# 3. FINAL SYSTEM COMPONENTS
# ------------------------------------------------------------

st.subheader("🧩 System Components")

system_components70 = [
    {
        "Component": "Road Network",
        "Purpose": "Represents intersections and roads using a graph"
    },
    {
        "Component": "Weighted Edges",
        "Purpose": "Represent travel cost on roads"
    },
    {
        "Component": "Traffic Simulation",
        "Purpose": "Simulates congestion by changing road weights"
    },
    {
        "Component": "QPSO",
        "Purpose": "Searches for near-optimal vehicle routes"
    },
    {
        "Component": "Classical PSO-style Baseline",
        "Purpose": "Provides a comparison method"
    },
    {
        "Component": "Benchmarking",
        "Purpose": "Evaluates cost, runtime and stability"
    },
    {
        "Component": "Streamlit Dashboard",
        "Purpose": "Provides interactive experimental visualization"
    }
]

st.table(system_components70)


# ------------------------------------------------------------
# 4. FINAL EXPERIMENTAL RESULTS
# ------------------------------------------------------------

st.subheader("📊 Final Experimental Results")

final_results70 = [
    {
        "Metric": "QPSO Average Objective Cost",
        "Result": round(qpso_average69, 4)
    },
    {
        "Metric": "QPSO Best Objective Cost",
        "Result": round(qpso_best69, 4)
    },
    {
        "Metric": "QPSO Worst Objective Cost",
        "Result": round(qpso_worst69, 4)
    },
    {
        "Metric": "QPSO Standard Deviation",
        "Result": round(qpso_std69, 4)
    },
    {
        "Metric": "QPSO Average Runtime (seconds)",
        "Result": round(qpso_runtime_average69, 4)
    },
    {
        "Metric": "Classical PSO-style Average Objective Cost",
        "Result": round(pso_average69, 4)
    },
    {
        "Metric": "Classical PSO-style Average Runtime (seconds)",
        "Result": round(pso_runtime_average69, 4)
    }
]

st.table(final_results70)


# ------------------------------------------------------------
# 5. TRAFFIC-AWARE ROUTING RESULT
# ------------------------------------------------------------

st.subheader("🚗 Traffic-Aware Routing")

st.write(
    "The prototype also evaluates route optimization before "
    "and after simulated traffic congestion."
)

traffic_summary70 = [
    {
        "Condition": "Normal Traffic",
        "Route": " → ".join(map(str, normal_route61)),
        "Objective Cost": round(normal_cost61, 4)
    },
    {
        "Condition": "Traffic Disturbed",
        "Route": " → ".join(map(str, traffic_route61)),
        "Objective Cost": round(traffic_cost61, 4)
    }
]

st.table(traffic_summary70)


if normal_route61 != traffic_route61:

    st.success(
        "The demonstration produced a route change after the "
        "traffic disturbance, showing the prototype's "
        "traffic-aware rerouting capability."
    )

else:

    st.info(
        "For this particular simulated network, the optimized "
        "route remained unchanged after the disturbance."
    )


# ------------------------------------------------------------
# 6. PROJECT WORKFLOW
# ------------------------------------------------------------

st.subheader("🔄 Complete Project Workflow")

workflow70 = [
    "1. Create a weighted road network",
    "2. Define depot and delivery locations",
    "3. Assign travel costs to road segments",
    "4. Simulate traffic congestion",
    "5. Apply QPSO to the routing problem",
    "6. Decode the optimized vehicle route",
    "7. Measure objective cost and runtime",
    "8. Compare with a Classical PSO-style baseline",
    "9. Repeat experiments for statistical evaluation",
    "10. Analyze convergence, scalability and parameter sensitivity",
    "11. Visualize final results using Streamlit"
]

for step70 in workflow70:

    st.write(step70)


# ------------------------------------------------------------
# 7. PROJECT OBJECTIVES CHECK
# ------------------------------------------------------------

st.subheader("✅ Objective Completion")

objective_check70 = [
    {
        "Project Requirement": "Graph-based road modeling",
        "Status": "Completed"
    },
    {
        "Project Requirement": "Vehicle route optimization",
        "Status": "Completed"
    },
    {
        "Project Requirement": "Quantum-inspired optimization",
        "Status": "Completed"
    },
    {
        "Project Requirement": "Traffic disturbance simulation",
        "Status": "Completed"
    },
    {
        "Project Requirement": "Traffic-aware rerouting demonstration",
        "Status": "Completed"
    },
    {
        "Project Requirement": "Convergence analysis",
        "Status": "Completed"
    },
    {
        "Project Requirement": "Multiple independent runs",
        "Status": "Completed"
    },
    {
        "Project Requirement": "Parameter sensitivity analysis",
        "Status": "Completed"
    },
    {
        "Project Requirement": "Algorithm benchmarking",
        "Status": "Completed"
    },
    {
        "Project Requirement": "Interactive visualization",
        "Status": "Completed"
    }
]

st.table(objective_check70)


# ------------------------------------------------------------
# 8. KEY FINDINGS
# ------------------------------------------------------------

st.subheader("🔎 Key Findings")

st.write(
    "• QPSO provides a metaheuristic approach for searching "
    "large route-solution spaces."
)

st.write(
    "• Changing road weights can represent simulated traffic "
    "conditions and influence route selection."
)

st.write(
    "• Multiple independent runs allow optimization stability "
    "to be examined rather than relying on a single run."
)

st.write(
    "• Parameter sensitivity experiments demonstrate the "
    "trade-off between particle population and computational "
    "runtime."
)

st.write(
    "• Benchmarking against a Classical PSO-style baseline "
    "provides a comparative evaluation of the prototype."
)


# ------------------------------------------------------------
# 9. LIMITATIONS
# ------------------------------------------------------------

st.subheader("⚠️ Limitations")

limitations70 = [
    "The road networks used in the prototype are simulated.",
    "Traffic conditions are represented using artificial weight changes.",
    "The prototype does not currently use live traffic data.",
    "The experiments do not represent every possible real-world traffic scenario.",
    "The Classical PSO implementation is used as a prototype comparison baseline.",
    "The results are specific to the tested networks and parameter configurations."
]

for limitation70 in limitations70:

    st.write("• " + limitation70)


# ------------------------------------------------------------
# 10. FUTURE SCOPE
# ------------------------------------------------------------

st.subheader("🚀 Future Scope")

future_scope70 = [
    "Integration with real road-network data such as OpenStreetMap.",
    "Integration of real-time traffic information.",
    "Support for larger vehicle-routing problems.",
    "Multiple vehicles and vehicle-capacity constraints.",
    "Time-window constraints for deliveries.",
    "More rigorous comparison with established VRP algorithms.",
    "GPU and parallel optimization for larger experiments.",
    "Deployment as a real-time intelligent transportation system."
]

for future70 in future_scope70:

    st.write("• " + future70)


# ------------------------------------------------------------
# 11. FINAL PROJECT CONCLUSION
# ------------------------------------------------------------

st.subheader("🏆 Final Conclusion")

st.success(
    "The QuantumRoute prototype demonstrates how Quantum "
    "Particle Swarm Optimization can be implemented on a "
    "classical computer to investigate traffic-aware vehicle "
    "route optimization."
)

st.write(
    "The project successfully combines graph-based road "
    "modeling, traffic-weight simulation, QPSO optimization, "
    "convergence analysis, statistical experiments, parameter "
    "sensitivity analysis and algorithm benchmarking."
)

st.write(
    "The experimental results should be interpreted as evidence "
    "from the simulated test environments rather than as a "
    "claim of universal superiority of QPSO."
)


# ------------------------------------------------------------
# 12. FINAL PERFORMANCE INDICATORS
# ------------------------------------------------------------

st.subheader("📈 Final Performance Indicators")

indicator70_a, indicator70_b, indicator70_c = st.columns(3)

with indicator70_a:

    st.metric(
        "Benchmark Runs",
        benchmark_runs69
    )

with indicator70_b:

    st.metric(
        "QPSO Particles",
        particles69
    )

with indicator70_c:

    st.metric(
        "Optimization Iterations",
        iterations69
    )


# ------------------------------------------------------------
# 13. FINAL TECHNICAL CONFIGURATION
# ------------------------------------------------------------

st.subheader("⚙️ Final Technical Configuration")

technical_configuration70 = [
    {
        "Parameter": "Optimization Algorithm",
        "Value": "Quantum Particle Swarm Optimization"
    },
    {
        "Parameter": "Programming Language",
        "Value": "Python"
    },
    {
        "Parameter": "Visualization / Interface",
        "Value": "Streamlit"
    },
    {
        "Parameter": "Graph Library",
        "Value": "NetworkX"
    },
    {
        "Parameter": "Numerical / Scientific Tools",
        "Value": "Python scientific computing stack"
    },
    {
        "Parameter": "Benchmark Runs",
        "Value": benchmark_runs69
    },
    {
        "Parameter": "QPSO Particles",
        "Value": particles69
    },
    {
        "Parameter": "Optimization Iterations",
        "Value": iterations69
    }
]

st.table(technical_configuration70)


# ------------------------------------------------------------
# 14. FINAL PROJECT MESSAGE
# ------------------------------------------------------------

st.subheader("💡 Final Project Message")

st.info(
    "QuantumRoute demonstrates a classical-computer implementation "
    "of a quantum-inspired metaheuristic for intelligent traffic "
    "route optimization. The prototype establishes the complete "
    "experimental workflow required for further development toward "
    "real-world transportation applications."
)


# ------------------------------------------------------------
# 15. FINAL COMPLETION
# ------------------------------------------------------------

st.success(
    "🎉 PART 70 COMPLETE — QUANTUMROUTE PROJECT COMPLETE"
)

st.success(
    "All planned experimental and analytical sections have "
    "been implemented in the Streamlit prototype."
)

print("PART 70 COMPLETE")
print("QUANTUMROUTE PROJECT COMPLETE")

