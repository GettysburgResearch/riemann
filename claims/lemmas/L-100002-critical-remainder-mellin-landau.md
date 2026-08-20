# L-100002 — Every final centered remainder is a zero-real-carrier RH detector

Claim ID: `L-100002`  
Status: **PROVED EXACT ANALYTIC CONSUMER**  
Created: 2026-08-20  
Depends on: `L-100000`; the specialized Landau theorem of PR #653  
RH status: **not assumed**

For an integer `m>=3`, let

\[
C_m(x)=R_{m,m-1}(x)
\]

be the final centered remainder of `L-100000`.

## 1. Mellin multiplier

Initially for `Re(s)>m/2`,

\[
\int_1^\infty H_m(x)x^{-s-1}\,dx
=\mathcal B(s+1/2)\,M_m(s),
\tag{L-100002.1}
\]

where

\[
\boxed{
M_m(s)
=2\,4^m m!\,{\Gamma(2s-m)\over\Gamma(2s+1)}
={2\,4^m m!\over\prod_{j=0}^{m}(2s-m+j)}.
}
\tag{L-100002.2}
\]

Equivalently,

\[
M_m(s)=4^m\sum_{\ell=0}^{m}
 {(-1)^\ell\binom m\ell\over s-(m-\ell)/2}.
\tag{L-100002.3}
\]

The recursive carriers in `L-100000` cancel, one by one, the real poles at

\[
s=m/2,(m-1)/2,\ldots,1.
\]

The remaining kernel pole at `s=1/2` is canceled by

\[
\mathcal B(1)=0,
\]

which is the simple zero of `1/zeta(z)` at the zeta pole `z=1`. Since zeta has
no real zero on `(1/2,1)`, the resulting meromorphic continuation is regular at
every positive real `s`.

## 2. Off-line poles survive

Let `rho` be a nontrivial zeta zero with `Re(rho)>1/2`, and put

\[
s_\rho=\rho-1/2.
\]

Then `Re(s_rho)>0` and

\[
1-67^{-\rho}\ne0.
\]

Also `M_m(s_rho)` is nonzero because its numerator is constant and all its
poles are real. The finite carrier corrections have only real poles and cannot
cancel the reciprocal-zeta pole at `s_rho`. Therefore every such zero produces
a nonremovable pole in the Mellin transform of `C_m`.

## 3. Conclusion criteria

If, for one integer `m>=3`,

\[
C_m(x)\ge0
\]

eventually, Landau's real-abscissa theorem contradicts the surviving nonreal
pole. The functional equation then gives RH.

More generally, it is enough that

\[
\boxed{
\int_1^X(C_m(t))_-\,{dt\over t}=X^{o(1)}.
}
\tag{L-100002.4}
\]

Indeed the negative-part Mellin transform is holomorphic in `Re(s)>0`; adding
it to the full transform leaves a nonnegative Mellin witness with every
off-line pole intact.

Thus

\[
\boxed{
\text{critical centered negative mass for any }m\ge3
\Longrightarrow RH.
}
\tag{L-100002.5}
\]

The theorem is an exact consumer. It does not assert that the critical
remainder has the required sign.
