# R-99611 — Critical SHARP homogeneity is the exact owner-Carleson wall

Claim ID: `R-99611`  
Status: **PROVED PHASE-TRANSITION / METHOD FIREWALL**  
Created: 2026-08-20  
Depends on: `L-99613`; PR #653 scalar consumer  
RH status: **not assumed**

The all-scale theorem `L-99613` is already valid at the quadratic boundary
power. Its labelled one-prime removal gains

\[
q^{-3/2},
\]

and the total labelled prime mass is strictly below one. This makes every odd
Euler level smaller than its preceding even level and forces global positivity.

For a general boundary power `m`, the owner ratio gains

\[
q^{-(m+1)/2}.
\tag{R-99611.1}
\]

At the RH-sensitive linear power `m=1`, (R-99611.1) is exactly `1/q`, and

\[
\sum_q{1\over q}=\infty.
\]

No improvement of a fixed numerical constant repairs this divergence.

One might normalize a supercritical power back to square-root growth:

\[
\widetilde K_m(y)=y^{-(m-1)/2}T(y)^m
=\sqrt y\left(4-{3\over\sqrt y}\right)^m.
\]

But the normalizing power cancels the additional owner decay exactly, returning
again to the critical `1/q` scale. Thus supercritical source contraction cannot
be imported into the conclusion-producing normalization for free.

The Mellin symbols give the same firewall. For the quadratic kernel,

\[
\int_1^\infty T(y)^2y^{-s-1}dy
={16\over s-1}-{24\over s-1/2}+{9\over s}.
\]

The local reciprocal-zeta zero cancels the `s=1/2` pole, but the positive-real
pole at `s=1` remains. For the cubic kernel, positive-real poles remain at
`s=1` and `s=3/2`. Landau sees those real growth singularities before it can
exclude off-line zeta poles.

Hence:

```text
every SHARP power `m>=2`        unconditional global source positivity;
linear SHARP power              reciprocal-zeta sensitivity;
critical renormalization        exact return to prime-harmonic congestion.
```

The open `SOCE99610` embedding is therefore the exact critical theorem rather
than an artifact of a poor norm or insufficient filtering.
