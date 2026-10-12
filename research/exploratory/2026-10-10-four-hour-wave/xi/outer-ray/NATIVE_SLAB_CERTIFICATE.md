# One native companion slab with a complete spectral complement

Status: proposed directed finite certificate; independent exact-source review
pending. The claim requires `PASS_DIRECTED_NATIVE_COMPANION_SLAB` from the
retained checker and its named analytic/library dependencies.
Scope: actual `Xi(z)=xi(1/2+iz)`, derivative order zero, fixed `lambda=10`,
the **entire closed rectangle** `z=T-iy`, `-2<=T<=2`, `0<=y<=1/2`.
No higher-order, larger-height, unbounded-domain or RH claim is made.
Primitive source: actual completed zeta through directed Gamma/zeta at every
retained Hardy-Z endpoint; the native complete-count contract of FLINT at
`R=8192`, explicitly qualified below.
What was actually run: the producer and [check_native_slab.py](check_native_slab.py).
The artifact [native_slab_certificate.json](native_slab_certificate.json)
records primitive and full-box replay, exact rational margins and source/backend
hashes. Candidate roots alone are never accepted as a complete census.
Smallest remaining gap: a complete unbounded-domain continuation with effective
margins and source/coverage inputs. This finite rectangle cannot supply it.

## 1. Exact claim and producer/checker boundary

For

\[
E(z)=\Xi(z)-10i\Xi'(z),\qquad W(z)=iE(z)/E'(z),
\tag{N1}
\]

the accepted certificate gives

\[
E(z)\ne0,\qquad E'(z)\ne0,\qquad \operatorname{Re}W(z)>0
\quad(-2\le\operatorname{Re}z\le2,\ -1/2\le\operatorname{Im}z\le0).
\tag{N2}
\]

This is a finite source-bound theorem, using
[FINITE_CENSUS_COMPLEMENT.md](FINITE_CENSUS_COMPLEMENT.md), including its
complete high-zero tail. It adds a protected example within the remaining
slab to the all-order outer theorem; it does not change the latter's global
entry height or establish a slab theorem for arbitrary real `T`.

[produce_native_candidates.py](produce_native_candidates.py) uses
`acb.zeta_zeros` only to propose dyadic root brackets with denominator `2^24`.
Its output [native_candidates.json](native_candidates.json) is explicitly
labeled `CANDIDATES_ONLY_NOT_A_ZERO_CENSUS`. The checker never calls that
candidate routine. It instead evaluates each endpoint independently through
the directed actual Gamma/zeta expression and re-evaluates the complete count
through its separately stated library contract. Producer and checker use the
same Arb implementation; this is primitive replay, not a second independent
arithmetic implementation.

## 2. Actual primitive root replay and the imported complete-count contract

At a positive real ordinate `t`, set

\[
\theta(t)=\operatorname{Im}\log\Gamma(1/4+it/2)
               -(t/2)\log\pi,
\qquad Z(t)=e^{i\theta(t)}\zeta(1/2+it).
\tag{N3}
\]

The completed functional equation makes `Z(t)` real. The completed formula
gives

\[
\xi(1/2+it)
 =-\tfrac12(t^2+1/4)\pi^{-1/4}
   |\Gamma(1/4+it/2)|Z(t).
\tag{N4}
\]

The factor multiplying `Z` is real and nonzero. Branch changes by `2pi` in
the Gamma argument do not affect the exponential in (N3). Strict opposite
directed signs at the two exact dyadic endpoints therefore prove a genuine
critical-line zero in each interval by continuity. The checker verifies all
8,049 intervals are positive, strictly disjoint, and lie below `R=8192`;
it also verifies `Z(R)` is nonzero, avoiding endpoint-count ambiguity.

The call `arb(8192).zeta_nzeros()` returns the exact integer 8,049 under
FLINT's **complete nontrivial-zero counting contract**, including analytic
multiplicity. The precise imported contract matters: FLINT 3.6.0's
implementation uses verified finite Gram/Rosser rules up to its stated cutoff,
and Turing's method for the higher regime. At this index the finite Rosser
input is used; that historical finite verification is **not replayed here**.

