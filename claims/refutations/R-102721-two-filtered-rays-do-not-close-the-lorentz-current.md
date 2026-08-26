# R-102721 — Two filtered SHARP rays do not determine the full Lorentz current

Claim ID: `R-102721`  
Status: **PROVED ALGEBRAIC SCOPE FIREWALL**  
Created: 2026-08-22  
Depends on: `L-102727`  
RH status: **unproved**

Write, at one filtered scale,

\[
A=P_2a_\tau,
\qquad
G=G_\tau,
\qquad
Q=P_2Q_\tau.
\]

`L-102727` proves

\[
Q-5G\ge0,
\qquad
Q-4G-\frac34A\ge0.
\tag{R-102721.1}
\]

These two inequalities do not force the conclusion-facing coordinate

\[
5A-G
\]

to be nonnegative or even bounded below by a source-free constant.

Indeed the exact scalar fixture

\[
A=1,\qquad G=6,\qquad Q=30
\]

satisfies

\[
Q-5G=0,
\]

\[
Q-4G-\frac34A=\frac{21}{4}>0,
\]

while

\[
5A-G=-1<0.
\]

Thus the two filtered rays are a genuine advance through the signed filter, but
they are not a replacement for transporting the single S-lemma slack or for a
carrier-recombined lower bound on the filtered wavelet current.

Any successor must use additional arithmetic structure; linear programming on
only the two ray inequalities cannot establish `FLC102730`.