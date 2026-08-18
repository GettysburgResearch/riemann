# L-98064 — Complement-cube duality extends positive switches to the `3/2 log X` wall

Claim ID: `L-98064`  
Status: **PROVED UNCONDITIONAL UNIFORM ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Depends on: `L-98061--L-98063`; the prime number theorem  
RH status: **not assumed**

For a prime `q>=67`, put

\[
Q(q)=\prod_{67\le r<q\atop r\ {m prime}}r,
\qquad
\sigma(q)=\mu(Q(q)),
\tag{L-98064.1}
\]

and let `U_(<q)` be the complete normalized finite cube of `L-98063`.
Then for every `R>0` one has the exact complement identity

\[
\boxed{
U_{<q}(RQ(q))
={\sigma(q)\over Q(q)}
\sum_{e\mid Q(q)}\mu(e)e\,h(Re).
}
\tag{L-98064.2}
\]

Indeed, substitute `e=Q(q)/d` in the ordinary divisor expansion and use

\[
\mu(Q/e)=\mu(Q)\mu(e).
\]

For the natural switch endpoint, set

\[
R={X\over q^2Q(q)}.
\tag{L-98064.3}
\]

Then

\[
\boxed{
\begin{aligned}
&U_{<q}(X/q)-U_{<q}(X/q^2)\\
&\qquad={\sigma(q)\over Q(q)}
\sum_{e\mid Q(q)}\mu(e)e
\left[h(qRe)-h(Re)\right].
\end{aligned}
}
\tag{L-98064.4}
\]

The fully activated proof of `L-98063` corresponds to `R` bounded below by a
fixed positive constant.  The complement form remains effective when `R`
decays exponentially with `q`.

## Positive dual main term

Use

\[
h(x)=a_*+c_*x^{-1/2}+O(x^{-2}),
\qquad c_*<0.
\tag{L-98064.5}
\]

The constant `a_*` cancels pointwise in the difference.  The complete
`c_*` contribution in (L-98064.4) is

\[
\boxed{
{|c_*|(1-q^{-1/2})\over\sqrt{RQ(q)}}
\prod_{67\le r<q}
\left(1-{1\over\sqrt r}\right)>0.
}
\tag{L-98064.6}

To see this, use

\[
\sum_{e\mid Q}\mu(e)\sqrt e
=
\prod_{r\mid Q}(1-\sqrt r)
=
\sigma(q)\sqrt{Q(q)}
\prod_{r\mid Q}\left(1-{1\over\sqrt r}\right).
\]

Thus the adverse parity of the full complement cancels exactly, leaving a
positive square-root mode.

## Uniform error below the one-third complement depth

Let `x_0` be a fixed threshold beyond which (L-98064.5) holds, and put

\[
E={x_0\over R}.
\]

For complements `e<E`, use the global boundedness of `h`.  Since

\[
\sum_{1\le e<E}e\ll E^2,
\]

their total contribution to (L-98064.4) is

\[
O\!\left({1\over Q(q)R^2}\right).
\tag{L-98064.7}
\]

For `e>=E`, insert (L-98064.5).  The omitted small-complement part of the
`c_*` sum has the same bound, while the asymptotic remainders contribute

\[
O\!\left(
{1\over Q(q)R^2}
\sum_{e\mid Q(q)}{1\over e}
\right)
=
O\!\left({\log q\over Q(q)R^2}\right).
\tag{L-98064.8}
\]

Consequently

\[
\boxed{
\begin{aligned}
U_{<q}(X/q)-U_{<q}(X/q^2)
={}&{|c_*|(1-q^{-1/2})C_q\over\sqrt{RQ(q)}}\\
&+O\!\left({\log q\over Q(q)R^2}\right),
\end{aligned}
}
\tag{L-98064.9}
\]

where

\[
C_q=\prod_{67\le r<q}(1-r^{-1/2})
\ge\exp\!\left[-C{\sqrt q\over\log q}\right].
\tag{L-98064.10}
\]

If, for some fixed `delta>0`,

\[
R\ge\exp\!\left[-\left({1\over3}-\delta\right)q\right],
\tag{L-98064.11}
\]

then the error-to-main ratio in (L-98064.9) is

\[
\ll
Q(q)^{-1/2}R^{-3/2}
\exp\!\left[C{\sqrt q\over\log q}\right]
\le e^{-3\delta q/2+o(q)},
\tag{L-98064.12}
\]

and therefore tends to zero.

## The `3/2` logarithmic switch theorem

The prime number theorem gives

\[
\log Q(q)=q+o(q).
\]

Fix `epsilon>0`.  Uniformly for

\[
\boxed{
67\le q\le\left({3\over2}-\epsilon\right)\log X,
}
\tag{L-98064.13}
\]

one has

\[
\log R
=\log X-2\log q-\log Q(q)
\ge-\left({1\over3}-\delta_\epsilon\right)q
\]

for some `delta_epsilon>0` and all sufficiently large `X`.  Hence
(L-98064.11) applies and

\[
\boxed{
U_{<q}(X/q)-U_{<q}(X/q^2)>0.
}
\tag{L-98064.14}

By `L-98062`, every adaptive cutoff switch through this enlarged range has
positive source-faithful boundary cost.

## New wall

The value `3/2` is the exact frontier of the present **source-blind complement
remainder estimate**.  At `R=e^{-alpha q}`, the positive square-root mode has
size

\[
Q^{-1/2}R^{-1/2}e^{-o(q)},
\]

whereas the absolute local-complement remainder has size `Q^-1 R^-2`.
Their exponents balance at `alpha=1/3`, which corresponds to
`q=(3/2+o(1))log X`.

This is a method wall, not a counterexample.  Crossing it requires signed
cancellation among the small complements or another exact source state.

```text
fully activated switches q~log X          CLOSED BY L-98063
complement-depth alpha<1/3                 CLOSED
switches q<=(3/2-epsilon)log X             PROVED POSITIVE
source-blind complement estimate at 3/2    EXHAUSTED
post-3/2 logarithmic product boundary       OPEN / RH-BEARING
GPC67 / RH                                 UNPROVEN
```