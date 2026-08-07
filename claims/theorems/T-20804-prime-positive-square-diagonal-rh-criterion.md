# T-20804 — Prime-positive square-diagonal criterion

Claim ID: `T-20804`  
Title: One adaptively dilated scalar per square cutoff is equivalent to RH and has no negative prime coefficient  
Status: `PROPOSED — COMPLETE DIAGONAL EXTRACTION; COFINAL POSITIVE-PRIME INEQUALITY OPEN`  
Authoring agent: `gpt56-03-w`  
Created: 2026-08-07  
Dependencies: `L-20814`; `T-20201` / `T-20203` integer-dilation positivity; the explicit screw formula used in `T-20802`  
Scope: a single finite prime-positive inequality for every integer `n`

## 1. Prime-free base point and adaptive integer dilation

Fix once and for all a real number

\[
 \boxed{0<a<\log2.}
 \tag{T-20804.1}
\]

For every integer `n>=2`, put

\[
 \boxed{
 r_n=\left\lceil{2\log n\over a}\right\rceil,
 \qquad
 t_n={2\log n\over r_n}.}
 \tag{T-20804.2}
\]

Then `r_n` is an integer at least two and

\[
 0<t_n\le a<\log2.
 \tag{T-20804.3}
\]

Moreover

\[
 r_n\le{2\log n\over a}+1,
 \qquad
 t_n\ge {a\over1+a/(2\log n)}.
 \tag{T-20804.4}
\]

Thus the lower evaluation stays in one fixed compact prime-free interval. For
example, with

\[
 a={1\over2}\log2,
 \tag{T-20804.5}
\]

one has `e^(t_n)<=sqrt(2)<2` at every level.

Define the adaptive dilation defect

\[
 \boxed{
 \mathcal J_a(n)
 =r_n^2\Psi(t_n)-\Psi(2\log n).}
 \tag{T-20804.6}
\]

This uses a different integer dilation at each square cutoff, but the spectral
filter is always the canonical integer-dilation Fejér portfolio of `T-20203`.

## 2. RH-side positivity

Under RH, the real-zero expansion gives

\[
 \Psi(t)=2\sum_{\gamma>0}m_\gamma
 {1-\cos(\gamma t)\over\gamma^2}.
 \tag{T-20804.7}
\]

For every integer `r>=2`,

\[
 |1-e^{irx}|\le r|1-e^{ix}|,
\]

so

\[
 r^2(1-\cos x)-(1-\cos rx)\ge0.
 \tag{T-20804.8}
\]

Applying this with `r=r_n` and `x=gamma t_n` gives

\[
 \boxed{
 \mathrm{RH}\quad\Longrightarrow\quad
 \mathcal J_a(n)\ge0
 \quad(n\ge2).}
 \tag{T-20804.9}
\]

## 3. Converse from the upper square-sample envelope

Because `t_n` remains in a fixed compact subset of `(0,log2)`, the explicit
prime-free screw term is bounded there:

\[
 |\Psi(t_n)|\le C_a.
 \tag{T-20804.10}
\]

Also `r_n=O_a(log n)`. If, for every `epsilon>0`,

\[
 \mathcal J_a(n)
 \ge-C_\epsilon n^\epsilon
 \tag{T-20804.11}
\]

eventually, then

\[
\begin{aligned}
 \Psi(2\log n)
 &\le r_n^2\Psi(t_n)+C_\epsilon n^\epsilon\\
 &\le C'_a(1+\log n)^2+C_\epsilon n^\epsilon.
\end{aligned}
 \tag{T-20804.12}
\]

Hence

\[
 \bigl(\Psi(2\log n)\bigr)_+=n^{o(1)}.
 \tag{T-20804.13}
\]

`L-20814` now implies RH. Combining this with Section 2 gives the exact
criterion

\[
 \boxed{
 \mathrm{RH}
 \iff
 \bigl(-\mathcal J_a(n)\bigr)_+=n^{o(1)}.}
 \tag{T-20804.14}
\]

In particular,

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal J_a(n)\ge0
 \text{ for every sufficiently large integer }n.}
 \tag{T-20804.15}
\]

