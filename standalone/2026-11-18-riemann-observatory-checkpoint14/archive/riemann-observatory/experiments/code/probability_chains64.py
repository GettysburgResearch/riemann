"""Render the two zeta-zero probability constructions for checkpoint 8."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


OUTPUT = Path(__file__).resolve().parents[1] / "results"
INK = "#182939"
SECONDARY = "#405569"
PANEL_STYLES = (
    ("#24577b", "#eef5fa", "#9cbad1"),
    ("#245f50", "#edf6f1", "#91b9aa"),
)
plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "mathtext.fontset": "dejavusans",
        "pdf.fonttype": 42,
        "svg.fonttype": "path",
        "svg.hashsalt": "probability-chains64",
    }
)


def add_text(ax, x, y, s, size, color=INK, **kwargs):
    return ax.text(
        x, y, s, fontsize=size, color=color, va="center", **kwargs
    )


def draw_box(ax, center, bottom, height, title, lines, style):
    accent, background, outline = style
    width = 6.0
    left = center - width / 2
    ax.add_patch(
        FancyBboxPatch(
            (left, bottom), width, height, boxstyle="round,pad=0.02,rounding_size=0.13",
            facecolor=background, edgecolor=outline, linewidth=1.0, zorder=1,
        )
    )
    add_text(ax, left + 0.23, bottom + height - 0.25, title, 12, accent, weight="bold")
    for row, line in enumerate(lines):
        add_text(ax, left + 0.23, bottom + height - 0.62 - 0.33 * row, line, 11)


def arrow(ax, center, start, end, label, accent):
    ax.add_patch(
        FancyArrowPatch(
            (center, start), (center, end), arrowstyle="-|>",
            mutation_scale=13, linewidth=1.3, color=accent,
            shrinkA=0, shrinkB=0,
        )
    )
    add_text(ax, center + 0.16, (start + end) / 2, label, 9, accent)


def main():
    fig = plt.figure(figsize=(13.5, 10.0), facecolor="white")
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set(xlim=(0, 13.5), ylim=(0, 10))
    ax.set_axis_off()

    add_text(ax, 0.43, 9.60, "Two probability laws from zeta zeros", 25, weight="bold")
    add_text(
        ax, 0.45, 9.12,
        "Multiplicity-weighted jumps on the real line and derivative-weighted phases on the prime torus",
        12, SECONDARY,
    )

    left = 3.45
    right = 10.05
    blue, green = PANEL_STYLES
    add_text(ax, 0.45, 8.55, "A  Real-line jump law", 15, blue[0], weight="bold")
    add_text(ax, 7.05, 8.55, "B  Prime-phase law", 15, green[0], weight="bold")

    draw_box(ax, left, 6.95, 1.30, "Arithmetic criterion", [
        r"Exact arithmetic exponent $g_\zeta$",
        r"$\mathrm{RH}\ \Longleftrightarrow\ e^{g_\zeta}$ is an infinitely divisible characteristic function",
    ], blue)
    draw_box(ax, left, 5.25, 1.16, "Finite Lévy measure on the additive real line", [
        r"$\nu_{\rm mult}=\sum_{\gamma\ {\rm distinct}}(m_\gamma/\gamma^2)\,\delta_{-\gamma}$",
        r"Both signs, with zero multiplicity $m_\gamma$.",
    ], blue)
    draw_box(ax, left, 3.60, 1.16, r"Compound Poisson law $\mu$", [
        r"$X=\sum_{j=1}^{N}J_j$,  $N\sim{\rm Pois}(S)$,  $S=\nu_{\rm mult}(\mathbb{R})$",
        r"Independent jumps with law $\nu_{\rm mult}/S$, independent of $N$.",
    ], blue)
    draw_box(ax, left, 0.80, 2.27, "Tail, scaling and atoms", [
        r"$\Pr(|X|>Y)=\frac{\log(Y/(2\pi))+1}{\pi Y}+O\!\left(\frac{\log^3Y}{Y^2}\right)$",
        r"$\frac{X_1+\cdots+X_n}{n\log n/2}\ \Rightarrow\ {\rm Cauchy}(0,1)$ for iid copies",
        r"Countably many dense atoms, with $\Pr(X=0)\approx95.49\%$.",
    ], blue)
    arrow(ax, left, 6.90, 6.48, "Assume RH", blue[0])
    arrow(ax, left, 5.19, 4.82, "Poisson compounding", blue[0])
    arrow(ax, left, 3.54, 3.13, "Zero counting and the cusp at zero", blue[0])

    draw_box(ax, right, 6.95, 1.30, "Derivative weights on signed ordinates", [
        r"$\nu_{\rm deriv}=\sum_{\rho}|\zeta'(\rho)|^2\,|\rho|^{-2}\,\delta_\gamma$",
        r"Under RH, $\rho=1/2+i\gamma$. Multiple zeros have zero mass.",
    ], green)
    draw_box(ax, right, 5.25, 1.16, "One draw from the high tail", [
        r"Normalize $\nu_{\rm deriv}$ on $|\gamma|>Y$.",
        r"Send $\gamma$ to $(e^{-i\gamma\log p})_p$ on the prime torus.",
    ], green)
    draw_box(ax, right, 3.60, 1.16, "Poisson-circle product model", [
        r"Independent circle coordinates of radii $r_p=p^{-1/2}$.",
        r"At $m/n$ the Fourier coefficient is $\gcd(m,n)/\sqrt{mn}$.",
    ], green)
    draw_box(ax, right, 0.80, 2.27, "Gaussian limit for the arithmetic draw", [
        r"$P=(\log Y)^D$ for fixed $D>0$,  $W_P=\sum_{p\leq P}p^{-1/2}\cos(\gamma\log p)$",
        r"$H_P=\sum_{p\leq P}p^{-1}$,  $V_P=\frac{1}{2}\sum_{p\leq P}(p^{-1}-p^{-2})$",
        r"$(W_P-H_P)/\sqrt{V_P}\ \Rightarrow\ \mathcal{N}(0,1)$ as $Y\to\infty$",
        "Every fixed normalized moment converges.",
    ], green)
    arrow(ax, right, 6.90, 6.48, "Restrict and normalize", green[0])
    arrow(ax, right, 5.19, 4.82, "Weak limit by HLZ character estimates", green[0])
    arrow(ax, right, 3.54, 3.13, "Uniform HLZ bounds match fixed moments", green[0])

    add_text(
        ax, 0.45, 0.40,
        "Both limit theorems assume RH. The prime-phase limit uses uniform rational-character estimates.",
        10, SECONDARY,
    )
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf", "svg"):
        metadata = {"Creator": "probability_chains64.py"}
        if ext == "pdf":
            metadata["CreationDate"] = None
        if ext == "svg":
            metadata["Date"] = None
        fig.savefig(OUTPUT / f"probability_chains64.{ext}", dpi=200, metadata=metadata)
    plt.close(fig)


if __name__ == "__main__":
    main()
