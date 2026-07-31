# T-15106 — Cofinal certified-zero residue capture implies RH

Claim ID: `T-15106`  
Status: **PROVED CONDITIONAL COMPOSITION THEOREM; COFINAL CAPTURE INEQUALITY OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15117`--`L-15119`, `L-15122`, `L-15123`, `T-15104`, and the finite Connes--van Suijlekom real-zero theorem  
Scope: exact phase-aware completion of the smooth-target arithmetic scalar-line program  
Related counterexample candidates: none

## 1. Data at level `j`

Let

\[
 \ell_j\to\infty,
 \qquad
 N_j\to\infty,
 \qquad
 L_j=2\ell_j.
\]

Let `p_j` be the exact CCM coefficient vector of the actual smooth-window
Hermite-radical target from `L-15117`, normalized by

\[
 \eta_j^{\mathsf T}p_j=1,
\]

with every used coordinate nonzero.  Let

\[
 P_j(s)=\sum_i(p_j)_i\phi_{j,i}(s)
\]

be its finite target polynomial.

Let `beta_j^W` be the complete actual arithmetic source from `L-15119`, including
the polar term, the archimedean term, and every prime power through the exact
finite cutoff.

Let `f_j` denote the compactly supported finite transform before boundary
normalization.

## 2. Directed finite gates

Assume that for every sufficiently large `j` one has proof objects establishing
the following.

### A. Actual smooth target

Every coefficient of `p_j` is enclosed by the source-bound smooth interval of
`L-15117`; all phase, cutoff, and normalization adapters are fixed.

### B. Simple real target roots

The polynomial `P_j` has exactly `2N_j` simple real roots

\[
 u_{j,1}<\cdots<u_{j,2N_j}.
 \tag{T-15106.1}
\]

This may be proved by directed canonical Loewner inertia, by a Sturm/Hermite
certificate from directed coefficients, or by another exact real-rootedness
certificate.  A midpoint root list is not sufficient.

### C. Selected certified zeros

There is a finite proof-grade multiset `Z_j` of centered critical-line zeros,
with multiplicities and disjoint directed ordinate balls.  Their exact positive
source contribution is formed by `L-15122` and subtracted from the complete
prime-side source:

\[
 \beta_j^{\rm rem}=\beta_j^W-\beta_j^{Z_j}.
 \tag{T-15106.2}
\]

No sign assumption is made on the remainder.

### D. Complete residue capture

For each target root, directed arithmetic gives

\[
 v_{j,k}
 =\frac{\Omega_j(u_{j,k})}{P_j'(u_{j,k})},
\]

all selected cardinal values, and a residual residue interval

\[
 e_{j,k}^{\rm rem}
 =-\frac{R_{j,\rm rem}(u_{j,k})}{P_j'(u_{j,k})}.
\]

There is one rational scalar `c_j` such that every directed lower endpoint of

\[
 \boxed{
 w_{j,k}(c_j)
 =c_jv_{j,k}
  +\sum_{\gamma\in Z_j}
    A_{\gamma,L_j}
    \mathcal K_{j,k}(r_{\gamma,L_j})
  +e_{j,k}^{\rm rem}}
 \tag{T-15106.3}
\]

is strictly positive.

It is sufficient to verify the conservative interval of `L-15123`; it is not
necessary.  The exact root-threshold test may be used whenever the conservative
capture bound is inconclusive.

## 3. Finite conclusion

By `L-15122`, (T-15106.3) is exactly the complete residue weight of the actual
arithmetic target-pinned matrix.  By `L-15114`, strict positivity of every
weight gives

\[
 \boxed{
 T_{p_j}(c_j)\succeq0,
 \qquad
 \ker T_{p_j}(c_j)=\mathbb Rp_j.}
 \tag{T-15106.4}
\]

The scalar update preserves the finite special divided-difference structure and
parity.  The finite Connes--van Suijlekom theorem therefore implies that every
zero of `f_j` is real.

## 4. Cofinal conclusion

Assume additionally that

\[
 f_j\longrightarrow\Xi
\]

locally uniformly on the open strip

\[
 |\operatorname{Im}z|<\frac12.
\]

The corrected exact Hermite target, smooth localization tail, and finite Fourier
tail supply this convergence once their directed schedules tend to zero.

Every sufficiently large `f_j` is zero free in each nonreal half-strip.  Hurwitz
therefore shows that `Xi` has no nonreal zero in the open centered critical
strip.  Equivalently every nontrivial zero of zeta has real part `1/2`.

Hence

\[
 \boxed{\mathrm{RH}.}
\]

## 5. Compact phase-aware cofinal condition

Choose an injective pairing of the target roots with selected zeros and define
`epsilon_(j,k)`, `C_(j,k)^Z`, and `E_(j,k)` as in `L-15123`.  A sufficient
cofinal condition is

\[
 \boxed{
 \exists c_j\in\mathbb Q:\quad
 \min_k
 \left[
 A_{j,k}(1-\varepsilon_{j,k})
 -C_{j,k}^{Z_j}
 -E_{j,k}
 +c_jv_{j,k}
 \right]>0}
 \tag{T-15106.5}
\]

for every sufficiently large `j`.

The stronger zero-scalar condition

\[
 \boxed{
 \max_k\left(
 \varepsilon_{j,k}
 +\frac{C_{j,k}^{Z_j}+E_{j,k}}{A_{j,k}}
 \right)<1}
 \tag{T-15106.6}
\]

proves the finite gate with `c_j=0`.

An asymptotic package sufficient for (T-15106.6) is

\[
 \boxed{
 \max_k\varepsilon_{j,k}
 +
 \max_k\frac{C_{j,k}^{Z_j}+E_{j,k}}{A_{j,k}}
 \longrightarrow0.}
 \tag{T-15106.7}
\]

This is the finalized phase-aware cofinal statement for the selected-zero
route.  It is dimension aware, invariant under the source gauge, includes the
complete prime-side remainder, and has no canonical-ray normalization choice.

## 6. Relation to the canonical-ray LP

The proof-producing program now has two independent finite consumers:

```text
A. root-free canonical-ray LP
   E_p(a,c) < a m_can;

