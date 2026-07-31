# L-18507 — Critical-line uniqueness gives the full harmonic complement

Claim ID: `L-18507`  
Title: Finitely many simple critical-line zeros frame the entire metric complement of every finite harmonic radical packet  
Status: `PROPOSED — COMPLETE ABSTRACT/ANALYTIC PROOF; QUANTITATIVE MOAT SEPARATE`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: Paley–Wiener/Jensen zero counting; Conrey's unconditional positive proportion of simple critical-line zeros; exact harmonic lift and selected-zero evaluation normalization  
Scope: the full complementary packet missing from the harmonic count architecture  
Related candidates: none

## 1. Harmonic packet and its actual complement

Fix one finite support level. Let `U` be the **actual complete finite low packet**,
not a packet reconstructed from selected zero cardinals. Let

\[
 J:U\longrightarrow L^2(I)
\]

be the exact harmonic lift

\[
 Ju=(u,-C^{-1}Lu)
\]

written in the localized Hilbert realization. Here `I` is a bounded logarithmic
interval and `J` is injective because its first component is `u`.

Let

\[
 G_C=J^*GJ\succ0
\]

be the harmonic metric, and let `R subset U` be the exact localized radical
packet. Put

\[
 \boxed{W=R^{\perp_{G_C}}\cap U.}                         \tag{L-18507.1}
\]

Then

\[
 \boxed{U=R\oplus_{G_C}W,\qquad
        \operatorname{codim}_U W=\dim R.}                \tag{L-18507.2}
\]

The issue is to prove that **this full complement `W` itself**, rather than a
separately constructed packet, has a finite proof-grade selected-zero frame.

For a real centered critical-line zero ordinate `gamma`, define

\[
 \mathcal E_\gamma u=\widehat{Ju}(\gamma).                \tag{L-18507.3}
\]

The Fourier convention is the one fixed by the localized Weil/zero-gram
interface. A harmless positive multiplicity or normalization weight may be
inserted throughout.

## 2. A Paley–Wiener zero-count lemma

Let `I=[-a,a]`. If `0!=f in L2(I)`, then

\[
 F(z)=\int_I f(x)e^{-izx}\,dx                            \tag{L-18507.4}
\]

is a nonzero entire function of exponential type at most `a`.

### Lemma

The number `n_F(T)` of distinct real zeros of `F` in `[-T,T]` satisfies

\[
 \boxed{n_F(T)=O_F(T).}                                   \tag{L-18507.5}
\]

### Proof

Cauchy--Schwarz gives

\[
 |F(z)|\le |I|^{1/2}\|f\|_2 e^{a|\operatorname{Im}z|}.
 \tag{L-18507.6}
\]

After translating the center if necessary and dividing out a finite zero at the
origin, Jensen's formula on `|z|=2T` gives

\[
 \int_0^{2T}\frac{n_F(r)}r\,dr
 \le
 \frac1{2\pi}\int_0^{2\pi}
 \log^+|F(2Te^{i\theta})|d\theta+O_F(1).                 \tag{L-18507.7}
\]

By (L-18507.6), the right side is `O_F(T)`. Since

\[
 n_F(T)\log2
 \le\int_T^{2T}\frac{n_F(r)}r\,dr,
\]

(L-18507.5) follows. QED.

Only the linear zero-count order is used; no sharp Cartwright density constant
is needed.

## 3. Critical-line zeros are a uniqueness set

Let

\[
 \mathcal Z_{0}^{\rm simp}
 =\{\gamma\in\mathbb R:
   \zeta(1/2+i\gamma)=0\text{ and the zero is simple}\}.
\]

Conrey's unconditional mollifier theorem gives a positive proportion of all
nontrivial zeta zeros that are both simple and on the critical line. Since

\[
 N(T)\asymp T\log T,
\]

there is a constant `c>0` such that, for all sufficiently large `T`,

\[
 \boxed{
 \#\bigl(\mathcal Z_0^{\rm simp}\cap[-T,T]\bigr)
 \ge cT\log T.}                                           \tag{L-18507.8}
\]

### Theorem — uniqueness

For every nonzero `f in L2(I)`, its transform (L-18507.4) cannot vanish at every
point of `mathcal Z_0^simp`.

### Proof

If it did, then (L-18507.8) would give

\[
 n_F(T)\ge cT\log T
\]

for arbitrarily large `T`, contradicting the linear bound (L-18507.5). QED.

Thus the simple critical-line ordinates form a uniqueness set for every
Paley--Wiener space associated with a bounded support interval, regardless of
the interval length.

## 4. Finite extraction on the full complement

Apply the uniqueness theorem to `f=Ju`. Since `J` is injective, every nonzero
`u in W` has a nonzero transform. Hence

\[
 \bigcap_{\gamma\in\mathcal Z_0^{\rm simp}}
 \ker(\mathcal E_\gamma|_W)=\{0\}.                       \tag{L-18507.9}
\]

Because `W` is finite-dimensional, finitely many evaluations already have zero
common kernel.

### Constructive finite extraction

Start with `W_0=W`. If `W_k!=0`, choose `0!=u_k in W_k`. By uniqueness there is
`gamma_(k+1) in mathcal Z_0^simp` with

\[
 \mathcal E_{\gamma_{k+1}}u_k\ne0.
\]

Put

\[
 W_{k+1}=W_k\cap\ker\mathcal E_{\gamma_{k+1}}.
\]

