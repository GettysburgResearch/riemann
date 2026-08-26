#!/usr/bin/env python3
"""Exact bounded replay for graph-indexed quadratic Kummer characters."""

from __future__ import annotations

import argparse
import json
import math
import time
from collections import Counter
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTE_PATH = HERE / "FFPS_GRAPH_KUMMER_CHARACTER_SPECTRUM.md"

MAX_VERTICES = 5
MAX_SIMPLE_GRAPHS = 1 << math.comb(MAX_VERTICES, 2)
MAX_ENUMERATED_EDGES = math.comb(MAX_VERTICES, 2)
MAX_EDGE_SUBSET_EVALUATIONS = 1_000_000
MAX_MASK_ENUMERATION_DIMENSION = 12
MAX_WALL_SECONDS = 3.0


def gf2_basis(vectors: tuple[int, ...]) -> tuple[int, ...]:
    """Return a deterministic high-pivot basis over F_2."""

    basis: dict[int, int] = {}
    for original in vectors:
        value = original
        while value:
            pivot = value.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = value
                break
            value ^= basis[pivot]
    return tuple(basis[pivot] for pivot in sorted(basis, reverse=True))


def gf2_rank(vectors: tuple[int, ...]) -> int:
    return len(gf2_basis(vectors))


def span_elements(vectors: tuple[int, ...]) -> tuple[int, ...]:
    elements = [0]
    for vector in gf2_basis(vectors):
        elements += [element ^ vector for element in elements]
    return tuple(elements)


def _validate_graph(
    vertex_count: int, edges: tuple[tuple[int, int], ...]
) -> tuple[tuple[tuple[int, int], ...], tuple[int, ...], tuple[int, ...]]:
    if (
        isinstance(vertex_count, bool)
        or not isinstance(vertex_count, int)
        or vertex_count < 2
    ):
        raise ValueError("vertex_count must be at least two")
    normalized: set[tuple[int, int]] = set()
    degrees = [0] * vertex_count
    incidence: list[int] = []
    for edge in edges:
        if len(edge) != 2:
            raise ValueError("every edge must have two endpoints")
        left, right = edge
        if (
            isinstance(left, bool)
            or isinstance(right, bool)
            or not isinstance(left, int)
            or not isinstance(right, int)
            or not 0 <= left < vertex_count
            or not 0 <= right < vertex_count
            or left == right
        ):
            raise ValueError("edge endpoints must be distinct graph vertices")
        canonical = (min(left, right), max(left, right))
        if canonical in normalized:
            raise ValueError("parallel edges are not allowed")
        normalized.add(canonical)
        degrees[left] += 1
        degrees[right] += 1
        incidence.append((1 << left) | (1 << right))
    if any(degree == 0 for degree in degrees):
        raise ValueError("graph vertices must all be incident")
    return tuple(sorted(normalized)), tuple(degrees), tuple(incidence)


