# L-103302 — The unsieved normalized cubic has a strictly positive one-prime transition defect

Claim ID: `L-103302`  
Status: **PROVED EXACT LOCAL KERNEL THEOREM**  
Created: 2026-08-21  
Depends on: PR #676 `L-100001`; `L-103300`  
RH status: **not assumed**

Normalize the critical cubic by its deep square-root carrier:

\[
 g(u)=e^{-u/2}\frac{\Psi(e^u)}{192}
 =\begin{cases}
 e^{u/2}-\frac13e^u,&u\le0,\\
 1-\frac13e^{-u/2},&u\ge0.
 \end{cases}
\tag{L-103302.1}
\]

A direct calculation gives

\[
(D+1)Dg(u)
=\begin{cases}
\frac34e^{u/2}-\frac23e^u,&u\le0,\\
\frac1{12}e^{-u/2},&u\ge0,
\end{cases}
\tag{L-103302.2}
\]

and both branches are strictly positive.

Let `h=log p` and let `(tau_h f)(u)=f(u-h)`.  The elementary Green identity

\[
(I-\tau_h)(I-e^{-h}\tau_h)f(u)
=\int_0^h\int_0^h e^{-s}
 D(D+1)f(u-r-s)\,dr\,ds
\tag{L-103302.3}
\]

therefore yields

\[
\boxed{
(I-V_p)(I-p^{-1}V_p)g(u)>0
\qquad(p\text{ prime},\ u\in\mathbb R).
}
\tag{L-103302.4}
\]

By `L-103300`, this is exactly the carrier-centered local generator of the
balanced homotopy.  Hence the distinguished transition is positive before the
remaining native prime factors are applied.

The theorem is intentionally local.  `R-103300` proves that this positive cone
is not invariant under arbitrary subsequent native factors, so no global sign
is inferred from (L-103302.4) alone.
