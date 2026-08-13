# L-91409 — Weighted paired-source dilation charges the child coefficient exactly once

Claim ID: `L-91409`  
Status: **PROVED EXACT ROW INTERTWINING; FINITE PACKET NORMALIZATION OPEN**  
Created: 2026-08-13  
Depends on: the paired source of `L-91333/L-91404` and normalized component profiles of `L-91341`  
Supersedes: `L-91408` via `R-91405`  
RH status: **unproved**

## 1. Weighted source atom

For channel parameter `a>=1`, source index `k`, and endpoint `X`, put

\[
 w_a(X,k)=k^{-1/2}(a\sqrt{X/k}-1).
\]

The component-row density per unit source mass is

\[
 \rho_a(Z;j)=\frac{Q_Z(j)}{a\sqrt Z-1}.
\]

Their product is the literal row atom:

\[
 w_a(X,k)\rho_a(X/k;j)=k^{-1/2}Q_{X/k}(j).
 \tag{L-91409.1}
\]

## 2. Exact multiplicative covariance

Let `m>=1`, `Y=X/m`, and `c=m^-1/2`. Then

\[
 w_a(X,mk)=c\,w_a(Y,k)
 \tag{L-91409.2}
\]

and

\[
 \rho_a(X/(mk);j)=\rho_a(Y/k;j).
 \tag{L-91409.3}
\]

Hence a weighted child packet pushed from source `k` to source `mk` satisfies

\[
 \boxed{R_X(cD_mP_Y)=cR_Y(P_Y)}.
 \tag{L-91409.4}
\]

The component-row coordinate `j` is unchanged. The explicit coefficient `c` is
the only scale factor.

The same identity holds after parity swaps, balanced/reserve direct sums, and
fixed linear target or score observations.

## 3. Physical packing assembly

Ordinary and radix-four response maps are linear in the row vector. Therefore a
feasible child packing `d_Y` is inserted into the parent as

\[
 \boxed{d_Y\mapsto c\,d_Y}.
 \tag{L-91409.5}
\]

No affine map of row indices is used.

For an exact source-disjoint identity

\[
 P_X=F_X+\sum_b c_bD_{m_b}P_b,
 \qquad c_b=m_b^{-1/2},
 \qquad Y_b=X/m_b,
\]
we obtain exact target, score, and row identities with the same coefficients.
If `d_F` and `d_b` are feasible for their packets, then

\[
 d_X=d_F+\sum_bc_bd_b
 \tag{L-91409.6}
\]

is feasible for the parent.

For packet deficit `Delta`, positive homogeneity gives

\[
 \boxed{
 \Delta_X(P_X)
 \le \Delta_X(F_X)+\sum_bc_b\Delta_{Y_b}(P_b).
 }
 \tag{L-91409.7}
\]

## 4. Application and boundary

Each rough child in `L-91404` has `m_b=dp`, `c_b=(dp)^-1/2`, and endpoint
`X/(dp)`, so the recursive child-row assembly uses (L-91409.5), not the refuted
affine Pascal lift.

The complete finite forcing realization, a bounded packet mass, and the root
endpoint implication remain separate load-bearing interfaces.

```text
weighted source covariance                 EXACT
single child coefficient                   EXACT
identity on component-row coordinates      EXACT
scaled child physical assembly             EXACT
finite forcing realization/debt            REPLAY REQUIRED
bounded packet mass                        OPEN / R-91404
root endpoint implication                  REPLAY REQUIRED
Riemann Hypothesis                         UNPROVEN
```