This is a genuine diagonal theorem: unlike the compact-cell criterion of
`T-20205`, it requires neither a continuum of base points nor every prime knot
in an exponentially growing annulus. There is exactly one scalar at each square
cutoff.

## 4. Exact finite prime-positive formula

Write the complete screw function as in `T-20802`:

\[
 \Psi(T)=A(T)-
 \sum_{\log q\le T}{\Lambda(q)\over\sqrt q}(T-\log q),
 \tag{T-20804.16}
\]

where `A` is the explicit pole/gamma/trivial-zero term. Since
`t_n<log2`, the small-scale prime sum is empty. Since
`r_nt_n=2log n`, one obtains

\[
 \boxed{
\begin{aligned}
 \mathcal J_a(n)={}&
 r_n^2A(t_n)-A(2\log n)\\
 &+\sum_{q\le n^2}{\Lambda(q)\over\sqrt q}
   \log{n^2\over q}.
\end{aligned}}
 \tag{T-20804.17}
\]

Every prime-power coefficient is nonnegative. The endpoint coefficient at
`q=n^2` is zero. There is

- no adverse old-prime prefix;
- no signed prime cancellation;
- no selected zero data;
- no support interpolation;
- no matrix or Schur complement.

The large positive prime ramp and the explicit archimedean term still cancel to
subpolynomial accuracy. Their common sign structure is a simplification of the
full theorem, not an automatic proof.

## 5. Finite disproof and production interface

At one fixed level, a directed certificate needs only

1. the integer `r_n` and interval for `t_n`;
2. the complete duplicate-free prime-power manifest through `n^2`;
3. outward evaluation of the positive ramp in (T-20804.17);
4. outward evaluation of `A(t_n)` and `A(2log n)`;
5. one final interval for `mathcal J_a(n)`.

A strictly negative upper endpoint is an unconditional RH-disproof witness,
subject to the inherited screw normalization audit. A finite positive sequence,
however long, does not prove eventual positivity.

For stable production, the ramp may be accumulated from the two prefix moments

\[
 P(n^2)=\sum_{q\le n^2}{\Lambda(q)\over\sqrt q},
 \qquad
 Q(n^2)=\sum_{q\le n^2}{\Lambda(q)\log q\over\sqrt q},
 \tag{T-20804.18}
\]

as

\[
 2\log n\,P(n^2)-Q(n^2).
 \tag{T-20804.19}
\]

A direct termwise positive replay should be retained as the independent
producer.

## 6. Best base-point normalization

For fixed `a`,

\[
 r_n^2A(t_n)
 ={4A(a)\over a^2}\log^2n+O_a(\log n)
 \tag{T-20804.20}
\]

along the ceiling schedule. Thus the proof-independent numerical conditioning
may be improved by minimizing

\[
 c(a)={A(a)\over a^2}
 \qquad(0<a<\log2).
 \tag{T-20804.21}
\]

This optimization changes only the polynomial reserve, never the logical
criterion. `O-20807` records an ordinary high-precision minimizer near
`a=0.6422230406`; a proof-grade implementation may instead freeze any simple
rational or logarithmic `a<log2`, such as `(log2)/2`.

## 7. Relation to the live global routes

- `T-20802` takes the exact infimum over every prime prefix.
- `T-20803` replaces its logarithmic moment by a positive shrinking-strip sum.
- `T-20205/L-20207` use an entire compact base interval and then reduce it to
  prime knots.
- The present theorem takes one adaptive point from that prime-free region at
  every critical square sample. The square mesh supplies the missing global
  coverage through `L-20814`.

The remaining theorem is therefore the single all-positive finite inequality

\[
 \boxed{
 r_n^2A(t_n)
 +\sum_{q\le n^2}{\Lambda(q)\over\sqrt q}\log{n^2\over q}
 \ge A(2\log n)-n^{o(1)}.}
 \tag{T-20804.22}
\]

A structural proof of (T-20804.22), with the pole and prime main terms centered
before estimation, proves RH.

## 8. Proof boundary

- The diagonal extraction, prime-positive formula, and converse are exact given
  the imported integer-dilation and screw/Landau claims.
- The theorem does not prove the cofinal inequality (T-20804.22).
- Coarse PNT errors remain exponentially larger than the allowed square-sample
  envelope.
- No RH resolution is claimed.