The audited reference source is FLINT commit
`8d5454b96761fafe4d5a9da76a369a602f500f49` (`v3.6.0`),
[`src/acb_dirichlet/isolate_hardy_z_zero.c`](https://github.com/flintlib/flint/blob/8d5454b96761fafe4d5a9da76a369a602f500f49/src/acb_dirichlet/isolate_hardy_z_zero.c).
Its SHA256 is
`7276e21c6d241a4ca939b57476f530ae7a7eecbe142cefe11e26aa0a95088280`.
The source states `GRAMS_LAW_MAX=126`, `ROSSERS_RULE_MAX=13999526`, selects
the finite-rule or Turing separation routine, and implements the exact count
from the separated list. It cites Arias de Reyna's 2012 algorithm account.
The artifact also binds the loaded Python extension and native-library
binaries; no independently reproduced build is claimed.

Together, the imported complete count and 8,049 replayed disjoint sign changes
prove exactly one root of analytic multiplicity one per interval and exclude
any omitted root below `R`. Thus the finite product in (C1) has exactly these
simple real roots. An internally consistent list of candidates, or sign
changes without a complete count, would not establish that premise.

## 3. Full compact polynomial coverage and complete tail

For the finite polynomial `P_R`, its logarithmic derivatives are

\[
l_1=P_R'/P_R=-\sum_j\frac{2z}{\gamma_j^2-z^2},\qquad
l_2=l_1'=-\sum_j\frac{2(\gamma_j^2+z^2)}{(\gamma_j^2-z^2)^2}.
\tag{N5}
\]

The unknown exact `gamma_j` is enclosed by its accepted root interval. The
constant `Xi(0)` cancels. Exact algebra gives

\[
W_P=\frac{i(1-10il_1)}{l_1-10i(l_1^2+l_2)}.
\tag{N6}
\]

The checker covers the whole closed target rectangle by all `32*8=256`
complex interval boxes of widths `1/8` in `T` and `1/16` in `y`. Each box
evaluates both **complete finite sums** (N5), guards division, and encloses
(N6) using outward Arb/acb ball arithmetic. Let its proved rational bounds be
`Re W_P>=a>0` and `|W_P|<=b`, and set `tau=a/b>0`.

The rectangle lies in `|z|<=B=17/8<R`, since `4+1/4<(17/8)^2`. The actual
source count from [COARSE_ZERO_COUNT.md](../../heights/COARSE_ZERO_COUNT.md)
and the accepted endpoint count give the complete tail bound

\[
S_R\le S=\frac{2(\log R+1)}R-\frac{8049}{R^2}.
\tag{N7}
\]

The checker independently encloses actual `xi(1/2)>1/4`, supplying the
coarse count's single finite primitive input. The infinite counting theorem
itself, actual classical strip and complete genus-zero product remain
analytic dependencies; the finite checker does not authenticate them.

From the tail formulas (C5)--(C9),

\[
M_1=\frac{2BS}{1-B^2/R^2},\qquad
M_2=\frac{2S}{(1-B/R)^2},\qquad
|p_R'/p_R|\le M_1,\quad |p_R''/p_R|\le M_1^2+M_2.
\tag{N8}
\]

For each box the checker then sets

\[
\alpha=10M_1,\qquad
\beta=b[2M_1+10(M_1^2+M_2)]
\tag{N9}
\]

and requires **strictly** `beta<1` and

\[
\tau-\alpha-(1+\tau)\beta>0.
\tag{N10}
\]

This is exactly (C14)/(C17) for `r=0`. Every source multiplier derivative in
the full tail is retained, including nonreal zeros permitted above `R`.
The final directed lower bound

\[
\operatorname{Re}W[\Xi]
\ge a-b\frac{\alpha+\beta}{1-\beta}>0
\tag{N11}
\]

is also checked and retained per box. These inequalities protect the actual
companion and its derivative, so the conclusion does not assume either is
already nonzero in the slab.

## 4. Replay and boundaries

Run in the repository root after the documented tool activation:

```sh
source /workspace/.riemann-tools/activate.sh
python research/exploratory/2026-10-10-four-hour-wave/xi/outer-ray/produce_native_candidates.py
python research/exploratory/2026-10-10-four-hour-wave/xi/outer-ray/check_native_slab.py
```

The checker fixes Python-flint 0.9.0 / FLINT 3.6.0 and precision 128 bits,
uses exact dyadic primitive and domain endpoints, and requires every assertion
to pass. Its artifact contains all box bounds and hashes of the primitive
candidate data, producer, checker, analytic sources and loaded binaries.
The implementation is a directed interval computation; its acceptance rule
requires explicit strict ball inequalities and never uses fitted decimals.

The result retains the imported finite counting input, named classical
analytic dependencies and the backend's correctness contract. It neither
checks a different arithmetic implementation nor replays a historical
all-height verification. A larger domain, a different parameter, a higher
derivative order or a changed backend needs a new certificate and review.
Finite success in this rectangle is compatible with an off-real quartet far
outside it, and supplies no RH conclusion.
