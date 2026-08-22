# All-out continuation: global Pascal reward extremality and the annular filter-cone frontier

Date: 2026-08-10  
Branch: `research/gpt56-pro/90102-liouville-bernstein-extremality`  
PR: #356  
Status: exact theorem packet plus finite replay; RH unproved

## 1. Starting point

The preceding pass had already established:

```text
frozen binary–ternary GFEP / producer positivity    REFUTED
uniform internal Pascal kernel                      RESONANCE-FREE
canonical two-low-row source                        ZERO-SAFE / RH-BEARING
ordered quarter-balanced policy                     STRICT CONTINUUM GAP
```

The live question was whether the resonance-free Pascal geometry could be strengthened by a better finite boundary reward or combined directly with the improved factor-64 annular filter.

This pass answers both structural questions exactly.

## 2. The `15:4` reward is globally extremal

For uniform Pascal,

\[
 P_m(k)=\frac{2k}{m(m-1)}.
\]

Any eventually constant potential with nonnegative reward `d=f-Pf` and the no-3-channel normalization has forced rewards

\[
 d(2)=r/2,
 \qquad d(3)=1/3.
\]

The exact hitting law `Pr_m(hit j)=2/(j+1)` gives the reward budget

\[
 1=\sum_{j\ge2}\frac2{j+1}d(j).
\]

Therefore

\[
 r\le5/2.
\]

Equality forces every reward above state three to vanish, uniquely giving

\[
 d(2):d(3)=15:4
\]

and the dyadic source polynomial

\[
 Q(t)=(1-t)(1-t/2).
\]

This is `L-90214`. It rules out every attempted improvement by adding finitely or infinitely many positive boundary rewards while keeping the same affine tail and removing the independent 3-channel.

Within the simpler constant-tail family, `L-90213` also proves that every genuine ordered balance cutoff has only `r<=2`; its extremum is the single Haar factor `1-t`.

## 3. The scalar has a positive forcing and one Möbius boundary

For

\[
 \omega=(\varepsilon-\delta_2)*(2\varepsilon-\delta_2)*\mu,
\]

let `H(x)` be the two-low-row square-root-hinge scalar. The critical divisor operator

\[
 (\mathcal P f)(x)=\sum_{d\le x}d^{-1/2}f(x/d)
\]

satisfies

\[
 \mathcal P H(x)=\Phi(x),
\]

where

\[
 \Phi(x)=6\left[
 \sum_{d\le x}d^{-1/2}-\frac{\lfloor x\rfloor}{\sqrt x}
 \right]-\frac{15}{2}+\frac9{\sqrt2}.
\]

`L-90215` proves

\[
 \Phi(x)>0\qquad(x\ge4)
\]

and the exact inverse formula

\[
 H(x)=\sum_{d\le x}\frac{\mu(d)}{\sqrt d}\Phi(x/d).
\]

Thus the uniform-Pascal geometry, finite reward, and deterministic forcing are all positive. The only remaining sign loss is the final critical Möbius inversion. This is a sharp normal form, not a sign proof.

## 4. Complete finite dyadic filter cone

Let

\[
 Q(t)=\sum_{j=0}^{J}q_jt^j,
 \qquad q_0=1,
 \qquad Q(1)=0.
\]

Put

\[
 S_j=\sum_{\ell\le j}q_\ell,
 \qquad
 A_j=2\sum_{\ell<j}2^\ell S_\ell.
\]

For the associated uniform-Pascal reward, `L-90216` proves on the block `2^j<=m<2^(j+1)`:

\[
 m(m-1)d(m)=A_j+(m+1-2^{j+1})S_j.
\]

Hence reward positivity is equivalent to the finite cone conditions

\[
 A_j\ge0,
 \qquad
 A_j-(2^j-1)S_j\ge0
\]

at every scale, together with the tail inequality.

This is a necessary-and-sufficient fail-closed filter-design interface.

## 5. Global annular no-go

Finite summation by parts and the cone coordinates give

\[
 -Q'(1)
 =\frac12+
 \sum_{j=2}^{J-1}\frac{A_j}{2^{j+1}}
 +\frac{A_J}{2^J}.
\]

Therefore every positive-reward filter satisfies

\[
 Q'(1)\le-1/2,
\]

with equality only for

\[
 Q(t)=(1-t)(1-t/2).
\]

This is `L-90218`. In particular, **no finite double-neutral annular filter can have coordinatewise-positive uniform-Pascal reward**. The incompatibility applies to the entire factor-`2^J` annular hierarchy, not only one factor-64 design.

`L-90219` quantifies the signed failure. For every double-neutral filter,

\[
 \sum_{j=2}^{J-1}\frac{A_j}{2^{j+1}}
 +\frac{A_J}{2^J}=-1/2,
\]

so the weighted average block numerator is exactly `-2`. If the eventual tail reward is nonnegative, some pre-tail block obeys

\[
 A_j\le-\frac{2}{1-2^{2-J}}.
\]

Thus annular cancellation carries an unavoidable quantitative Pascal debt.

## 6. Improved factor-64 reward is compactly signed

Applying the cone to

\[
 P_{64}^*(t)
 =(1-t)^2(1-t/\sqrt2)(1+t)(1+3t/4+t^2)
\]

gives the exact witness

\[
 d(15)=\frac{1-\sqrt2}{42}<0.
\]

`L-90217` proves the full sign classification:

\[
 d_{64}(m)<0
 \iff13\le m\le63,
\]

while

\[
 d_{64}(m)>0
 \quad(2\le m\le12\text{ and }m\ge64),
\]

with exact tail

\[
 d_{64}(m)=\frac{39(\sqrt2-1)}{m(m-1)}
 \qquad(m\ge64).
\]

Thus the annular/Pascal mismatch is one finite 51-state debt block, not a diffuse signed tail.

If the critical uniform-Pascal occupation is nonnegative, the missing bridge is exactly

\[
\sum_{m=13}^{63}[-d_{64}(m)]M(m)
\le
\sum_{m=2}^{12}d_{64}(m)M(m)
+39(\sqrt2-1)
\sum_{m\ge64}\frac{M(m)}{m(m-1)}.
\]

No proof of this payment is supplied.

## 7. Reconnaissance

A direct uniform-Pascal occupation scan of the critical target at

```text
X=10^3, 3*10^3, 10^4, 3*10^4, 10^5, 3*10^5, 10^6
```

found:

```text
all computed occupations nonnegative;
low-row positive reserve / 13..63 debt ratio: 8.60 -> 7.40;
positive tail / debt ratio: about 0.10;
complete factor-64 reward pairing positive at every tested endpoint.
```

These are discovery values only. They are not directed interval certificates and are not promoted to the 51-state payment theorem.

## 8. Route verdict

```text
stronger positive uniform-Pascal boundary reward     CLOSED: impossible
adding more positive dyadic taps                      CLOSED: q1 cannot improve
positive Pascal realization of double-neutral annulus CLOSED: impossible
signed factor-64/Pascal mismatch                      CLOSED to states 13..63
payment of the compact block                          OPEN / RH-BEARING
15:4 low-row sign after positive renewal              OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```

The next valid attack is not another generic filter search. It is one of:

1. prove the explicit 51-state factor-64 payment from the critical occupation;
2. prove the low-row scalar after the positive forcing/Möbius boundary normal form;
3. change policy or admit a genuinely signed multi-channel reward.

Everything else in the finite positive-boundary/double-neutral design space is now decided by theorem.
