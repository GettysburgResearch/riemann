# L-98610 — Exact prime update of the Tao completion and parity-neutral reserve

Claim ID: `L-98610`  
Status: **PROVED EXACT SEMIGROUP IDENTITY**  
Created: 2026-08-18  
Depends on: PR #610 definitions  
RH status: **not assumed**

For a finite prime set `P`, let `S_P` be its multiplicative semigroup and define,
for real `x>=1`,

\[
A_P(x)=\sum_{\substack{n\le x\\n\in S_P}}\frac{\mu(n)}n,
\quad N_P(x)=\#(S_P\cap[1,x]),
\quad H_P(x)=\sum_{\substack{n\le x\\n\in S_P}}\frac1n.
\]

Let `N_(P^c)(x)` count integers at most `x` all of whose prime factors lie
outside `P`, and put

\[
C_P(x)=\frac{N_P(x)+N_{P^c}(x)-H_P(x)}x,
\qquad
K_P(x)=\begin{pmatrix}C_P(x)&A_P(x)\\A_P(x)&C_P(x)\end{pmatrix}.
\]

For a prime `p` not in `P`, set `y_k=x/p^k`. The exact semigroup recurrences imply

\[
\boxed{
K_{P\cup\{p\}}(x)
=K_P(x)-p^{-1}K_P(x/p)+\mathcal R_{P,p}(x)I_2,
}
\]

where

\[
\boxed{
x\mathcal R_{P,p}(x)
=
\bigl(N_P(y_1)-H_P(y_1)\bigr)
+
\sum_{k\ge1}\bigl(N_P(y_k)-p^{-k}H_P(y_k)\bigr)
\ge0.}
\]

All sums are finite. The inequality follows termwise from `N_P(t)>=H_P(t)` and
`N_P(t)>=p^{-k}H_P(t)`.

In the parity eigenbasis, with

\[
E_P^\pm=C_P\pm A_P,
\]

one has

\[
E_{Pp}^\pm(x)=E_P^\pm(x)-p^{-1}E_P^\pm(x/p)+\mathcal R_{P,p}(x).
\]

Hence the positive reserve cancels exactly from the ordering channel:

\[
\boxed{
E_{Pp}^+(x)-E_{Pp}^-(x)
=
\bigl(E_P^+(x)-E_P^-(x)\bigr)
-p^{-1}\bigl(E_P^+(x/p)-E_P^-(x/p)\bigr).
}
\]

Thus the local completion controls magnitude and positivity, but its reserve is
parity-neutral and does not itself prove the native sign.
