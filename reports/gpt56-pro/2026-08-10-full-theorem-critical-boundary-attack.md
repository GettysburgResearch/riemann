# Full-theorem attack: the critical boundary collapses to CN3

Date: 2026-08-10  
Branch: `research/gpt56-pro/90102-liouville-bernstein-extremality`  
PR: #356  
Status: exact theorem packet and replay; RH unproved

## 1. Mission

The preceding pass reduced the live positive-Pascal route to two apparent
last steps:

1. prove the extremal `15:4` low-row scalar after one Möbius inversion;
2. or pay the explicit factor-64 reward debt on states `13..63`.

This pass attacked the first boundary without replacing it by a size estimate.

## 2. The all-scale renewal needed a boundary repair

`L-90215` correctly identified a positive forcing for `x>=4`, but its displayed
Möbius inversion sampled `x/d<4`.  The omitted finite collar changes the
recovered scalar.

The corrected all-scale forcing is

\[
 \widetilde\Phi(x)=
 \begin{cases}
 0,&1\le x<2,\\
 6J(x)-6+9/\sqrt2-3/\sqrt x,&2\le x<4,\\
 6J(x)-15/2+9/\sqrt2,&x\ge4,
 \end{cases}
\]

with

\[
 J(x)=\sum_{d\le x}d^{-1/2}
      -\lfloor x\rfloor/\sqrt x.
\]

It is nonnegative everywhere, and the exact inversion is

\[
 \mathcal H(x)
 =\sum_{d\le x}\mu(d)d^{-1/2}
  \widetilde\Phi(x/d).
\]

The positive-forcing normal form survives, now without a domain mismatch.  The
last sign loss is genuinely the Möbius boundary inversion.

## 3. Positive Pascal geometry cannot cancel the critical mode

For an arbitrary nonnegative uniform-Pascal reward `d`, normalized by

\[
 1=\sum_{j\ge2}\frac2{j+1}d(j),
\]

its deterministic transfer has the form

\[
 \mathcal A_d(s)=\zeta(s)-Q_d(s),
 \qquad
 Q_d(s)=\sum_{j\ge2}d(j)B_j(s).
\]

At the square-root exponent,

\[
 B_j(1/2)
 =\frac2{j+1}\sum_{n\le j+1}n^{-1/2}
  -\sqrt j+\frac{j-2}{\sqrt{j+1}}.
\]

`L-90220` proves

\[
 B_j(1/2)>0\qquad(j\ge2).
\]

Therefore

\[
 Q_d(1/2)>0
\]

for every nonzero positive reward, even with infinitely many boundary states.

This globalizes the earlier dyadic annular no-go:

```text
positive uniform-Pascal reward
and
exact square-root critical cancellation
are incompatible.
```

A full theorem must use signed reward, multiple channels, another policy, or a
nonlocal state.

## 4. The unique minimax signed adapter

Among finite dyadic filters satisfying

\[
 Q(1)=Q(1/\sqrt2)=0,
\]

write the Pascal block numerators as

\[
 A_j=2\sum_{\ell<j}2^\ell S_\ell.
\]

With `lambda=1/(2sqrt(2))`, `L-90221` proves the exact identity

\[
 \sum_{k=2}^{J-1}
 (1-\lambda)\lambda^{k-1}A_k
 +\lambda^{J-1}A_J
 =-2(1-\lambda).
\]

The weighted average block debt is therefore exactly

\[
 2-4\sqrt2.
\]

Hence

\[
 \min_j A_j\le2-4\sqrt2,
\]

and equality uniquely selects

\[
 \boxed{
 Q_\star(t)=(1-t)(1-\sqrt2\,t).
 }
\]

Its complete uniform-Pascal reward is

\[
 d_\star(2)=\frac{2+\sqrt2}{2},
 \qquad
 d_\star(3)=\frac13,
 \qquad
 d_\star(m)=\frac{2-4\sqrt2}{m(m-1)}
 \quad(m\ge4).
\]

Thus the least-negative possible critical adapter has only two positive low
rows and one reciprocal-square negative tail.

