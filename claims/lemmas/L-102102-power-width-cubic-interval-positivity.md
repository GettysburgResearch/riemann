# L-102102 — Cubic double-owner intervals are positive through every width \(q\le p^A\), \(A<e^{16/17}\)

Claim ID: `L-102102`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC INTERVAL THEOREM**  
Created: 2026-08-21  
Depends on: `L-102101`; Mertens' prime-reciprocal theorem  
RH status: **not assumed**

Fix `1<A<e^(16/17)=2.562994...`. Let `p<q` be actual primes with `p>=67` and `q<=p^A`. For every interior prime `p<ell<q`, `L-102101` gives

\[
\ell^{-1/2}K_{p,q}(y/\ell)\le {17\over16\ell}K_{p,q}(y).
\tag{L-102102.1}
\]

Mertens' theorem gives, uniformly in `q<=p^A`,

\[
\sum_{p<\ell<q\atop \ell\ \mathrm{prime}}{1\over\ell}\le\log A+o_{p\to\infty}(1).
\]

Because `(17/16)log A<1`, there is `p_0(A)` such that

\[
{17\over16}\sum_{p<\ell<q}{1\over\ell}<1
\qquad(p\ge p_0(A),\ q\le p^A).
\tag{L-102102.2}
\]

Let `M_d(y)` be the unsigned weight of the `d`th interior Euler level. Removing one selected prime gives

\[
dM_d(y)\le\left({17\over16}\sum_{p<\ell<q}{1\over\ell}\right)M_{d-1}(y).
\]

Pairing consecutive parity levels yields

\[
\boxed{
\prod_{p<\ell<q}(I-\ell^{-1/2}U_\ell)(I-U_p)(I-U_q)\Psi(y)\ge0.
}
\tag{L-102102.3}
\]

Thus the unconditional positive region expands from `A<e^(3/4)=2.117...` to

\[
\boxed{A<e^{16/17}=2.562994\ldots.}
\]

The theorem does not cover arbitrary endpoint separation. `R-102100` shows that the one-prime Harnack operators do not form an invariant cone, so the complete level budget is load-bearing.
