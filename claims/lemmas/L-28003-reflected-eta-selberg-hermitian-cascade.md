# L-28003 — Reflected eta–Selberg identity for the central cascade

Claim ID: `L-28003`  
Title: The reciprocal-eta central resolvent has an exact two-frequency Selberg identity whose diagonal is the Hermitian square `|eta'/eta|^2`  
Status: **PROPOSED EXACT ALGEBRAIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #280  
Dependencies: generalized reflected Selberg algebra of `L-9516/L-9518`; `L-28001`  
Scope: initially `Re(s)>1`; no critical estimate or RH claim

## 1. Eta coefficients and inverse

Let

\[
 e(n)=(-1)^{n-1},
 \qquad
 \eta(s)=\sum_{n\ge1}e(n)n^{-s},
\]

and let `b` be the Dirichlet-convolution inverse from `L-28001`:

\[
 e*b=\varepsilon,
 \qquad
 \sum_{n\ge1}b(n)n^{-s}={1\over\eta(s)}
 \quad(\operatorname{Re}s>1).
\]

Define the generalized eta von Mangoldt coefficients by

\[
 -{\eta'\over\eta}(s)
 =\sum_{n\ge1}\Lambda_\eta(n)n^{-s}.
\tag{L-28003.1}

Then exactly

\[
 \boxed{
 \Lambda_\eta=b*(e\log).
 }
\tag{L-28003.2}

The usual differentiated inverse identity gives

\[
 \boxed{
 b*(e\log^2)
 =\Lambda_\eta\log+\Lambda_\eta*\Lambda_\eta.
 }
\tag{L-28003.3}

## 2. Explicit generalized prime coefficients

Since

\[
 \eta(s)=(1-2^{1-s})\zeta(s),
\]

one has

\[
 -{\eta'\over\eta}(s)
 =-{\zeta'\over\zeta}(s)
  -(\log2){2^{1-s}\over1-2^{1-s}}.
\tag{L-28003.4}

Expanding in `Re(s)>1` yields

\[
 \boxed{
 \Lambda_\eta(n)=
 \begin{cases}
 \Lambda(n),&n\ne2^r,\\[1mm]
 (1-2^r)\log2,&n=2^r,\ r\ge1.
 \end{cases}}
\tag{L-28003.5}

The generalized prime source is signed only on the dyadic tower.  No ordinary
prime or off-line zeta pole is deleted.

## 3. Independent twists

For real frequencies `t,u`, put

\[
 e_t(n)=e(n)n^{-it},
 \qquad
 b_t(n)=b(n)n^{-it},
 \qquad
 \Lambda_{\eta,t}(n)=\Lambda_\eta(n)n^{-it}.
\]

Their Dirichlet series are `eta(s+it)`, `1/eta(s+it)`, and
`-eta'/eta(s+it)`.

For the product series

\[
 \eta(s+it)\eta(s-iu),
\]

the coefficient, inverse, and generalized von Mangoldt sequences are

\[
 e_{t,-u}^{\times}=e_t*e_{-u},
 \qquad
 b_{t,-u}^{\times}=b_t*b_{-u},
\]

and

\[
 \Lambda_{\eta,t,-u}^{\times}
 =\Lambda_{\eta,t}+\Lambda_{\eta,-u}.
\]

Apply (L-28003.3) to the product and subtract the two individual identities.
Every linear logarithmic term cancels, leaving

\[
 \boxed{
 \begin{aligned}
 &b_{t,-u}^{\times}*
   (e_{t,-u}^{\times}\log^2)
 -b_t*(e_t\log^2)
 -b_{-u}*(e_{-u}\log^2)\\
 &\hspace{28mm}
 =2\,\Lambda_{\eta,t}*\Lambda_{\eta,-u}.
 \end{aligned}}
\tag{L-28003.6}

This is an exact coefficient identity.

## 4. Hermitian diagonal

Taking Dirichlet series at a real line `sigma>1` gives

\[
 \boxed{
 \mathcal C_\eta(\sigma;t,-u)
 -\mathcal C_\eta(\sigma;t)
 -\mathcal C_\eta(\sigma;-u)
 =2L_\eta(\sigma+it)L_\eta(\sigma-iu),
 }
\tag{L-28003.7}

where

\[
 L_\eta(s)=-{\eta'\over\eta}(s).
\]

On the diagonal `u=t`, real coefficients give

\[
 \boxed{
 \mathcal C_\eta(\sigma;t,-t)
 -\mathcal C_\eta(\sigma;t)
 -\mathcal C_\eta(\sigma;-t)
 =2\left|{\eta'\over\eta}(\sigma+it)\right|^2.
 }
\tag{L-28003.8}

Thus the all-stage central cascade has the same exact reflected Hermitian
orientation that repaired the scalar `H(z)^2` mismatch in the zeta Selberg
route.

## 5. Local physical block

Let `H` be a real compact source window.  The two-frequency adapter of
`L-9518`, applied with `Lambda_eta` in place of `Lambda`, gives the exact local
normal block

\[
 \boxed{
 B_{J,\eta}(H)
 =\sum_{m,n}
 {\Lambda_\eta(m)\Lambda_\eta(n)\over\sqrt{mn}}
 K_{J}^{H}(\log m,\log n),
 }
\tag{L-28003.9}

with every independent-frequency cross term retained.  Equation
(L-28003.6) supplies its coefficient forcing through the reciprocal-eta inverse
`b`.

This is an exact source map, not an estimate.  A critical bound still requires
complete dyadic-boundary, mixed-radix, cutoff, and lower-scale ledgers.

## 6. Pole preservation

The logarithmic derivatives satisfy

\[
 {\eta'\over\eta}(s)
 ={\zeta'\over\zeta}(s)
 +{(\log2)2^{1-s}\over1-2^{1-s}}.
\tag{L-28003.10}

The second term has poles only on `Re(s)=1`.  Hence every zeta zero in the open
critical strip produces the same uncancelled logarithmic-derivative pole in the
eta source.

Therefore a source-specific bound for the reflected eta block is genuinely
RH-sensitive.  The central cascade has not canceled the difficult zero mode;
it has converted it into one dyadic-boundary generalized-prime packet.

## 7. Exact connection to the product-six mutation

The inverse coefficients in the forcing are the Neumann-resolvent coefficients
of `L-28001`.  Their first mixed-radix sign is

\[
 b(6)=-1,
\]

arising from the two ordered factorizations `2*3` and `3*2`.  Any packet proof
of (L-28003.9) must therefore retain the complete binary--ternary cross family
before taking a norm.  An entrywise absolute-value estimate fails the mandatory
product-six mutation.

## 8. Proof boundary

Closed exactly:

- the eta generalized Selberg identity;
- explicit generalized-prime coefficients;
- independent-frequency reflected subtraction;
- the Hermitian diagonal;
- the local-block adapter at algebraic scope;
- preservation of every off-line zeta pole;
- the product-six source mutation.

Open:

- a critical source-specific reflected block estimate;
- complete mixed-radix endpoint recombination;
- a strict lower-scale recurrence;
- RH.