## 5. The infinite tail sums exactly

The reciprocal-square reward

\[
 e(m)=\frac1{m(m-1)}
\]

has constant Pascal potential `1/2` above state one.  For any
size-conserving source and its uniform-Pascal occupation,

\[
 \sum_{m\ge2}\frac{M_m}{m(m-1)}
 =-\frac{s_1}{2}.
\]

Consequently the complete `Q_star` pairing is

\[
 \mathcal K_\star
 =\frac{\sqrt2}{6}(15M_2+4M_3)
 +(2\sqrt2-1)s_1
\]

and hence

\[
 \boxed{
 \mathcal K_\star
 =-s_1+\frac{\sqrt2}{2}s_2+\frac{\sqrt2}{3}s_3.
 }
\]

The entire infinite reward has collapsed to the single inequality

\[
 \boxed{
 3s_2+2s_3\ge3\sqrt2\,s_1.
 }
\]

Equivalently,

\[
 2[U(2)-U(4)]
 \ge\sqrt2[U(1)-U(2)].
\]

This is `CN3`.

## 6. Positive renewal for the minimax scalar

Let

\[
 b_\star
 =(\varepsilon-\delta_2)
  *(\varepsilon-\sqrt2\delta_2)*\mu
\]

and

\[
 \mathcal K_\star(x)
 =-\sum_{2\le q\le x}b_\star(q)
  (q^{-1/2}-x^{-1/2}).
\]

Then

\[
 \mathcal P\mathcal K_\star=\Psi_\star,
\]

where

\[
 \Psi_\star(x)=
 \begin{cases}
 0,&1\le x<2,\\
 J(x)+1/\sqrt2-\sqrt{2/x},&2\le x<4,\\
 J(x),&x\ge4.
 \end{cases}
\]

Every line is nonnegative.  Thus both live scalar frontiers now have complete
positive deterministic forcing:

```text
canonical 15:4 scalar    -> positive forcing widetilde Phi;
minimax CN3 scalar       -> positive forcing Psi_star.
```

The unresolved operation in both is exactly weighted Möbius inversion.

## 7. CN3 is already a full RH criterion

The Mellin transform is

\[
 \widehat{\mathcal K_\star}(s)
 =
 \frac{
  1-Q_\star(2^{-s-1/2})/\zeta(s+1/2)
 }{
  2s(s+1/2)
 }.
\]

A hypothetical zeta zero `rho` with `Re rho>1/2` produces a genuine nonreal
pole at `s=rho-1/2`; the two local roots of `Q_star` cannot cancel it.  There
is no positive-real singularity.

Landau therefore gives

\[
 \mathrm{CN3}\Longrightarrow\mathrm{RH}.
\]

The criterion is much smaller than SHARP, OBH, or the factor-64 payment, but it
is not softer: the pole audit proves that the remaining inequality is itself
RH-bearing.

## 8. Verification

`X-90208-critical-boundary-attack` replays:

- the corrected canonical renewal on the full boundary collar;
- the `Q_star` renewal;
- critical-defect positivity through boundary state 10,000;
- 100 exact critical-neutral filter debt identities over `Q(sqrt(2))`;
- 255 exact `Q_star` reward rows;
- 30 exact random-source tail-sweep identities.

The retained verdict is

```text
PASS_X_90208_CRITICAL_BOUNDARY_ATTACK
```

The analytic proofs are in the claim files; the replay is a mutation bank.

## 9. Honest theorem boundary

```text
all-scale positive forcing repair                  CLOSED
positive reward critical cancellation              IMPOSSIBLE
critical-neutral dyadic minimax debt                CLOSED
unique minimax adapter Q_star                       CLOSED
infinite reciprocal-square tail                    SUMMED EXACTLY
CN3 -> RH                                           COMPLETE CONDITIONAL
CN3                                                 OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVEN
```

The full-theorem attack did not reveal another intermediate estimate.  It
removed the last infinite-dimensional Pascal object and exposed one arithmetic
inequality among the first three source coordinates.  Proving that inequality
would prove RH.
