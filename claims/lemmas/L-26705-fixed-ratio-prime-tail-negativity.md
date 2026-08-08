# L-26705 — Fixed-ratio prime tails are eventually nonpositive

Claim ID: `L-26705`  
Title: The continuum parabolic tail majorization transfers unconditionally to prime-sampled residual tails on every fixed outer ratio  
Status: **PROPOSED COMPLETE ASYMPTOTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: PR #265 `L-26202`; PR #248 `L-24507`; the prime number theorem  
Scope: fixed-ratio localization of the queue in `L-26704`; no shrinking-ratio estimate and no RH conclusion

## 1. Statement

For the parabolic seed, let

\[
r_X(p)
=v_p(b_X^{(0)})-p^{-1/2}\log(X/p)
\tag{L-26705.1}
\]

for ordinary primes `p<=X`.

For every fixed

\[
0<\vartheta<1,
\]

there exists `X_0(vartheta)` such that, for every integer `X>=X_0(vartheta)` and every prime `P` with

\[
\vartheta X\le P\le X,
\]

one has

\[
\boxed{
\sum_{P\le p\le X}r_X(p)\le0.
}
\tag{L-26705.2}

Consequently, if a tail realizes the positive queue of `L-26704`, then either the queue is zero or its initial prime satisfies

\[
\boxed{
\frac{P_X^{\rm start}}{X}\longrightarrow0.
}
\tag{L-26705.3}

Thus the entire positive queue is forced into a genuinely lower multiplicative scale.

## 2. Uniform one-row asymptotic

Retain the continuum parabolic derivative

\[
g(u)=\frac{\log u+4}{\sqrt u}-4
\tag{L-26705.4}
\]

and its finite dilation defect

\[
E(\theta)
=\sum_{1\le k\le1/\theta}g(k\theta)
-\theta^{-1/2}\log(1/\theta).
\tag{L-26705.5}
\]

Fix `vartheta>0`. On

\[
\vartheta\le\theta\le1,
\]

there are at most `1/vartheta` summands and `g'` is bounded on `[vartheta,1]`. The same finite-difference comparison used in `L-24507` therefore gives uniformly

\[
\boxed{
\sqrt X\,r_X(q)
=E(q/X)+O_{\vartheta}(X^{-1})
}
\tag{L-26705.6}

for every integer `q` in that ratio range. Terminal equalities `kq=X` cause no error because both the discrete terminal term and `g(1)` vanish.

## 3. Prime Riemann sums

On every compact interval `[vartheta,1]`, the function `E` is bounded and piecewise continuously differentiable, with only finitely many reciprocal-integer knots.

The prime number theorem and partial summation give, uniformly for

\[
\vartheta\le t\le1,
\]

\[
\boxed{
\frac{\log X}{X}
\sum_{tX\le p\le X}E(p/X)
=
\int_t^1E(u)\,du+o_{\vartheta}(1).
}
\tag{L-26705.7}

A direct proof first handles step functions on a finite partition avoiding the reciprocal knots, applies the uniform PNT to every interval, and then squeezes `E` between upper and lower step functions. The error is uniform because the partition is fixed once `vartheta` and the approximation accuracy are fixed.

Combining (L-26705.6) with (L-26705.7), and using

\[
\pi(X)=O(X/\log X),
\]

gives

\[
\boxed{
\frac{\log X}{\sqrt X}
\sum_{tX\le p\le X}r_X(p)
=
H(t)+o_{\vartheta}(1),
}
\tag{L-26705.8}

where

\[
H(t)=\int_t^1E(u)\,du.
\tag{L-26705.9}

## 4. Strict continuum tail sign

PR #265 `L-26202` proves

\[
H(t)\le0
\qquad(0<t\le1).
\tag{L-26705.10}

Its reciprocal-cell proof is strict in the interior:

\[
\boxed{
H(t)<0
\qquad(0<t<1).
}
\tag{L-26705.11}

Indeed every nontrivial reciprocal endpoint is strictly negative; on each cell the convexity or monotonicity argument bounds the interior strictly below the zero endpoint, with equality only at `t=1` and in the limiting total-mass identity `t downarrow0`.

If `vartheta<1/28`, compactness gives

\[
\max_{\vartheta\le t\le1/28}H(t)=-c_{\vartheta}<0.
\tag{L-26705.12}

Equation (L-26705.8) then makes every prime tail beginning in that range negative for all sufficiently large `X`.

For `t>=1/28`, the pointwise outer theorem `L-24507` gives

\[
r_X(p)\le0
\]

for every prime in the tail once `X>=104301`. Thus all such tails are nonpositive without an asymptotic summation argument.

This proves (L-26705.2).

## 5. Queue localization

Let

\[
\mathcal Q_X(b_X^{(0)})
=
\max_{P\le X}
\left(\sum_{P\le p\le X}r_X(p)\right)_+.
\]

For any fixed `vartheta>0`, Section 4 rules out every maximizing prime `P>=vartheta X` for sufficiently large `X`, unless the maximum is zero. Since `vartheta` is arbitrary, (L-26705.3) follows.

The result is a genuine strict-scale theorem. It is stronger than the fixed outer sign `q>=X/28`: positive residuals may exist well below that line, but no positive **complete tail** can remain at any fixed ratio.

## 6. What remains

The theorem does not bound a tail whose initial prime tends to zero relative to `X`. That shrinking-ratio regime contains the same logarithmic/inverse-zeta scalar isolated by `L-26703/T-26702`.

A completion may now seek a recurrence of the form

\[
\mathcal Q_X
\le
\mathcal Q_{Y_X}
+X^{o(1)},
\qquad
Y_X=o(X),
\tag{L-26705.13}

or, preferably, a fixed-ratio half-scale recurrence after the dyadic two-contact recombination of PR #269.

## 7. Proof boundary

Closed here, subject to review:

1. uniform finite-difference convergence on fixed ratio intervals;
2. uniform prime Riemann-sum convergence;
3. transfer of strict continuum tail negativity;
4. localization of every positive prime-tail queue below every fixed output ratio.

Open:

1. a quantitative shrinking-ratio tail estimate;
2. a lower-scale recurrence with subpower boundary cost;
3. the critical prime-ramp lower bound and RH.
