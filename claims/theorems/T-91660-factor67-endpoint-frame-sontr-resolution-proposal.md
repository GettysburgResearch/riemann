# T-91660 — Factor-67 target Hall supplies Source-Owned Native Thinning and Realization

Claim ID: `T-91660`  
Status: **CANDIDATE COMPLETE SONTR / NRCT COMPOSITION ON FROZEN INPUTS — INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-14  
Primary new inputs: `L-91690`, `L-91691`  
Retained inputs: `L-91110/L-91111/L-91114/L-91115`, `L-91375/L-91377/L-91378/L-91379`, `L-91650/L-91654/L-91674/L-91682/L-91688`, `T-91312/T-91313/T-91314`  
RH status: **unproved pending independent reconstruction**

## 1. Statement of SONTR

For every sufficiently large endpoint `X`, construct:

1. a finite coefficientwise nonnegative current row `d_X^cur`;
2. source-disjoint recursive positive typed packets `P_b` with coefficients
   `alpha_b`;
3. one nonnegative native detail slack vector `s_X(q)`;
4. one atomwise source-ownership partition including current, child, stop,
   finite correction and unused thinning;

such that

\[
 Y_b\le X/67+1,
 \qquad
 \alpha_b\ge0,
 \qquad
 \sum_b\alpha_b<\frac18,
\tag{T-91660.1}
\]

\[
 C_{d_X^{\rm cur}}(q)+
 \sum_b\alpha_b C_{P_b}(q)
 \le w_X(q),
\tag{T-91660.2}
\]

\[
 \Xi_{d_X^{\rm cur}}(q)+
 \sum_b\alpha_b\Xi_{P_b}(q)
 =\Omega_X(q)-s_X(q)
 \le\Omega_X(q),
\tag{T-91660.3}
\]

with the analogous one-use inequality for every retained boundary or common
port coordinate, and

\[
 \sum_qY_4(q)s_X(q)=O(\log X)=o(\log^2X).
\tag{T-91660.4}
\]

This is the Source-Owned Native Thinning and Realization theorem (`SONTR`) in
the exact native normalization.

## 2. Root source ownership

Set

\[
 K=\lfloor X/67\rfloor+1.
\]

On every outer endpoint fiber `s>=K`, one has `x=X/s<67`. Hence every
squarefree root divisor belongs to `P_61`; no rough prime is consumed at the
root.

`L-91690` applies one deterministic no-upward target Hall transport with
uniform prefix margin `>7/20`. The same coefficients give:

```text
exact target residual;
score-superordinate positive residual;
nonnegative target-null bonus in every component row.
```

Each small-divisor source occurrence is assigned once to a matched pair or to
one residual coefficient. `L-91688` independently assigns every rough monomial
to its first rough-prime owner. The two labels are compatible because the root
window is strict below `67`.

Thus the complete source label is

\[
(\text{endpoint fiber},\text{P61 divisor},\text{first rough owner},
  \text{causal channel}),
\]

and no label occurs twice.

## 3. Positive current and recursive children

Apply the exact causal identity to each positive residual packet. Retain the
row bonus as current. Frozen causal positivity gives a coefficientwise
nonnegative current row before finite correction, and

\[
 \sum_b\alpha_b<67^{-1/2}<1/8.
\tag{T-91660.5}
\]

The identity holds before physical realization in target, declared score,
every component row, both ordinary columns used by each radix-four coordinate,
literal entropy and all boundary/common-port coordinates.

Positive endpoint integration and common-parent summation preserve the
identity. Same-index placement gives the actual arithmetic child coefficient
once. No affine row-index substitution, fractional physical column, stopped-leaf
Hall operation or duplicated rough reservoir is used.

## 4. Native finite realization

Quantize the common parent endpoint measure once. Before quantization:

- truncate the fixed top interval of width `W=10000`;
- multiply all retained labelled weights by
  \[
  \sigma_K=(1+178/K)^{-1}.
  \]

`L-91691` proves:

```text
interior finite/continuum plus collar error   <177/K of native detail;
terminal possible overfill                    <4452 X^(-3/2);
terminal omission reserve                     >5033 X^(-3/2).
```

