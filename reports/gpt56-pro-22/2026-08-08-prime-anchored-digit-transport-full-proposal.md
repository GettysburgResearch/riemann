# Full proposal — prime-anchored digit-depletion transport

Agent: `gpt56-pro-22`  
Date: 2026-08-08  
Issue: #258  
Base: PR #250 at `f179ab93e7e0dc748e0e9fb9e5a6800b80b6d224`  
Status: **FULL PROPOSAL; PRODUCTION SIGNED DIPOLE TRANSPORT OPEN; RH UNPROVED**

## Executive conclusion

PR #250 isolated the correct top reflected source and showed why aggregate
reflected positivity cannot estimate it: the corresponding Schur complement is
exactly zero. The remaining problem was formulated as a source-specific
contraction `PARC(K)`.

This continuation supplies a new exact mechanism between the top source and
that contraction.

The top source has the form

\[
T_{K,V}=\Lambda*r_V^{*(K-1)}
       =g_{K-1}*\mu_{>V}^{*(K-1)},
\]

where

\[
g_{K-1}(b)
={d_{K-1}(b)\log b\over K-1}\ge0
\]

and every active representation contains only one aggregate short coordinate
`b<V`.

For a scale-adapted radix `Q`, introduce the positive nonmultiple-count kernel

\[
a_Q(n)=1-\mathbf1_{Q\mid n}
\]

and the reciprocal-free potential

\[
Z=a_Q*T.
\]

Finite resolvent nilpotence gives the exact source identity

\[
\boxed{
D:=(\varepsilon-\delta_Q)T
=\mu_V*Z.}
\]

The physical field therefore satisfies the fixed-scale recurrence

\[
\boxed{
T_J=Q^{-1/2}T_{J-\log Q}+D_J.}
\]

The new arithmetic theorem is to estimate the **complete signed dipole `D`** by
transporting the truncated Möbius factor through the reciprocal-free potential
`Z`, while preserving every lower-depth sibling and every two-frequency cross
term.

This is Prime-Anchored Digit Transport, `PADT(K)`.

It is not a proof of RH yet. It is a substantially more concrete proposal than
a black-box balanced Type-II theorem:

```text
exact top source
-> positive scale-adapted digit depletion
-> reciprocal-free potential
-> signed mu_V divergence
-> adjacent carry transport
-> bounded prime-power cluster solve
-> exact two-frequency transport Gram
-> fixed-scale dipole recurrence
-> vanishing packet loss
-> RH.
```

## 1. Exact top source

Let

\[
r_V=\varepsilon-\mathbf1*\mu_V,
\qquad
X\le V^K.
\]

The top finite-resolvent prime row is initially

\[
\mu_V*r_V^{*(K-1)}*\ell.
\]

Every nonzero coefficient of `r_V^(K-1)` is supported above
`(V+1)^(K-1)`. Therefore the remaining factor is less than `V`, and truncating
`mu` has no effect on its logarithmic convolution. Coefficientwise through
`X`,

\[
\boxed{
\mu_V*r_V^{*(K-1)}*\ell
=\Lambda*r_V^{*(K-1)}.}
\]

Since

\[
r_V=\mathbf1*\mu_{>V},
\]

one gets

\[
\boxed{
T_{K,V}
=g_{K-1}*\mu_{>V}^{*(K-1)},
\qquad
g_{K-1}=\Lambda*\mathbf1^{*(K-1)}.}
\]

Writing `d_r=1^(*r)`, symmetry gives

\[
\boxed{
g_{K-1}(b)
={d_{K-1}(b)\log b\over K-1}\ge0.}
\]

Every active representation

\[
n=b\,d_1\cdots d_{K-1},
\qquad d_i>V,
\qquad n\le V^K,
\]

satisfies

\[
\boxed{b<V.}
\]

Thus the top source is not an untyped `K`-dimensional short face. It has one
positive aggregate anchor and a genuine large-factor Möbius tensor.

## 2. Positive nonmultiple-count kernel

For an integer radix `Q>=2`, let `delta_Q` be the arithmetic atom at `Q` and
put

\[
a_Q=\mathbf1*(\varepsilon-\delta_Q).
\]

Then

\[
\boxed{a_Q(n)=1-\mathbf1_{Q\mid n}\ge0}
\]

and

\[
\sum_{n\ge1}{a_Q(n)\over n^s}
=(1-Q^{-s})\zeta(s).
\]

The positive physical primitive is

\[
\boxed{
\mathcal C_Q(t)
=e^{-t/2}
\left(
\lfloor e^t\rfloor
-\left\lfloor{e^t\over Q}\right\rfloor
\right)\mathbf1_{t\ge0}.}
\]

It satisfies

\[
\left(\partial_t+{1\over2}\right)\mathcal C_Q
=
\sum_{n\ge1}{a_Q(n)\over\sqrt n}\delta_{\log n}
\]

and

