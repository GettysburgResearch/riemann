# L-32301 — Quartic-weighted shifted analytic contraction

Claim ID: `L-32301`  
Title: The complete shifted central operator contracts a fourth-order weighted analytic power tail by the same `6/7` reserve  
Status: **PROPOSED COMPLETE ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #286 `L-28401`  
Scope: analytic power/faster-power sector only; no cutoff/cap propagation or RH conclusion

## 1. Shifted central coefficient operator

For `s>0`, PR #286 proves

\[
\mathscr C[x^{-s}]
=[1-\eta(s)]x^{-s}
+\sum_{\ell\ge1}
 c_{s,\ell}x^{-s-\ell},
\]

where

\[
c_{s,\ell}
=\frac{(s)_\ell}{\ell!}
 2^{-s-\ell}\zeta(s+\ell)
\ge0.
\tag{L-32301.1}
\]

For every `s>=1/2`, the weighted row at radius `1/4` satisfies

\[
1-\eta(s)+\sum_{\ell\ge1}c_{s,\ell}4^{-\ell}
\le\frac67.
\tag{L-32301.2}
\]

This is the exact shifted operator, including the `2kq-1` lattice displacement; it is not the unshifted continuum surrogate.

## 2. Quartic coefficient norm

Fix `sigma>=1/2`. For

\[
f(x)=\sum_{h\ge0}a_hx^{-\sigma-h},
\]

define

\[
\boxed{
\|f\|_{\sigma,\star}
=\sum_{h\ge0}|a_h|(1+h)^4 64^{-h}.
}
\tag{L-32301.3}

The fourth-order weight is chosen to absorb every polynomial-in-exponent loss occurring in the all-depth affine-log boundary estimates.

## 3. Exact contraction

An input coefficient at exponent `s=sigma+h` which moves upward by `ell` changes the norm weight by

\[
\frac{(1+h+\ell)^4 64^{-(h+\ell)}}
     {(1+h)^4 64^{-h}}
\le(1+\ell)^4 64^{-\ell}.
\tag{L-32301.4}

For every integer `ell>=1`,

\[
1+\ell\le2^\ell,
\]

and therefore

\[
\boxed{
(1+\ell)^4 64^{-\ell}
\le4^{-\ell}.
}
\tag{L-32301.5}

The same-exponent coefficient carries weight ratio one. Consequently the weighted absolute row sum is at most

\[
1-\eta(s)
+\sum_{\ell\ge1}c_{s,\ell}4^{-\ell},
\]

which is at most `6/7` by (L-32301.2). Summing over input coefficients gives

\[
\boxed{
\|\mathscr C f\|_{\sigma,\star}
\le\frac67\|f\|_{\sigma,\star}.
}
\tag{L-32301.6}

No new zeta estimate, spectral computation, or finite-endpoint extrapolation enters this proof.

## 4. All-depth affine-log normal form

Let

\[
L=2^a,
\qquad
\alpha=1-L^{-1}\in[0,1),
\]

and consider the all-depth endpoint profile appearing on PRs #309/#316,

\[
h_{a,X,s}(x)
=x^{-s}\log\!\bigl(\min\{L(x-1)+1,X\}\bigr).
\tag{L-32301.7}
\]

Its cap point is

\[
x_*=1+\frac{X-1}{L}.
\tag{L-32301.8}
\]

For `2<=x<x_*`,

\[
L(x-1)+1=Lx\left(1-\frac\alpha x\right),
\]

so the lower analytic branch has the exact expansion

\[
\boxed{
 h_{a,X,s}(x)
=x^{-s}
\left[
 \log L+\log x
 -\sum_{\ell\ge1}\frac{\alpha^\ell}{\ell}x^{-\ell}
\right].
}
\tag{L-32301.9}

For `x>=x_*`,

\[
\boxed{
 h_{a,X,s}(x)=\log X\,x^{-s}.
}
\tag{L-32301.10}

The faster-power coefficient tail in (L-32301.9) obeys the uniform quartic bound

\[
\begin{aligned}
\sum_{\ell\ge1}
\frac{\alpha^\ell}{\ell}
(1+\ell)^4 64^{-\ell}
&\le
\sum_{\ell\ge1}\frac{4^{-\ell}}{\ell}\\
&=\log\frac43
<\frac13.
\end{aligned}
\tag{L-32301.11}

Thus the analytic interior of every depth has a coefficient budget independent of `a` and `X`, apart from the explicit `log L`, `log X`, and one logarithmic Jordan companion.

## 5. Exact cap interface

The two analytic branches agree at `x=x_*`. The profile is continuous there. Put `u=xh'`. Direct differentiation gives the one derivative jump

\[
\boxed{
[u]_{x_*}
=-\frac{Lx_*^{1-s}}{X}.
}
\tag{L-32301.12}

Hence all nonanalyticity of the all-depth profile is concentrated in one declared cap interface. This agrees with the cap ledger of PR #316 `L-30902`.

## 6. Consequence for the live proof graph

Equations (L-32301.6)--(L-32301.12) show that the all-generation problem cannot reside in the analytic power/faster-power interior:

```text
analytic interior and every faster-power descendant
    -> strict 6/7 contraction in a norm already strong enough
       to absorb fourth-order exponent losses;

all depth dependence
    -> explicit affine-log coefficients plus one cap interface.
```

PR #316 already proves polylogarithmic native central-flow debt for every *fresh* cap injection. Therefore the only remaining all-generation question is the propagation/recombination of the cap-interface boundary state itself. Generic analytic-tail growth, fixed-order derivative loss, and proliferation of faster-power channels are removed from the frontier.

## 7. Proof boundary

Closed here, subject to review:

1. the quartic-weighted analytic norm;
2. the exact `6/7` contraction in that stronger norm;
3. the all-depth affine-log expansion;
4. a uniform `1/3` faster-power tail budget;
5. localization of all nonanalyticity to one cap derivative jump.

Open:

1. an all-generation contraction/renewal theorem for the propagated cap-interface measure;
2. Cycle Debt at subpower scale;
3. RH.