def _component_masks(
    vertex_count: int, edges: tuple[tuple[int, int], ...]
) -> tuple[int, ...]:
    adjacency = [set() for _ in range(vertex_count)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    unseen = set(range(vertex_count))
    components: list[int] = []
    while unseen:
        root = unseen.pop()
        frontier = [root]
        component = 0
        while frontier:
            vertex = frontier.pop()
            component |= 1 << vertex
            for neighbor in adjacency[vertex]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    frontier.append(neighbor)
        components.append(component)
    return tuple(sorted(components))


def incidence_boundary(edge_subset: int, incidence: tuple[int, ...]) -> int:
    if (
        isinstance(edge_subset, bool)
        or not isinstance(edge_subset, int)
        or edge_subset < 0
        or edge_subset >= 1 << len(incidence)
    ):
        raise ValueError("edge_subset is outside the edge-coordinate space")
    boundary = 0
    for edge_index, column in enumerate(incidence):
        if edge_subset & (1 << edge_index):
            boundary ^= column
    return boundary


def graph_profile(
    vertex_count: int, edges: tuple[tuple[int, int], ...]
) -> dict[str, object]:
    normalized, degrees, incidence = _validate_graph(vertex_count, edges)
    components = _component_masks(vertex_count, normalized)
    rank = gf2_rank(incidence)
    expected_rank = vertex_count - len(components)
    if rank != expected_rank:
        raise ArithmeticError("binary incidence rank disagrees with |V|-c")
    edge_count = len(normalized)
    beta = edge_count - rank
    top_boundary = incidence_boundary((1 << edge_count) - 1, incidence)
    expected_top = sum(
        1 << vertex for vertex, degree in enumerate(degrees) if degree % 2
    )
    if top_boundary != expected_top:
        raise ArithmeticError("all-edge boundary is not the odd-degree divisor")
    return {
        "vertex_count": vertex_count,
        "edge_count": edge_count,
        "component_count": len(components),
        "component_masks": components,
        "incidence_columns": incidence,
        "incidence_rank": rank,
        "cycle_dimension": beta,
        "forest": beta == 0,
        "connected": len(components) == 1,
        "degrees": degrees,
        "top_boundary_bits": top_boundary,
        "top_boundary_vertices": top_boundary.bit_count(),
        "top_invariant": top_boundary == 0,
    }


def admissible_boundary(pattern: int, component_masks: tuple[int, ...]) -> bool:
    return all(
        (pattern & component).bit_count() % 2 == 0 for component in component_masks
    )


def exact_fiber_census(
    vertex_count: int, edges: tuple[tuple[int, int], ...]
) -> dict[str, object]:
    profile = graph_profile(vertex_count, edges)
    if profile["edge_count"] > MAX_ENUMERATED_EDGES:
        raise RuntimeError("exact fiber census edge cap exceeded")
    incidence = profile["incidence_columns"]
    fibers = Counter(
        incidence_boundary(edge_subset, incidence)
        for edge_subset in range(1 << profile["edge_count"])
    )
    admissible = {
        pattern
        for pattern in range(1 << vertex_count)
        if admissible_boundary(pattern, profile["component_masks"])
    }
    fiber_size = 1 << profile["cycle_dimension"]
    if set(fibers) != admissible or set(fibers.values()) != {fiber_size}:
        raise ArithmeticError("incidence-boundary fibers are not uniform")
    branch_histogram = Counter()
    for pattern, multiplicity in fibers.items():
        branch_histogram[pattern.bit_count()] += multiplicity
    return {
        **profile,
        "admissible_boundary_patterns": len(admissible),
        "fiber_size": fiber_size,
        "invariant_modes": fibers[0],
        "nontrivial_invariant_modes": fibers[0] - 1,
        "fiber_histogram": dict(sorted(Counter(fibers.values()).items())),
        "branch_vertex_histogram": dict(sorted(branch_histogram.items())),
    }


def connected_branch_betti_spectrum(
    vertex_count: int, edge_count: int, closed_place_degree: int
) -> dict[str, object]:
    if (
        isinstance(vertex_count, bool)
        or not isinstance(vertex_count, int)
        or vertex_count < 2
    ):
        raise ValueError("vertex_count must be at least two")
    if (
        isinstance(edge_count, bool)
        or not isinstance(edge_count, int)
        or not vertex_count - 1 <= edge_count <= math.comb(vertex_count, 2)
    ):
        raise ValueError("edge_count is impossible for a connected simple graph")
    if (
        isinstance(closed_place_degree, bool)
        or not isinstance(closed_place_degree, int)
        or closed_place_degree < 1
    ):
        raise ValueError("closed_place_degree must be positive")

    beta = edge_count - vertex_count + 1
    fiber_size = 1 << beta
    rows: list[dict[str, int]] = []
    for branch_vertices in range(0, vertex_count + 1, 2):
        branch_points = closed_place_degree * branch_vertices
        multiplicity = fiber_size * math.comb(vertex_count, branch_vertices)
        minimal_h1 = 0 if branch_vertices == 0 else branch_points - 2
        minimal_h2 = 1 if branch_vertices == 0 else 0
        rows.append(
            {
                "branch_vertices": branch_vertices,
                "geometric_branch_points": branch_points,
                "multiplicity": multiplicity,
                "minimal_h1_per_mode": minimal_h1,
                "minimal_h2_per_mode": minimal_h2,
                "minimal_h1_contribution": multiplicity * minimal_h1,
                "minimal_h2_contribution": multiplicity * minimal_h2,
            }
        )

    total_modes = 1 << edge_count
    invariant_modes = fiber_size
    nonconstant_modes = total_modes - invariant_modes
    total_branch_points = closed_place_degree * vertex_count * (1 << (edge_count - 1))
    total_minimal_h1 = fiber_size * (
        closed_place_degree * vertex_count * (1 << (vertex_count - 2))
        - 2 * ((1 << (vertex_count - 1)) - 1)
    )
    common_punctures = closed_place_degree * vertex_count
    total_common_h1 = nonconstant_modes * (common_punctures - 2) + invariant_modes * (
        common_punctures - 1
    )
    total_nonconstant_tax = sum(
        row["multiplicity"] * (common_punctures - row["geometric_branch_points"])
        for row in rows
        if row["branch_vertices"]
    )
    if sum(row["multiplicity"] for row in rows) != total_modes:
        raise ArithmeticError("branch spectrum does not close to 2^|E|")
    if sum(row["minimal_h1_contribution"] for row in rows) != total_minimal_h1:
        raise ArithmeticError("closed minimal-H1 total disagrees with the spectrum")
    return {
        "vertex_count": vertex_count,
        "edge_count": edge_count,
        "cycle_dimension": beta,
        "closed_place_degree": closed_place_degree,
        "rows": rows,
        "closed_totals": {
            "all_modes": total_modes,
            "invariant_modes": invariant_modes,
            "nontrivial_invariant_modes": invariant_modes - 1,
            "nonconstant_modes": nonconstant_modes,
            "geometric_branch_points_across_all_modes": total_branch_points,
            "minimal_h1_across_all_modes": total_minimal_h1,
            "minimal_h2_across_all_modes": invariant_modes,
            "common_open_h1_across_all_modes": total_common_h1,
            "nonconstant_removable_puncture_tax": total_nonconstant_tax,
        },
    }


def mask_transversality_profile(
    vertex_count: int,
    edges: tuple[tuple[int, int], ...],
    generators: tuple[int, ...],
) -> dict[str, object]:
    profile = graph_profile(vertex_count, edges)
    edge_count = profile["edge_count"]
    if any(
        isinstance(generator, bool)
        or not isinstance(generator, int)
        or generator < 0
        or generator >= 1 << edge_count
        for generator in generators
    ):
        raise ValueError("mask generator is outside the edge-coordinate space")
    basis = gf2_basis(generators)
    image_basis = gf2_basis(
        tuple(
            incidence_boundary(generator, profile["incidence_columns"])
            for generator in basis
        )
    )
    mask_dimension = len(basis)
    image_dimension = len(image_basis)
    intersection_dimension = mask_dimension - image_dimension
    invariant_nonzero = (1 << intersection_dimension) - 1

    enumerated_invariant_nonzero: int | None = None
    if mask_dimension <= MAX_MASK_ENUMERATION_DIMENSION:
        enumerated_invariant_nonzero = sum(
            element != 0
            and incidence_boundary(element, profile["incidence_columns"]) == 0
            for element in span_elements(basis)
        )
        if enumerated_invariant_nonzero != invariant_nonzero:
            raise ArithmeticError("mask-cycle intersection count failed")
    return {
        "mask_dimension": mask_dimension,
        "boundary_image_dimension": image_dimension,
        "cycle_dimension": profile["cycle_dimension"],
        "mask_cycle_intersection_dimension": intersection_dimension,
        "invariant_nontrivial_selected_modes": invariant_nonzero,
        "boundary_restriction_injective": intersection_dimension == 0,
        "enumerated_invariant_nontrivial_selected_modes": enumerated_invariant_nonzero,
    }


def _is_connected(vertex_count: int, edges: tuple[tuple[int, int], ...]) -> bool:
    if not edges:
        return False
    adjacency = [set() for _ in range(vertex_count)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    reached = {0}
    frontier = [0]
    while frontier:
        vertex = frontier.pop()
        for neighbor in adjacency[vertex] - reached:
            reached.add(neighbor)
            frontier.append(neighbor)
    return len(reached) == vertex_count


def connected_graph_census(max_vertices: int = MAX_VERTICES) -> dict[str, object]:
    if (
        isinstance(max_vertices, bool)
        or not isinstance(max_vertices, int)
        or not 2 <= max_vertices <= MAX_VERTICES
    ):
        raise ValueError(f"max_vertices must lie between two and {MAX_VERTICES}")
    rows: list[dict[str, int]] = []
    graph_count = 0
    edge_subset_evaluations = 0
    for vertex_count in range(2, max_vertices + 1):
        complete_edges = tuple(combinations(range(vertex_count), 2))
        connected_count = 0
        tree_count = 0
        path_count = 0
        for graph_mask in range(1, 1 << len(complete_edges)):
            edges = tuple(
                edge
                for edge_index, edge in enumerate(complete_edges)
                if graph_mask & (1 << edge_index)
            )
            if not _is_connected(vertex_count, edges):
                continue
            connected_count += 1
            graph_count += 1
            census = exact_fiber_census(vertex_count, edges)
            evaluations = 1 << census["edge_count"]
            edge_subset_evaluations += evaluations
            if edge_subset_evaluations > MAX_EDGE_SUBSET_EVALUATIONS:
                raise RuntimeError("edge-subset evaluation cap exceeded")

            observed_spectrum = Counter()
            for edge_subset in range(1 << census["edge_count"]):
                boundary = incidence_boundary(edge_subset, census["incidence_columns"])
                observed_spectrum[boundary.bit_count()] += 1
            fiber_size = 1 << census["cycle_dimension"]
            expected_spectrum = {
                branch_vertices: fiber_size * math.comb(vertex_count, branch_vertices)
                for branch_vertices in range(0, vertex_count + 1, 2)
            }
            if dict(observed_spectrum) != expected_spectrum:
                raise ArithmeticError("connected branch spectrum mismatch")

            if census["forest"]:
                tree_count += 1
                is_path = max(census["degrees"]) <= 2
                if (census["top_boundary_vertices"] == 2) != is_path:
                    raise ArithmeticError("tree top mode has two branches off a path")
                path_count += int(is_path)
        rows.append(
            {
                "vertex_count": vertex_count,
                "connected_graphs": connected_count,
                "trees": tree_count,
                "paths": path_count,
            }
        )
    return {
        "rows": rows,
        "connected_graphs": graph_count,
        "edge_subset_evaluations": edge_subset_evaluations,
    }


def build_report() -> dict[str, object]:
    started = time.monotonic()
    census = connected_graph_census()
    path_edges = ((0, 1), (1, 2), (2, 3), (3, 4))
    star_edges = ((0, 1), (0, 2), (0, 3), (0, 4))
    cycle_edges = ((0, 1), (1, 2), (2, 3), (3, 4), (0, 4))
    path = exact_fiber_census(5, path_edges)
    star = exact_fiber_census(5, star_edges)
    cycle = exact_fiber_census(5, cycle_edges)
    path_spectrum = connected_branch_betti_spectrum(5, 4, 3)
    star_spectrum = connected_branch_betti_spectrum(5, 4, 3)
    formula_histogram = {
        row["branch_vertices"]: row["multiplicity"] for row in path_spectrum["rows"]
    }
    if (
        path_spectrum != star_spectrum
        or path["branch_vertex_histogram"] != star["branch_vertex_histogram"]
        or path["branch_vertex_histogram"] != formula_histogram
    ):
        raise ArithmeticError("tree topology changed the full character spectrum")

    full_cycle_mask = mask_transversality_profile(
        5, cycle_edges, tuple(1 << edge for edge in range(5))
    )
    cycle_broken_mask = mask_transversality_profile(
        5, cycle_edges, tuple(1 << edge for edge in range(4))
    )
    if full_cycle_mask["invariant_nontrivial_selected_modes"] != 1:
        raise ArithmeticError("full cycle mask lost its invariant selected mode")
    if not cycle_broken_mask["boundary_restriction_injective"]:
        raise ArithmeticError("cycle-broken mask is not transverse")
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return {
        "schema": "riemann.function_field.ffps_graph_kummer_character_spectrum.v1",
        "status": "EXACT_GRAPH_KUMMER_CHARACTER_SPECTRUM",
        "theorems": {
            "boundary_map": "F2 edge incidence boundary",
            "kernel_dimension": "beta=|E|-|V|+components",
            "uniform_fiber_size": "2^beta",
            "nontrivial_invariant_modes": "2^beta-1",
            "connected_branch_multiplicity": "2^beta*binomial(|V|,2r)",
            "mask_invariant_multiplicity": "2^dim(W intersect cycle)-1",
            "mask_transversality": "no invariant iff boundary restricted to W is injective",
        },
        "controls": {
            "path_top_boundary_vertices": path["top_boundary_vertices"],
            "star_top_boundary_vertices": star["top_boundary_vertices"],
            "cycle_beta": cycle["cycle_dimension"],
            "cycle_nontrivial_invariant_modes": cycle["nontrivial_invariant_modes"],
            "tree_spectrum": path_spectrum,
            "full_cycle_mask": full_cycle_mask,
            "cycle_broken_mask": cycle_broken_mask,
        },
        "exhaustive_census": census,
        "resource_ledger": {
            "max_vertices": MAX_VERTICES,
            "simple_graph_masks_cap": MAX_SIMPLE_GRAPHS,
            "enumerated_edges_cap": MAX_ENUMERATED_EDGES,
            "edge_subset_evaluations": census["edge_subset_evaluations"],
            "edge_subset_evaluations_cap": MAX_EDGE_SUBSET_EVALUATIONS,
            "finite_fields_enumerated": 0,
            "polynomials_enumerated": 0,
            "curves_enumerated": 0,
            "cohomology_groups_computed": 0,
        },
        "firewalls": [
            "formal edge Fourier modes may collapse to the same geometric Kummer line",
            "an invariant cycle mode carries H_c^2 and is not square-root cancellation",
            "tree spectral universality does not make the all-edge top mode source-canonical",
            "mask transversality is not a varying-conductor trace estimate",
            "no FFPS source realization, CYSEL, RH, or GRH follows",
        ],
    }


def run_checks() -> dict[str, object]:
    report = build_report()
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "cycle space",
        "2^\\beta-1",
        "Mask transversality",
        "only relocates the distinguished top mode",
        "varying-conductor trace estimate",
        "No external novelty or priority claim",
    ):
        if marker not in note:
            raise RuntimeError(f"note contract marker missing: {marker}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = run_checks() if args.check else build_report()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
