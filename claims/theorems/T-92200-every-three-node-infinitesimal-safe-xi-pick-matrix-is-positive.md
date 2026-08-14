# T-92200 — Every three-node infinitesimal safe Xi Pick matrix is positive

Claim ID: `T-92200`  
Status: **PROPOSED UNCONDITIONAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-14  
Depends on: `L-91904/L-91905`; `L-92000/L-92001`; `L-92200/L-92201`  
RH status: **unproved**

## Statement

Put

\[
 \Xi(z)=\xi\!\left(\frac12+z\right),
 \qquad
 F(x)=\frac{\Xi'(x)}{\Xi(x)}
 \qquad(x>1/2).
\]

For distinct safe real nodes `x_1,...,x_N`, define

\[
 \mathscr H[\mathbf x]_{ij}
 =\frac{F(x_i)+F(x_j)}{x_i+x_j}.
\]

Then, subject to independent review of the declared dependencies,

\[
 \boxed{
 \mathscr H[\mathbf x]\succ0
 \qquad(1\le N\le3).
 }
\]

No Riemann-hypothesis assumption is used.

## Proof

Put

\[
 t_i=x_i^2,
 \qquad
 p(t)=\frac{F(\sqrt t)}{\sqrt t},
 \qquad
 Z(t)=\frac1{p(t)},
 \qquad
 Z^*(t)=t p(t).
\]

### One and two nodes

`L-91905` proves unconditionally that

\[
 p(t)>0,
 \qquad
 p'(t)<0,
 \qquad
 (tp(t))'>0.
\]

Its exact two-node determinant formula gives strict positivity of every
one- and two-node principal minor.

### Three nodes

`L-92000` proves the exact factorization

\[
\boxed{
 \det\mathscr H
 =\frac{
 p_1p_2p_3\,\Delta(t)^2
 }{
 \prod_{i<j}(x_i+x_j)^2
 }
 [t_1,t_2,t_3]Z
 [t_1,t_2,t_3]Z^*.
 }
\]

`L-92001` proves

\[
 (Z^*)''(t)=(tp(t))''<0
 \qquad(t>1/4).
\]

`L-92200/L-92201` prove

\[
 p p''-2(p')^2>0,
\]

hence

\[
 Z''(t)=\frac{2(p')^2-pp''}{p^3}<0.
\]

Both second divided differences in the determinant are therefore strictly
negative.  Every remaining prefactor is strictly positive, so

\[
 \det\mathscr H>0.
\]

Together with the one- and two-node principal minors, Sylvester's criterion
gives `H>0` for every three-node packet.

## Significance

The infinitesimal safe-real RH criterion of `L-91904` is an all-order
Carathéodory hierarchy.  The preceding stack established:

```text
order one: scalar positivity;
order two: two conjugate monotonicities;
order three: two conjugate concavities.
```

The present theorem closes the first interpolation order at which a generic
high off-line orbit can fail.  The closure is source specific: it uses the
huge rigorously verified critical-line reserve below height `3e12` and an
explicit local zero-count bound to dominate every possible off-line local
curvature interaction.

The theorem does **not** prove RH.  A false-RH witness may first appear at
four or more safe nodes.  In the complete-Bernstein language of PR #449, the
remaining problem is higher Loewner positivity, not ordinary concavity.

## Review boundary

The conclusion is only as strong as the proposed dependencies.  Review in
this order:

1. `L-92200` squared-pole product and pairwise curvature identity;
2. the external verified-height/local-count source lock;
3. `L-92201` angle localization and row domination;
4. `L-92001` companion curvature;
5. `L-92000` determinant factorization;
6. this assembly.

## Exact boundary

```text
one-node safe Xi positivity                 PROPOSED UNCONDITIONAL
all two-node safe Xi matrices               PROPOSED UNCONDITIONAL
all three-node safe Xi matrices             PROPOSED UNCONDITIONAL
four-node and higher Loewner/Pick levels     OPEN / RH-BEARING
complete-Bernstein Xi impedance             OPEN / RH-EQUIVALENT
Riemann Hypothesis                          UNPROVED
```
