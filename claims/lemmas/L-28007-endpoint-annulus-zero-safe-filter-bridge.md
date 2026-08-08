# L-28007 — Zero-safe filter bridge from the complete endpoint scalar to the binary–ternary prime annulus

Claim ID: `L-28007`  
Title: The complete endpoint discrepancy and the top-six pole-preserving commutator differ by one explicit zero-safe finite filter and one holomorphic benchmark gauge  
Status: **PROPOSED COMPLETE EXACT MELLIN ADAPTER PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: PR #291 `L-27906`; `L-28006/T-28002`

## 1. Complete endpoint transform

Let

\[
\mathcal A_\Lambda(X)
=
\sum_{m=2}^{X}
2\sqrt m(1-\sqrt{m/X})\log\frac m{m-1}
-\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
\]

be the complete endpoint scalar of PR #291.  Put

\[
s=z+\frac12
\]

and

\[
\Phi(z)
=\sum_{m\ge2}\log\frac m{m-1}\,m^{1/2-z}.
\]

`L-27906` proves initially for `Re z>1/2`, and then meromorphically in the
right half-plane,

\[
\boxed{
\widehat{\mathcal A}_\Lambda(z)
:=\int_1^\infty\mathcal A_\Lambda(X)X^{-z-1}dX
=
\frac{\Phi(z)}{zs}
+rac1z\frac{\zeta'}{\zeta}(s).}
\tag{L-28007.1}
\]

The apparent pole at `s=1` cancels between the two terms.

## 2. Prime-annulus transform

Retain

\[
E_{2,3}(s)=(1-2^{-s})(1-3^{-s-1})
\]

and

\[
R(s)=\frac{s-1}{s(s+1)}.
\]

The top-six binary–ternary commutator of `L-28006` has transform

\[
\boxed{
\widehat P_{2,3}(z)
=-E_{2,3}(s)R(s)\frac{\zeta'}{\zeta}(s)
-E_{2,3}(s)R'(s).}
\tag{L-28007.2}
\]

## 3. Exact filter identity

Define

\[
\boxed{
M_{2,3}(z)
=-zE_{2,3}(s)R(s).}
\tag{L-28007.3}
\]

Then direct substitution of (L-28007.1) into (L-28007.2) gives

\[
\boxed{
\widehat P_{2,3}(z)
=M_{2,3}(z)\widehat{\mathcal A}_\Lambda(z)
+G_{2,3}(z),}
\tag{L-28007.4}
\]

where the benchmark gauge is

\[
\boxed{
G_{2,3}(z)
=E_{2,3}(s)
\left[
\frac{R(s)}s\Phi(z)-R'(s)
\right].}
\tag{L-28007.5}
\]

No prime or zero term occurs in `G_(2,3)` beyond the elementary `zeta(s)`
contained in the continuation of `Phi`.

## 4. The gauge is holomorphic in the full right half-plane

The function `Phi` has the decomposition

\[
\Phi(z)=\zeta(s)-1+R_0(z),
\]

where `R_0` is holomorphic for `Re z>-1/2`.  Its only right-half-plane
singularity is the zeta pole at `s=1`.

But `R(s)` has the simple zero `s-1`.  Hence the product `R(s)Phi(z)` is
regular at `s=1`.  The remaining denominators of (L-28007.5) lie at
`s=0,-1`, outside `Re z>0`.  Therefore

\[
\boxed{G_{2,3}\text{ is holomorphic for }\Re z>0.}
\tag{L-28007.6}
\]

On every closed vertical substrip of that half-plane it has at most polynomial
growth, by the absolutely convergent representation of `R_0` and standard
bounds for `zeta` away from its pole.

Thus the gauge creates no off-line pole and has zero rightmost exponential
source exponent.

## 5. Exact physical filter

Writing `a=log2` and `b=log3`, equation (L-28007.3) is

\[
\boxed{
M_{2,3}(z)
=-
\frac{z(z-1/2)}{(z+1/2)(z+3/2)}
(1-2^{-1/2}e^{-az})
(1-3^{-3/2}e^{-bz}).}
\tag{L-28007.7}

Hence the endpoint-to-annulus map consists only of:

```text
one derivative;
one stable exponential resolvent at rates 1/2 and 3/2;
one zero-safe dyadic difference;
one zero-safe ternary difference;
one centered zero at z=1/2 removing the zeta pole model.
```

There is no infinite arithmetic inverse.

## 6. No off-line pole is lost

Let `rho` be a nontrivial zeta zero with

\[
\frac12<\Re\rho<1
\]

and put `z_rho=rho-1/2`.  Then

\[
z_\rho\ne0,
\qquad z_\rho\ne\frac12,
\]

and neither Euler factor in (L-28007.7) vanishes.  Thus

\[
M_{2,3}(z_\rho)\ne0.
\tag{L-28007.8}
\]

If the multiplicity is `m_rho`, the endpoint transform has residue

\[
\frac{m_\rho}{z_\rho}.
\]

Multiplication by `M_(2,3)` gives

\[
\boxed{
M_{2,3}(z_\rho)\frac{m_\rho}{z_\rho}
=-m_\rho E_{2,3}(\rho)R(\rho),}
\tag{L-28007.9}
\]

exactly the prime-annulus residue of `L-28006`.  The holomorphic gauge cannot
alter it.

Therefore the complete endpoint scalar and the top-six commutator have exactly
the same pole multiset in

\[
0<\Re z<\frac12.
\]

## 7. Unified pole frontier

For every `delta in (0,1/2)`, equations (L-28007.4)--(L-28007.9) give

\[
\boxed{
\widehat{\mathcal A}_\Lambda
\text{ is holomorphic on }\Re z>\delta
\iff
\widehat P_{2,3}
\text{ is holomorphic there}.}
\tag{L-28007.10}
\]

Equivalently, their rightmost nontrivial singularity exponents coincide.

Thus the following live frontiers are exact coordinate systems for one pole
family:

```text
CEP / complete endpoint stability on PR #291;
EPD after the deterministic prime-square reserve;
BT-PAE / top-six annulus energy on this branch;
the compact critical-source energy of L-28004;
the WSTS shell scalar on PR #276.
```

The identity does not make any one of their required estimates automatic.  It
prevents them from being counted as independent evidence and gives an exact
adapter for any proof built in one coordinate.

## 8. Review consequence

The physical programme may work with the compact annulus source, while the
endpoint programme may work with the elementary benchmark-minus-prime scalar.
A claimed completion must replay (L-28007.4) and show that its estimate survives
the finite filter and the gauge at the exact quantitative scope used.

In particular:

- a proof of CEP gives the annulus criterion after applying the explicit filter;
- a proof of BT-PAE excludes the same poles directly;
- the prime-square reserve then transfers a sufficiently strong complete
  endpoint estimate to ordinary-prime EPD and zero WSTS debt.

## 9. Proof boundary

Closed exactly, subject to review:

1. the Mellin filter identity;
2. holomorphy of the benchmark gauge;
3. the finite physical filter formula;
4. equality of every off-line pole and residue after filtering;
5. equality of the rightmost pole frontiers.

Open:

1. CEP;
2. BT-PAE;
3. the compact-source energy theorem;
4. RH.
