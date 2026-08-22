# R-102722 — Full filtered-disk positivity does not orient the Lorentz current

Claim ID: `R-102722`  
Status: **PROVED EXACT MATRIX COUNTERMODEL / SCOPE FIREWALL**  
Created: 2026-08-23  
Depends on: `L-102729--L-102731`  
RH status: **unproved**

The full filtered SHARP disk gives a quadratic

\[
 P(w)=P_0+2B\Re w+A|w|^2
 \ge0
 \qquad(|w|\le1/2).
\]

The conclusion-facing Lorentz functional is

\[
 \mathcal L=4A-B.
\]

Disk positivity alone does not determine its sign.

Take

\[
 P(w)=1-4|w|^2.
\]

Then

\[
 P(w)\ge0
 \qquad(|w|\le1/2),
\]

and the boundary of the disk is saturated.  The corresponding coefficients are

\[
 P_0=1,
 \qquad B=0,
 \qquad A=-4.
\]

Hence

\[
 \boxed{4A-B=-16<0.}
\]

The same countermodel admits the exact S-lemma slack `lambda=4`, for which

\[
 \begin{pmatrix}
 A+\lambda&B\\B&P_0-\lambda/4
 \end{pmatrix}
 =0.
\]

Therefore none of the following implications is valid without an additional
source-specific carrier statement:

```text
full filtered SHARP disk positivity
  -> Lorentz orientation;

post-filter S-lemma matrix PSD
  -> Lorentz orientation;

three positive filtered rays
  -> centered barycentric sign.
```

The missing input is exactly the transport of the **single** S-lemma slack
through one-time affine-carrier subtraction and physical source
recombination.  Duplicating the slack between matrix entries or estimating the
center ray before carrier cancellation is forbidden.