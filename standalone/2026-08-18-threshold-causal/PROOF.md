# Threshold-Flexible Causality for the Factor-67 Annular Scalar

**Scientific status:** unconditional source theorems and no-go theorem; the
critical-saddle producer and the Riemann Hypothesis remain unproved.

## 1. Native root

Let `b(X)=F_61(X)` be the complete grouped finite-`P_61` annular `5:3`
scalar. Unique factorization gives

\[
\mathcal A_X
=\sum_{m\in\mathcal R_{67}^{sf}}
 \mu(m)m^{-1/2}b(X/m).
\]

For `m=p_1...p_t`, the unique ordered history has magnitude `m^-1/2`,
activation `X/m`, and parity `(-1)^t`. At `X=184`, the six rough primes
`67,71,73,79,83,89` contribute more than `1.36314`, so the root is not the
finite `P_61` base.

## 2. Exact threshold ledger

At every raw prime edge `r=p^-1/2`, a threshold `0<=a<=r` has the positive
one-use split

\[
rSP=(r-a)SP\oplus aSP.
\]

Thus every native coefficient is retained exactly once. If two `r^2` copies
have already been charged, the compulsory residual is

\[
r-2r^2>0.
\]

For the complete raw operator `R`, threshold operator `A`, local base `b`, and
native scalar `F`,

\[
F+RF=b,
\qquad
F+AF=g,
\qquad
\boxed{g=b-(R-A)F}.
\]

Raw exposure is conserved: `(r-a)F_child+aF_child=rF_child`. The minimal
two-node fixture has exact current `a-r<0`, so no universal local one-channel
positivity theorem can perform a strict contraction.

## 3. Odd history

At

```text
X=67*71*13,
history=(67),
terminal=(71,13),
```

an exact 239-atom dyadic calculation gives `E_T-O_T>17`. The incoming parity is
odd, so canonical leafwise Hall would require the impossible reverse target
inequality. The exact ledger preserves this obstruction rather than erasing it.

## 4. Subcritical-depth no-go

For even `L`, define the exact current

\[
C_L(X)=\sum_{\omega(m)<L}\mu(m)m^{-1/2}b(X/m).
\]

The sharp annular theorem gives `b(Y)=a sqrt(Y)+O(1)` with `a>0`. Put
`k=L-1`, `W=X^(1/(2k))`, and `z_U=sum_(67<=p<=U)1/p`. The last odd layer
restricted to primes at most `W` is bounded below by

\[
c\sqrt X\,{z_W^k\over k!}
\left(1-O(k^2/z_W^2)\right),
\]

whereas all previous positive layers are bounded above by

\[
C\sqrt X\,(1+o(1)){z_X^{k-1}\over(k-1)!}.
\]

Mertens' theorem gives `z_W=z_X-log(2k)+o(1)`. Hence, whenever

\[
L\log L=o(\log\log X),
\]

the last-to-previous ratio tends to infinity and `C_L(X)<0` eventually.
Directed finite checks give

```text
C_2(32605)>0>C_2(32606),
C_2(61841)<-21.3,
native scalar at 61841 >9.5.
```

## 5. Refutation of LAPBR67

The adaptive schedule of PR #578 has `L=O(log log log X)` and decomposes
`C_L=S_L+L_L`, with the small-prime cube `S_L>0`. The no-go theorem gives
`C_L<0`, so

\[
\boxed{L_L<0}
\]

eventually. Thus `LAPBR67` is false.

## 6. Surviving positive sector

Fix `theta>e^-1`. If the least rough prime satisfies `p_0>=Y^theta`, an active
product contains at most two primes. Since `b>=0`,

\[
\mathcal F_{p_0}(Y)
\ge b(Y)-\sum_{Y^\theta\le p\le Y/2}p^{-1/2}b(Y/p).
\]

The right side is

\[
a\sqrt Y\left(1-\log(1/\theta)+o(1)\right)>0.
\]

Hence this genuinely high-prime sector is positive.

## 7. Sharp remaining producer

The stopping line must enter the rough harmonic saddle
`k~log log X`. Let

\[
T_k(X)=\sum_{\omega(m)=k}m^{-1/2}b(X/m),
\qquad
\mathcal A_X=\sum_k(-1)^kT_k(X).
\]

`CSHT67` asks for one source-complete flow from odd-depth occurrences to
even-depth occurrences in this critical window, preserving coefficient,
activation, owner, parity, target and scalar coordinates. A local margin,
contracted mass bound, or depth count is not enough.

`CSHT67` would give eventual scalar positivity and then the exact `5:3`
Mellin-Landau consumer would imply RH. `CSHT67` is open.

```text
native owner ledger                       PROVED
r-2r^2 and (R-A)F residual               PROVED
root normalization                        PROVED
subcritical threshold method              REFUTED
LAPBR67                                   REFUTED
high-least-prime sector                   PROVED
CSHT67                                    OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVED
```
