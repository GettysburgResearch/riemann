# L-99024 — The complete all-depth equality row loses only an absolute score constant

Claim ID: `L-99024`  
Status: **PROPOSED COMPLETE HEREDITARY SCORE THEOREM**  
Created: 2026-08-18  
RH status: **not assumed**

The exact continuum equality endpoint frame has literal critical score

\[
\boxed{\mathcal H(R_X^{\rm eq})=4\sqrt X.}
\tag{L-99024.1}

The score is a nonnegative linear functional of the physical row. Compact Hall
and the causal split are exact row identities; direct endpoint integration and
optional cubature are exact; and the Hall row bonus has nonnegative literal
score. Therefore none of those operations lowers the total literal score.

## 1. Sourcewise all-depth telescope

The residual Hall source is supported on the fixed divisor set of `P_61`.
For one source node `d|P_61`, let

\[
Y_j=X/(d67^j)
\]

and let `k(d)` be the unique index with `1<=Y_{k(d)}<67`. Every nonterminal
causal row difference is positive and its literal entropy pays the corresponding
source-declared score difference. Telescoping gives

\[
[S(Y_0)-E(Y_0)]_+
\le[S(Y_{k(d)})-E(Y_{k(d)})]_+.
\tag{L-99024.2}

At the terminal quotient,

\[
[S(Y)-E(Y)]_+\le2T(Y)
\qquad(1\le Y<67).
\]

The Hall residual coefficient at every source node lies in `[0,1]`. Hence the
complete score-realization debt over all descendants is bounded by

\[
2(4\sqrt{67}-3)
\sum_{d\mid P_{61}}d^{-1/2}
=
2(4\sqrt{67}-3)
\prod_{p\le61}(1+p^{-1/2})
<3600.
\tag{L-99024.3}

This is one all-depth bound, not a debt paid once per generation.

## 2. Current-owned safety losses

The exact direct-integral row has no quantization loss. The sole common
thinning is

\[
\tau_K=\frac{\sqrt K}{\sqrt K+24},
\qquad K>X/67.
\]

Applied to the complete equality row, it costs at most

\[
4\sqrt X(1-\tau_K)
<96\sqrt{67}.
\tag{L-99024.4}

The fixed top omission and the finite anchored base have bounded literal score.
Let their combined bound be `C_top`. They are removed before physical
realization and are never copied to a child.

Combining (L-99024.1)--(L-99024.4), the final feasible row satisfies

\[
\boxed{
\mathcal H(d_X)
\ge4\sqrt X-C_*,
\qquad
C_*=3600+96\sqrt{67}+C_{\rm top}<\infty.
}
\tag{L-99024.5}

The actual child target-mass contraction below one eighth guarantees absolute
convergence and unique ownership of the all-depth positive tree. It is not
substituted for a signed score deficit.

## 3. Backup per-packet envelope

If one prefers a measure-valued truncation argument, define the deficit of a
restricted packet by the difference between its canonical row score and the
recursively realized score. The local terminal debt is bounded per target
mass, while the actual child mass is below one eighth. Thus

\[
\mathcal E(Y)
\le C_0+\frac18\mathcal E(Y/67+1),
\]

which gives a uniform bound. This is equivalent to the sourcewise telescope
above but weaker numerically.

No estimate involving `J_Lambda-4sqrt(X)` and no false `Y4` pricing of the
complete benchmark enters the proof.
