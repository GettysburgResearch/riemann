# L-97700 - Complete small-prime cube and exact largest-prime Bellman identity

Claim ID: `L-97700`  
Status: **PROVED EXACT SOURCE THEOREM + UNCONDITIONAL ASYMPTOTIC POSITIVITY**  
Created: 2026-08-18  
Inputs: PR #576 `L-97400`; the exact finite-prime recurrence of PR #564/#557  
RH status: **not assumed**

Let

\[
 Z=Z_X=(\log X)^{1/4},
 \qquad
 Q_Z=\prod_{67\le p\le Z}p.
\]

Define the *complete* small-prime cube

\[
 \mathcal B_Z(X)=
 \sum_{d\mid Q_Z}\frac{\mu(d)}{\sqrt d}\,b(X/d),
 \qquad
 U_Z(X)=\frac{\mathcal B_Z(X)}{\sqrt X}.
\]

Unlike PR #578's depth-`L` cube, this includes every subset of the primes below
`Z`.

## 1. Complete cube positivity

For all sufficiently large `X`,

\[
 \boxed{\mathcal B_Z(X)>0.}
\]

More precisely,

\[
 \boxed{
 \mathcal B_Z(X)
 =a_*\sqrt X\prod_{67\le p\le Z}\left(1-\frac1p\right)
 +c_*\prod_{67\le p\le Z}\left(1-\frac1{\sqrt p}\right)
 +o(1),
 }
\]

where

\[
 a_*=12\prod_{p\le61}\left(1-\frac1p\right)>0.
\]

Consequently

\[
 U_Z(X)\sim a_*\prod_{67\le p\le Z}\left(1-\frac1p\right)
 \asymp\frac1{\log Z}.
\]

### Proof

For `Y` beyond the fixed `P_61` activation range, `L-97400` gives

\[
 b(Y)=a_*\sqrt Y+c_*+O(Y^{-3/2}).
\]

The largest divisor of `Q_Z` is

\[
 Q_Z=\exp((1+o(1))Z)=X^{o(1)},
\]

so `X/d` lies uniformly in that asymptotic range. Substitution and exact divisor
factorization give the two Euler products above. The total remainder is

\[
 O\!\left(X^{-3/2}\sum_{d\mid Q_Z}d\right)
 =O\!\left(X^{-3/2}\prod_{67\le p\le Z}(1+p)\right)=o(1).
\]

The positive square-root main term dominates.

## 2. Largest-prime Bellman ownership

Order the active primes greater than `Z` as

\[
 Z<p_1<\cdots<p_k\le X/2.
\]

Starting from `U_0=U_Z`, adjoin them in increasing order by the exact normalized
finite-prime recurrence

\[
 U_i(Y)=U_{i-1}(Y)-\frac1{p_i}U_{i-1}(Y/p_i),
\]

with zero extension below support. Then `U_k(X)` is the actual complete
normalized rough scalar at the root and

\[
 \boxed{
 U_k(X)=U_Z(X)-
 \sum_{Z<p\le X/2}\frac1p\,U_{<p}(X/p),
 }
\]

where `U_<p` means that every rough prime in `(Z,p)` has already been adjoined.
Every nonempty large-prime history is owned exactly once, by its largest prime.

Expanding the child gives the explicit signed Möbius correlation

\[
 \boxed{
 U_{<p}(Y)=
 \sum_{\substack{v\ \mathrm{squarefree}\\
                  Z<P^-(v),\ P^+(v)<p}}
 \frac{\mu(v)}v\,U_Z(Y/v).
 }
\]

Therefore

\[
 \boxed{
 U_k(X)=U_Z(X)-
 \sum_{Z<p\le X/2}\frac1p
 \sum_{\substack{v\ \mathrm{squarefree}\\
                  Z<P^-(v),\ P^+(v)<p}}
 \frac{\mu(v)}v\,U_Z(X/(pv)).
 }
\]

All support restrictions are carried by the zero extension of `U_Z`; there is
no unrestricted reservoir, no duplicated history, and no absolute-value
replacement.

## 3. Exact relation to PR #578's residual

Let `S` be the child operator using primes at most `Z`, `H=R-S`, and

\[
 P_{<L}(T)=\sum_{j=0}^{L-1}(-T)^j.
\]

The truncated large-prime residual has the exact noncommutative Duhamel form

\[
 \boxed{
 P_{<L}(R)b-P_{<L}(S)b
 =-\sum_{\substack{a,b\ge0\\a+b\le L-2}}
 (-1)^{a+b}S^a H R^b b.
 }
\]

Thus the first large prime is preceded by `a` small-prime owners and followed by
at most `b` further owners. This is the exact short-history form requested by
`LAPBR67`; `R-97700` proves that its total sign is nevertheless negative at the
published depth.