B. root-explicit selected-zero quadrature
   w_k(c) > 0 for every target root.
```

Consumer B is necessary and sufficient after simple real-rootedness when the
weights are evaluated exactly; its conservative root-capture bound is only
sufficient.  Consumer A is cheaper and may certify a level without root
isolation, but it can fail even when B passes.

A production implementation should therefore run A first and B second, never
interpret failure of A as failure of the arithmetic line, and retain the exact
weights from B as the final finite verdict.

## 7. What the breakthrough changes

The last arithmetic arrow is no longer an opaque comparison between the Weil
source and `-P'/P`.  It is the exact identity

\[
 \boxed{
 \text{arithmetic residue}
 =\text{selected positive zero mass}
  +\text{complete prime-side residual}
  +\text{one scalar boundary direction}.}
\]

Thus the remaining cofinal problem is exactly one weighted cardinal-leakage
inequality.  Known critical-line zeros can be used positively without assuming
anything about the unselected zeros, and the unknown part is carried by one
explicit directed source residual.

## 8. Proof boundary

The theorem does not prove any of the following for the Riemann data:

- cofinal simple real-rootedness of the smooth finite targets;
- a growing root-to-zero pairing;
- the selected-zero cardinal cross bound;
- decay of the complete prime-side residual residue;
- the strict cofinal inequality (T-15106.5).

Those statements are RH bearing.  No finite ladder, ordinary quadrature, or
assumed positive unselected-zero measure may replace them.  This theorem closes
the composition and exposes the exact final arithmetic quantity; it is not an
unconditional proof of RH.