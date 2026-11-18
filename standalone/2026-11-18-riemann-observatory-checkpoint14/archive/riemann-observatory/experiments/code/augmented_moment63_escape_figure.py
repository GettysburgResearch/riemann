#!/usr/bin/env python3
"""Check and plot the synthetic augmented-moment escape example."""

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, LogFormatterMathtext, ScalarFormatter


@dataclass(frozen=True)
class MomentPoint:
    index: int
    node: int
    weights: tuple[Fraction, Fraction, Fraction]
    cost_gap: Fraction
    leading_term: Fraction
    remote_second_moment: Fraction


def exact_point(index: int) -> MomentPoint:
    node = index * (index - 1)
    remote_weight = Fraction(1, (node - 6) * (node - 2))
    weight_at_two = Fraction(1, 4 * (node - 2))
    weight_at_six = 1 - remote_weight - weight_at_two
    weights = (weight_at_two, weight_at_six, remote_weight)
    nodes = (2, 6, node)

    assert all(weight > 0 for weight in weights)
    moments = tuple(
        sum(weight * location**degree for weight, location in zip(weights, nodes))
        for degree in range(3)
    )
    assert moments == (1, 6, 37)

    remote_cost = Fraction(1, (index - 1) ** 2)
    cost = weight_at_two + weight_at_six / 4 + remote_weight * remote_cost
    gap = cost - Fraction(1, 4)
    leading = Fraction(3, 16 * node)
    remainder = (node - 10 + Fraction(8, index - 1)) / (
        8 * node * (node - 2) * (node - 6)
    )
    assert gap > 0
    assert gap - leading == remainder
    assert 0 < remainder <= Fraction(1, 8 * node**2)

    contribution = node**2 * remote_weight
    assert contribution > 1
    return MomentPoint(index, node, weights, gap, leading, contribution)


def save_checks(points: list[MomentPoint], directory: Path) -> None:
    report = {
        "profile": "Synthetic positive measures on nodes 2, 6 and m(m-1)",
        "arithmetic": "Python Fraction",
        "first_index": points[0].index,
        "last_index": points[-1].index,
        "checked_profiles": len(points),
        "checks_passed": [
            "All three weights are strictly positive",
            "Moments in degrees 0, 1 and 2 are exactly 1, 6 and 37",
            "The cost gap is strictly positive",
            "The exact cost gap exceeds 3/(16x) by at most 1/(8x^2)",
            "The remote second-moment contribution exceeds 1",
        ],
        "profiles": [
            {
                "m": point.index,
                "x": point.node,
                "weights_at_2_6_x": [str(weight) for weight in point.weights],
                "cost_gap": str(point.cost_gap),
                "leading_term": str(point.leading_term),
                "remote_second_moment": str(point.remote_second_moment),
            }
            for point in points
        ],
    }
    path = directory / "augmented_moment63_escape_checks.json"
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


