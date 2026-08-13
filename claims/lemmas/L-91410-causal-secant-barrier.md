# L-91410 — Causal secant barrier

Status: **PROVED EXACT STRUCTURAL LEMMA**  
Depends on the single-endpoint monotonicity theorem in PR #439. RH remains unproved.

For `2<=j<=66`, set
\[
S(Y)=5\sqrt Y-3,
\qquad
\phi_j(Y)=Q_Y(j)/S(Y),
\]
with `Q_Y(j)=0` before activation. The imported theorem says that `phi_j` is nondecreasing.

Let `p>=67`, `r=p^{-1/2}`, and `z>=1`. Define
\[
q^{in}_{p,j}(z)=
\frac{Q_{pz}(j)-rQ_z(j)}{S(pz)-rS(z)}.
\]
The denominator is positive, and direct substitution gives
\[
\boxed{
q^{in}_{p,j}(z)-\phi_j(pz)=
\frac{rS(z)[\phi_j(pz)-\phi_j(z)]}
{S(pz)-rS(z)}\ge0.
}
\]
Therefore
\[
q^{in}_{p,j}(z)\ge\phi_j(pz)\ge\phi_j(p).
\]

At parent endpoint `x=py`, a source `d>y` has no child term and
\[
q^{out}_{p,j}(d)=\phi_j(py/d)\le\phi_j(p).
\]
Consequently
\[
\boxed{
\inf_{d\le y}q_{p,j}(d)
\ge\phi_j(p)
\ge\sup_{d>y}q_{p,j}(d).
}
\]
The outer ratio is also nonincreasing in `d`.

Thus the continuous child-active counterexample does not cross the child boundary. Since the live score-Lorenz cutoff satisfies `c_L>y`, its residual lies entirely in the ordered outer sector.
