# L-100704 — Every one-prime balanced transition is strictly positive on the critical Peano kernel

Claim ID: `L-100704`  
Status: **PROVED EXACT LOCAL KERNEL THEOREM; NORMALIZATION REPAIRED**  
Created: 2026-08-20  
Depends on: `L-100001`, corrected `L-100703`  
RH status: **not assumed**

For the quadratic critical Peano kernel

\[
\kappa(t)=\begin{cases}2t-t^2,&0<t\le1,\\1,&t\ge1,
\end{cases}
\]

put

\[
w_x(n)=n^{-3/2}\kappa(\sqrt{n/x}).
\]

For a prime `p`, the balanced transition operator is

\[
R_p=p^{-1/2}U_p-p^{-1}U_{p^2}.
\]

When `R_p` acts on the unsieved physical critical carrier, the common outside factor converts its two shifted terms exactly into `w_x(np)` and `w_x(np^2)`.  Thus the correct local statement is

\[
\boxed{
w_x(np)-w_x(np^2)>0
\qquad(x,n>0).
}
\tag{L-100704.1}
\]

The former display with additional factors `p^-1/2` and `p^-1` double-counted the shift coefficients and is withdrawn.

## Proof

Put `t=sqrt(n/x)`.  After removing the positive common factor `n^-3/2 p^-3`, inequality (L-100704.1) is equivalent to

\[
\boxed{
p^{3/2}\kappa(\sqrt p\,t)>\kappa(pt).}
\tag{L-100704.2}
\]

The function `kappa(s)/s` is nonincreasing on `(0,infinity)`: it equals `2-s` on `(0,1]` and `1/s` on `[1,infinity)`.  Hence

\[
{\kappa(pt)\over pt}
\le
{\kappa(\sqrt p\,t)\over\sqrt p\,t},
\]

so

\[
\kappa(pt)\le\sqrt p\,\kappa(\sqrt p\,t).
\]

Since `p^(3/2)>sqrt p`, (L-100704.2) follows strictly.

Therefore the distinguished transition insertion is a positive local two-scale kernel.  This does not sign its completion by the other primes; the latter remains the balanced cross-source problem.