\[
\widehat{\mathcal C_Q}(z)
={1-Q^{-s}\over s}\zeta(s),
\qquad s=z+\frac12.
\]

This kernel cancels one reciprocal-zeta factor but is not claimed generically
coercive.

## 3. Exact depletion and nilpotence

Define

\[
Z_{K,V,Q}=a_Q*T_{K,V}.
\]

Since

\[
r_V*T_{K,V}
=\Lambda*r_V^K=0
\]

through `V^K`, one has

\[
\boxed{
D_{K,V,Q}
:=(\varepsilon-\delta_Q)*T_{K,V}
=\mu_V*Z_{K,V,Q}.}
\]

The potential is reciprocal-free:

\[
\boxed{
Z_{K,V,Q}(s)
=-(1-Q^{-s})\zeta'(s)R_V(s)^{K-1},
\qquad
R_V=1-\zeta M_V.}
\]

The dipole retains the complete hard source:

\[
D(s)
=-(1-Q^{-s}){\zeta'(s)\over\zeta(s)}R_V(s)^{K-1}.
\]

This is precisely why the theorem must transport `mu_V` with its signs rather
than estimate `Z` and invert zeta generically.

The exact geometric identity

\[
T=(\varepsilon-\delta_Q)^{-1}*\mu_V*Z
\]

is retained as algebra, but it is not used by an absolute norm bound.

## 4. Recovery-wedge correction

The first draft tried to charge `mu_V` once after estimating `Z` at the current
block. That inference is invalid.

The recovery includes blocks

\[
J-\log a,
\qquad a\le V.
\]

At the lower edge

\[
J-\log V
=\left(1-{1\over K}\right)J+O_K(1),
\]

while

\[
V^{K-1}
=e^{J-\log V+O_K(1)}.
\]

Thus the original `V` has full top-order capacity on the shifted block. The
balanced tensor has merely moved into the recovery wedge.

The corrected proof uses the one-step dipole recurrence

\[
\boxed{
T_J
=Q^{-1/2}T_{J-\log Q}+D_J.}
\]

For a fixed-fraction radix, the shifted term is strict lower scale and carries
an exponentially small normalization coefficient. The only estimate needed is
therefore the direct signed estimate for `D`.

## 5. Dyadic specialization and parity channel

Choose

\[
Q=2^L,
\qquad
L=\left\lfloor{\delta_0J\over\log2}\right\rfloor.
\]

Then

\[
\log Q=\delta_0J+O(1).
\]

The arithmetic depletion has the exact bit-layer factorization

\[
\boxed{
a_{2^L}=a_2*\sum_{j=0}^{L-1}\delta_{2^j}.}
\]

Correspondingly,

\[
\boxed{
\mathcal C_{2^L}(t)
=\sum_{j=0}^{L-1}2^{-j/2}
\mathcal C_2(t-j\log2).}
\]

If

\[
\lambda_2(n)=(-1)^{n+1},
\]

then

\[
2a_2=\mathbf1+\lambda_2.
\]

The causal primitive of `lambda_2` is exactly the positive parity comb of PR
#236. Hence the fixed-scale depletion contains the parity channel as an exact
source component.

Every production certificate must reproduce the bit-layer identity and the
three-tap parity mutation. This prevents the Euler-aligned Mertens mode from
being hidden in the depletion stack.

## 6. Adjacent transport in the reviewed physical block

For source vectors `v_j` and a signed flow `F_j`,

\[
c_j=b_j+F_{j-1}-F_j
\]

implies exactly

\[
\boxed{
\sum_jc_jv_j
=\sum_jb_jv_j
+\sum_jF_j(v_{j+1}-v_j).}
\]

For multiplicative translates,

\[
h_j=\log{j+1\over j}
\]

and

\[
\|v_{j+1}-v_j\|_2^2
\le h_j^2\,\|U'\|^2
\]

on the appropriate expanded block.

The complete adjacent current is represented in the corrected two-frequency
physical Gram of PR #241:

\[
\mathcal G_J^\nabla=B_J^*K_JB_J.
\]

No frequency diagonal and no packetwise self-energy replacement is permitted.

## 7. Exact connection to signed carry transport

The positive anchor satisfies

\[
g_{K-1}=\Lambda*d_{K-1},
\]

so it contains a marked prime-power coordinate before norms are taken.

The adjacent carry flow of PR #254 changes a prime-power row by

\[
\sum_jF_j
\left(
\mathbf1_{q\mid j+1}
-2\mathbf1_{q\mid j}
+\mathbf1_{q\mid j-1}
\right).
\]

After solving complete consecutive prime-power clusters jointly, every
remaining positive child lies at most at half the marked prime-power scale.
The cluster length is at most three above the single exceptional cluster
`{2,3,4,5}`, whose exact inverse is entrywise nonnegative.

The exact scalar carry objective is

\[
\omega_j
=\log{j^2\over j^2-1}.
\]

It dominates physical adjacent displacement:

\[
\boxed{
\log^2\left(1+{1\over j}\right)
\le {1\over j^2}
\le\log{j^2\over j^2-1}.}
\]

Thus the analytic bridge is one source-specific Transport Frame certificate:

\[
P_S^*B_J^*K_JB_JP_S
\preceq
\mathcal C_{K,J}P_S^*W_JP_S,
\]

with

\[
\log\mathcal C_{K,J}=o_K(J).
\]

This is a finite generalized-eigenvalue problem on the exact flow subspace.

## 8. `PADT(K)`

For every sufficiently large block, an accepted proof object contains:

1. the complete top-source manifest;
2. every lower-depth divisor-allocation sibling;
3. the scale-adapted dyadic depletion;
4. the reciprocal-free potential `Z`;
5. the complete signed dipole `D=mu_V Z`;
6. the reviewed two-frequency normal Gram;
7. exact signed adjacent-flow incidence;
8. complete same-scale prime-power cluster solves;
9. every lower-scale and boundary destination;
10. a quadratic dipole-cost certificate
    \[
    E_D(K,J)
    \le
    e^{(\eta_K+o_K(1))J}
    [1+M_K((1-\delta_1)J+C_K)]
    \]
    with `eta_K->0`;
11. the fixed-ratio and parity mutations.

It is rejected by any absolute `mu_V` step before signed transport, any missing
hypercube sibling, any one-row cluster solve, any omitted two-frequency cross
term, or any undeclared same-scale remainder.

## 9. Conditional deduction to RH

The dipole recurrence gives

\[
E_{\rm top}(K,J)
\le
2Q^{-1}E_{\rm top}(K,J-\log Q)
+2E_D(K,J).
\]

Since

\[
Q^{-1}=e^{-\delta_0J+O(1)},
\]

an accepted `PADT(K)` object yields

\[
M_K(J)
\le
\exp\{(\eta_K+o_K(1))J\}
\left[
1+M_K((1-\delta)J+C_K)
\right]
\]

for one fixed `delta>0`.

Scale contraction gives

\[
2\Theta_\zeta
\le {C\eta_K\over\delta}.
\]

Along an unbounded order sequence with `eta_K->0`,

\[
\Theta_\zeta=0,
\]

and functional-equation symmetry gives RH.

The fixed-ratio shell exported by the same certificate supplies an independent
Mertens audit.

## 10. Two production paths

### A. Top-half signed carry flow

Construct the same type of flow suggested by the PR #254 top-half
reconnaissance, now on the exact prime-anchor source graph. Rationalize it and
prove the Transport Frame LMI.

### B. Dyadic bit-layer induction

Telescope the `O(J)` odd-part layers before total variation, using complete
lattice cancellation for the all-integer channel and the parity three-tap
identity for the dyadic channel, while retaining every lower-depth sibling.

Neither path is currently proved.

## 11. Exact regression

`X-25801` verifies:

```text
finite top/depletion parameter cases       6
dyadic bit-layer rows                   3584
all algebraic mismatch counts              0
adjacent rational flow identity          PASS
mutation tests                             7/7
proof-object SHA-256
cfae02e722f534195e9bfef00065e5457b0da1e5a18a96589ea0e9560aa2a7b3
```

The checker validates finite algebra only. It does not construct the source
graph or prove the transport-cost theorem.

## 12. Literature boundary

The closest major analytic methodology is the contagion and scale-propagation
framework of Matomäki, Radziwiłł, Shao, Tao, and Teräväinen,
*Higher uniformity of arithmetic functions in short intervals II. Almost all
intervals*, Inventiones Mathematicae 244 (2026), arXiv:2411.05770.

Its theorem is on almost all intervals. PADT requires every sufficiently large
block, or a separate theorem excluding the fixed Mertens mode from the
exceptional set.

## 13. Exact status

```text
top-depth prime-anchor normal form          PROPOSED COMPLETE EXACT
positive nonmultiple-count kernel           PROPOSED COMPLETE EXACT
source-specific depletion and dipole        PROPOSED COMPLETE EXACT
dyadic bit-layer/parity interface           PROPOSED COMPLETE EXACT
two-frequency adjacent-flow identity        PROPOSED COMPLETE EXACT
prime-power cluster algebra                 PROPOSED COMPLETE FINITE
carry-weight / physical-frame adapter       PROPOSED COMPLETE CONDITIONAL
production signed source flow               OPEN
production Transport Frame LMI              OPEN
PADT(K) family                              OPEN
PADT(K) family -> RH                        PROPOSED COMPLETE CONDITIONAL
Riemann Hypothesis                          UNPROVED
```

## 14. Reviewer decision

The proposal is not accepted because the source-specific flow and frame have
not yet been produced. It is a credible full proposal because the remaining
object is finite, source-bound, and sharply falsifiable.

One missing lower-depth sibling, one physical generalized eigenvalue of size
`e^(cJ)`, one surviving same-scale child, or one failed parity/Mertens mutation
rejects the mechanism.
