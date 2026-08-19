# L-99710 — Cauchy–Poisson averaging gives a uniform owner spectral gap

Claim ID: `L-99710`  
Status: **PROVED EXACT ANALYTIC / FINITE-OWNER THEOREM**  
Created: 2026-08-20  
Depends on: PR #655 `L-99700/L-99701`  
RH status: **not assumed**

Let

\[
\beta=(\delta_1-\delta_{67})*\mu,
\qquad
g(n)=v_{67}(n)+1,
\qquad
a(n)={\beta(n)\over g(n)}.
\]

Let `Lambda_g` be the generalized von Mangoldt source of

\[
G(s)=\sum_{n\ge1}{g(n)\over n^s}
={\zeta(s)\over1-67^{-s}},
\]

and, for `n>1`, let

\[
P_n(q)={\Lambda_g(q)g(n/q)\over g(n)\log n}
\quad(q\mid n,\ q>1)
\]

be the exact logarithmic-owner law.  PR #655 proves `sum_q P_n(q)=1` and the
untwisted alternating martingale identity.

For real `gamma`, define the phase-owner square

\[
V_\gamma(n)
=\sum_qP_n(q)
 \left|a(n/q)q^{i\gamma}+a(n)\right|^2.
\tag{L-99710.1}
\]

For `tau>0`, let

\[
P_\tau(\gamma)={\tau\over\pi(\tau^2+\gamma^2)}
\]

be the Cauchy–Poisson density, and put

\[
\overline V_\tau(n)
=\int_{\mathbb R}P_\tau(\gamma)V_\gamma(n)\,d\gamma.
\tag{L-99710.2}
\]

The characteristic-function identity

\[
\int_{\mathbb R}P_\tau(\gamma)e^{i\gamma u}\,d\gamma
=e^{-\tau|u|}
\tag{L-99710.3}
\]

gives an exact finite formula for every owner edge.

## 1. Principal `67`-adic sectors

The support of `beta` consists of integers

\[
n=67^e m,
\qquad e\in\{0,1,2\},
\qquad m\text{ squarefree},\quad(67,m)=1.
\]

For `e=0` or `e=1`, every active owner satisfies

\[
a(n/q)=-a(n).
\]

Therefore

\[
\boxed{
\overline V_\tau(n)
=2|a(n)|^2
 \sum_qP_n(q)(1-q^{-\tau}).
}
\tag{L-99710.4}
\]

Since every `q>=2`,

\[
\overline V_\tau(n)
\ge2(1-2^{-\tau})|a(n)|^2.
\tag{L-99710.5}
\]

## 2. The duplicated-67 sector

For `e=2`, write `a=a(n)=mu(m)/3`.  The exact owner transitions are

```text
q=67:      a(n/q)=-3a,
q=67^2:    a(n/q)=+3a,
q=p|m:     a(n/q)=-a.
```

Consequently the Cauchy averages of the three edge types are

\[
(10-6\,67^{-\tau})|a|^2,
\qquad
(10+6\,67^{-2\tau})|a|^2,
\qquad
2(1-p^{-\tau})|a|^2.
\tag{L-99710.6}
\]

The first is at least `4|a|^2`, the second at least `10|a|^2`, and the third
at least `2(1-2^-tau)|a|^2`.  Since the owner probabilities sum to one,
(L-99710.5) holds here as well.

Thus, for every `n>1` with `beta(n) != 0`,

\[
\boxed{
\overline V_\tau(n)
\ge2(1-2^{-\tau})|a(n)|^2.
}
\tag{L-99710.7}
\]

For `0<tau<=1`, concavity of `1-2^-tau` gives

\[
2(1-2^{-\tau})\ge\tau,
\]
so

\[
\boxed{
|a(n)|^2\le\tau^{-1}\overline V_\tau(n).
}
\tag{L-99710.8}
\]

## 3. Why the averaging is load-bearing

At the physical phase `gamma=0`, every principal squarefree owner edge has
zero energy: `V_0(n)=0`.  No untwisted Doob variance can control the parity
channel.  Cauchy–Poisson averaging breaks that exact resonance and charges
every owner step by a quantitative amount while retaining the complete source
law and all cumulative parity data.

This theorem is coefficientwise and exact.  It does not by itself perform the
endpoint/source Carleson embedding needed to control the SHARP Harnack boundary.