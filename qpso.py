# ============================================================
# QPSO ROUTE OPTIMIZATION MODULE
# ============================================================

import random
import math
import networkx as nx


def calculate_route_cost(graph, route):
    """
    Calculate total travel cost of a route.
    """

    total_cost = 0

    for i in range(len(route) - 1):

        try:
            path = nx.shortest_path(
                graph,
                route[i],
                route[i + 1],
                weight="weight"
            )

            for j in range(len(path) - 1):

                total_cost += graph[
                    path[j]
                ][
                    path[j + 1]
                ].get("weight", 1)

        except nx.NetworkXNoPath:

            return float("inf")

    return total_cost


def qpso_vrp_optimization(
    graph,
    depot,
    delivery_points,
    particles=30,
    iterations=100
):
    """
    Quantum-inspired Particle Swarm Optimization
    adapted for the Vehicle Routing Problem.

    A continuous position vector is converted into
    a delivery sequence by sorting its values.
    """

    if not delivery_points:
        return [depot, depot], 0, [0]

    dimension = len(delivery_points)

    swarm = []

    # --------------------------------------------------------
    # INITIALIZE PARTICLES
    # --------------------------------------------------------

    for _ in range(particles):

        position = [
            random.uniform(0, 1)
            for _ in range(dimension)
        ]

        order_indices = sorted(
            range(dimension),
            key=lambda i: position[i]
        )

        order = [
            delivery_points[i]
            for i in order_indices
        ]

        route = [depot] + order + [depot]

        cost = calculate_route_cost(
            graph,
            route
        )

        swarm.append({
            "position": position,
            "pbest_position": position[:],
            "pbest_cost": cost
        })

    # --------------------------------------------------------
    # GLOBAL BEST
    # --------------------------------------------------------

    best_particle = min(
        swarm,
        key=lambda particle: particle["pbest_cost"]
    )

    gbest_position = (
        best_particle["pbest_position"][:]
    )

    gbest_cost = (
        best_particle["pbest_cost"]
    )

    convergence = []

    # --------------------------------------------------------
    # QPSO ITERATIONS
    # --------------------------------------------------------

    for iteration in range(iterations):

        # Mean best position
        mbest = []

        for d in range(dimension):

            mean_value = sum(
                particle["pbest_position"][d]
                for particle in swarm
            ) / len(swarm)

            mbest.append(mean_value)

        # Contraction-expansion coefficient
        beta_max = 1.0
        beta_min = 0.5

        if iterations > 1:

            beta = (
                beta_max
                -
                (
                    (beta_max - beta_min)
                    * iteration
                    / (iterations - 1)
                )
            )

        else:

            beta = beta_min

        # ----------------------------------------------------
        # UPDATE EVERY PARTICLE
        # ----------------------------------------------------

        for particle in swarm:

            old_position = particle["position"]

            new_position = []

            for d in range(dimension):

                u = random.random()

                u = max(
                    u,
                    1e-12
                )

                phi = random.random()

                # Local attractor
                p = (
                    phi
                    * particle["pbest_position"][d]
                    +
                    (1 - phi)
                    * gbest_position[d]
                )

                distance = abs(
                    mbest[d]
                    -
                    old_position[d]
                )

                # Quantum-inspired movement
                quantum_step = (
                    beta
                    * distance
                    * math.log(1 / u)
                )

                if random.random() < 0.5:

                    new_value = (
                        p
                        +
                        quantum_step
                    )

                else:

                    new_value = (
                        p
                        -
                        quantum_step
                    )

                # Keep position within limits
                new_value = max(
                    -2.0,
                    min(2.0, new_value)
                )

                new_position.append(
                    new_value
                )

            # ------------------------------------------------
            # DECODE POSITION INTO DELIVERY ORDER
            # ------------------------------------------------

            order_indices = sorted(
                range(dimension),
                key=lambda i: new_position[i]
            )

            candidate_order = [
                delivery_points[i]
                for i in order_indices
            ]

            candidate_route = (
                [depot]
                +
                candidate_order
                +
                [depot]
            )

            candidate_cost = calculate_route_cost(
                graph,
                candidate_route
            )

            # ------------------------------------------------
            # PERSONAL BEST
            # ------------------------------------------------

            if candidate_cost < particle["pbest_cost"]:

                particle["pbest_position"] = (
                    new_position[:]
                )

                particle["pbest_cost"] = (
                    candidate_cost
                )

            particle["position"] = (
                new_position
            )

            # ------------------------------------------------
            # GLOBAL BEST
            # ------------------------------------------------

            if particle["pbest_cost"] < gbest_cost:

                gbest_cost = (
                    particle["pbest_cost"]
                )

                gbest_position = (
                    particle["pbest_position"][:]
                )

        # Store best result for convergence graph
        convergence.append(
            gbest_cost
        )

    # --------------------------------------------------------
    # FINAL BEST ROUTE
    # --------------------------------------------------------

    best_order_indices = sorted(
        range(dimension),
        key=lambda i: gbest_position[i]
    )

    best_order = [
        delivery_points[i]
        for i in best_order_indices
    ]

    best_route = (
        [depot]
        +
        best_order
        +
        [depot]
    )

    return (
        best_route,
        gbest_cost,
        convergence
    )