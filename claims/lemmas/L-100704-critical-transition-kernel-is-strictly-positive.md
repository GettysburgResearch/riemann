# L-100704 — Every one-prime balanced transition is strictly positive on the critical Peano kernel

Claim ID: `L-100704`  
Status: **PROVED EXACT LOCAL KERNEL THEOREM**  
Created: 2026-08-20  
Depends on: `L-100001`, `L-100703`  
RH status: **not assumed**

For the quadratic critical Peano kernel

\[
\kappa(t)=\begin{cases}2t-t^2,&0<t\le1,\\1,&t\ge1,\end{cases}
\]

the source weight is

\[
w_x(n)=n^{-3/2}\kappa(\sqrt{n/x}).
\]

For a prime `p`, the balanced transition operator is

\[
R_p=p^{-1/2}U_p-p^{-1}U_{p^2}.
\]

Then for every `x,n>0`,

\[
\boxed{
 p^{-1/2}w_x(np)-p^{-1}w_x(np^2)>0.
}
\tag{L-100704.1}
\]

Indeed, putting `t=sqrt(n/x)` and removing the positive common factor `n^-3/2 p^-4`, (L-100704.1) is equivalent to

\[
p^2\kappa(\sqrt p\,t)>\kappa(pt).
\]

The function `kappa(t)/t` is nonincreasing on `(0,infinity)`: on `(0,1]` it is `2-t`, while on `[1,infinity)` it is `1/t`; the values agree at one. Hence

\[
\frac{\kappa(pt)}{pt}
\le
\frac{\kappa(\sqrt p\,t)}{\sqrt p\,t},
\]
so

\[
\kappa(pt)\le\sqrt p\,\kappa(\sqrt p\,t).
\]
Therefore

\[
p^2\kappa(\sqrt p\,t)-\kappa(pt)
\ge(p^2-\sqrt p)\kappa(\sqrt p\,t)>0.
\]

Thus the derivative insertion in the balanced homotopy is itself a positive local two-scale kernel. The remaining difficulty in `BTHC100700` is only the signed Euler completion by the other primes; no negative sign is created by the distinguished transition `R_p` itself.
