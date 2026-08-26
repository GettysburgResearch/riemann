# L-106670 — Regularized Pick free energy is an asymptotically lossless scalarization of canonical charge

Claim ID: `L-106670`  
Status: **PROVED EXACT IN FINITE DIMENSION**  
Created: 2026-08-26  
Depends on: `L-106506`, `L-106630`, `L-106650`; finite-dimensional spectral calculus  
RH status: **not assumed**

## 1. Abstract charge and partition function

Let `M,N` be finite-dimensional subspaces of a Hilbert space, put

\[
K=P_M P_N P_M\big|_M,
\qquad
Q=I_M-K,
\]

and write

\[
\mathfrak C(M,N)=\operatorname{tr}_M Q.
\tag{L-106670.1}
\]

The eigenvalues of `Q` are

\[
0\le \mu_1,\ldots,\mu_m\le1,
\qquad m=\dim M,
\]

and are the adverse squared sines of the principal angles.  For
`0<tau<1` define the regularized Pick partition function and free energy

\[
\boxed{
\mathfrak Z_\tau(M,N)=\det(I_M-\tau Q)
=\prod_{\nu=1}^m(1-\tau\mu_\nu),
}
\tag{L-106670.2}
\]

\[
\boxed{
\mathfrak F_\tau(M,N)
=-{1\over\tau}\log\mathfrak Z_\tau(M,N).
}
\tag{L-106670.3}
\]

Unlike the unregularized determinant `det K`, the partition function never
vanishes:

\[
(1-\tau)^m\le\mathfrak Z_\tau\le1.
\tag{L-106670.4}
\]

## 2. Lossless sandwich

For `0<=x<=1`, convexity of `-log(1-tau x)` and the chord from `0` to `1`
give

\[
\tau x
\le -\log(1-\tau x)
\le x\bigl[-\log(1-\tau)\bigr].
\]

Summing over the spectrum of `Q` yields

\[
\boxed{
\mathfrak C(M,N)
\le
\mathfrak F_\tau(M,N)
\le
c(\tau)\,\mathfrak C(M,N),
\qquad
c(\tau)={-\log(1-\tau)\over\tau}.
}
\tag{L-106670.5}
\]

Since

\[
c(\tau)=1+{\tau\over2}+O(\tau^2),
\]

any choice `tau_T -> 0` scalarizes the charge with relative error `o(1)`.
At the fixed value `tau=1/2`,

\[
\boxed{
\mathfrak C
\le -2\log\mathfrak Z_{1/2}
\le 2\log2\,\mathfrak C.
}
\tag{L-106670.6}
\]

Thus even a fixed regularization overpays by at most `2 log 2`, independently
of dimension and conditioning.

## 3. Positive cycle expansion

For `0<tau<1`, absolute convergence of the logarithmic series gives

\[
\boxed{
\mathfrak F_\tau
=
\sum_{n=1}^{\infty}{\tau^{n-1}\over n}\operatorname{tr}(Q^n)
=
\mathfrak C
+
\sum_{n=2}^{\infty}{\tau^{n-1}\over n}\operatorname{tr}(Q^n).
}
\tag{L-106670.7}
\]

All correction terms are nonnegative.  Since `Q^n <= Q` spectrally,

\[
\boxed{
0\le\mathfrak F_\tau-\mathfrak C
\le\bigl(c(\tau)-1\bigr)\mathfrak C.
}
\tag{L-106670.8}
\]

The first coefficient is the exact canonical charge.  Higher coefficients are
coherent closed cycles, suppressed by powers of `tau`; no standalone
nonnormality estimate is required.

## 4. Frame determinant

Let `E:C^m -> M` be any injective synthesis map and put

\[
G=E^*E,
\qquad
H=E^*P_NE.
\]

Then `G-H=E^*QE`, and therefore

\[
\boxed{
\mathfrak Z_\tau(M,N)
=
{\det\bigl((1-\tau)G+\tau H\bigr)\over\det G}
=
{\det\bigl(G-\tau(G-H)\bigr)\over\det G}.
}
\tag{L-106670.9}
\]

Both determinants acquire the same congruence factor under every change of
frame.  The ratio is basis invariant and contains the complete whitening.

## 5. Relation to T-106650

For finite inner functions `A,B`, with `M=K_B`, `N=K_A`, and denominator
kernel Gram `G`, `L-106650` gives

\[
G-H=D^*GD,
\qquad
D=\operatorname{diag}(A(b_1),\ldots,A(b_m))
\]

in the simple-zero kernel frame.  Hence

\[
\boxed{
\mathfrak Z_\tau(K_B,K_A)
=
{\det(G-\tau D^*GD)\over\det G}.
}
\tag{L-106670.10}
\]

The value–nonnormality decomposition is the first derivative at the origin:

\[
\boxed{
-\left.{d\over d\tau}\log\mathfrak Z_\tau\right|_{\tau=0}
=
\operatorname{tr}(G^{-1}D^*GD)
=
\sum_{B(b)=0}|A(b)|^2+\mathfrak N(A,B).
}
\tag{L-106670.11}
\]

Thus the regularized determinant does not discard the nonnormality debt.  It
packages it, together with every higher coherent cycle, into one positive
scalar object.

## 6. Scope

```text
canonical charge <= regularized Pick free energy       PROVED EXACT
free energy <= c(tau) canonical charge                  PROVED EXACT
as tau -> 0 the scalarization is lossless               PROVED EXACT
frame determinant contains all whitening                PROVED EXACT
Xi determinant lower bound at the 11/500 scale          OPEN
```
