# L-106082 — Minimum-owner blocks all lie in the coherent long-core range

Claim ID: `L-106082`  
Programme aliases: `LFAM1.ALL_BLOCK_PHASE_PACKING`, `STRESS.MINIMUM_OWNER_LONG_CORE`, `LFAM2.CORE_PAID_KUMMER_MOMENT`  
Status: **PROPOSED COMPLETE COHERENT PHASE THEOREM; HOSTILE SOURCE REVIEW REQUIRED**  
Created: 2026-08-25  
Depends on: parent `L-102882--L-102883`, `L-102860--L-102865`, `T-102890`; `L-106080--L-106081`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Work on one linearly projected balanced block

\[
B\le a<2B,
\qquad
L\le\lambda<2L,
\]

of `L-106081`, after complete carrier, Wick, gauge, marked-prime and overlap
recombination.  Every source atom occurs in exactly one such block.

By `L-106081`,

\[
\boxed{L^2<2B.}
\tag{L-106082.1}
\]

## 1. Same-family version of the centered phase theorem

Parent `L-102883` states the coherent estimate for two disjoint dyadic prime
families.  The clean minimum-owner packet can have both distinguished owners in
the same dyadic family, but the identical estimate holds after deleting the
shared-prime diagonal.

Indeed, for

\[
A_\ell(d)=\mathbf1_{\ell\mid d}-\frac1\ell,
\qquad
K_{\mathcal P}(d)=\sum_{\ell\in\mathcal P}A_\ell(d),
\]

one has exactly

\[
\boxed{
\sum_{\substack{\ell,\rho\in\mathcal P\\\ell\ne\rho}}
A_\ell(d)A_\rho(d)
=
K_{\mathcal P}(d)^2
-
\sum_{\ell\in\mathcal P}A_\ell(d)^2.
}
\tag{L-106082.2}
\]

For `d=0`, this has the same `O((L/log L)^2)` diagonal size as the two-family
kernel.  For `0<|d|<4B^2`,

\[
|K_{\mathcal P}(d)|
\ll
1+\frac{\log(2B)}{\log(2L)},
\]

and the deleted square sum is bounded by the same divisor-count argument.
Therefore the proof of `L-102883` gives, for the clean off-diagonal same-family
packet,

\[
\boxed{
\mathcal E_{B,L}^{\rm clean}
\ll
\frac{X^{o(1)}}{Q}
\left[
1+rac{L^2}{B\log^2(2L)}
\right].
}
\tag{L-106082.3}
\]

Here `Q` denotes the remaining literal co-owner source weight in the parent
allocation.  All Boolean Vaughan multiplicities, finite carrier charts and
shell labels are retained in the Hilbert vector and cost only `X^(o(1))`.
Equation (L-106082.3) is the same source allocation already used by the parent
long-core theorem; no selected owner weight is reused in another Cauchy step.

## 2. Every block is long-core

Substituting (L-106082.1) into (L-106082.3) gives

\[
\boxed{
\mathcal E_{B,L}^{\rm clean}=X^{o(1)}.
}
\tag{L-106082.4}

Thus the coherent nonzero double-phase transform is subpower on every
minimum-owner Boolean balanced block.  There is no residual short-core range.

The interpretation in the exact L-family coordinates of `L-106020` is:

```text
two distinguished owner phases
  = two nontrivial Kummer/Artin-Schreier coordinates;

lambda^2, rho^2 <= literal cores
  = both phase conductors are paid by the same source occurrence;

complete even-character fibres
  = retained before the physical observation.
```

## 3. Shared and overlapping labels

The deleted case `lambda=rho` is a shared-owner sector and is already a
polylogarithmic common-factor renewal.  Owner/core overlaps are likewise
removed by the inherited finite-Euler renewals before (L-106081.3).  Equal
physical products and representation multiplicity are subpower by the parent
energy theorem.

Consequently (L-106082.4) controls precisely the clean distinct-product row.
No negative part is taken separately on the equal-core, one-sided or two-sided
subpackets.

## 4. Global recombination

There are only `O(log^2 X)` pairs `(B,L)` on a dyadic physical horizon, and a
fixed/polylogarithmic number of marked, carrier, shell and renewal labels.
Cauchy across this **linear** partition therefore costs `X^(o(1))`.  It is
applied only after the complete all-chaos carrier has been recombined inside
each source coefficient.

Hence the complete Boolean balanced field satisfies

\[
\boxed{
\int_X^{2X}
|\mathcal B_{\rm sf}(t)|^2\frac{dt}{t}
=X^{o(1)}.
}
\tag{L-106082.5}

In particular its logarithmic negative mass is subpower.

## Scope and review flag

The new arithmetic input is only the range implication `L^2<2B`.  The analytic
centered-divisor estimate and literal owner-weight allocation are inherited
from `L-102882--L-102883` and the parent long-core composition.

Because (L-106082.5) would remove the last arithmetic row, a reviewer must
reconstruct that source allocation rather than accept the range comparison
alone.  The full conditional composition and its exact acceptance posture are
recorded in `T-106080` and `M-106080`.