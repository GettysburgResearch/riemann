# L-91665 — Direct Hall replacement supplies a coefficient-one factor-67 reset

Status: **proposed complete on frozen inputs; independent reconstruction required; RH unproved**

This lemma supersedes the root-complement construction in `L-91659`. It uses the
logarithmic-debt consumer `T-91101`, the exact row/capacity theorem `L-91663`,
the fixed-67 score-difference replay `L-91664`, and the imported one-prime
cocycle/Hall/source-tree claims locked with this packet.

## 1. Required recurrence

For a positive typed packet `P` at endpoint `X`, write

`Loss_X(P;d)=J_X(P)-Score_X(d)`

for a nonnegative row feasible in every ordinary, radix-four, and finite
boundary coordinate. The consumer requires

\[
 \boxed{
 Loss_X(P;d_X)\le Loss_K(P^{ch};d_K)+C_{reset},
 \qquad K\le X/67+C_0,
 }
\]

with absolute constants. A bounded charge per generation is enough; no absolute
all-depth transfer of the continuum score to one finite row is asserted.

## 2. Current analytic packet

Retain, as current-only objects, the positive outer equality producer, B-spline
quantization, width-three collar, finite/continuum mismatch, interior safety
factor, fixed top omission, terminal-annulus correction, and common endpoint
port from `T-91101` and its cited lemmas. They are summed before the child is
inserted and are never copied to a child. Their complete one-generation score
charge is an effective absolute constant `C_an` on the frozen normalized
window.

The port uses the corrected `P_61/67` theorem `L-91320`, namely

\[
 \prod_{p\le61}(1+p^{-1})<14/3
\]

with the strict `1/9` Schur reserve. The obsolete `P_53` constant is not used.

## 3. Exact inner cocycle and Hall row

At one rough prime, put

\[
 r=p^{-1/2},\qquad \kappa_s=1-r^2,\qquad \kappa_h=r^2.
\]

The imported controlled cocycle is exact in target, row-budgeted native score,
and every literal row coordinate. The merged Hall theorem then produces
positive residual sources and positive target-null row bonuses, with exact
parent target use, score superordination, and a literal parent-row identity.
`L-91621` applies Hall separately on mutually singular stopping leaves; no Hall
choice is commuted through the rough tree and no source atom is duplicated.

## 4. Same-index child replacement

Restrict both positive residual sources to the common child endpoint `K=X/67`.
Let `R_ch` be their canonical child row and let `d_ch` be any nonnegative row
feasible for the complete child capacities. The fully summed inner parent row is

\[
 d_X^{inner}=R_{parent}-R_{ch}+d_{ch}.
\]

Endpoint monotonicity makes `R_parent-R_ch` nonnegative. By `L-91663`, for every
physical integer column `q>=2`,

\[
 \boxed{
 \Gamma(d_X^{inner};q)
 =\Gamma(R_{parent};q)-\Gamma(R_{ch};q)+\Gamma(d_{ch};q)
 \le\Gamma(R_{parent};q),
 }
\]

and

\[
 \boxed{
 \Xi(d_X^{inner};q)
 =\Xi(R_{parent};q)-\Xi(R_{ch};q)+\Xi(d_{ch};q)
 \le\Xi(R_{parent};q).
 }
\]

These are the simultaneous residual inequalities requested by PR #450 after the
complete current row is summed. The child is inserted by the identity map on
row indices. There is no affine lift, fractional column, duplicated small-prime
block, or hidden scalar child. The detail inequality is established before
`L-90029` is invoked.

## 5. Score coefficient and reset debt

The exact component score is

\[
 E(Y)=\sum_{2\le m\le Y}\frac{\log m}{\sqrt m}\log(Y/m).
\]

The corrected base is

`E(67)-(5 sqrt(67)-3)=1.2764007195...>1`,

while the split base required by the reset is

`E(67)-5(sqrt(67)-1)=3.2764007195...>3`.

The elementary proof and exact replay in `X-91663` give, for every `Y>=67`,

\[
 \boxed{E(Y)-E(Y/67)\ge5(\sqrt Y-\sqrt{Y/67}).}
\]

Multiplication by `kappa_s,kappa_h` shows that the physical current row
difference pays the inherited row-budgeted native score difference with
coefficient one. The identity embedding changes neither row coefficients nor
score. All compact Hall, terminal, and finite-Euler terms are bounded; an
explicit terminal bound is

\[
 2(4\sqrt{67}-3)\prod_{p\le61}(1+p^{-1/2})<3600.
\]

Let `C_reset` be the sum of the explicit current analytic, Hall-window, port,
terminal, and finite-base maxima. Every maximum is over a fixed finite graph or
compact normalized interval and is therefore effective and independent of `X`.
Then

\[
 \boxed{Loss_X\le Loss_{X/67+C_0}+C_{reset}.}
\]

No source fraction is used as a coefficient of a signed deficit.

## 6. Iteration

After at most

\[
 1+\left\lceil\frac{\log X}{\log67}\right\rceil
\]

generations the endpoint is in the fixed finite base. Hence

\[
 \boxed{Loss_X=O(\log X)=o(\log^2X).}
\]

Independent review must reconstruct the frozen Hall cells, one-prime cocycle,
source-disjoint stopping identity, current/inner partition in `T-91101`, one-use
port, and effective constants. Passing the local replay does not establish RH.
