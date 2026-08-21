# L-32203 — Sharp continuum carry mass forces exact saturation

Claim ID: `L-32203`
Status: **PROPOSED COMPLETE EXACT CONTINUUM LEMMA — INDEPENDENT REVIEW REQUESTED**
Created: 2026-08-08
Dependencies: the continuum carry symbol `I(2)=1/2`
Scope: eliminates smooth-positive-minorant shortcuts; no RH conclusion

## 1. Continuum carry operator

Let

\[
K(x)=\frac{\lfloor x\rfloor[\lfloor x\rfloor+1-x]}x,
\qquad x\ge1,
\]

and for a nonnegative measurable profile `f` put

\[
(Tf)(t)=\int_t^1 f(s)K(s/t)\,ds,
\qquad0<t\le1.
\tag{L-32203.1}
\]

Assume

\[
0\le Tf(t)\le g(t):=t^{-1/2}\log(1/t)
\quad\text{a.e.}
\tag{L-32203.2}
\]

and

\[
\int_0^1s f(s)\,ds<\infty.
\]

## 2. Exact mass identity

Tonelli and the substitution `x=s/t` give

\[
\begin{aligned}
\int_0^1(Tf)(t)\,dt
&=\int_0^1 s f(s)\,ds
  \int_1^\infty K(x)x^{-2}\,dx\\
&=\frac12\int_0^1s f(s)\,ds,
\end{aligned}
\tag{L-32203.3}
\]

using the exact carry-symbol value

\[
\int_1^\infty K(x)x^{-2}\,dx=\frac12.
\]

On the other hand

\[
\boxed{
\int_0^1t^{-1/2}\log(1/t)\,dt=4.}
\tag{L-32203.4}
\]

Therefore every nonnegative continuum packing satisfies

\[
\boxed{
\int_0^1s f(s)\,ds\le8.}
\tag{L-32203.5}
\]

More precisely, the complete integrated slack is

\[
\boxed{
\int_0^1[g(t)-(Tf)(t)]\,dt
=4-\frac12\int_0^1s f(s)\,ds.}
\tag{L-32203.6}
\]

## 3. Equality case

If the sharp mass is attained,

\[
\int_0^1s f(s)\,ds=8,
\]

then the nonnegative function `g-Tf` has integral zero. Hence

\[
\boxed{Tf=g\quad\text{a.e.}}
\tag{L-32203.7}
\]

Thus a positive continuum profile cannot obtain the archimedean mass eight by
leaving a hidden positive residual.  At exact sharp mass it must solve the
full inverse problem.

For an approximate packing,

\[
\int s f=8-\varepsilon
\]

is equivalent to total continuum slack `epsilon/2` in (L-32203.6).

## 4. Consequence for proof design

This rules out a tempting shortcut:

```text
choose an elementary smooth positive density;
approximate the carry kernel crudely;
keep the exact mass eight anyway.
```

Any valid near-sharp positive construction must genuinely drive the complete
carry residual to zero in the source-sensitive norm at the same quantitative
rate as its mass deficit.  The reciprocal-zeta obstruction cannot be bypassed
by a continuum normalization trick.

## 5. Proof boundary

Closed exactly:

- mass upper bound eight for every continuum packing;
- exact integrated-slack identity;
- equality implies exact continuum saturation.

Not proved:

- existence of a nonnegative exact continuum inverse;
- a finite sharp packing;
- RH.
