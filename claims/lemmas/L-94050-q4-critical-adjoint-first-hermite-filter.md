# L-94050 — The scale-four critical adjoint square gives a phase-locked First-Hermite hierarchy

Claim ID: `L-94050`  
Status: **PROPOSED COMPLETE EXACT ANALYTIC DICTIONARY — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: PR #379 at its exact first-Hermite normalization; PR #474 `L-93019` for comparison only  
Scope: exact filtered zero scalar and prime kernel; no global positivity conclusion in this lemma

## 1. Critical scale-four factor

Put

\[
L=\log4,
\qquad
P(u)=5-4\cos(Lu).
\tag{L-94050.1}
\]

The exact factorization is

\[
\boxed{
P(u)=(2-e^{iLu})(2-e^{-iLu}).
}
\tag{L-94050.2}
\]

For real \(u\),

\[
1\le P(u)\le9.
\tag{L-94050.3}
\]

For a vertical displacement \(u=iy\),

\[
P(iy)=5-4\cosh(Ly).
\tag{L-94050.4}
\]

Since

\[
\cosh(L/2)=\cosh(\log2)={5\over4},
\]

one has

\[
\boxed{
P(iy)>0\quad(0\le |y|<1/2),
\qquad
P(\pm i/2)=0.
}
\tag{L-94050.5}
\]

If \(z=(s-1/2)/i\), then

\[
\boxed{
P(z)=4(1-4^{s-1})(1-4^{-s}).
}
\tag{L-94050.6}
\]

Thus the factor is the product of the Q4 zero-safe scale factor and its critical
adjoint. Its only horizontal boundary zeros occur at \(\Re s=0\) and
\(\Re s=1\); it is nonzero at every nontrivial open-strip zeta zero.

## 2. Filtered first-Hermite scalar

Let \(Z\) be the centered zeta-zero multiset used in PR #379. For an integer
\(m\ge0\), define

\[
\boxed{
\mathcal M_m(q,x)
 =\sum_{z\in Z}m_z(z-x)^2e^{-q(z-x)^2}P(z-x)^{2m}.
}
\tag{L-94050.7}
\]

For \(m=0\), this is the resident first-Hermite scalar.

Every real zero contributes a nonnegative summand because

\[
(z-x)^2e^{-q(z-x)^2}P(z-x)^{2m}\ge0
\qquad(z,x\in\mathbb R).
\tag{L-94050.8}
\]

At a matched off-line pair \(t\pm iy\), \(0<y<1/2\), the two-point
contribution at \(x=t\) is

\[
\boxed{
-2y^2e^{qy^2}P(iy)^{2m}<0.
}
\tag{L-94050.9}
\]

The filter therefore preserves the terminal negative sign and every open-strip
depth.

## 3. Exact prime-kernel operator

Retain the resident first-Hermite kernel

\[
h_q(u)=\left(1-{u^2\over2q}\right)e^{-u^2/(4q)}.
\tag{L-94050.10}
\]

For translations

\[
(T_a f)(u)=f(u-a),
\]

define

\[
\boxed{
D_L=5I-2T_L-2T_{-L}.
}
\tag{L-94050.11}
\]

Multiplication by \(P(v)^{2m}\) in the spectral variable is exactly the
finite-shift operator \(D_L^{2m}\) in the prime-log variable. Consequently the
Guinand–Weil prime polynomial is

\[
\boxed{
S_m(q,x)
 =\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
   (D_L^{2m}h_q)(\log n)n^{ix}.
}
\tag{L-94050.12}
\]

In the exact PR #379 normalization,

\[
\mathcal M_m(q,x)
 =\operatorname{pole}_m(q,x)
  +\operatorname{gamma}_m(q,x)
  -{1\over2\sqrt\pi q^{3/2}}\Re S_m(q,x).
\tag{L-94050.13}
\]

This follows by linearity from the original explicit formula; no new contour
normalization is introduced.

## 4. Critical saddle factorization

Set

\[
H_q(u)=e^{u/2}h_q(u).
\tag{L-94050.14}
\]

Conjugating one scale-four operator by the critical weight gives exactly

\[
\boxed{
 e^{u/2}D_Lh_q(u)
 =[(I-T_L)(4I-T_{-L})H_q](u).
}
\tag{L-94050.15}
\]

Indeed,

\[
 e^{u/2}D_Lh_q(u)
 =5H_q(u)-4H_q(u-L)-H_q(u+L).
\]

Thus every application contains one genuine backward finite difference of the
critical prime saddle. Iterating,

\[
\boxed{
 e^{u/2}D_L^{2m}h_q(u)
 =[(I-T_L)^{2m}(4I-T_{-L})^{2m}H_q](u).
}
\tag{L-94050.16}
\]

The factor \((I-T_L)^{2m}\) is the source of the unconditional saddle gain in
the successor theorem.

## 5. Relation to the compact-Q4 source

PR #474 `L-93019` writes the compact-Q4 Dirichlet source as the logarithmic
derivative of the scale-four zero-safe source. Equation (L-94050.6) shows that
the present heat filter is its critical adjoint square:

```text
Q4 source factor:               1-4^(1-s)
critical adjoint factor:         1-4^(-s)
phase-locked Hermite multiplier: product, up to a nonzero monomial
```

This is an exact source-level bridge, not a similarity of notation.

## 6. Proof boundary

Established:

1. critical factorization and boundary zeros;
2. positivity on the real zero line;
3. strict matched-pair negativity for every depth below `1/2`;
4. exact finite-shift prime kernel;
5. exact critical-saddle factorization;
6. exact Q4/First-Hermite source connection.

Open here:

1. a pointwise bound for the signed polynomial beyond the theorem below;
2. global filtered positivity;
3. RH.
