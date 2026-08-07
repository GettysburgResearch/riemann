# L-20802 — A fixed off-line zero survives every fixed-order support average

Claim ID: `L-20802`  
Title: Fixed endpoint notches suppress a fixed off-line zero only polynomially in logarithmic support  
Status: `PROVED FIXED-PACKET ASYMPTOTIC SCOPE THEOREM`  
Authoring agent: `gpt56-03-s`  
Created: 2026-08-01  
Dependencies: the finite Guinand--Weil dictionary; Watson's endpoint lemma  
Scope: support averaging with one fixed finite D-0001 response packet  
Related counterexample candidates: none

## 1. Finite dictionary response

Let \(T\) be a fixed real even trigonometric polynomial and put

\[
 K(\omega)=2\int_0^\omega T(t)T(\omega-t)\,dt.
\tag{L-20802.1}
\]

For multiplicative support parameter \(L=\log c\), the finite Guinand--Weil
dictionary gives the entire response

\[
 \boxed{
 g_L(z)
 =L\int_0^1K(\omega)
       \cos\bigl(zL(1-\omega)\bigr)\,d\omega.
 }
\tag{L-20802.2}
\]

Assume that \(T\) has exact fixed order \(r\) at the endpoint:

\[
 T(t)=a_rt^r+O(t^{r+1}),
 \qquad a_r\ne0.
\tag{L-20802.3}
\]

Then beta integration gives

\[
 \boxed{
 K(\omega)
 =2a_r^2 B(r+1,r+1)\omega^{2r+1}
 +O(\omega^{2r+2}).
 }
\tag{L-20802.4}
\]

## 2. Fixed off-line asymptotic

Let

\[
 z=a+ib,
 \qquad b>0
\]

be fixed. Then, as \(L\to\infty\),

\[
 \boxed{
 g_L(z)
 ={a_r^2(r!)^2\over(b-ia)^{2r+2}}
 {e^{(b-ia)L}\over L^{2r+1}}
 \left(1+O_z(L^{-1})\right)
 +O_z(e^{-bL}).
 }
\tag{L-20802.5}
\]

### Proof

Split the cosine into exponentials. The term containing \(e^{izL}\) decays like
\(e^{-bL}\). The growing term is

\[
 {L\over2}e^{-izL}
 \int_0^1K(\omega)e^{izL\omega}\,d\omega.
\]

Since \(e^{izL\omega}=e^{-(b-ia)L\omega}\), Watson's endpoint lemma and
(L-20802.4) yield

\[
 \int_0^1K(\omega)e^{-(b-ia)L\omega}\,d\omega
 =
 {2a_r^2B(r+1,r+1)\Gamma(2r+2)
  \over[(b-ia)L]^{2r+2}}
 \left(1+O_z(L^{-1})\right).
\]

Use

\[
 B(r+1,r+1)\Gamma(2r+2)=(r!)^2
\]

and multiply by \(L/2\). QED.

Thus every **fixed finite-order** source condition buys only the polynomial
factor \(L^{-(2r+1)}\); it does not remove the exponential \(e^{bL}\).

## 3. Local support averaging does not help a fixed packet

Let \(\mu_L\) be a probability measure supported on

\[
 [L-\delta_L,L+\delta_L],
 \qquad \delta_L\to0.
\]

For fixed \(T\) and fixed \(z\), equation (L-20802.5) and local uniformity give

\[
 \boxed{
 \int g_s(z)\,d\mu_L(s)
 =g_L(z)(1+o(1)).
 }
\tag{L-20802.6}
\]

Hence a positive local support average fine enough to preserve a pointwise
certificate preserves the full fixed off-line mode.

For a broad scaled average

\[
 {1\over T_0}\int_{T_0}^{2T_0}w(s/T_0)g_s(z)\,ds,
\]

if \(w\ge0\) has fixed finite-order nonzero behavior at the upper endpoint of
its support, Laplace's method again gives a nonzero term of the form

\[
 e^{2bT_0}T_0^{-O(1)}.
\tag{L-20802.7}
\]

Thus broad positive averaging may control moving high-frequency phases, but it
cannot uniformly suppress an unknown fixed off-line zero while the response
packet and endpoint order remain fixed.

## 4. What a growing packet must prove

A support-dependent family \(T_L\) can escape the theorem because its endpoint
order, leading coefficient, and metric normalization may all vary with \(L\).
The fixed-order asymptotic above does **not** by itself justify a formula uniform
in growing order.

A valid growing-notch proof must therefore retain a uniform endpoint Laplace
bound of the form

\[
 |g_L(a+ib)|
 \le
 \exp[-\omega_L(b)]\,e^{bL}
\tag{L-20802.8}
\]

in the whitened production metric, with

\[
 \omega_L(b)-bL\longrightarrow+\infty
\tag{L-20802.9}
\]

for every fixed \(0<b<1/2\). It must include the factorial/derivative cost of
the growing endpoint notch; counting endpoint zeros alone is insufficient.

## 5. Consequence for the prime-side schedule

The desired cofinal LMI cannot be proved merely by:

1. averaging support while holding a finite response packet fixed;
2. improving a fixed verified-height tail;
3. applying a prime-number-theorem remainder that permits one fixed off-line
   zero;
4. adding a fixed finite number of endpoint source conditions.

A successful support-averaged proof must simultaneously construct and certify
the growing packet required by (L-20802.8)--(L-20802.9). This is exactly where
the rapidly collapsing \(A_{WW}\) coercivity and large induced packet metrics
observed in `X-18506/X-20704/X-20801` enter.

## 6. Scope

This theorem separates two tasks:

- moving/high-frequency zero tails may be reduced by large-sieve averaging;
- the fixed-frequency core requires a growing endpoint notch with a uniform
  derivative and metric ledger.

No such uniform growing-notch estimate for the complete D-0001 packet is proved
here, and no RH conclusion is claimed.
