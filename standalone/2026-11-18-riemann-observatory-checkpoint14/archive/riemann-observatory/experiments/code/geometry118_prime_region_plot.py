#!/usr/bin/env python3
"""Plot the accepted Round 14 prime exponent regions using exact polygon clipping."""

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Polygon


STEM = "prime_regions_round14"
DOMAIN = (F(1, 2), F(2, 3), F(1, 4), F(3, 4))
SQUARE_LIMIT = F(9, 17)

# Each form a*theta + b*xi - c is negative in the accepted open region.
BAKER = (
    (F(1, 2), -1, 0),
    (-1, 1, 0),
    (F(11, 10), F(4, 5), 1),
    (1, F(11, 12), 1),
)
FOUVRY_SHPARLINSKI = (
    (0, -1, 0),
    (F(-3, 2), 1, 0),
    (F(13, 10), F(3, 5), 1),
    (F(13, 12), F(5, 6), 1),
)
ELEMENTARY = (1, 1, 1)

ALT = (
    "Exponent map for coprime-prime blocks with modulus K of order T to the theta "
    "and prime scale P of order T to the xi. Blue is Baker only, ochre is "
    "Fouvry–Shparlinski only, and violet is their overlap. Stronger fill above "
    "the descending dashed line xi = 1 − theta shows the additional prime "
    "region beyond the limiting elementary short-factor cutoff. The vertical "
    "dotted line at theta = 9/17 marks the separate all-square result to "
    "its left and does not bound the prime regions. The prime estimates hold "
    "at strict interior points for a fixed transition exponent sufficiently "
    "close to one. Longer primes remain outside the shaded regions."
)


def value(point, form):
    a, b, c = form
    return a * point[0] + b * point[1] - c


def opposite(form):
    return tuple(-coefficient for coefficient in form)


def clip(polygon, form):
    """Clip a closed plotting polygon. Open theorem boundaries are documented separately."""
    if not polygon:
        return []
    result = []
    for start, finish in zip(polygon, polygon[1:] + polygon[:1]):
        left = value(start, form)
        right = value(finish, form)
        if left * right < 0:
            ratio = left / (left - right)
            result.append(tuple(x + ratio * (y - x) for x, y in zip(start, finish)))
        if right <= 0:
            result.append(finish)
    return list(dict.fromkeys(result))


def intersection(polygon, forms):
    for form in forms:
        polygon = clip(polygon, form)
    return polygon


def difference(polygon, forms):
    """Disjoint interiors of the pieces outside the intersection of the forms."""
    pieces = []
    for form in forms:
        pieces.append(clip(polygon, opposite(form)))
        polygon = clip(polygon, form)
    return pieces


def draw(polygons, axes, color):
    for polygon in polygons:
        if len(polygon) >= 3:
            axes.add_patch(Polygon(polygon, closed=True, facecolor=color, edgecolor="none"))


