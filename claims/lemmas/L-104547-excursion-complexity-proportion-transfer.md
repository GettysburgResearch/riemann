# L-104547 — Excursion complexity transfers the Xi''' line proportion

Claim ID: `L-104547`  
Status: **PROVED EXACT CONDITIONAL PROPORTION TRANSFER**  
Created: 2026-08-24  
Depends on: `L-104545`, `L-104527`  
RH status: **not assumed**

Let `f=Xi''` and consider a regular fixed-order counting window. Let

```text
R = total number of simple real zeros of Xi''' in the window;
G = number of Rolle-generating such critical points;
W = number of wrong such critical points.
```

Thus `R=G+W`.

For a regular amplitude threshold `y>0`, put

\[
R_y=G_y+W_y,
\qquad
C_y=G_y-W_y=\frac12N_y.
\tag{L-104547.1}
\]

Define

\[
\delta_y=\frac{R_y}{R},
\qquad
\kappa_y=\frac{C_y}{R_y}
\quad(R_y>0).
\tag{L-104547.2}
\]

Here `delta_y` is the fraction of derivative-line critical points retained
above the threshold, while `kappa_y` is the normalized component complexity of
their excursion set.

Since `G>=G_y=(R_y+C_y)/2`,

\[
\boxed{
\frac{G-W}{R}
\ge
\delta_y(1+\kappa_y)-1.
}
\tag{L-104547.3}
\]

This inequality uses only:

```text
the Xi''' critical-point count R;
the unsigned superlevel critical count R_y;
the unsigned level-crossing count N_y.
```

It does not use or count real zeros of `Xi''`.

## Fixed-order proportion form

Let `alpha_3` be Conrey's line-zero proportion for `xi'''`. Suppose there is a
regular threshold scheme `y=y(T)` and `eta>0` such that

\[
\boxed{
\liminf_{T\to\infty}
\left[
\delta_{y(T)}(1+\kappa_{y(T)})-1
\right]
\ge\eta.
}
\tag{L-104547.4}
\]

Then the exact fixed-order orientation bridge gives

\[
\boxed{
\alpha_2\ge\eta\alpha_3.
}
\tag{L-104547.5}
\]

Using the imported unconditional value `alpha_3>0.9873`,

\[
\boxed{
\alpha_2>0.9873\,\eta.
}
\tag{L-104547.6}
\]

This is a genuine use of the third-derivative theorem. The independent Conrey
bound for `alpha_2` is not used.

The conclusion-facing gate is:

```text
EXCUR104600 — excursion retention and complexity

Find y(T) and eta>0 such that
  delta_y(T) * (1+kappa_y(T)) >= 1+eta+o(1).
```

Unlike a Laguerre-sign theorem, `EXCUR104600` asks only for two unsigned
statistics of the actual Xi'' excursion geometry.
