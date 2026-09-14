# R-106420 — Denominator cancellation does not control the all-pass index

Claim ID: `R-106420`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-24  
Depends on: `L-106400`, `L-106415--L-106416`  
RH status: **not assumed**

For any integer \(m\ge1\), put on the unit circle

\[
N_m(z)=1,
\qquad
D_m(z)=z^m,
\qquad
U_m(z)=\frac{N_m(z)}{D_m(z)}=z^{-m}.
\]

Then \(U_m\) is unimodular and

\[
\operatorname{wind}U_m=-m,
\qquad
\|H_{U_m}\|_{\mathcal S_2}^2=m.
\tag{R-106420.1}

But the denominator-cancelled difference is

\[
N_m-D_m=1-z^m,
\]

which is analytic in the disk.  Hence

\[
\boxed{
H_{N_m-D_m}=0
}
\tag{R-106420.2}

while the all-pass topological defect is arbitrarily large.

The exact identity

\[
H_{U_m}(D_mg)=H_{N_m-D_m}g=0
\]

shows what happens: the denominator-multiplied source is

\[
D_mH^2=z^mH^2=\ker H_{U_m},
\]

so it misses the complete initial model space

\[
K_{z^m}=\operatorname{span}\{1,z,\ldots,z^{m-1}\}.
\]

Accordingly,

\[
\mathcal C_{U_m,D_mH^2}=0.
\]

Consequences:

```text
small denominator-cancelled numerator energy
  does not imply a small all-pass Hankel charge;

source-for-source channel algebra
  does not imply coverage of the topological model space;

PWSAMP106420
  cannot be omitted or inferred from L-106410--L-106414 alone.
```

The counterfamily does not refute the Xi sampling theorem.  It proves that the
literal model-space coverage matrix of `L-106415` is the necessary bridge
between the endpoint source calculation and the real-zero index.
