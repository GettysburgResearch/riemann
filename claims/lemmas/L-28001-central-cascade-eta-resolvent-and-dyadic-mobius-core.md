# L-28001 — The full central cascade is the eta resolvent and decodes an odd-Möbius core

Claim ID: `L-28001`  
Title: The smooth central residual has multiplier `1-eta(s)`; its full resolvent is `1/eta(s)` and retains every off-line zeta pole  
Status: **PROPOSED COMPLETE EXACT TRANSFORM LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: the continuum operator of PR #280; elementary Dirichlet-series algebra  
Scope: exact transform/source identification; no positivity, energy bound, or RH conclusion

## 1. Dilation coefficient

For

\[
(\mathcal Tf)(x)
=\sum_{k\ge1}[f(2kx)-f((2k+1)x)],
\]

put

\[
c(1)=0,
\qquad
c(n)=
\begin{cases}
1,&2\mid n,\\
-1,&n\ge3\text{ odd}.
\end{cases}
\tag{L-28001.1}
\]

Then

\[
\mathcal Tf(x)=\sum_{n\ge1}c(n)f(nx)
\tag{L-28001.2}
\]

whenever the source is compactly supported so that the sum is finite.

For `Re(s)>1`,

\[
\begin{aligned}
C(s)
&:=\sum_{n\ge1}\frac{c(n)}{n^s}\\
&=2^{-s}\zeta(s)-[(1-2^{-s})\zeta(s)-1]\\
&=1-(1-2^{1-s})\zeta(s).
\end{aligned}
\tag{L-28001.3}
\]

Writing

\[
\eta(s)=(1-2^{1-s})\zeta(s),
\]

we obtain the exact symbol

\[
\boxed{C(s)=1-\eta(s).}
\tag{L-28001.4}
\]

Thus

\[
\boxed{I-\mathcal T\quad\text{has Mellin multiplier}\quad\eta(s).}
\tag{L-28001.5}
\]

## 2. Formal full resolvent

Where the Neumann series converges, and thereafter by meromorphic continuation,

\[
\sum_{j\ge0}\mathcal T^j
=(I-\mathcal T)^{-1}
\]

has multiplier

\[
\boxed{
\frac1{\eta(s)}
=\frac1{(1-2^{1-s})\zeta(s)}.
}
\tag{L-28001.6}
\]

The Euler factor `1-2^(1-s)` vanishes only on the vertical line `Re(s)=1`. It cannot cancel a nontrivial zeta zero in the open critical strip.

Therefore the complete central resolvent retains every hypothetical off-line zeta pole. The infinite cascade is not an arithmetic-free positive contraction; it is another exact gauge for the reciprocal-zeta source.

## 3. Exact Dirichlet coefficients

In the absolute-convergence half-plane,

\[
\frac1{1-2^{1-s}}
=\sum_{a\ge0}2^a(2^a)^{-s},
\]

and

\[
\frac1{\zeta(s)}=\sum_{m\ge1}\frac{\mu(m)}{m^s}.
\]

Write

\[
n=2^v m,
\qquad m\text{ odd}.
\]

Only the terms `a=v` and, when `v>=1`, `a=v-1` survive the Möbius factor. The coefficient `a_eta(n)` of `1/eta(s)` is therefore

\[
\boxed{
a_\eta(n)=
\begin{cases}
\mu(m),&v=0,\\[1mm]
2^{v-1}\mu(m),&v\ge1.
\end{cases}}
\tag{L-28001.7}
\]

This is a signed odd-Möbius core with an explicit dyadic valuation weight. It is not coefficientwise positive.

## 4. Relation to the repository's dyadic sources

The central cascade, the Euler-aligned dyadic Mertens shell, and the opposite-parity carry sources differ only by finite two-adic multipliers and half-shifts. In particular:

```text
single central cascade resolvent  -> 1/eta(s);
dyadic shell source               -> finite Euler factor / zeta(s);
opposite-parity source            -> two finite Euler factors / zeta(s).
```

All three retain the same nontrivial zero set. The compact two-contact and factor-five carry identities therefore describe the boundary source left after the smooth central contraction, rather than a separate arithmetic obstruction.

## 5. Why boundary knots are load bearing

For the stopped critical source, smooth Mellin multiplication describes each open reciprocal cell. The endpoint derivatives generate atoms at

\[
x=1/n.
\]

Those atoms carry precisely the finite dyadic source which is absent from a calculation that commutes logarithmic derivatives through the stopped dilation sum. The exact counterexamples in `R-28001` are the first visible manifestations.

Consequently a corrected proof must split

\[
\boxed{
\text{central output}
=
\text{smooth eta-contracted bulk}
+
\text{reciprocal-knot dyadic boundary source}.
}
\tag{L-28001.8}

Neither term may be discarded:

- the smooth bulk supplies the factor `1-log 2` at the mass coordinate;
- the boundary source supplies the reciprocal-zeta pole and the fixed-ratio Mertens mutation.

## 6. Scope consequence

A theorem proving a generic all-stage positive central cascade would imply positivity for a resolvent with multiplier `1/eta(s)` and would therefore already contain the RH-bearing source. The exact transform does not refute such a source-specific theorem, but it rules out treating it as a routine consequence of the scalar mass contraction.

The correct next theorem must control the dyadic knot source jointly with the smooth bulk, preferably before any absolute value or positive-part operation.

## 7. Proof boundary

Established exactly:

1. the central multiplier `1-eta(s)`;
2. the full resolvent multiplier `1/eta(s)`;
3. the explicit odd-Möbius Dirichlet coefficients;
4. persistence of every nontrivial zeta pole;
5. the conceptual identification of the reciprocal-knot source.

Not established:

1. a positive parity-paired boundary contraction;
2. a subexponential source energy bound;
3. RH.