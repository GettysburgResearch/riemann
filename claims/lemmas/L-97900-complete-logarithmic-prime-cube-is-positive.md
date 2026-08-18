# L-97900 — The complete rough-prime cube through almost `log X` is positive

Claim ID: `L-97900`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Frozen base: PR #594 at `ef76157a516c520a0f829ea4ee346c62759743ed`  
Inputs: PR #590 `L-97700`; the sharp `P_61` annular asymptotic; classical PNT and Mertens theorems  
RH status: **not assumed**

Let `b(Y)=F_61(Y)` be the complete grouped `P_61` annular `5:3`
base. The retained all-real theorem gives, beyond a fixed activation range,

\[
 b(Y)=a_*\sqrt Y+c_*+O(Y^{-3/2}),
 \qquad
 a_*=12\prod_{q\le61}\left(1-\frac1q\right)>0.
 \tag{L-97900.1}
\]

For large `X`, put

\[
 \delta_X=(\log\log X)^{-1/4},
 \qquad
 P_X=(1-2\delta_X)\log X,
 \tag{L-97900.2}
\]

and let

\[
 Q_X=\prod_{67\le q\le P_X}q.
\]

Define the complete logarithmic cube and its normalized value by

\[
 \mathcal B_{P_X}(X)=
 \sum_{d\mid Q_X}\frac{\mu(d)}{\sqrt d}b(X/d),
 \qquad
 U_{P_X}(X)=\frac{\mathcal B_{P_X}(X)}{\sqrt X}.
 \tag{L-97900.3}
\]

Then

\[
 \boxed{U_{P_X}(X)>0}
 \tag{L-97900.4}
\]

for all sufficiently large `X`. More precisely,

\[
 \boxed{
 U_{P_X}(X)
 =a_*\prod_{67\le q\le P_X}\left(1-\frac1q\right)
 +o\!\left(\frac1{\log P_X}\right)
 \asymp\frac1{\log\log X}.
 }
 \tag{L-97900.5}
\]

## Proof

The effective prime number theorem gives

\[
 \vartheta(P_X)=P_X+o(\delta_X\log X).
\]

Consequently

\[
 \log Q_X\le(1-\delta_X)\log X
 \tag{L-97900.6}
\]

for all sufficiently large `X`. Thus every divisor `d|Q_X` satisfies

\[
 X/d\ge X^{\delta_X}\longrightarrow\infty,
 \tag{L-97900.7}
\]

uniformly. We may substitute (L-97900.1) into every term of
(L-97900.3). Exact divisor factorization gives

\[
 \begin{aligned}
 \mathcal B_{P_X}(X)
 ={}&a_*\sqrt X
      \prod_{67\le q\le P_X}(1-q^{-1})\\
 &+c_*\prod_{67\le q\le P_X}(1-q^{-1/2})
 +O\!\left(
 X^{-3/2}\prod_{67\le q\le P_X}(1+q)
 \right).
 \end{aligned}
 \tag{L-97900.8}
\]

The final product has logarithm

\[
 \sum_{q\le P_X}\log(1+q)
 =\vartheta(P_X)+O(\log\log P_X),
\]

so its contribution in (L-97900.8), after division by `sqrt(X)`, is

\[
 O(X^{-1-\delta_X+o(1)}).
\]

The constant term is also negligible after division by `sqrt(X)`; indeed its
Euler product has magnitude at most one. Mertens' theorem now gives

\[
 \prod_{67\le q\le P_X}(1-q^{-1})\asymp(\log P_X)^{-1}.
\]

The positive square-root main term therefore dominates, proving
(L-97900.4)--(L-97900.5).

## Exact Bellman interpretation

Starting from the complete small cube of PR #590 and adjoining every prime up
to `P_X`, largest-prime telescoping gives exactly

\[
 U_{P_X}(X)
 =U_Z(X)-
 \sum_{Z<p\le P_X}\frac1pU_{<p}(X/p).
 \tag{L-97900.9}
\]

Thus every history whose largest rough prime is at most
`(1-o(1))log X` has already been resummed into one positive source object.
No count-depth truncation and no absolute value is used.