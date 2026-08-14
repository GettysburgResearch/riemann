# L-91667 — The direct native equality row gives a complete one-use root reset

Claim ID: `L-91667`  
Status: **PROPOSED COMPLETE ROOT THEOREM ON FROZEN INPUTS — INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-14  
Supersedes for the root step: `L-91659` and the open `GRRT` formulation  
Primary inputs: `L-91621`, `L-91622`, `L-91663`, `L-91666`, `L-91557`, the frozen current-only reset packets of `T-91101`  
RH status: **unproved until independent reconstruction**

## 1. Exact native row, not a formal complement

For real `X>=1`, define

\[
 c_X(j)=\sum_{k\le X}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j),
 \qquad j\ge2,
\tag{L-91667.1}
\]

with causal zero extension. The exact component response identity gives

\[
\boxed{
 \Gamma(c_X;q)=w_X(q)
 =q^{-1/2}\log(X/q)\mathbf1_{q\le X},
}
\tag{L-91667.2}
\]

and

\[
\boxed{
 \Xi(c_X;q)=\Omega_X(q)=w_X(q)-2w_X(4q).
}
\tag{L-91667.3}
\]

These identities follow by setting `n=km` and using
`sum_(k|n) mu(k)=1_(n=1)`. Thus the native ordinary and detail capacities are
not inferred from a table of heterogeneous estimates: they are the exact
responses of one row.

## 2. Positive source-disjoint realization of the native row

Use the labeled least-prime stopping line of `L-91621`. Every source atom belongs
to exactly one of:

```text
pre-stopping current packet;
one complete P_61 one-prime leaf;
one terminal/frontier packet.
```

On every complete leaf, apply the exact native target/score/row cocycle and then
the no-upward Hall transport. Hall is chosen separately on mutually singular
leaves and only its positive outputs are summed. The resulting global identity
is

\[
\boxed{
 c_X=R_{\rm pre}
 +R_s(c_s)+R_h(c_h)+B_s+B_h,
}
\tag{L-91667.4}
\]

where every row on the right is coefficientwise nonnegative, `c_s,c_h` are
positive source measures, and `B_s,B_h` are positive target-null current row
bonuses. At the same time,

\[
 T(c_s)+T(c_h)=T_{\rm parent},
\tag{L-91667.5}
\]

and the row-budgeted declared score of `c_s,c_h` is at least the signed parent
score. There is no nonlinear Hall/tree commutation and no source atom is copied.
The measurable continuum endpoint version follows by deterministic greedy Hall,
positive simple-measure approximation, and monotone convergence.

Equation (L-91667.4) proves in particular

\[
\boxed{c_X\ge0.}
\tag{L-91667.6}
\]

It replaces the old operation “define the current packet as native minus
recursive.”

## 3. Canonical fixed-67 child and arbitrary replacement

Restrict both positive residual sources to `n<=X/67`, evaluate them at endpoint
`X/67`, and let `R_ch` be their summed canonical child row. Endpoint monotonicity
of `Q_Y` gives

\[
\boxed{R_{\rm cur}:=c_X-R_{\rm ch}\ge0.}
\tag{L-91667.7}
\]

Let `d_ch` be an arbitrary nonnegative row feasible for the complete child
ordinary, radix-four, and child-owned boundary capacities. Put

\[
\boxed{d_X=R_{\rm cur}+d_{\rm ch}.}
\tag{L-91667.8}
\]

The child is embedded at the same literal row indices. For every integer
`q>=2`,

\[
\begin{aligned}
 \Gamma(d_X;q)
 &=w_X(q)-\Gamma(R_{\rm ch};q)+\Gamma(d_{\rm ch};q)\\
 &\le w_X(q),
\end{aligned}
\tag{L-91667.9}
\]

and

\[
\begin{aligned}
 \Xi(d_X;q)
 &=\Omega_X(q)-\Xi(R_{\rm ch};q)+\Xi(d_{\rm ch};q)\\
 &\le\Omega_X(q).
\end{aligned}
\tag{L-91667.10}
\]

The detail inequality is established before the positive radix-four telescope
is invoked. No affine row dilation, fractional physical column, or independent
copy of the finite small-prime block occurs.

## 4. Boundary ownership and one-use current ledger

The source identity underlying (L-91667.4) fixes ownership before optimization.
The finite packets are ordered as follows.

