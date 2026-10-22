# L-90007 — A resident RH-to-WSTS sampling bound

Claim ID: `L-90007` (provisional range 90001+; allocate at registry before integration)  
Status: **PROPOSED COMPLETE CONDITIONAL THEOREM — independent review required**  
Authoring agent: `gpt56-sol`  
Date: 2026-08-09  
Depends on: Proposition 1 and the Moat Lemma of `T-90001`; the classical RH estimate `vartheta(t)-t = O(sqrt(t) log^2(2t))`.  
Scope: proves `RH => WSTS`; it does not prove RH.

## 1. Statement

With the notation of `T-90001`, assume RH. Then uniformly for integer `X>=4`,
\[
\boxed{
B_X\ll\log^4(2X).
}
\tag{L-90007.1}
\]
In particular, for every `epsilon>0`,
\[
B_X=O_\varepsilon(X^\varepsilon),
\]
so WSTS holds.

The exponent four is intentionally the conservative resident bound.  The
source session reports a sharper `O(log^3 X)` estimate after exploiting an
additional dyadic-difference cancellation.  That refinement is not needed for
the equivalence and is not promoted by this lemma without its complete
bookkeeping.

## 2. Exact cell formula

Recall
\[
E(\theta)
=F(\theta)-\theta^{-1/2}\log(1/\theta),
\qquad 0<\theta\le1.
\]
On the cell
\[
\frac1{N+1}<\theta\le\frac1N,
\]
`T-90001` gives
\[
\boxed{
E(\theta)
=\theta^{-1/2}
[A_N+(S_N+1)\log\theta+4S_N]-4N,
}
\tag{L-90007.2}
\]
where
\[
S_N=\sum_{k\le N}k^{-1/2},
\qquad
A_N=\sum_{k\le N}k^{-1/2}\log k.
\]
The entering summand at a reciprocal knot has value `g(1)=0`; hence `E` is
continuous and piecewise continuously differentiable.

## 3. Two elementary sum-integral estimates

Monotone integral comparison gives
\[
\boxed{S_N=2\sqrt N+O(1).}
\tag{L-90007.3}
\]
For
\[
f(x)=x^{-1/2}\log x,
\]
the total variation on `[1,infinity)` is finite because
\[
|f'(x)|\ll x^{-3/2}(1+\log x)
\]
is integrable.  Therefore the unit-interval sum-integral error is bounded, and
\[
\begin{aligned}
A_N
&=\int_1^N x^{-1/2}\log x\,dx+O(1)\\
&=2\sqrt N\log N-4\sqrt N+O(1).
\end{aligned}
\tag{L-90007.4}
\]

Put
\[
x=\theta^{-1},
\qquad N\le x<N+1.
\]
Then
\[
\log x=\log N+O(N^{-1}),
\qquad
\sqrt x=\sqrt N+O(N^{-1/2}).
\tag{L-90007.5}
\]
Using `log(theta)=-log(x)`, equations (L-90007.3)--(L-90007.5) give
\[
A_N-(S_N+1)\log x+4S_N
=4\sqrt N+O(1+\log N).
\tag{L-90007.6}
\]
After multiplication by `sqrt(x)`, the leading `4N` cancels the final term in
(L-90007.2). Thus
\[
\boxed{
|E(\theta)|
\ll\theta^{-1/2}[1+\log(1/\theta)].
}
\tag{L-90007.7}
\]

## 4. Piecewise variation

Inside one reciprocal cell, differentiation of (L-90007.2) gives
\[
E'(\theta)
=\theta^{-3/2}
\left[
(S_N+1)
-\frac12\{A_N+(S_N+1)\log\theta+4S_N\}
\right].
\tag{L-90007.8}
\]
The bracketed quantity has its two `2 sqrt(N)` main terms cancel by
(L-90007.3) and (L-90007.6), leaving `O(1+log N)`. Hence
\[
\boxed{
|E'(\theta)|
\ll\theta^{-3/2}[1+\log(1/\theta)]
}
\tag{L-90007.9}
\]
on every open cell. Since `E` is continuous at reciprocal knots, no knot atom
appears in its bounded-variation measure.

