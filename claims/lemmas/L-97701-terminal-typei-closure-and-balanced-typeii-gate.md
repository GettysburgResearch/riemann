# L-97701 - Terminal Type-I closure and the balanced large-prime Type-II gate

Claim ID: `L-97701`  
Status: **PROVED EXACT DECOMPOSITION; TYPE-I RANGE CLOSED; ONE TYPE-II ESTIMATE OPEN**  
Created: 2026-08-18  
Depends on: `L-97700`; classical Mertens/PNT estimates  
RH status: **unproved**

Use the exact largest-prime Bellman budget

\[
 \mathfrak D_Z(X)=
 \sum_{Z<p\le X/2}\frac1pU_{<p}(X/p).
\]

Split it at `p=X/Z`:

\[
 \mathfrak D_Z(X)=\mathfrak I_Z(X)+\mathfrak T_Z(X),
\]

where

\[
 \mathfrak I_Z(X)=
 \sum_{X/Z<p\le X/2}\frac1pU_Z(X/p)
\]

and

\[
 \mathfrak T_Z(X)=
 \sum_{Z<p\le X/Z}\frac1pU_{<p}(X/p).
\]

The equality in the Type-I range is exact: `X/p<Z`, so no prime greater than
`Z` is active in the child.

## 1. Terminal Type-I range

The complete small-prime cube obeys the elementary uniform bound

\[
 |U_Z(y)|\ll\log(2y)\qquad(2\le y\le Z).
\]

Indeed `b(t)/sqrt(t)` is bounded and the unsigned divisor mass is

\[
 \prod_{67\le q\le y/2}(1+1/q)\ll\log(2y).
\]

Mertens' theorem gives

\[
 \sum_{X/Z<p\le X/2}\frac1p
 \ll\frac{\log Z}{\log X}.
\]

Therefore

\[
 \boxed{
 |\mathfrak I_Z(X)|
 \ll\frac{(\log Z)^2}{\log X}
 =o(U_Z(X)).
 }
\]

This is a genuinely terminal one-large-prime estimate. No absolute value is
placed on the Type-II source and no large sieve is used.

## 2. Signed Type-II correlation

The remaining term is exactly

\[
 \boxed{
 \mathfrak T_Z(X)=
 \sum_{Z<p\le X/Z}\frac1p
 \sum_{\substack{v\ \mathrm{squarefree}\\
                  Z<P^-(v),\ P^+(v)<p}}
 \frac{\mu(v)}v\,U_Z(X/(pv)).
 }
\]

Both the owner prime and its child endpoint are at least `Z`. The condition
`P^+(v)<p` is the literal largest-prime owner and removes all multiplicity.
For a dyadic owner block `p~P` and a product block `v~V`, the source is the
signed bilinear form

\[
 \mathfrak T(P,V;X)=
 \sum_{p\sim P}\frac1p
 \sum_{\substack{v\sim V\\Z<P^-(v),\ P^+(v)<p}}
 \frac{\mu(v)}v\,U_Z(X/(pv)).
\]

Only blocks with `PV<=X/2` occur. In the original depth-`L` Duhamel expansion,
the remaining history has length at most `L-2-a`; the corrected full Bellman
form resums those short blocks instead of demanding their separate positivity.

## 3. Minimal finishing estimate

Define `BLPTE67` (Balanced Large-Prime Type-II Estimate, factor 67) by

\[
 \boxed{
 \mathfrak T_Z(X)\le U_Z(X)-\mathfrak I_Z(X)
 }
\]

for every sufficiently large root endpoint, together with the identical
state-wise inequality after replacing `67` by the state's least allowed prime.

This is the strongest exact replacement for `LAPBR67`:

- it is one-sided rather than absolute;
- it retains every Möbius sign;
- it is largest-prime owned and activation exact;
- Type I has already been removed;
- it is a prime-versus-Möbius Type-II correlation;
- it is exactly sufficient, with no reserve or Hall surrogate.

Since `mathfrak I_Z=o(U_Z)`, it is enough to prove the slightly stronger
asymptotic form

\[
 \mathfrak T_Z(X)\le(1-\eta_X)U_Z(X),
 \qquad
 \eta_X\gg\frac{(\log Z)^3}{\log X}.
\]

No such Type-II estimate is proved in this packet. It is the single remaining
arithmetic theorem.
