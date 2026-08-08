# L-27903 — Finite one-crossing collapses WSTS to one total dyadic shell scalar

Claim ID: `L-27903`  
Title: Once the shell residual has one sign change, the maximum over all prime tails is attained at the full tail and the RH frontier becomes one endpoint-domination inequality  
Status: **PROPOSED COMPLETE EXACT REDUCTION**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #276 at `a65a02b9463c1cc3a10d0af03ab359a637e357cd`  
Dependencies: `L-27902`; PR #276 `T-27501`  
Scope: exact finite order algebra; no sign or asymptotic estimate is asserted

## 1. Finite shell and WSTS charge

For

\[
Y=\lfloor X/2\rfloor,
\]

retain

\[
s_X(p)=r_X(p)-\mathbf1_{p\le Y}r_Y(p)
\]

on ordinary primes. Put

\[
a_X(p)=(\log p)s_X(p).
\]

The WSTS charge is

\[
\mathcal B_X
=\max_z\left[\sum_{z\le p\le X}a_X(p)\right]_+.
\tag{L-27903.1}
\]

## 2. One crossing determines every tail

Assume `FSCR`: there is a threshold `q_*(X)` such that

\[
s_X(p)\ge0\quad(p\le q_*(X)),
\qquad
s_X(p)\le0\quad(p>q_*(X)).
\]

Because `log p>0`, the same order holds for `a_X(p)`.

Starting from the largest prime and moving the tail endpoint downward, the tail sum first decreases while only nonpositive terms are added. Once the crossing is passed, it increases monotonically while only nonnegative terms are added. Therefore its maximum is attained either at the empty tail or at the complete prime tail.

Hence

\[
\boxed{
\mathcal B_X
=\left[\sum_{p\le X}(\log p)s_X(p)\right]_+.
}
\tag{L-27903.2}
\]

The entire family of WSTS cuts has collapsed to one scalar.

## 3. The scalar is the dyadic increment of the prime-ramp discrepancy

Define

\[
\boxed{
\Delta_X
=J_{\mathbb P,X}(b_X^{(0)})-P_X,
}
\tag{L-27903.3}
\]

where

\[
P_X=\sum_{p\le X}{\log p\over\sqrt p}\log{X\over p}.
\]

By the exact ordinary-prime dual identity,

\[
\Delta_X=\sum_{p\le X}(\log p)r_X(p).
\tag{L-27903.4}
\]

Consequently

\[
\boxed{
\sum_{p\le X}(\log p)s_X(p)
=\Delta_X-\Delta_Y.
}
\tag{L-27903.5}
\]

Under `FSCR`,

\[
\boxed{
\mathcal B_X=[\Delta_X-\Delta_{\lfloor X/2\rfloor}]_+.
}
\tag{L-27903.6}
\]

Thus WSTS is reduced to dyadic one-sided regularity of one globally meaningful discrepancy.

## 4. Endpoint derivative of the discrepancy

For real `X` away from an integer support knot, differentiate the parabolic seed with respect to `log X`:

\[
\boxed{
\dot b_X(m)
:=\partial_{\log X}b_X(m)
=2\sqrt m\left(1-\sqrt{m/X}\right)
\mathbf1_{m\le X}.}
\tag{L-27903.7}
\]

Define its ordinary-prime endpoint residual

\[
\eta_X(p)
=v_p(\dot b_X)-p^{-1/2}.
\tag{L-27903.8}
\]

The entering endpoint has zero coefficient, so differentiation creates no omitted support atom. Therefore

\[
\boxed{
\partial_{\log X}\Delta_X
=\sum_{p\le X}(\log p)\eta_X(p).
}
\tag{L-27903.9}
\]

This is the infinitesimal endpoint-atom version of the same prime-sampling problem.

## 5. Endpoint Prime Domination

Define **EPD** by

\[
\boxed{
\sum_{p\le X}(\log p)
\left[v_p(\dot b_X)-p^{-1/2}\right]
\le0
\qquad(X\ge X_0).}
\tag{EPD}
\]

If `EPD` holds, then `Delta_X` is nonincreasing. In particular,

\[
\Delta_X-\Delta_{\lfloor X/2\rfloor}\le0
\]

for all sufficiently large `X`, after the bounded integer-knot correction is included.

Combining with (L-27903.6),

\[
\boxed{
\mathrm{FSCR}+\mathrm{EPD}
\Longrightarrow
\mathcal B_X=0
\quad\text{eventually}.}
\tag{L-27903.10}
\]

This is stronger than WSTS.

## 6. A weaker endpoint theorem is enough

Full pointwise monotonicity is not necessary. Under `FSCR`, it suffices to prove

\[
\boxed{
[\Delta_X-\Delta_{\lfloor X/2\rfloor}]_+
=O_\varepsilon(X^\varepsilon).}
\tag{L-27903.11}
\]

The proposal in `T-27901` nevertheless targets `EPD`, because it is a clean global sign theorem with an exact endpoint source and no tail maximum.

## 7. Why this is a full-problem attack

The former carry graph ended at an arbitrary maximum over all prime tails. The one-crossing geometry removes that combinatorial freedom. The final target is now a single scalar at each scale:

```text
endpoint parabolic atom
versus
critical ordinary-prime increment.
```

It can be attacked through any of the repository's global coordinates:

- Kummer/Legendre carry entropy;
- squarefree incidence collectors;
- reflected two-frequency Selberg energy;
- the parity-paired inverse-zeta frame;
- the first-cell Mertens mutation;
- the square-screw explicit formula.

Any successful proof of `EPD` must still preserve the logarithmic/von-Mangoldt ray; the reduction has not hidden the RH scalar.

## 8. Proof boundary

Closed exactly:

- one-crossing tail collapse;
- identification of the total shell with `Delta_X-Delta_Y`;
- endpoint derivative formula;
- `FSCR+EPD => B_X=0 => WSTS`.

Open:

- `FSCR`;
- `EPD` or its dyadic subpower weakening;
- WSTS and RH.