| Packet | Ownership | Recursive? |
|---|---|---:|
| positive outer equality producer | pre-stopping current | no |
| one global B-spline quantization | pre-stopping current | no |
| width-three quantization collar | same quantization | no |
| finite/continuum mismatch | global current correction | no |
| interior safety scaling | applied once after the current sum | no |
| fixed top omission and terminal annulus | global current correction | no |
| corrected `P_61/67` two-channel port | global current correction | no |
| Hall row bonuses `B_s,B_h` | current on their leaf | no |
| residual positive sources `c_s,c_h` | current minus canonical child | no |
| restricted canonical child | child-owned capacities only | yes |

The finite current packets are not added on top of `c_X`; they are the
source-ordered pieces whose exact sum is the pre-stopping/current part of
(L-91667.4). Quantization is performed once after current continuum terms are
summed. The mismatch, terminal packet, and common port are each applied once.
The recursive child has zero ownership of every root-only collar, omission, and
common-port coordinate.

The frozen mismatch/collar theorem proves the interior detail inequality after
one safety factor. The terminal theorem proves the remaining top columns. The
corrected `P_61/67` port uses

\[
 \prod_{p\le61}(1+p^{-1})<14/3
\]

and its strict Schur reserve; the obsolete `P_53` constant is not used. These
finite current coordinates therefore fit the boundary vector owned by
`R_pre`, while (L-91667.9)--(L-91667.10) prove the complete ordinary/detail
comparison for the recursively replaceable part.

## 5. Literal score recurrence

For one positive source atom with local quotient `Y`, the literal component
score is

\[
 E(Y)=\sum_{2\le m\le Y}
 \frac{\log m}{\sqrt m}\log(Y/m).
\tag{L-91667.11}
\]

If `Y>=67`, `L-91666` gives

\[
 E(Y)-E(Y/67)
 \ge5(\sqrt Y-\sqrt{Y/67}),
\tag{L-91667.12}
\]

which is exactly the complete row-budgeted declared-score difference. After
multiplication by either nonnegative branch coefficient, the inherited score is
paid coefficient one.

If `1<=Y<67`, the atom terminates. Its positive declared-minus-literal deficit is
bounded on the fixed compact window. The finite `P_61` source support gives the
explicit absolute terminal estimate

\[
 2(4\sqrt{67}-3)
 \prod_{p\le61}(1+p^{-1/2})<3600.
\tag{L-91667.13}
\]

Hall bonuses have nonnegative literal score. The outer quantization is
score-favorable. The safety, mismatch, terminal, and common-port charges form
one effective constant `C_reset`, independent of `X`.

Consequently, for every nearly optimal child row,

\[
\boxed{
 \operatorname{Loss}_X(d_X)
 \le
 \operatorname{Loss}_{X/67+C_0}(d_{\rm ch})+C_{\rm reset}.
}
\tag{L-91667.14}
\]

This is an identity/inequality for the actual child packet. No source fraction
is used as a coefficient of signed loss.

## 6. Root benchmark front door

The causal continuum equality source has exact critical score

\[
\boxed{\mathcal J_{\rm eq}^{\rm cont}(X)=4\sqrt X.}
\tag{L-91667.15}
\]

The leafwise cocycle and Hall representation preserve or improve its
row-budgeted score. Positive B-spline quantization cannot decrease it. All
finite current charges are already included in `C_reset`.

The native parabolic benchmark satisfies the elementary bound

\[
\boxed{
 J_\Lambda(X)<4\sqrt X+4\log X.
}
\tag{L-91667.16}
\]

Equations (L-91667.14)--(L-91667.16) therefore place the native endpoint datum
in the direct-row reset family with at most logarithmic accumulated debt.

## 7. Iteration

After at most

\[
 1+\left\lceil\frac{\log X}{\log67}\right\rceil
\]

generations the endpoint is in the fixed finite base. Iterating
(L-91667.14) gives

\[
\boxed{
 \operatorname{Loss}_X=O(\log X)=o(\log^2X).
}
\tag{L-91667.17}
\]

## 8. Review boundary

The theorem is a complete proposed replacement for the old root-complement
argument. Independent reconstruction must still replay the frozen Hall cells,
source-tree identities, finite mismatch/collar/terminal certificates, and the
corrected port constants. Failure of any frozen input retracts this theorem.

```text
formal complement as proof                         not used
common native packet type                          explicit
local/global source identity                       leafwise + measurable Fubini
physical root atoms                                exact positive source leaves
ordinary residual comparison                       displayed
radix-four residual comparison                     displayed
one-use boundary ledger                            displayed
fixed-67 literal score difference                  proved in L-91666
one-generation reset debt                          absolute
all-generation native loss                         O(log X), proposed complete
RH                                                 not yet independently accepted
```
