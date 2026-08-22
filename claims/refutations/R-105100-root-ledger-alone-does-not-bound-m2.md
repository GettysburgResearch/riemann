# R-105100 — The root fourth-moment ledger alone does not bound M2

Claim ID: R-105100

Status: **PROPOSED EXACT ALGEBRAIC FIREWALL; review pending**

Created: 2026-08-23

Depends on: L-105100

RH status: **unproved**

Consider

\[
p(x)=x^4-2x^2+2.
\]

Its derivative has the three simple real zeros \(-1,0,1\), and

\[
\rho_{-1}=\frac18,\qquad
\rho_0=-\frac12,\qquad
\rho_1=\frac18.
\]

Therefore

\[
\boxed{
\sum_{p'(c)=0,\ c\in\mathbb R}\rho_c^2
=\frac9{32}.
}
\tag{R-105100.1}
\]

The roots of \(p''=12x^2-4\) satisfy \(d^2=1/3\). At each of the two roots,

\[
\tau_d
=\frac{p(d)^2}{p'(d)p'''(d)}
=-\frac{169}{1728},
\]

so

\[
\boxed{
\sum_{p''(d)=0}\tau_d=-\frac{169}{864}.
}
\tag{R-105100.2}
\]

For this quartic, \(V_2=4\) and \(V_4=0\). Thus

\[
\boxed{
\mathcal K_4(p)=\frac{37}{432}.
}
\tag{R-105100.3}
\]

Indeed,

\[
\frac9{32}-\frac{169}{864}=\frac{37}{432}.
\]

Consequently

\[
\sum_{p'(c)=0,\ c\in\mathbb R}\rho_c^2
>
\mathcal K_4(p).
\]

The tempting inference

    complete-root V2/V4 ledger
      -> upper bound for the real critical-residue second moment

is false even when every critical point of \(p\) is real. The
second-derivative cross-residue debt is conclusion bearing and cannot be
dropped. With nonreal critical points, the additional correction in
L-105100.11 is also mandatory.