def render(points: list[MomentPoint], directory: Path) -> None:
    mpl_style = {
        "font.family": "DejaVu Sans",
        "mathtext.fontset": "dejavusans",
        "font.size": 10,
        "text.color": "#18242F",
        "axes.labelcolor": "#18242F",
        "axes.edgecolor": "#64737F",
        "axes.linewidth": 0.75,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.color": "#364955",
        "ytick.color": "#364955",
        "xtick.direction": "out",
        "ytick.direction": "out",
        "savefig.facecolor": "white",
        "svg.fonttype": "none",
        "svg.hashsalt": "augmented-moment-escape",
        "pdf.fonttype": 42,
    }
    with plt.rc_context(mpl_style):
        figure, (cost_axis, remote_axis) = plt.subplots(ncols=2, figsize=(9.3, 4.5))
        figure.subplots_adjust(left=0.104, right=0.975, bottom=0.225, top=0.756, wspace=0.36)

        ink = "#18242F"
        teal = "#006B73"
        plum = "#704074"
        gray = "#596B77"
        figure.text(0.104, 0.965, "An unattainable limit for a lattice moment cost",
                    ha="left", va="top", fontsize=17, fontweight="bold", color=ink)
        figure.text(0.104, 0.888, "Every measure has total mass 1, mean 6 and second moment 37",
                    ha="left", va="top", fontsize=10.5, color=gray)

        indices = [point.index for point in points]
        markers = {4, 5, 7, 10, 15, 23, 35, 53, 80, 120, 160, 200}
        sampled = [point for point in points if point.index in markers]

        for axis in (cost_axis, remote_axis):
            axis.set_xscale("log")
            axis.set_xlim(3.65, 223)
            axis.xaxis.set_major_locator(FixedLocator([4, 10, 20, 50, 100, 200]))
            axis.xaxis.set_major_formatter(ScalarFormatter())
            axis.tick_params(axis="x", which="minor", bottom=False)
            axis.tick_params(which="major", length=4, pad=4)
            axis.set_axisbelow(True)
            axis.grid(axis="y", color="#D8E1E6", linewidth=0.65)

        cost_axis.set_title("A   Cost above the lower bound", loc="left", fontsize=11.2,
                            fontweight="bold", pad=9)
        cost_axis.set_yscale("log")
        cost_axis.set_ylim(3.6e-6, 2.9e-2)
        cost_axis.yaxis.set_major_locator(FixedLocator([1e-5, 1e-4, 1e-3, 1e-2]))
        cost_axis.yaxis.set_major_formatter(LogFormatterMathtext())
        cost_axis.tick_params(axis="y", which="minor", left=False)
        cost_axis.set_ylabel(r"Cost gap, $c-1/4$")
        leading_line, = cost_axis.plot(indices, [float(point.leading_term) for point in points],
                                       color=gray, linestyle=(0, (4, 3)), linewidth=1.25,
                                       label=r"Leading term $3/(16x)$")
        cost_points, = cost_axis.plot([point.index for point in sampled],
                                      [float(point.cost_gap) for point in sampled],
                                      linestyle="none", marker="o", markersize=4.3,
                                      markerfacecolor=teal, markeredgecolor="white",
                                      markeredgewidth=0.5, label="Exact cost gap")
        cost_axis.legend(handles=[cost_points, leading_line], loc="upper right", frameon=False,
                         fontsize=9, handlelength=2.3, borderaxespad=0.5)

        remote_axis.set_title("B   Remote atom's second moment", loc="left", fontsize=11.2,
                              fontweight="bold", pad=9)
        remote_axis.set_ylim(0.85, 2.56)
        remote_axis.set_yticks([1.0, 1.5, 2.0, 2.5])
        remote_axis.set_ylabel(r"Contribution, $x^2 w_x$")
        remote_axis.plot(indices, [float(point.remote_second_moment) for point in points],
                         color=plum, linewidth=2.1, solid_capstyle="round")
        remote_axis.plot([point.index for point in sampled],
                         [float(point.remote_second_moment) for point in sampled],
                         linestyle="none", marker="o", markersize=4.0,
                         markerfacecolor=plum, markeredgecolor="white", markeredgewidth=0.5)
        remote_axis.axhline(1, color=gray, linestyle=(0, (4, 3)), linewidth=1.05, zorder=2)
        remote_axis.text(190, 1.10, "Limit = 1", ha="right", va="bottom", color=gray, fontsize=9)

        figure.supxlabel(r"Remote lattice index, $m$, with $x=m(m-1)$", x=0.54, y=0.137, fontsize=10.5)
        figure.text(0.104, 0.079, r"Strict Jensen inequality rules out $c=1/4$ at variance 1.",
                    fontsize=9.4, ha="left", color=ink)
        figure.text(0.104, 0.036, "Synthetic lattice measures", fontsize=9.1, ha="left", color=gray)

        title = "An unattainable limit for a lattice moment cost"
        stem = directory / "augmented_moment63_escape"
        figure.savefig(stem.with_suffix(".png"), dpi=300, metadata={"Title": title})
        figure.savefig(stem.with_suffix(".svg"), metadata={"Title": title, "Date": None})
        figure.savefig(stem.with_suffix(".pdf"), metadata={"Title": title, "CreationDate": None})
        plt.close(figure)


def main() -> None:
    default_directory = Path(__file__).resolve().parents[1] / "results"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=default_directory)
    directory = parser.parse_args().output_dir
    directory.mkdir(parents=True, exist_ok=True)

    points = [exact_point(index) for index in range(4, 201)]
    save_checks(points, directory)
    render(points, directory)
    print(f"Verified {len(points)} exact profiles and wrote PNG, SVG, PDF and JSON to {directory}")


if __name__ == "__main__":
    main()
