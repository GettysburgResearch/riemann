#!/usr/bin/env python3
"""Plot joint limits of the finite Legendre prefix cost."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import iv


OUTPUT = Path(__file__).resolve().parents[1] / "results"
STEM = "witness62_prefix_transition"
INK = "#172332"
MUTED = "#4b5c6b"
COLORS = ["#8b3f64", "#a65228", "#275d89", "#137268"]


def scaled_cost(m, r):
    """Compute c_m(b)/m² from the exact integral of a positive polynomial."""
    if r == 0:
        return 1.0
    term = 1.0
    derivative_coefficients = np.empty(m - 1)
    for k in range(1, m):
        term *= ((m - k) / m) * ((m + k - 1) / m) * (r / (k * k))
        derivative_coefficients[k - 1] = k * term / r
    squared_coefficients = np.convolve(derivative_coefficients, derivative_coefficients)
    powers_plus_one = np.arange(1, squared_coefficients.size + 1)
    return 1.0 + r * np.sum(squared_coefficients / powers_plus_one)


def bessel_cost(r):
    z = 2.0 * np.sqrt(r)
    i0 = iv(0, z)
    i1 = iv(1, z)
    return (i0 - i1) * (i0 + i1)


def render():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "mathtext.fontset": "dejavusans",
        "font.size": 10,
        "axes.labelcolor": INK,
        "axes.edgecolor": "#94a2af",
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "pdf.fonttype": 42,
        "svg.fonttype": "none",
        "svg.hashsalt": STEM,
    })
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.2, 4.75), facecolor="white")
    fig.subplots_adjust(left=0.084, right=0.96, bottom=0.16, top=0.76, wspace=0.32)
    fig.text(0.084, 0.923, "Joint limits of the finite Legendre prefix cost",
             fontsize=19, fontweight="bold", color=INK)
    fig.text(0.084, 0.853,
             r"$r=m^2b/(1-b)$  ·  $F(r)=I_0(2\sqrt{r})^2-I_1(2\sqrt{r})^2$",
             fontsize=11.5, color=MUTED)

    r = np.linspace(0, 10, 251)
    left.plot(r, bessel_cost(r), color=INK, linestyle=(0, (5, 2.5)), linewidth=2,
              label=r"$F(r)$", zorder=5)
    for color, m in zip(COLORS, (4, 8, 16, 32)):
        cost = np.array([scaled_cost(m, value) for value in r])
        left.plot(r, cost, color=color, label=rf"$m={m}$", linewidth=1.6)
    left.set(xlim=(0, 10), ylim=(0.93, 1650), yscale="log", xlabel=r"$r$",
             ylabel=r"$c_m(b)/m^2$")
    left.set_title("Bounded crossover", loc="left", color=INK, fontweight="bold", pad=10)
    left.legend(loc="upper left", frameon=False, ncol=2, fontsize=9)

    scale = np.linspace(0.05, 2, 220)
    right.plot(scale, np.exp(-(2.0 / 3.0) * scale**1.5), color=INK,
               linestyle=(0, (5, 2.5)), linewidth=2, label=r"$e^{-2\lambda^{3/2}/3}$", zorder=5)
    for color, m in zip((COLORS[3], COLORS[2], COLORS[0]), (32, 128, 512)):
        r_curve = scale * m**(4.0 / 3.0)
        ratio = np.array([scaled_cost(m, value) for value in r_curve]) / bessel_cost(r_curve)
        right.plot(scale, ratio, color=color, label=rf"$m={m}$", linewidth=1.6)
    right.set(xlim=(0.05, 2), ylim=(0, 1.02), xlabel=r"$\lambda$",
              ylabel=r"$[c_m(b)/m^2]/F(r)$")
    right.set_title(r"At $r=\lambda m^{4/3}$", loc="left", color=INK,
                    fontweight="bold", pad=10)
    right.legend(loc="upper right", frameon=False, fontsize=9)

    for ax in (left, right):
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_axisbelow(True)
        ax.grid(axis="y", color="#dce2e6", linewidth=0.65)
        ax.tick_params(width=0.65, length=3)
    return fig


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    fig = render()
    fig.savefig(OUTPUT / f"{STEM}.pdf", metadata={"CreationDate": None, "ModDate": None})
    fig.savefig(OUTPUT / f"{STEM}.svg", metadata={"Date": None})
    fig.savefig(OUTPUT / f"{STEM}.png", dpi=225)
    plt.close(fig)


if __name__ == "__main__":
    main()
