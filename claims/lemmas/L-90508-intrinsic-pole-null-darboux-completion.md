# L-90508 — An intrinsic pole-null Darboux–Sobolev completion

Claim ID: `L-90508`  
Status: **PROPOSED COMPLETE FUNCTIONAL-ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: `L-90505`; corrected pole algebra `L-90506/R-90501`; the super-Gaussian Xi-cardinals of PR #365  
Scope: one intrinsically pole-null trace-class completion; no prime-side sign theorem

## 1. The local pole-killing operator

Put

\[
 \mathcal D=\partial_u^2-\frac14.
 \tag{L-90508.1}
\]

For

\[
 \widehat f(z)=\int_{\mathbb R}f(u)e^{izu}\,du,
\]

one has

\[
 \widehat{\mathcal Df}(z)
 =-\left(z^2+\frac14\right)\widehat f(z),
 \qquad
 z^2+\frac14=s(1-s),\quad s=\frac12+iz.
 \tag{L-90508.2}
\]

Thus the multiplier vanishes exactly at the two pole coordinates `z=±i/2` and nowhere else. On the real Fourier axis it is bounded away from zero.

## 2. Exact division on the super-Gaussian core

The Green kernel is

\[
 G(u)=-e^{-|u|/2},
 \qquad \mathcal DG=\delta_0.
 \tag{L-90508.3}
\]

Let `f` be super-Gaussian and satisfy

\[
 \widehat f(i/2)=\widehat f(-i/2)=0.
 \tag{L-90508.4}
\]

For `h=G*f` and `x>0`,

\[
 h(x)=
 -e^{-x/2}\int_{-\infty}^{x}e^{u/2}f(u)\,du
 -e^{x/2}\int_x^\infty e^{-u/2}f(u)\,du.
 \tag{L-90508.5}
\]

The first pole moment rewrites the first integral as a tail; the second moment gives the analogous statement as `x→-∞`. Hence `h` and all derivatives are super-Gaussian. The homogeneous solutions `e^{±u/2}` are not super-Gaussian, so the solution is unique. Therefore

\[
 \boxed{
 f\text{ is super-Gaussian and pole-null}
 \iff f=\mathcal Dh
 \text{ for a unique super-Gaussian }h.
 }
 \tag{L-90508.6}
\]

The two pole constraints are exactly the range conditions for one local second-order Darboux operator.

## 3. Intrinsic trace-class completion

Fix `1/2<a<c`, put `w_a(u)=e^{-a|u|}` and `B_c=(c^2-\partial_u^2)^{-1}`, and define

\[
 \boxed{
 J_{a,c}^{(D)}=\mathcal D B_c^2M_{w_a}.
 }
 \tag{L-90508.7}
\]

Its complex Fourier multiplier after confinement is

\[
 m_{D,c}(z)=-\frac{z^2+1/4}{(c^2+z^2)^2}.
 \tag{L-90508.8}
\]

Every image vector is therefore pole-null. Its evaluation kernel is

\[
 \boxed{
 \mathcal K_{a,c}^{(D)}(z,w)=
 \frac{4a(z^2+1/4)(\bar w^2+1/4)}
 {(c^2+z^2)^2(c^2+\bar w^2)^2
 [4a^2+(z-\bar w)^2]}.
 }
 \tag{L-90508.9}
\]

It vanishes when either argument is a pole coordinate, and on `|Im z|≤1/2`,

\[
 \mathcal K_{a,c}^{(D)}(z,z)
 \ll_{a,c}(1+|\Re z|^2)^{-2}.
 \tag{L-90508.10}
\]

The complete zero-side operator is therefore trace class.

## 4. Complete prime-side trace norm

The kernel of `B_c^2` is

\[
 b_c^{(2)}(x)=\frac{e^{-c|x|}(1+c|x|)}{4c^3}.
\]

Using `\partial_u^2B_c^2=c^2B_c^2-B_c`, the convolution kernel of `\mathcal DB_c^2` is

\[
 \ell_c(x)=
 \frac{e^{-c|x|}}{4c^3}
 \left[c\left(c^2-\frac14\right)|x|-\left(c^2+\frac14\right)\right].
 \tag{L-90508.11}
\]

Hence `|\ell_c(x)|≤C_c(1+|x|)e^{-c|x|}`. The nuclear decomposition used in `L-90505` gives, non-optimally,

\[
 \boxed{
 \|(J_{a,c}^{(D)})^*T_yJ_{a,c}^{(D)}\|_1
 \le C_{a,c}(1+|y|)^3e^{-a|y|}.
 }
 \tag{L-90508.12}
\]

Therefore

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \|(J_{a,c}^{(D)})^*(T_{\log n}+T_{-\log n})J_{a,c}^{(D)}\|_1<\infty.
 \tag{L-90508.13}
\]

The all-prime explicit-formula expansion is trace-norm convergent and contains no pole term or external finite-rank projection.

## 5. Global cardinal capture and exact index

Let `q_\omega` be a pole-null super-Gaussian Xi-cardinal from corrected `L-90506`. By (L-90508.6), write `q_\omega=\mathcal Dh_\omega` with `h_\omega` super-Gaussian and put

\[
 g_\omega=w_a^{-1}(c^2-\partial_u^2)^2h_\omega.
 \tag{L-90508.14}
\]

Then `g_\omega∈L^2` and `J_{a,c}^{(D)}g_\omega=q_\omega`. Thus every actual off-line-cardinal negative direction is present.

Let `A_{a,c}^{(D)}` represent the complete Weil form on the image of `J_{a,c}^{(D)}`. The zero-coordinate pullback gives an upper bound by the number `q` of reflected off-line pairs, while the mutually Weil-orthogonal captured cardinals give the reverse bound. Hence

\[
 \boxed{
 n_-(A_{a,c}^{(D)})
 =\#\{\text{distinct reflected off-line zero pairs}\}.
 }
 \tag{L-90508.15}
\]

In particular

\[
 \boxed{\mathrm{RH}\iff A_{a,c}^{(D)}\succeq0.}
 \tag{L-90508.16}
\]

## 6. Proof boundary

Proved here:

- exact super-Gaussian division by `s(1-s)` under the two pole moments;
- an intrinsic pole-null trace-class completion;
- its explicit evaluation kernel and prime-shift trace-norm bound;
- capture of every fixed off-line Xi-cardinal;
- exact negative-index equality.

Not proved:

- positivity of `A_{a,c}^{(D)}`;
- a prime-side heat-pressure inequality;
- RH.