## 5. Uniform finite dyadic shell

For
\[
Y=\lfloor X/2\rfloor,
\qquad c=Y/X\in[1/3,1/2],
\]
put
\[
E_c(\theta)
=E(\theta)-c^{-1/2}E(\theta/c)\mathbf1_{\theta\le c}.
\]
The scale factors cancel exactly in (L-90007.7)--(L-90007.9), and `c` stays in
a fixed compact subinterval of `(0,1)`. Therefore, uniformly in the actual
finite ratio,
\[
\boxed{
|E_c(\theta)|
\ll\theta^{-1/2}[1+\log(1/\theta)],
}
\tag{L-90007.10}
\]
\[
\boxed{
|E_c'(\theta)|
\ll\theta^{-3/2}[1+\log(1/\theta)]
}
\tag{L-90007.11}
\]
away from the finitely many cell boundaries. At `theta=c`, continuity follows
from `E(1)=0`.

## 6. RH input and Stieltjes integration by parts

Assume RH. The classical von Koch bound, with elementary prime-power removal,
gives
\[
\boxed{
R(t):=\vartheta(t)-t
=O(\sqrt t\log^2(2t)).
}
\tag{L-90007.12}
\]
Proposition 1 of `T-90001` contains the exact sampling remainder
\[
\mathcal E_{X,Y}(z)
=X^{-1/2}\int_{[z,X]}E_c(t/X)\,dR(t),
\qquad2\le z\le X.
\tag{L-90007.13}
\]
Because `E_c` is continuous and piecewise absolutely continuous and
`E_c(1)=0`, Stieltjes integration by parts gives
\[
\begin{aligned}
\mathcal E_{X,Y}(z)
={}&-X^{-1/2}E_c(z/X)R(z^-)\\
&-X^{-3/2}\int_z^X R(t)E_c'(t/X)\,dt,
\end{aligned}
\tag{L-90007.14}
\]
with the usual harmless one-sided endpoint convention at a prime.

The boundary term satisfies, by (L-90007.10) and (L-90007.12),
\[
\ll [1+\log(X/z)]\log^2(2z)
\ll\log^3(2X).
\tag{L-90007.15}
\]
For the integral term, (L-90007.11)--(L-90007.12) give
\[
\begin{aligned}
X^{-3/2}\int_z^X|R(t)|\,|E_c'(t/X)|dt
&\ll\int_z^X
\frac{\log^2(2t)[1+\log(X/t)]}{t}\,dt\\
&\ll\log^4(2X).
\end{aligned}
\tag{L-90007.16}
\]
Thus
\[
\boxed{
\sup_{2\le z\le X}|\mathcal E_{X,Y}(z)|
\ll\log^4(2X).
}
\tag{L-90007.17}
\]

## 7. Proposition 1 plus the Moat

Proposition 1 gives
\[
T^s(z)
=\sqrt X\,H_c(z/X)+\mathcal E_{X,Y}(z)+\mathrm{fl}(z),
\]
with
\[
|\mathrm{fl}(z)|\ll1+\log X.
\]
The Moat Lemma proves
\[
H_c(\theta)\le0
\qquad(0<\theta\le1).
\]
Therefore the deterministic continuum term cannot contribute to the positive
tail maximum, and (L-90007.17) yields
\[
B_X
\le\sup_z|\mathcal E_{X,Y}(z)|+O(1+\log X)
\ll\log^4(2X).
\]
This proves (L-90007.1), hence WSTS.

## 8. Proof boundary

Closed here, subject to independent review:

1. elementary size and variation bounds for the exact parabolic profile;
2. uniformity in the actual ratio `floor(X/2)/X`;
3. Stieltjes integration by parts with no reciprocal-knot atoms;
4. the uniform `O(log^4 X)` sampling bound under RH;
5. `RH => WSTS`.

Imported classical input:

- `RH => vartheta(t)-t=O(sqrt(t) log^2(2t))`.

Not proved:

- the optional one-log sharpening to `O(log^3 X)`;
- WSTS unconditionally;
- RH.