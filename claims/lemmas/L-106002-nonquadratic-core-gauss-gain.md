# L-106002 — Nonquadratic characters retain the square core and exhibit an exact Gauss gain

Claim ID: `L-106002`  
Programme aliases: `LFAM1.NONQUADRATIC_CORE_VISIBILITY`, `LFAM2.GAUSS_MODEL`  
Status: **PROVED EXACT FINITE-FIELD MECHANISM**  
Created: 2026-08-24  
Depends on: `L-106001`; PR #719 `R-102867`  
RH status: **not assumed**

PR #719 proves that the naive product of four quadratic symbols collapses by
quadratic reciprocity. That firewall is correct, but it is specific to
quadratic characters. General characters see the square core.

## 1. Exact square-core factor

Let `k` be a finite field of odd cardinality `Q`, let `chi` be a
multiplicative character of `k^*`, and let `P,c` be nonzero. Then

\[
\boxed{
\chi(Pc^2)=\chi(P)\chi^2(c).
}
\tag{L-106002.1}
\]

If `chi` is quadratic, `chi^2=1`, so the core `c` disappears. This is the
mechanism behind the quadratic-character collapse.

If `chi^2` is nontrivial, the square core remains as a genuine
multiplicative phase.

Because `k^*` is cyclic of even order, exactly two characters satisfy

\[
\chi^2=1:
\]

the principal and quadratic characters. Every other character retains core
oscillation.

## 2. Exact Gauss norm

Let `psi` be a nontrivial additive character of `k`, let `a` be nonzero, and
put

\[
G(\eta,\psi_a)
=
\sum_{c\in k^*}\eta(c)\psi(ac).
\tag{L-106002.2}
\]

If `eta` is nontrivial, then

\[
\boxed{|G(\eta,\psi_a)|^2=Q.}
\tag{L-106002.3}
\]

If `eta=1`, then

\[
G(1,\psi_a)=-1.
\tag{L-106002.4}
\]

### Proof

Expand and set `t=x/y`:

\[
\begin{aligned}
|G|^2
&=
\sum_{x,y\in k^*}
\eta(x/y)\psi(a(x-y))\\
&=
\sum_{t\in k^*}\eta(t)
\sum_{y\in k^*}\psi(ay(t-1)).
\end{aligned}
\]

The inner sum is `Q-1` for `t=1` and `-1` otherwise. If `eta` is nontrivial,
its complete sum is zero, giving `Q`. The trivial case is the ordinary
nonzero additive-character sum.

Applying this with `eta=chi^2` gives

\[
\boxed{
\left|
\sum_{c\in k^*}\chi(Pc^2)\psi(ac)
\right|
=
\sqrt Q
}
\tag{L-106002.5}
\]

for every character except the principal and quadratic channels. The factor
`chi(P)` has unit modulus and does not affect the gain.

Thus all but two channels in the full multiplicative-character family possess
an exact square-root core cancellation in the constant-coefficient model.

## 3. Exact collision-line cancellation

Let `tau,alpha,beta` lie in `k`, with `tau` nonzero. On one of the two
collision lines from `L-106001`, put

\[
c=\pm\tau d.
\]

Then

\[
\sum_{d\in k^*}\psi(\alpha c+\beta d)
=
\sum_{d\in k^*}
\psi((\pm\alpha\tau+\beta)d).
\]

Therefore

\[
\boxed{
\sum_{d\in k^*}\psi((\pm\alpha\tau+\beta)d)
=
\begin{cases}
Q-1,&\pm\alpha\tau+\beta=0,\\
-1,&\pm\alpha\tau+\beta\ne0.
\end{cases}
}
\tag{L-106002.6}
\]

A complete nonresonant line has size `O(1)`, not `O(Q)`. The only large line
is an explicitly classifiable phase resonance.

This is the finite-field prototype of the desired CV/XD family moment:

```text
general multiplicative character
+ inherited nonzero owner/core phase
+ squareclass collision line
-> square-root or complete-line cancellation,
except on explicit resonant strata.
```

## 4. Meaning for the number-field packet

The actual stopped-Vaughan coefficients are not constant and the ranges are
incomplete. Consequently (L-106002.3)--(L-106002.6) do not prove the
number-field collision-line estimate.

They do identify the structure that a useful moment theorem must retain:

- use the full character family, not only quadratic characters;
- keep `chi^2(c)` attached to the core;
- retain the existing nonzero additive phases;
- classify resonant lines before taking absolute values;
- estimate incomplete weighted trace sums on the remaining lines.

This is the handoff to the function-field mirror `L-106003` and the open
hybrid moment in `T-106000`.
