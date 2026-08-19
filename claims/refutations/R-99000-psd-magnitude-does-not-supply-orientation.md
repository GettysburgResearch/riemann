# R-99000 — Pointwise Schur magnitude does not close the half-order prefix

Claim ID: `R-99000`  
Status: **PROVED EXACT FINITE FIREWALL**  
RH status: **not assumed**

A positive-semidefinite completion matrix

\[
\begin{pmatrix}\Gamma&A\\A&\Gamma\end{pmatrix}\succeq0
\]
proves only `|A|<=Gamma`.  It does not orient the off-diagonal.  The abstract
matrix `[[1,-1/2],[-1/2,1]]` is already a counterexample to any implication
`PSD => A>=0`.

For the literal half-order threshold source there is a stronger arithmetic
counterexample.  Retain the three dyadic labels

```text
cost 2, activity 1/sqrt(2);
cost 2, activity 1/sqrt(2);
cost 2, activity 1/sqrt(8),
```

and the odd-prime labels `3,5,7,11,13`, each with activity `1/sqrt(p)`.  At
threshold `t=26`, put

\[
F_V(26)=\sum_{\substack{\varnothing\ne S\subseteq V\\P(S)\le26}}
(-1)^{|S|+1}r(S).
\]

Direct finite expansion gives

\[
\begin{aligned}
F_V(26)={}&-1+{11\sqrt2\over8}+{2\sqrt3\over3}
+{2\sqrt5\over5}+{\sqrt7\over7}+{\sqrt{11}\over11}
+{\sqrt{13}\over13}\\
&-{\sqrt{15}\over15}-{\sqrt{21}\over21}
-{5\sqrt{14}\over28}-{\sqrt{10}\over4}
-{5\sqrt{22}\over44}-{5\sqrt{26}\over52}
-{11\sqrt6\over24}.
\end{aligned}
\]

The exact `2^60` enclosure in `X-99000` is

\[
{-150591072045175446\over2^{60}}
\le F_V(26)\le
{-150591072045175410\over2^{60}}<0.
\]

Thus a finite pointwise completion/Schur port can overshoot the unit boundary
before the missing future-prime singleton sources are installed.  The full
primitive prefix through the same endpoint is positive; the repair is genuinely
nonlocal in the future-prime profile.

Consequently neither generic PSD magnitude nor independent pointwise Schur
ports prove `C(t)>=0`.  A valid global proof must transport the correlated
completion across scales or prove the weighted-threshold Euler-characteristic
inequality directly.
