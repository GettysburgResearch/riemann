# L-102960 — The selector-tied owner Gram has an exact transpose signature

Claim ID: `L-102960`  
Status: **PROVED EXACT HILBERT SIGNATURE NORMAL FORM**  
Created: 2026-08-25  
Depends on: PR #751 `T-106081.8--T-106081.10`  
RH status: **not assumed**

Retain one clean minimum-owner Boolean block and the selector-tied fields

\[
\mathcal A_{\ell\to\rho;k},
\qquad
\ell\ne\rho,
\qquad
1\le k<\rho,
\]

of `T-106081`. Its clean physical cross-owner Gram is

\[
\mathcal G
=
\sum_{\ell\ne\rho}{1\over\ell\rho}
\sum_{h=1}^{\ell-1}
\sum_{k=1}^{\rho-1}
\left\langle
\mathcal A_{\ell\to\rho;k},
\mathcal A_{\rho\to\ell;h}
\right\rangle.
\tag{L-102960.1}
\]

## 1. Canonically normalized phase array

Define

\[
s_{\ell,\rho}
=
\left[
{\rho-1\over\ell\rho(\ell-1)}
\right]^{1/2}
\]

and form the array

\[
F_{\ell,\rho,h,k}
=
s_{\ell,\rho}
\mathcal A_{\ell\to\rho;k}.
\tag{L-102960.2}
\]

The entry is independent of \(h\), but the \(h\)-coordinate is retained as a genuine phase-cardinality coordinate.

Let \(\mathsf T\) be the unitary involution

\[
(\mathsf TF)_{\ell,\rho,h,k}
=
F_{\rho,\ell,k,h}.
\tag{L-102960.3}
\]

Since

\[
s_{\ell,\rho}s_{\rho,\ell}
={1\over\ell\rho},
\]

one has the exact identity

\[
\boxed{
\mathcal G=\langle F,\mathsf TF\rangle.
}
\tag{L-102960.4}
\]

Moreover,

\[
\boxed{
\|F\|^2
=
\sum_{\ell\ne\rho}
{\rho-1\over\ell\rho}
\sum_{k=1}^{\rho-1}
\|\mathcal A_{\ell\to\rho;k}\|^2
=
\mathfrak P,
}
\tag{L-102960.5}
\]

where \(\mathfrak P\) is exactly the positive Cauchy majorant of `T-106081.10`.

## 2. Symmetric and antisymmetric owner currents

Put

\[
F_+=\frac12(I+\mathsf T)F,
\qquad
F_-=\frac12(I-\mathsf T)F.
\]

Because \(\mathsf T\) is a self-adjoint involution,

\[
\boxed{
\mathfrak P
=
\|F_+\|^2+\|F_-\|^2,
}
\tag{L-102960.6}
\]

and

\[
\boxed{
\mathcal G
=
\|F_+\|^2-\|F_-\|^2.
}
\tag{L-102960.7}
\]

Consequently

\[
\boxed{
(\mathcal G)_-
\le
\|F_-\|^2,
}
\tag{L-102960.8}
\]

and, more sharply,

\[
(\mathcal G)_-
=
\left(
\|F_-\|^2-\|F_+\|^2
\right)_+.
\tag{L-102960.9}
\]

## 3. Research consequence

The positive-moment criterion `MOBOSM106081`, which asks for

\[
\mathfrak P=X^{o(1)},
\]

is a sufficient but generally overstrong route. The one-sided physical obstruction lies only in the antisymmetric owner-incidence current.

Define

```text
OICURL102960:
  the carrier-recombined antisymmetric transpose current F_- has subpower
  energy on every Boolean minimum-owner block, after the frozen renewals and
  incidence masks.
```

Then `OICURL102960` controls the adverse part of the clean owner Gram without requiring the favorable symmetric current to be small.

## Scope

This theorem is an exact normal form, not a bound for \(F_-\). A source-blind family of unrelated owner fields may have large antisymmetric energy. Any proof of `OICURL102960` must use the literal Boolean coefficients, minimum-owner filtration, or an equivalent arithmetic transport.