# L-104512 — The Laguerre defect is exact Hermite–Biehler phase velocity

Claim ID: `L-104512`  
Status: **PROVED EXACT**  
Created: 2026-08-22  
RH status: **not assumed**

Let `F_k=F^(k)` for a real entire function `F`, and fix `lambda>0`. Define

\[
E_{k,\lambda}(z)=F_k(z)-i\lambda F_{k+1}(z).
\tag{L-104512.1}
\]

Then

\[
\boxed{E_{k,\lambda}'=E_{k+1,\lambda}.}
\tag{L-104512.2}
\]

On the real axis, away from common zeros, choose a continuous phase

\[
\theta_{k,\lambda}(t)=\arg E_{k,\lambda}(t).
\]

A direct calculation gives

\[
\boxed{
\theta_{k,\lambda}'(t)
=
\lambda\,
\frac{F_{k+1}(t)^2-F_k(t)F_{k+2}(t)}
     {F_k(t)^2+\lambda^2F_{k+1}(t)^2}.
}
\tag{L-104512.3}
\]

At a simple critical point `c`, where `F_(k+1)(c)=0`,

\[
\operatorname{sgn}\theta_{k,\lambda}'(c)
=
-\operatorname{sgn}(F_k(c)F_{k+2}(c)).
\tag{L-104512.4}
\]

Hence a wrong extremum is precisely a clockwise crossing of the real axis by
the Hermite–Biehler companion.

## Riccati form

With

\[
h_k=-F_{k+1}/F_k,
\]

equation (L-104512.3) is the boundary diagonal of the Pick kernel of `h_k`,
while

\[
h_{k+1}=h_k-h_k'/h_k.
\]

Thus the local phase velocity, the positive-residue test, and the Riccati–Pick
recursion are three exact descriptions of one defect.

## Scope firewall

`R-104511` shows that `theta'>=0` on the whole real line is not sufficient to
make the parent real-rooted. The total half-plane index of `L-104510` must also
be retained.
