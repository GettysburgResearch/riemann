# L-98910 — The fractional zeta-pole branch has heat-energy rate one half

Claim ID: `L-98910`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Frozen target: PR #613 at `f28aa51a6d6740067202611d8ebda4be2ef0a1c9`  
RH status: **not assumed**

Let

\[
 B_\diamond(s)=\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)},
 \qquad 0<\theta<1,
\]

and take the branch of `B_diamond(s)^theta` positive for real `s>1`. Write

\[
 B_\diamond(s)^\theta=\sum_{n\ge1}b_\theta(n)n^{-s}
 \qquad(\Re s>1)
\]

and define the heat packet used in PR #613,

\[
 \mathscr B_{\theta,T}(\tau)
 =\sum_{n\ge1}\frac{b_\theta(n)}{\sqrt n}
   e^{-(\log n)^2/(4T)}e^{-i\tau\log n}.
 \tag{L-98910.1}
\]

Then, for fixed `theta` and uniformly for `|tau|<=T^(-1/2)`,

\[
\boxed{
 \mathscr B_{\theta,T}(\tau)
 =\frac{2\sqrt\pi(3/8)^\theta}{\Gamma(-\theta)}
  T^{-\theta-1/2}(1-2i\tau)^{-\theta-1}
  e^{T(1/2-i\tau)^2}
  \bigl(1+O_\theta(T^{-1/2})\bigr).
 }
 \tag{L-98910.2}
\]

Consequently, with

\[
 w_T(\tau)=\sqrt{T/\pi}\,e^{-T\tau^2},
\]

one has

\[
\boxed{
 \int_{\mathbb R}|\mathscr B_{\theta,T}(\tau)|^2w_T(\tau)\,d\tau
 =\frac{4\pi(3/8)^{2\theta}}
        {\sqrt3\,|\Gamma(-\theta)|^2}
  T^{-2\theta-1}e^{T/2}
  \bigl(1+o_\theta(1)\bigr).
 }
 \tag{L-98910.3}
\]

Thus the source-side heat energy at center zero has exponential rate `1/2`,
independent of the fractional intensity.

## Proof

Near `s=1`,

\[
 \zeta(s)^{-1}=(s-1)(1+O(s-1))
\]

and

\[
 (1-2^{-s})(1-2^{-s-1})=\frac38+O(s-1).
\]

Hence

\[
 B_\diamond(s)^\theta
 =(3/8)^\theta(s-1)^\theta(1+O_\theta(s-1)).
 \tag{L-98910.4}
\]

Selberg--Delange, applied with exponent `-theta`, gives

\[
 A_\theta(x):=\sum_{n\le x}b_\theta(n)
 =\frac{(3/8)^\theta}{\Gamma(-\theta)}
   x(\log x)^{-\theta-1}
   \left(1+O_\theta((\log x)^{-1})\right).
 \tag{L-98910.5}
\]

Partial summation in (L-98910.1), followed by `x=e^u`, reduces the leading term
to

\[
 \frac{(3/8)^\theta}{\Gamma(-\theta)}
 \int_0^\infty
 u^{-\theta-1}e^{u/2-u^2/(4T)-i\tau u}\,du.
 \tag{L-98910.6}
\]

The saddle is `u_0=T(1-2i tau)`. Completing the square and applying the uniform
complex Laplace expansion proves (L-98910.2). Squaring it and using

\[
 \sqrt{T/\pi}\int_{\mathbb R}e^{-3T\tau^2}\,d\tau=1/\sqrt3
\]

proves (L-98910.3).

## Scope

This is the deterministic contribution of the fractional branch at the zeta
pole. It does not use or assume an off-line zero and is present even if RH is
true.
