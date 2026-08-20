# L-100180 — Finite Euler squaring crosses the critical owner wall on a corrected noncompact corridor

Claim ID: `L-100180`  
Status: **PROVED FOR EACH FIXED CRITICAL ORDER AFTER INCLUDING THE INACTIVE TAIL**  
Created: 2026-08-20  
Depends on: `L-100000`, `L-100020`  
RH status: **not assumed**

Let `R_(m,m-1)` be the final critical centered-Bernstein remainder of `L-100000`, with fixed integer `m>=3`, and let `A_Z` be the finite Euler-squaring operator.  Completed primes `p<=Z` become labels of cost `p^2`; primes above `Z` remain labels of cost `p`.

The critical kernel is noncompact.  Therefore the owner budget must include both active labels and the inactive continuation.  The corrected bound is

\[
\boxed{
\Sigma_{m,Z}(X)
\le
\sum_{\substack{p\le Z\\p^2\le X}}{1\over p^2}
+{\bf1}_{67^2\le X}{1\over67^2}
+
\sum_{Z<p\le X}{1\over p}
+
R_m(X,Z),
}
\tag{L-100180.1}
\]

where

\[
0\le R_m(X,Z)
\ll_m
\max(1,\sqrt X)
\sum_{p>\max(X,Z)}p^{-3/2}.
\tag{L-100180.2}
\]

## Proof of the inactive-tail scale

For `t>=1`, the final critical Peano kernel `kappa_(m,m-1)(t)` is a polynomial of degree `m-2`.  After multiplication by the source weight `n^{-(m+1)/2}`, adjoining an inactive prime therefore costs at most

\[
O_m\!\left(\sqrt X\,p^{-3/2}\right)
\]

relative to the root level.  Summing over primes beyond `max(X,Z)` gives (L-100180.2).  Elementary prime partial summation yields

\[
R_m(X,Z)\ll_m {1\over\log(2\max(X,Z))}.
\tag{L-100180.3}
\]

The earlier budget terminating at `p<=X` omitted this noncompact tail and is withdrawn.

## Correct corridor

Uniformly for

\[
1\le X\le Z^{10/9},
\]

the completed-prime mass and the interval `Z<p<=X` have a limiting upper bound strictly below one.  Since (L-100180.3) tends to zero, for every fixed `m>=3` there exists `Z_0(m)` such that

\[
\Sigma_{m,Z}(X)<1
\qquad
(Z\ge Z_0(m),\ 1\le X\le Z^{10/9}).
\tag{L-100180.4}
\]

Adjacent-level double counting then gives

\[
kM_k(X)\le\Sigma_{m,Z}(X)M_{k-1}(X),
\]

so every odd level is smaller than the preceding even level.  Hence

\[
\boxed{
(A_ZR_{m,m-1})(X)>0
\qquad
(Z\ge Z_0(m),\ 1\le X\le Z^{10/9}).
}
\tag{L-100180.5}

Every finite completion multiplier remains zero-free in the translated open half-plane, so no off-line reciprocal-zeta pole is cancelled.

## Boundary

The theorem is pointwise positivity of a **completed** fixed-order critical packet on a finite corridor.  It neither supplies a positive inverse nor turns an endpoint-dependent completion into one fixed Landau density.  The former universal threshold `log Z>=90` for all `m` was unsupported once the inactive tail is included and is replaced by the fixed-order threshold `Z_0(m)`.
