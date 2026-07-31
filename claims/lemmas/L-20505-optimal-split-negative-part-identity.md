# L-20505 — The optimized conditional split exactly recovers the negative part

Claim ID: `L-20505`  
Title: With exact residual endpoints and the empty selected block allowed, the best frame–residual lower bound has exactly the same negative part as the fully corrected kernel  
Status: `PROVED FINITE SCOPE CLASSIFICATION`  
Authoring agent: `gpt56-03-q`  
Created: 2026-08-01  
Dependencies: elementary min--max/Weyl inequality; `L-20504`  
Scope: logical strength of the optimized scalar in `T-20501`  
Related counterexample candidates: none

## 1. Abstract split

Let \(S=S^*\) be a finite Hermitian operator on a Hilbert space with metric
\(G\succ0\). Let \(\mathcal P\) be any family of positive semidefinite operators
\(P\succeq0\) containing

\[
0\in\mathcal P.
\tag{L-20505.1}
\]

In the zeta application, \(S\) is the fully Schur-corrected kernel and \(P\) is
a finite selected simple-line-zero Gram.

For \(P\in\mathcal P\), put

\[
R_P=S-P.
\tag{L-20505.2}
\]

Define the exact generalized endpoints

\[
\sigma(P)
=
\lambda_{\min}(P,G)
\ge0,
\tag{L-20505.3}
\]

and

\[
\nu(P)
=
\bigl(-\lambda_{\min}(R_P,G)\bigr)_+.
\tag{L-20505.4}
\]

The exact selected-plus-joint-residual lower bound is

\[
\boxed{
b(P)=\sigma(P)-\nu(P).
}
\tag{L-20505.5}
\]

Let

\[
\boxed{
\mathfrak J(S;\mathcal P)
=
\sup_{P\in\mathcal P}b(P).
}
\tag{L-20505.6}
\]

## 2. Every split bound lies below the exact floor

Write

\[
r(P)=\lambda_{\min}(R_P,G).
\]

Weyl's lower-eigenvalue inequality gives

\[
\lambda_{\min}(S,G)
\ge
\sigma(P)+r(P).
\tag{L-20505.7}
\]

If \(r(P)\le0\), then

\[
b(P)=\sigma(P)+r(P)
\le\lambda_{\min}(S,G).
\]

If \(r(P)>0\), then

\[
b(P)=\sigma(P)
<\sigma(P)+r(P)
\le\lambda_{\min}(S,G).
\]

Therefore

\[
\boxed{
b(P)\le\lambda_{\min}(S,G)
\quad\text{for every }P\in\mathcal P.
}
\tag{L-20505.8}
\]

## 3. The negative case is attained by the empty frame

For \(P=0\),

\[
\sigma(0)=0,
\qquad
R_0=S.
\]

If

\[
\lambda_{\min}(S,G)<0,
\]

then

\[
\nu(0)=-\lambda_{\min}(S,G)
\]

and hence

\[
\boxed{
b(0)=\lambda_{\min}(S,G).}
\tag{L-20505.9}
\]

Together with (L-20505.8), this proves

\[
\boxed{
\mathfrak J(S;\mathcal P)
=
\lambda_{\min}(S,G)
\quad\text{whenever }\lambda_{\min}(S,G)<0.
}
\tag{L-20505.10}
\]

## 4. The nonnegative case

If

\[
\lambda_{\min}(S,G)\ge0,
\]

then the empty frame gives

\[
b(0)=0.
\]

Therefore

\[
\boxed{
0\le\mathfrak J(S;\mathcal P)
\le\lambda_{\min}(S,G).
}
\tag{L-20505.11}
\]

No completeness property of the positive family \(\mathcal P\) is needed for
the sign conclusion.

## 5. Exact negative-part identity

Combining the two cases gives

\[
\boxed{
\bigl(-\mathfrak J(S;\mathcal P)\bigr)_+
=
\bigl(-\lambda_{\min}(S,G)\bigr)_+.
}
\tag{L-20505.12}
\]

Equivalently,

\[
\boxed{
\mathfrak J(S;\mathcal P)\ge0
\quad\Longleftrightarrow\quad
S\succeq0.
}
\tag{L-20505.13}
\]

Thus the exact optimized conditional-frame scalar is sign-equivalent to the
fully corrected kernel itself.

## 6. Cofinal consequence

For a sequence \(S_j,G_j\),

\[
\boxed{
\bigl(-\mathfrak J_j\bigr)_+
=
\bigl(-\lambda_{\min}(S_j,G_j)\bigr)_+.
}
\tag{L-20505.14}
\]

Hence a statement such as

\[
\Lambda_j(-\mathfrak J_j)_+\to0
\]

is exactly the negative-part lower-floor statement after the declared metric
adapter. It is not a softer theorem obtained merely by optimizing selected line
zeros.

## 7. What the decomposition genuinely adds

The two-frame construction remains useful because it supplies **finite
proof-producing lower bounds**

\[
\underline b(P)
=
\underline\sigma(P)-\overline\nu(P)
\le b(P)
\]

from independently auditable objects:

- selected simple-line evaluations;
- a complete one-sided corrected residual;
- exact graph and metric algebra.

A successful proof does not evaluate the abstract supremum. It exhibits a
finite block \(P_j\) and directed endpoints satisfying

\[
\Lambda_j
\bigl(-\underline b(P_j)\bigr)_+
+
\delta_j
\to0.
\tag{L-20505.15}
\]

This is a proof interface and search architecture, not an automatic reduction
of logical difficulty.

## 8. Scope correction

The optimized scalar in early drafts of `T-20501` was described as a narrower
remaining theorem. Equation (L-20505.12) shows that this language is too strong.
The correct statement is:

```text
exact optimized scalar:
    same negative part as the final corrected kernel;

finite certified split:
    potentially far easier to evaluate or bound than the whole matrix at once.
```

No RH proof follows from the decomposition without the directed cofinal
certificate (L-20505.15).