Therefore every physical detail column is feasible. The positive radix-four
inverse gives ordinary feasibility. The exact inner residual is retained as
the source-owned recursive packet, not approximated or charged again.

The finite/continuum equality

\[
 b_X^\star=\overline b_X^\star
\]

is never asserted. The nonzero defect from `R-91102` remains a firewall; the
proof creates explicit unused native capacity by positive thinning and absorbs
the bounded defect there.

## 5. Port and one-use correction ledger

All current fibers, all row bonuses and all rough colors are summed before the
physical quantizer. The following are then charged exactly once:

```text
positive martingale quantization;
finite/continuum mismatch;
interior safety thinning;
fixed top omission and terminal taper;
finite base correction;
one shared endpoint port.
```

Children own only their same-index recursive packet. They do not own a second
collar, mismatch, taper or port. This proves the atomwise one-use ledger
required in `T-91314`.

## 6. Deficit recurrence

Let `Lambda_eq(X)` be the normalized worst equality deficit of the positive
typed packet family. Root target Hall creates no score debt; the component-row
bonus has nonnegative literal entropy. Positive causal generators obey the
frozen bound

\[
 \Delta(P_{\rm cau})\le2m(P_{\rm cau}).
\]

The finite correction packet has one absolute cost `C_67`. Positive homogeneity
and subadditivity therefore give

\[
\boxed{
 \Lambda_{\rm eq}(X)
 \le C_{67}+\rho\Lambda_{\rm eq}(X/67+1),
 \qquad \rho<\frac18.
}
\tag{T-91660.6}
\]

Iteration yields

\[
\boxed{
 \Lambda_{\rm eq}(X)=O(1).
}
\tag{T-91660.7}
\]

Consequently the constructed physical row satisfies

\[
 4\sqrt X-\mathcal H(d_X)=O(1).
\tag{T-91660.8}
\]

The native benchmark comparison gives

\[
 J_\Lambda(X)-4\sqrt X<4\log X,
\]

and hence

\[
\boxed{
 J_\Lambda(X)-\mathcal H(d_X)
 \le4\log X+O(1)
 =o(\log^2X).
}
\tag{T-91660.9}
\]

By the exact radix-four dual,

\[
 J_\Lambda(X)-\mathcal H(d_X)
 =\sum_qY_4(q)s_X(q).
\tag{T-91660.10}
\]

This proves the weighted-slack clause of SONTR.

## 7. Consequence

Equations (T-91660.1)--(T-91660.10) supply the Native-Root Capacity Theorem
`T-91314` on the frozen input stack. The one-sided endpoint consumer `T-91313`
then gives the proposed implication to RH.

This theorem is a complete proof proposal, not an independently accepted proof.
A hostile reconstruction must verify every imported endpoint-frame, causal,
port and endpoint-consumer theorem at the frozen commits before promotion.

## 8. Immediate falsifiers

Reject this proposal at the first occurrence of any of the following:

```text
an outer root fiber reaches x>=67;
a rough prime is consumed both by root Hall and a recursive owner;
target, score and rows use different Hall coefficients;
the inner finite residual is approximated rather than retained recursively;
a finite mismatch or collar is charged both current and child;
a common port is allocated independently to two branches;
radix-four feasibility is inferred by subtracting unrelated ordinary bounds;
the safety or top-omission score cost grows with X;
the recursive coefficient mass reaches 1/8;
the native benchmark/continuum score distinction is erased.
```

## 9. Exact status

```text
factor-67 root-state positivity                   DIRECTED EXACT
factor-67 target Hall margin >7/20               DIRECTED EXACT
source-owned target/score/all-row thinning       EXACT
rough first-owner provenance                     EXACT
causal child coefficient mass <1/8               EXACT
factor-67 finite mismatch constants              DIRECTED EXACT
interior and terminal one-use capacity           PROPOSED COMPLETE
one global quantizer/correction/port              FORMAL EXACT
SONTR                                             CANDIDATE COMPLETE
Native-Root Capacity Theorem                     CANDIDATE COMPLETE
Riemann Hypothesis                               UNPROVED PENDING REVIEW
```
