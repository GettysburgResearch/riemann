# L-20705 — A fixed off-line zero survives finite-order support averaging

Claim ID: `L-20705`  
Title: Endpoint notches suppress a fixed off-line zero only polynomially unless their order grows with support  
Status: `PROVED ASYMPTOTIC SCOPE THEOREM`  
Authoring agent: `gpt56-03-s`  
Created: 2026-08-01  
Dependencies: the finite Guinand--Weil dictionary; Watson's endpoint lemma  
Scope: support averaging and exact D-0001 response functions  
Related counterexample candidates: none

## 1. Finite dictionary response

Let \(T\) be a real even trigonometric polynomial and put

\[
 K(\omega)=2\int_0^\omega T(t)T(\omega-t)\,dt.
\tag{L-20705.1}
\]

For multiplicative support parameter \(L=\log c\), the finite Guinand--Weil
dictionary gives the entire response

\[
 \boxed{
 g_L(z)
 =L\int_0^1K(\omega)
       \cos\bigl(zL(1-\omega)\bigr)\,d\omega.
 }
\tag{L-20705.2}
\]

This is the response whose values at centered zeta zeros form the finite Weil
quadratic value.

Assume that \(T\) has exact order \(r\) at the endpoint:

\[
 T(t)=a_rt^r+O(t^{r+1}),
 \qquad a_r\ne0.
\tag{L-20705.3}
\]

Then beta integration gives

\[
 \boxed{
 K(\omega)
 =2a_r^2 B(r+1,r+1)\omega^{2r+1}
 +O(\omega^{2r+2}).
 }
\tag{L-20705.4}
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
\tag{L-20705.5}
\]

### Proof

Split the cosine into exponentials. The term containing \(e^{izL}\) decays like
\(e^{-bL}\). The growing term is

\[
 {L\over2}e^{-izL}
 \int_0^1K(\omega)e^{izL\omega}\,d\omega.
\]

Since \(e^{izL\omega}=e^{-(b-ia)L\omega}\), Watson's endpoint lemma and
(L-20705.4) yield

\[
 \int_0^1K(\omega)e^{-(b-ia)L\omega}\,d\omega
 =
 {2a_r^2B(r+1,r+1)\Gamma(2r+2)
  \over[(b-ia)L]^{2r+2}}
 \left(1+O(L^{-1})\right).
\]

Use

\[
 B(r+1,r+1)\Gamma(2r+2)=(r!)^2
\]

and multiply by \(L/2\). QED.

Thus a fixed finite-order source condition buys only the polynomial factor
\(L^{-(2r+1)}\). It does not remove the exponential \(e^{bL}\).

## 3. Necessary growing-notch rate

For a support-dependent family \(T_L\) with endpoint order \(r_L\) and leading
coefficient \(a_{r_L,L}\), suppression of one fixed off-line ordinate requires,
at minimum,

\[
 \boxed{
 (2r_L+1)\log L
 -2\log|a_{r_L,L}r_L!|
 \ge bL-o(L).
 }
\tag{L-20705.6}
\]

This is a conditioning-aware statement. Counting endpoint zeros without
tracking the leading derivative is insufficient: factorial growth may consume
the apparent gain.

For the exact difference packet

\[
 T_m(t)=(1-\cos 2\pi t)^m,
\]

one has \(r=2m\) and \(a_r=(2\pi^2)^m\). Stirling's formula shows that the
competition is exponential in \(L\) when \(m\asymp L\), not when \(m\) is fixed.
This explains why a genuinely growing packet can change the fixed-zero balance,
while the finite verified-height ladder cannot.

## 4. Local support averaging does not help

Let \(\mu_L\) be a probability measure supported on

\[
 [L-\delta_L,L+\delta_L],
 \qquad \delta_L\to0.
\]

For fixed \(T\) and fixed \(z\), (L-20705.5) is locally differentiable in \(L\)
and gives

\[
 \boxed{
 \int g_s(z)\,d\mu_L(s)
 =g_L(z)(1+o(1)).
 }
\tag{L-20705.7}
\]

Hence any positive local average fine enough to preserve a pointwise support
certificate also preserves the full fixed off-line mode.

For a broad scaled average

\[
 {1\over T}\int_T^{2T}w(s/T)g_s(z)\,ds,
\]

if \(w\ge0\) has finite-order nonzero behavior at its upper support endpoint,
Laplace's method again gives an exponential term

\[
 e^{2bT-o(T)}.
\tag{L-20705.8}
\]

Broad averaging may cancel moving high-frequency phases, but it does not provide
a uniform bound for an unknown fixed off-line zero without a corresponding
growing endpoint notch or complete-frame conditioning estimate.

## 5. Consequence for the prime-side schedule

The desired cofinal LMI cannot be proved merely by:

1. averaging the support while holding a finite response packet fixed;
2. improving a fixed verified-height tail;
3. applying a prime-number-theorem remainder that permits one fixed off-line
   zero;
4. adding a finite number of endpoint source conditions.

A successful support-averaged proof must simultaneously certify a growing
packet for which (L-20705.6) holds in the **whitened production metric**. This is
exactly where the very small \(A_{WW}\) coercivity and the large induced kernel
metrics observed in `X-18506/X-20704` enter.

## 6. Scope

This theorem does not say that all support averaging is useless. It separates
two tasks:

- moving/high-frequency zero tails can be reduced by large-sieve averaging;
- the fixed-frequency core requires a growing endpoint notch with controlled
  derivative and metric cost.

No such uniform growing-notch estimate for the complete D-0001 packet is proved
here, and no RH conclusion is claimed.