def write_figure(destination):
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.labelsize": 11,
        "svg.hashsalt": STEM,
    })
    fig, ax = plt.subplots(figsize=(8.2, 5.9))
    fig.subplots_adjust(left=0.112, right=0.965, bottom=0.200, top=0.779)
    xmin, xmax, ymin, ymax = DOMAIN
    box = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
    baker = intersection(box, BAKER)
    fs = intersection(box, FOUVRY_SHPARLINSKI)
    overlap = intersection(baker, FOUVRY_SHPARLINSKI)
    groups = [
        (difference(baker, FOUVRY_SHPARLINSKI), "#bad5e6", "#3b84b0"),
        (difference(fs, BAKER), "#f1dcc3", "#dd9a55"),
        ([overlap], "#d6cce8", "#8e76b0"),
    ]
    for polygons, light, strong in groups:
        draw([clip(polygon, ELEMENTARY) for polygon in polygons], ax, light)
        draw([clip(polygon, opposite(ELEMENTARY)) for polygon in polygons], ax, strong)

    ax.set(xlim=(float(xmin), float(xmax)), ylim=(float(ymin), float(ymax)))
    ax.set_xticks([0.50, 0.55, 0.60, 0.65, float(xmax)],
                  labels=["0.50", "0.55", "0.60", "0.65", r"$2/3$"])
    ax.set_yticks([0.25, 0.35, 0.45, 0.55, 0.65, 0.75])
    ax.set_xlabel(r"Modulus exponent $\theta$  ($K\asymp T^\theta$)")
    ax.set_ylabel(r"Prime exponent $\xi$  ($P\asymp T^\xi$)")
    ax.grid(color="#283b4f", linewidth=0.5, alpha=0.12)
    ax.spines[["right", "top"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#65717c")
    ax.tick_params(color="#65717c", labelcolor="#253747")
    ax.plot([xmin, xmax], [1 - xmin, 1 - xmax], color="#233e53",
            dashes=(6, 4), linewidth=1.55, zorder=4)
    ax.axvline(SQUARE_LIMIT, color="#515962", linestyle=":", linewidth=1.4, zorder=5)
    ax.annotate(
        r"$\theta=9/17$  ·  all-square threshold" "\n" r"Square estimate applies to the left",
        xy=(float(SQUARE_LIMIT), 0.643), xytext=(0.537, 0.677),
        ha="left", va="center", color="#37434d",
        arrowprops={"arrowstyle": "-", "color": "#515962", "lw": 0.8},
        bbox={"facecolor": "white", "edgecolor": "none", "pad": 2}, zorder=6,
    )
    ax.text(0.612, 0.544, "Longer primes\nremain open", color="#4e5d69",
            ha="center", va="center", linespacing=1.25)

    fig.text(0.112, 0.951, "Verified regions for the prime remainder",
             fontsize=19, fontweight="bold", color="#162d40")
    fig.text(0.112, 0.903, "Round 14  ·  Power savings for coprime-prime dyadic blocks",
             fontsize=10.5, color="#425867")
    handles = [
        Patch(facecolor="#3b84b0", label="Baker only"),
        Patch(facecolor="#dd9a55", label="Fouvry–Shparlinski only"),
        Patch(facecolor="#8e76b0", label="Overlap"),
        Line2D([], [], color="#233e53", dashes=(6, 4),
               label=r"Elementary limit $\xi=1-\theta$"),
    ]
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.104, 0.864), ncol=4,
               frameon=False, handlelength=2.0, columnspacing=1.15, fontsize=9)
    fig.text(0.112, 0.084, "Stronger fill marks the prime region added above the elementary limit.",
             color="#253747", fontsize=9.3)
    fig.text(0.112, 0.047,
             r"Strict interiors only, with fixed $\kappa<1$ sufficiently close to 1. "
             "No numerical onset is supplied.", color="#4e5d69", fontsize=8.9)
    for extension in ("png", "svg"):
        metadata = {"Description": ALT}
        if extension == "png":
            metadata["Software"] = "Matplotlib"
        else:
            metadata.update({"Date": None, "Title": "Verified regions for the prime remainder"})
        fig.savefig(destination / f"{STEM}.{extension}", dpi=190, facecolor="white",
                    metadata=metadata)
    plt.close(fig)
    return {"Baker": baker, "Fouvry–Shparlinski": fs, "overlap": overlap}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    root = Path(__file__).resolve().parents[2]
    parser.add_argument("--output-dir", type=Path, default=root / "experiments" / "results")
    destination = parser.parse_args().output_dir
    destination.mkdir(parents=True, exist_ok=True)
    polygons = write_figure(destination)
    receipt = {
        "source": "audits/adversarial_reviews/director_arithmetic_strata_round14.md",
        "code": f"experiments/code/{Path(__file__).name}",
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "plot_domain": {"theta": ["1/2", "2/3"], "xi": ["1/4", "3/4"]},
        "strict_prime_regions": {
            "Baker": ["theta/2 < xi < theta", "(11/10)theta + (4/5)xi < 1",
                      "theta + (11/12)xi < 1"],
            "Fouvry–Shparlinski": ["0 < xi < (3/2)theta",
                                   "(13/10)theta + (3/5)xi < 1",
                                   "(13/12)theta + (5/6)xi < 1"],
        },
        "closed_plot_polygon_vertices_exact": {
            name: [[str(x), str(y)] for x, y in vertices]
            for name, vertices in polygons.items()
        },
        "elementary_limiting_short_factor_region": "xi < 1 - theta as kappa tends to 1 from below",
        "stronger_fill_region": "the union of the two prime regions intersected with xi > 1 - theta",
        "separate_square_scope": "all prime squares for 1/2 < theta < 9/17",
        "scope": "Strict interiors, fixed sufficiently close kappa < 1, no numerical onset, longer primes open.",
        "alt_text": ALT,
        "sha256": {
            extension: hashlib.sha256((destination / f"{STEM}.{extension}").read_bytes()).hexdigest()
            for extension in ("png", "svg")
        },
    }
    with (destination / f"{STEM}.json").open("w", encoding="utf-8") as handle:
        json.dump(receipt, handle, indent=2, ensure_ascii=False, sort_keys=True)
        handle.write("\n")


if __name__ == "__main__":
    main()
