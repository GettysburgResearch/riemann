#!/usr/bin/env python3
"""Render the adjudicated weighted-closure phase diagram."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


OUTPUT = Path(__file__).resolve().parents[1] / "results"
STEM = "witness62_weighted_criterion_phase"
INK = "#172332"
MUTED = "#4b5c6b"
TEAL = "#11615a"
TEAL_FILL = "#d9f0ec"
RUST = "#943e2b"
RUST_FILL = "#f7e4db"


def create_figure():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "mathtext.fontset": "dejavusans",
        "pdf.fonttype": 42,
        "svg.fonttype": "none",
        "svg.hashsalt": STEM,
        "axes.unicode_minus": True,
    })
    fig = plt.figure(figsize=(9.0, 5.25), facecolor="white")
    ax = fig.add_axes((0.095, 0.17, 0.55, 0.64), facecolor="white")

    fig.text(0.095, 0.929, "Weighted closure and its zero-free threshold",
             color=INK, fontsize=20, fontweight="bold")
    fig.text(0.095, 0.862,
             r"$b=(1-\alpha)/2-a$  ·  domain $-3\leq\alpha\leq-2,\quad 1\leq a<(1-\alpha)/2$",
             color=MUTED, fontsize=11.4)

    alpha = np.linspace(-3, -2, 200)
    critical = -alpha / 2
    upper = (1 - alpha) / 2
    ax.fill_between(alpha, 1, critical, color=TEAL_FILL, zorder=1)
    ax.fill_between(alpha, critical, upper, color=RUST_FILL, zorder=1)
    ax.plot(alpha, critical, color=INK, linewidth=1.8, zorder=4)
    ax.plot(alpha, upper, color=MUTED, linewidth=1.5, linestyle=(0, (5, 3)), zorder=3)
    ax.plot([-3, -3, -2, -2], [2, 1, 1, 1.5],
            color=MUTED, linewidth=1.15, zorder=3)
    ax.scatter([-3, -2], [2, 1.5], marker="o", s=30, facecolor="white",
               edgecolor=MUTED, linewidth=1.2, zorder=5)

    ax.text(-2.42, 1.47, r"$0<b<\frac{1}{2}$", color=RUST,
            fontweight="bold", ha="center", va="center", fontsize=12)
    ax.text(-2.73, 1.14, r"$b>\frac{1}{2}$", color=TEAL,
            fontweight="bold", ha="center", va="center", fontsize=12)
    ax.text(-2.39, 1.765, r"$a=(1-\alpha)/2$",
            color=MUTED, rotation=-23, ha="center", va="bottom", fontsize=10)

    ax.scatter([-3], [1.75], marker="D", s=53, facecolor=RUST,
               edgecolor="white", linewidth=0.9, zorder=6)
    ax.scatter([-3], [1], marker="o", s=60, facecolor=TEAL,
               edgecolor="white", linewidth=0.9, zorder=6)
    ax.annotate(r"$(-3,\,7/4)$", xy=(-3, 1.75), xytext=(-2.94, 1.82),
                color=RUST, fontsize=10, ha="left", va="bottom",
                arrowprops={"arrowstyle": "-", "color": RUST, "lw": 0.9})
    ax.annotate(r"$(-3,\,1)$", xy=(-3, 1), xytext=(-2.93, 0.971),
                color=TEAL, fontsize=10, ha="left", va="top",
                arrowprops={"arrowstyle": "-", "color": TEAL, "lw": 0.9})

    ax.set(xlim=(-3.065, -1.965), ylim=(0.92, 2.055),
           xlabel=r"$\alpha$", ylabel=r"$a$")
    ax.xaxis.set_major_locator(MultipleLocator(0.25))
    ax.set_yticks([1, 1.25, 1.5, 1.75, 2])
    ax.tick_params(colors=MUTED, labelsize=9, width=0.7, length=3, pad=4)
    ax.xaxis.label.set_color(INK)
    ax.yaxis.label.set_color(INK)
    ax.spines[["top", "right"]].set_visible(False)
    for spine in ("bottom", "left"):
        ax.spines[spine].set_color("#a1adb5")
        ax.spines[spine].set_linewidth(0.8)

    panel_x = 0.699
    fig.text(panel_x, 0.776, "Above the line", color=RUST,
             fontsize=11.2, fontweight="bold")
    fig.text(panel_x, 0.674, "Closure is impossible.\nDiamond marks the counterexample\nto the printed reverse implication.",
             color=INK, fontsize=9.9, linespacing=1.42)
    fig.text(panel_x, 0.583, r"On the line $a=-\alpha/2$", color=INK,
             fontsize=11.2, fontweight="bold")
    fig.text(panel_x, 0.524, r"$b=1/2$. Closure is equivalent to RH.",
             color=INK, fontsize=9.9)
    fig.text(panel_x, 0.440, "Below the line", color=TEAL,
             fontsize=11.2, fontweight="bold")
    fig.text(panel_x, 0.307,
             r"Closure is equivalent to" "\n"
             r"zero-freeness in $\operatorname{Re}s>b$." "\n"
             "That condition is weaker than RH." "\n"
             "Circle marks unconditional closure.",
             color=INK, fontsize=9.9, linespacing=1.42)
    fig.text(panel_x, 0.215, "Dashed upper edge is excluded.",
             color=MUTED, fontsize=9.65)
    return fig


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    fig = create_figure()
    fig.savefig(OUTPUT / f"{STEM}.pdf",
                metadata={"Title": "Weighted closure phase diagram",
                          "CreationDate": None, "ModDate": None})
    fig.savefig(OUTPUT / f"{STEM}.svg",
                metadata={"Title": "Weighted closure phase diagram", "Date": None})
    fig.savefig(OUTPUT / f"{STEM}.png", dpi=225,
                metadata={"Title": "Weighted closure phase diagram"})
    plt.close(fig)


if __name__ == "__main__":
    main()
