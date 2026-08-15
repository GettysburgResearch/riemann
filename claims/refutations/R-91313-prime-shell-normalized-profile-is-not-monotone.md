# R-91313 — The normalized prime-shell component profile is not continuously monotone

Claim ID: `R-91313`  
Status: **EXACT COUNTEREXAMPLE**  
Created: 2026-08-14  
RH status: **unproved**

For `p>1` and row `j`, define

\[
 \mathcal R^{\rm sh}_{p,j}(z)=
 \frac{Q_{pz}(j)-Q_z(j)}
      {5(\sqrt p-1)\sqrt z}.
\]

A tempting route is to claim that this ratio is nondecreasing and then apply a
no-upward Hall transport.  The claim is false.

At

\[
 p=67,
 \qquad j=5,
 \qquad z=\frac{201}{40},
\]

one has `floor(z)=5` and `floor(pz)=336`.  On these fixed cells write

\[
 Q_z(j)=C_c\log z-D_c,
 \qquad
 Q_{pz}(j)=C_p\log(pz)-D_p.
\]

The logarithmic derivative numerator of the ratio has the sign of

\[
 N=(C_p-C_c)-\frac12[Q_{pz}(j)-Q_z(j)].
\]

Directed rational square-root and logarithm enclosures prove

\[
 N<-0.03218
\]

and therefore

\[
\boxed{
 \partial_{\log z}\mathcal R^{\rm sh}_{67,5}(201/40)
 <-\frac1{4000}<0.
}
\]

Thus continuous row-per-score monotonicity cannot prove the shell producer.
A valid proof must use a discrete arithmetic order, a finite row bonus, the
Green/Kantorovich campaign, or an explicit finite primal certificate.
