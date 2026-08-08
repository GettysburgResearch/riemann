# L-28402 — Finite-cutoff Euler boundary-jet ledger

Claim ID: `L-28402`  
Title: Every difference between the finite central cascade and its strictly contracting analytic bulk is an explicit endpoint-jet ledger with a geometrically damped Euler remainder  
Status: **PROPOSED COMPLETE REDUCTION — BOUNDARY CONTRACTION NOT CLAIMED HERE**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #284  
Dependencies: `L-28401`; finite Euler transformation; PR #262 Peano finite-difference interface  
Scope: exact reduction of DCCS to finite boundary jets

## 1. Finite and infinite operators

Let `f` be a smooth function on `(0,infinity)` and let

\[
f^{[N]}(n)=f(n)\mathbf1_{n\le N}
\]

on the positive integers. Define

\[
(\mathscr C_N f^{[N]})(q)
=\sum_{k\ge1}
\left[
 f^{[N]}(2kq-1)-f^{[N]}((2k+1)q)
\right].
\tag{L-28402.1}

This is exactly the central residual operator used in PR #280. Let `mathscr C` be the infinite analytic operator of `L-28401`.

Then

\[
\boxed{
\mathscr C_N f^{[N]}
=(\mathscr C f)|_{q\le N/2}
-\mathscr Q_Nf,
}
\tag{L-28402.2}

where the cutoff tail is the explicit finite-at-each-`q` expression

\[
\begin{aligned}
(\mathscr Q_Nf)(q)
={}&
\sum_{2kq-1>N}f(2kq-1)\\
&-
\sum_{(2k+1)q>N}f((2k+1)q).
\end{aligned}
\tag{L-28402.3}

Equation (L-28402.2) is an equality of conditionally paired series, initially with an Abel factor and then by passage to the paired limit. No asymptotic estimate has entered.

## 2. Exact finite Euler transformation

For a sequence `a_0,a_1,...` and integer `M>=1`, write

\[
\Delta a_j=a_j-a_{j+1}.
\]

For every starting index `K`, the alternating tail has the exact identity

\[
\boxed{
\sum_{j\ge K}(-1)^{j-K}a_j
=
\sum_{m=0}^{M-1}2^{-m-1}\Delta^ma_K
+2^{-M}
\sum_{j\ge K}(-1)^{j-K}\Delta^Ma_j.
}
\tag{L-28402.4
}

The equality is finite when the source has finite support and follows by repeated pairing in the Abel-regularized case.

Apply (L-28402.4) separately to the first omitted even/odd multiple in (L-28402.3), after first using the exact shifted Taylor expansion from `L-28401` on the `2kq-1` leg. For every fixed `M`, this gives

\[
\boxed{
\mathscr Q_Nf
=
\mathscr J_{N,M}f
+2^{-M}\mathscr R_{N,M}f.
}
\tag{L-28402.5}

Here:

- `mathscr J_(N,M)f` is a finite list of values
  \[
  \Delta_k^m f(kq+a),
  \qquad 0\le m<M,
  \quad a\in\{-1,0\},
  \]
  at the first omitted quotient index determined by `floor(N/q)`;
- `mathscr R_(N,M)f` is the same paired operator applied to the `M`th finite differences;
- every term carries its exact quotient, parity, shift, and endpoint convention.

Thus no unspecified `O(boundary)` term is present.

## 3. Positive Peano representation

For a smooth one-variable function,

\[
\Delta_h^mf(x)
=(-1)^m
\int_{[0,h]^m}
f^{(m)}(x+t_1+\cdots+t_m)
\,dt_1\cdots dt_m.
\tag{L-28402.6}

Equivalently, every finite difference is an integral against the nonnegative cardinal B-spline of order `m`. Therefore each jet in `mathscr J_(N,M)` has a proof-facing positive Peano kernel once the sign of the corresponding derivative is retained.

This is the valid one-variable B-spline interface. It does not assert positivity of a two-variable Hankel kernel and is unaffected by the `-233/64` refutation of the former conditional-Hankel route.

## 4. Strictly lower scale

The first omitted multiple in every tail satisfies

\[
kq>N/2.
\]

After one central step, every output coordinate obeys

\[
q\le\frac{N+1}{2}.
\]

Consequently all jet destinations are attached to the next formal endpoint

\[
N^+=\left\lfloor\frac{N+1}{2}\right\rfloor.
\tag{L-28402.7}

The finite cutoff ledger is therefore a strict half-scale boundary state. It is not a same-scale packet or a growing face dictionary.

## 5. Canonical boundary state

For fixed Euler order `M`, define the boundary state `b_(N,M)(f)` to consist of:

```text
all first-omitted quotient indices;
parity of each omitted leg;
all shifted/unshifted jets of orders 0,...,M-1;
all endpoint atoms created by zero extension;
the Mth-difference Euler remainder;
```

with repetitions at the same arithmetic destination recombined before any norm.

Iteration of (L-28402.2)--(L-28402.5) gives the exact noncommutative Duhamel expansion

\[
\boxed{
\mathscr C_N^Jf^{[N]}
=
\mathscr C^Jf
+
\sum_{a=0}^{J-1}
\mathscr C_{N_{a+1}}^{J-1-a}
\left[-\mathscr J_{N_a,M}
-2^{-M}\mathscr R_{N_a,M}ight]
\mathscr C^af,
}
\tag{L-28402.8}

where `N_(a+1)=floor((N_a+1)/2)` and every operator is restricted to its declared finite support.

Equation (L-28402.8) separates the cascade into:

```text
analytic bulk, contracted by 6/7;
finite source-bound boundary jets;
geometrically damped Mth Euler remainder.
```

## 6. Initial critical-source bounds

For

\[
f_X(x)=x^{-1/2}\log(X/x),
\]

every ordinary derivative is an explicit power-log function. In particular,

\[
|f_X^{(m)}(x)|
\le C_mx^{-m-1/2}
[1+\log(X/x)].
\tag{L-28402.9}

Therefore the complete first-generation jet ledger satisfies, in the capacity-weighted variation used by PR #280,

\[
\boxed{
\|b_{X,M}(f_X)\|_{\rm cap}
\le C_M(1+\log X)^{A_M}.
}
\tag{L-28402.10}

The proof is the divisor switch

\[
\sum_{q}\sqrt q
\sum_{2q\mid n+a}n^{-3/2}
\ll
\sum_n\frac{\tau(n+a)}n,
\]

followed by the elementary average divisor bound. No prime estimate or Möbius estimate is used.

## 7. Exact remaining theorem

The first-generation estimate is not enough by itself; the boundary jets must remain stable after they are propagated through later finite cascades.

The required theorem is the **Renormalized Boundary-Jet Contraction** `RBJC(M)` in `T-28401`:

\[
\mathcal J_{a+1}
\le\theta_M\mathcal J_a
+C_M(1+a)^{A_M}(1+\log X)^{A_M},
\qquad\theta_M<1.
\]

Unlike DCCS, `RBJC(M)` is a finite source-state theorem after the analytic bulk has already been removed. Unlike the old two-contact and Brion proposals, it never counts arithmetic source coordinates.

## 8. Proof boundary

Closed here:

1. the exact finite/infinite operator separation;
2. the exact `M`th Euler boundary expansion;
3. the positive one-variable Peano representation;
4. strict half-scale routing of every boundary jet;
5. the exact Duhamel expansion;
6. the polylogarithmic first-generation critical-source ledger.

Open:

1. uniform all-generation `RBJC(M)`;
2. DCCS;
3. RH.
