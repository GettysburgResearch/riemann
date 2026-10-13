# The exact paired-frequency collision bound at every fixed moment order

Status: proved finite-Euler inequalities. No bound for the full independent
2k-frequency source trace, individual reciprocal factors, or signed R_k.
The optional global frequency bound imports the named classical reciprocal
zeta theorem explicitly.

## PH1. Literal source factor and all pair degrees

Use P1–P4 of `PRIME_SLOT_CANCELLATION.md`, SHA256
`d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13`.
Its finite collision factor Q is the full finite coprime Euler polynomial
divided by the individual reciprocal Euler factors. It factors into all
reciprocal pair factors and a uniformly bounded degree-three remainder E.
Take any fixed k>=2, left slots `s_i=1/2+i t_i` and right slots their
conjugates. Every t_i is independent on this k-dimensional paired plane.
This plane is smaller than the full independent 2k-frequency Mellin domain.

At an eligible prime p, q=Np, write `x=1/q`, `a=eta_u(p)` with |a|=1,
and `v_i=exp(-i t_i log q)`. The same-side pair characters retain a^2
and its conjugate; cross pairs retain the principal nonunit mask. All
deleted primes have local factor one. The exact full pair product has modulus

\[
 (1-x)^k\prod_{i<j}|1-a^2v_iv_jx|^2
                    \prod_{i<j}|1-v_i\overline{v_j}x|^2.
\tag{PH1}
\]

The k cross self-pairs are essential. Applying |1-a^2 v_i v_j x|<=1+x
to precisely the same-side pairs proves

\[
 |\text{all pairs}|\le
 (1-x)^{k(2-k)}(1-x^2)^{k(k-1)}
              \prod_{i<j}|1-q^{-1-i(t_i-t_j)}|^2.
\tag{PH2}
\]

This holds for every source ray phase, not only sixth roots of unity.
No sign or local character has been erased from the identity PH1.

## PH2. Exact partial principal Euler bound

Let `Z_(Y,SuQ)(s)=product_(Np<=Y,p outside S,uQ)(1-(Np)^(-s))^(-1)`.
The source moving nonunit exclusions are exactly those displayed. The
bounded remainder and PH2 give

\[
 |Q|\le C_k Z_{Y,SuQ}(1)^{k(k-2)}
                \prod_{i<j}|Z_{Y,SuQ}(1+i(t_i-t_j))|^{-2}.
\tag{PH3}
\]

The factor `(1-x^2)^(k(k-1))` was bounded by one, so PH3 is an upper
bound and need not be an equality. All denominators are nonzero finite
Euler factors. For k=2 the positive factor is absent, recovering PF2 of
`PAIRED_FREQUENCY_COLLISION.md`, SHA256
`d057fd4138a4f9c7fcb5455c51e8eabe04b707b8817d4a6ae3359cdfdb85df9a`.
For common frequencies, the exact local PH2 instead gives
`(1-x)^k(1-x^2)^(k(k-1))`, recovering P7 and the sharper common-slice
mask price of P10.

## PH3. Completed zeta comparison and the paid logarithms

Put delta=1/logY, Y>=3. The elementary fixed-field Chebyshev comparison
PF3 in the frozen paired fourth-slot note gives, uniformly at every real t,
`|Z_(Y,empty)(1+it)|` within constant factors of
`|zeta_K(1+delta+it)|`. It also gives `Z_(Y,empty)(1)<=C logY`,
using the positive zeta pole. Since k(k-2)>=0, deleting primes can only
decrease the first factor in PH3. Each reciprocal frequency factor loses
at most the principal-mask inverse product, bounded by
`C[1+log log(3N(uQ))]`, using the frozen P5 elementary norm-budget proof.
Thus, unconditionally,

\[
 |Q|\le C_k(\log Y)^{k(k-2)}
 [1+\log\log(3N(uQ))]^{k(k-1)}
 \prod_{i<j}|\zeta_K(1+1/\log Y+i(t_i-t_j))|^{-2}.
\tag{PH4}
\]

The complete zeta is evaluated strictly in its absolute Euler half-plane.
For N(uQ)<=Y^c, its displayed mask price is at most
`C_(c,k)(1+loglogY)^(k(k-1))`. No uniform finite row support is inferred
from the source spatial Schwartz majorant. For all source rows the explicit
loglog norm weight in PH4 is retained and is integrable against that majorant.

The pole estimate `|1/zeta_K(s)|<=C|s-1|` near 1 proves a paid clustered
frequency estimate. If every `|t_i-t_j|<=b/logY` with fixed b, then

\[
 |Q|\le C_{k,b,c}(\log Y)^{-k}
                         (1+\log\log Y)^{k(k-1)}.
\tag{PH5}
\]

The common slice has the better mask exponent k from P10. PH5 concerns
the entire paired cluster; its central frequency is arbitrary.

## PH4. Optional global paired plane, and the unpaid source gate

Importing exactly CLASSICAL-PF6 of the frozen paired fourth-slot note,
`|1/zeta_K(sigma+it)|<=C(1+|t|)^B` for 1<=sigma<=2, gives

\[
 |Q|\le C_k(\log Y)^{k(k-2)}
 [1+\log\log(3N(uQ))]^{k(k-1)}
 \prod_{i<j}(1+|t_i-t_j|)^{2B}.
\tag{PH6}
\]

The theorem is a named classical input; this packet does not reconstruct
its zero-free proof. The positive endpoint log exponent k(k-2) is smaller
than the phase-erased all-pair exponent k(2k-1). It is attached solely to
the paired plane and the collision factor. The individual factors at real
part 1/2 and independent left/right frequencies remain unpaid. The local
indefinite-kernel controls PF8 preclude an automatic local Cauchy extension.
P13's literal source trace contract, and hence its signed moment price,
remain open.

## PH5. Finite exact controls

`check_paired_higher_collision.py` checks PH1–PH2 with exact Eisenstein
rational arithmetic, all six sextic phases and all paired slot phase
allocations at k=1,2,3,4, for the four actual prime norms 7,13,19,31.
These finite controls test every pair's inclusion and the exponent signs.
They do not prove an infinite Euler estimate, the classical reciprocal
zeta theorem, or the source moment.
