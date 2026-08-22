# L-105203 — Every critical-residue moment is a debt-free quotient-algebra trace

Claim ID: `L-105203`  
Status: **PROPOSED EXACT FINITE-ALGEBRA THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: PR #720 `L-104524`; PR #723 `L-105100`  
RH status: **not assumed**

## 1. Quotient-algebra construction

Let `K` be a characteristic-zero field and let `p in K[z]` be monic of degree
`n>=2`.  Put

\[
q=p'.
\]

Assume `q` is squarefree.  Equivalently,

\[
\gcd(q,q')=\gcd(p',p'')=1.
\]

Hence `p''` is invertible in the finite algebra

\[
\mathcal A=K[z]/(p').
\]

Let `u in K[z]` be the unique polynomial of degree `<n-1` satisfying

\[
\boxed{
p''u\equiv p\pmod{p'}.
}
\tag{L-105203.1}
\]

Let `C` be the matrix of multiplication by `z` on `mathcal A` in any basis,
and put

\[
U=u(C).
\tag{L-105203.2}
\]

## 2. Exact all-moment trace theorem

Over a splitting field, let `c_1,...,c_(n-1)` be the distinct zeros of `p'`
and define

\[
\rho_j={p(c_j)\over p''(c_j)}.
\tag{L-105203.3}
\]

Evaluation at `c_j` in (L-105203.1) gives

\[
u(c_j)=\rho_j.
\]

Because `p'` is squarefree, the Chinese remainder theorem diagonalizes
`mathcal A`:

\[
\mathcal A\otimes\overline K
\cong
\prod_{j=1}^{n-1}\overline K,
\]

and multiplication by `u` has eigenvalues `rho_j`.  Therefore, for every
integer `r>=1`,

\[
\boxed{
\operatorname{Tr}_{\mathcal A/K}(U^r)
=
\sum_{p'(c)=0}
\left({p(c)\over p''(c)}\right)^r.
}
\tag{L-105203.4}
\]

This computes the critical-residue moments without introducing poles at zeros
of `p''`.  The cross-residue term in `L-105100` is a feature of the convenient
rational function `p^2/(p'p'')`, not an intrinsic debt in the second moment.

## 3. First and second moments

For `r=1`, `L-104524` gives

\[
\boxed{
\operatorname{Tr}U
=-{1\over n^2}
\sum_{j=1}^{n}(z_j-\bar z)^2.
}
\tag{L-105203.5}
\]

For `r=2`, combine (L-105203.4) with `L-105100`:

\[
\boxed{
\operatorname{Tr}U^2
=
\mathcal K_4(p)
-
\sum_{p''(d)=0}
{p(d)^2\over p'(d)p'''(d)}.
}
\tag{L-105203.6}
\]

Equation (L-105203.6) is an equality between two exact coordinates:

```text
left:   one finite quotient-algebra trace with no auxiliary poles;
right:  explicit centred root V2/V4 ledger minus the second-level residue debt.
```

## 4. Exact coherence as spectral flatness

Assume now that `K` is a subfield of `R`, that `p` has real coefficients, and
that every zero of `p'` is real and simple.  Then every `rho_j` is real.  Put

\[
R=n-1,
\qquad
\bar\rho={\operatorname{Tr}U\over R}.
\]

The root-evaluation isomorphism identifies `U` with the real diagonal matrix
`diag(rho_1,...,rho_R)`.  Consequently

\[
\boxed{
\operatorname{Tr}(U-\bar\rho I)^2
=
\operatorname{Tr}U^2-{(\operatorname{Tr}U)^2\over R}
=
\sum_{j=1}^{R}(\rho_j-\bar\rho)^2
\ge0.
}
\tag{L-105203.7}
\]

If `Tr U<0`, the residue coherence of `L-104522` is exactly

\[
\boxed{
\mathfrak C
={ (\operatorname{Tr}U)^2\over R\operatorname{Tr}U^2}
=1-
{\operatorname{Tr}(U-\bar\rho I)^2\over\operatorname{Tr}U^2}.
}
\tag{L-105203.8}
\]

Thus the Xi input `RCMV104530` is a concrete spectral-flatness statement for
one multiplication operator in the critical-point quotient algebra.

## 5. Algorithmic form

The theorem is root-free computationally:

1. compute the extended-Euclidean inverse of `p'' mod p'`;
2. form `u=(p''^(-1)p) mod p'`;
3. form the companion multiplication matrix `C` of `K[z]/(p')`;
4. evaluate `Tr(u(C)^r)`.

For rational `p`, every step is exact rational arithmetic.  No numerical root
finding and no assignment of critical points is required.

## 6. Scope

The trace representation supplies an exact finite coordinate, not an automatic
bound.  Positivity of `Tr(U-bar(rho)I)^2` only restates the variance when the
critical points are real.  Analytic progress requires proving that this
variance is small relative to `Tr U^2`; `L-105202` does so unconditionally on
the natural high-derivative Xi tail.
