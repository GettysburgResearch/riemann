# L-15152 — Product-dilation polarization ledger

Claim ID: `L-15152`  
Title: The complete Selberg second-order channel has an exact polarized ledger, with explicit negative bulk masses and a strict separation from the prime ratio Gram  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15150`; the operator definitions in `L-15147/L-15148`; `R-15113`  
Scope: repairs Gate A and the operator-orientation error; no coercivity or RH claim

## 1. Causal dilation semigroup

Work on

\[
 \mathcal H=L^2([1,\infty),dx),
\]

with zero extension below one. For `r>=1`, define

\[
 (U_rf)(x)=r^{-1/2}f(x/r).
 \tag{L-15152.1}
\]

Then

\[
 U_r^*U_r=I,
 \qquad
 U_rU_r^*=Q_r,
 \qquad
 Q_r=\mathbf1_{[r,\infty)},
 \tag{L-15152.2}
\]

and

\[
 U_rU_s=U_{rs}.
 \tag{L-15152.3}
\]

The adjoint is

\[
 (U_r^*g)(x)=r^{1/2}g(rx).
 \tag{L-15152.4}
\]

Let

\[
 M f=(\log x)f,
 \qquad
 (\mathcal H_0f)(x)={1\over x}\int_1^x f(t)dt,
 \]

\[
 \mathcal A=M-\mathcal H_0,
 \qquad
 \mathcal P=\sum_{n\ge2}{\Lambda(n)\over\sqrt n}U_n,
 \qquad
 \mathcal L=\mathcal A+\mathcal P.
 \tag{L-15152.5}
\]

Every displayed sum is finite in a quadratic form on a compactly supported test.

The exact commutators are

\[
 [M,U_n]=(\log n)U_n,
 \qquad
 [\mathcal H_0,U_n]=0.
 \tag{L-15152.6}
\]

Therefore

\[
 [M,\mathcal P]+\mathcal P^2
 =\sum_{n\ge2}{\Lambda_2(n)\over\sqrt n}U_n
 =:\mathcal P_{\Lambda_2}.
 \tag{L-15152.7}
\]

## 2. Complete arithmetic channel set

For every `n`, define a finite multiset `C(n)` of channels.

1. If `Lambda(n)>0`, include one derivative channel
   \[
   c=(1,n),
   \qquad w_c=\Lambda(n)\log n.
   \]
2. For every ordered factorization `de=n` with `d,e>=2`, include one convolution channel whenever `Lambda(d)Lambda(e)>0`, with
   \[
   c=(d,e),
   \qquad w_c=\Lambda(d)\Lambda(e).
   \]

Then

\[
 \boxed{
 \sum_{c\in C(n)}w_c
 =\Lambda(n)\log n+(\Lambda*\Lambda)(n)
 =\Lambda_2(n).}
 \tag{L-15152.8}
\]

This includes every prime-power channel and every two-distinct-prime channel of `L-15150`; there are no channels for integers with three or more distinct prime divisors.

Put

\[
 \alpha_c^2={w_c\over\sqrt{de}}
 \qquad(c=(d,e)).
 \tag{L-15152.9}
\]

## 3. Exact polarized product-dilation form

For every test vector `f`,

\[
 \boxed{
 \operatorname{Re}\langle f,\mathcal P_{\Lambda_2}f\rangle
 =\sum_c\alpha_c^2
 \operatorname{Re}\langle U_d^*f,U_ef\rangle.}
 \tag{L-15152.10}
\]

Polarization gives the exact identity

\[
 \boxed{
 \begin{aligned}
 \operatorname{Re}\langle f,\mathcal P_{\Lambda_2}f\rangle
 ={1\over2}\sum_c\alpha_c^2
 \Big(&\|U_d^*f+U_ef\|^2\\
 &-\|Q_df\|^2-\|f\|^2\Big).
 \end{aligned}}
 \tag{L-15152.11}
\]

The first term is a genuine positive square. The other two terms are genuine negative masses. In particular, scalar positivity of `Lambda_2` does **not** make the product-dilation form positive.

The projection `Q_d` is not an unspecified endpoint symbol. It removes the full physical interval `[1,d)`. Since `d` varies over the arithmetic manifest, this is an explicit bulk/initial-support ledger and cannot be replaced by a fixed-width annular boundary projector.

An equivalent difference form is

\[
 \operatorname{Re}\langle f,U_nf\rangle
 =\|f\|^2-{1\over2}\|f-U_nf\|^2,
 \tag{L-15152.12}
\]

which displays the product channel as a positive mass minus a dilation Dirichlet energy.

## 4. Full second-order quadratic ledger

Let `ell` be real. `R-15113` gives

\[
 \mathcal L(\mathcal L-\ell)
 =\mathcal A(\mathcal A-\ell)
 +2\mathcal P\mathcal A-\ell\mathcal P
 +\mathcal P_{\Lambda_2}.
 \tag{L-15152.13}
\]

Write

\[
 a_n={\Lambda(n)\over\sqrt n}.
\]

For every compactly supported `f`, the real quadratic form is exactly

\[
 \boxed{
 \begin{aligned}
 &\operatorname{Re}\langle f,
 \mathcal L(\mathcal L-\ell)f\rangle\\
={}&\operatorname{Re}\langle f,\mathcal A(\mathcal A-\ell)f\rangle\\
&+\sum_n a_n
 \left(
 \|\mathcal Af+U_n^*f\|^2
 -\|\mathcal Af\|^2
 -\|Q_nf\|^2
 \right)\\
&+\sum_n a_n
 \left(
 {\ell\over2}\|f-U_nf\|^2
 -\ell\|f\|^2
 \right)\\
&+{1\over2}\sum_c\alpha_c^2
 \left(
 \|U_d^*f+U_ef\|^2
 -\|Q_df\|^2
 -\|f\|^2
 \right).
 \end{aligned}}
 \tag{L-15152.14}
\]

No term has been named boundary-local without proof. The continuous Hardy operator remains inside the complete bulk form

\[
 \operatorname{Re}\langle f,\mathcal A(\mathcal A-\ell)f\rangle.
\]

Equation (L-15152.14) is the corrected coefficient-level completion requested in Gate A. It is an **indefinite polarized ledger**, not a positive Selberg square.

## 5. Why PR #216 has a different orientation

For distinct primes `p,q`, the ordinary-prime Gram in PR #216 contains

\[
 \langle U_pf,U_qf\rangle
 =\langle f,U_p^*U_qf\rangle,
 \tag{L-15152.15}
\]

which is a factor-ratio channel. The product-dilation term in (L-15152.10) is

\[
 \langle f,U_{pq}f\rangle
 =\langle U_p^*f,U_qf\rangle.
 \tag{L-15152.16}
\]

These are not the same operator. The first belongs naturally to an adjoint square `P^*P`; the second belongs to `P^2` after the Selberg derivative completion.

Thus PR #216 remains the correct positive finite geometry for the compact prime-energy route, while (L-15152.14) is the correct indefinite geometry of the second-order causal Selberg route.

## 6. Consequences for future proposals

A valid continuation must choose one of two honest architectures:

1. remain with the product-dilation ledger (L-15152.14) and control every negative bulk mass and mixed term source-specifically; or
2. use the adjoint/ratio Gram of PR #216 directly and prove a localized balanced Type-II dispersion estimate.

It may not import the ratio Gram as a positive factorization of the product channel.

## 7. Proof boundary

Closed exactly:

- the complete `Lambda_2` channel decomposition;
- the product-dilation polarization;
- the mixed `P A` and `-ell P` polarizations;
- the full second-order real quadratic ledger;
- the product-versus-ratio distinction;
- the explicit bulk projection terms.

Not closed:

- positivity or coercivity of the complete ledger;
- a polynomial estimate for the actual arithmetic solution;
- RH.