Then `dim W_(k+1)<dim W_k`. After at most `dim W` steps one obtains a finite set

\[
 Z=\{\gamma_1,\ldots,\gamma_m\},
 \qquad m\le\dim W,                                      \tag{L-18507.10}
\]

for which the evaluation map

\[
 V_Z:W\to\mathbb C^m,
 \qquad
 V_Zu=(\mathcal E_{\gamma_1}u,\ldots,
       \mathcal E_{\gamma_m}u)                           \tag{L-18507.11}
\]

is injective. Since `dim codomain <= dim W`, discarding redundant rows gives
`m=dim W` and an isomorphism onto its image if desired.

Every selected zero is simple and isolated. Therefore each member of `Z` admits
a finite argument-principle/Turing/Hardy-sign proof-grade isolator. The theorem
is existential and gives no complexity bound for locating the first passing
set.

## 5. The full complementary frame

Let

\[
 K_Z^C=V_Z^*M_ZV_Z,                                      \tag{L-18507.12}
\]

where `M_Z` is any declared positive diagonal matrix of certified zero weights;
for simple zeros one may take the identity in the normalized coordinates.
Because `V_Z|W` is injective and `W` is finite-dimensional,

\[
 K_Z^C|_W\succ0.
\]

Define the exact generalized frame floor

\[
 \boxed{
 \sigma_Z^2
 =\lambda_{\min}
 \left(
 (G_C|_W)^{-1/2}
 K_Z^C|_W
 (G_C|_W)^{-1/2}
 \right)>0.}                                             \tag{L-18507.13}
\]

Then

\[
 \boxed{
 K_Z^C|_W\succeq\sigma_Z^2G_C|_W,\qquad
 \operatorname{codim}_U W=\dim R.}                       \tag{L-18507.14}
\]

This is the requested **full complementary packet**. No cardinal-packet capture,
source-surjectivity statement, principal angle, or dimension-only comparison is
used: the packet is exactly `R^(perp_GC)` inside the actual complete harmonic
low space.

## 6. Exact count consequence

Let `K_T^C` be any larger proof-grade critical-line Gram containing `K_Z^C`, so

\[
 K_T^C\succeq K_Z^C.                                     \tag{L-18507.15}
\]

For every threshold

\[
 0<\tau<\sigma_Z^2,                                      \tag{L-18507.16}
\]

Courant--Fischer and (L-18507.14) give

\[
 \boxed{
 N_{G_C^{-1/2}K_T^CG_C^{-1/2}}(\tau)
 \le\dim R.}                                             \tag{L-18507.17}
\]

If in addition the exact radical evaluations satisfy

\[
 K_T^C|_R\preceq\epsilon G_C|_R,
 \qquad 0\le\epsilon<\tau,                               \tag{L-18507.18}
\]

then min--max gives the reverse inequality and hence exact saturation:

\[
 \boxed{
 N_{G_C^{-1/2}K_T^CG_C^{-1/2}}(\tau)=\dim R.}            \tag{L-18507.19}
\]

The automatic principal-angle estimate is

\[
 \boxed{
 \|P_{N_\tau^\perp}P_{G_C^{1/2}R}\|^2
 \le\epsilon/\tau.}                                      \tag{L-18507.20}
\]

This is the finite algebra checked by `X-18502`.

## 7. Application to the harmonic threshold

In the harmonic visible theorem put

\[
 \tau_\lambda=B_{T,\lambda}+\beta_\lambda.               \tag{L-18507.21}
\]

At every finite support, the displayed count follows as soon as the selected
simple-zero frame is certified with

\[
 \boxed{
 B_{T,\lambda}+\beta_\lambda<\sigma_{Z,\lambda}^2.}       \tag{L-18507.22}
\]

Together with

\[
 \epsilon_\lambda<B_{T,\lambda}+\beta_\lambda,
\]

this gives exact saturation and the harmonic visible Schur floor already proved
in the parent stack.

The finite extraction theorem proves `sigma_(Z,lambda)>0`; it does **not** by
itself compare that number with the complete omitted-zero budget. That
quantitative comparison is the remaining cofinal moat.

## 8. Stronger interpretation

The failure modes are now exact:

1. **Algebraic capture failure is impossible.** Finitely many simple line zeros
   always frame the complete finite complement.
2. **Numerical conditioning may be arbitrarily poor.** The frame floor may be
   tiny as support and packet rank grow.
3. **Omitted-zero domination is RH-bearing.** Under false RH, localized
   off-line-cardinal directions can make `sigma_Z^2` smaller than the absolute
   omitted-zero budget for every finite selected set.

Thus the full complement exists unconditionally, while a cofinal lower bound for
its frame-to-tail ratio remains the substantive arithmetic theorem.

## 9. Proof boundary

- The Paley--Wiener zero count and finite extraction are unconditional.
- The positive proportion of simple critical-line zeros is imported from
  Conrey's theorem; any later unconditional positive-proportion result is also
  sufficient.
- The harmonic lift must remain inside one bounded localized interval and be
  injective in the declared metric realization.
- Production zero intervals and evaluation rectangles require directed
  arithmetic, but only finitely many at each level.
- No quantitative lower bound for `sigma_(Z,lambda)` is claimed.
- Consequently this lemma proves the full complementary packet and finite count
  interface, but not the cofinal moat or RH.
