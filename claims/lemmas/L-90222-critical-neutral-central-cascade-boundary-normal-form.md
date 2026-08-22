# L-90222 — The critical-neutral scalar is a five-coordinate central-cascade boundary correction

Claim ID: `L-90222`  
Status: **PROPOSED COMPLETE EXACT FINITE / ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: critical-neutral source `L-90221`; central first-difference identity of `L-32403`; shifted analytic contraction interface of `L-32301/L-32404`  
Scope: exact scalar boundary normal form; no estimate for the cutoff correction and no RH conclusion

## 1. Source and divisor prefix

Retain

\[
 b_\star
 =(\varepsilon-\delta_2)
  *(\varepsilon-\sqrt2\,\delta_2)*\mu.
 \tag{L-90222.1}
\]

Its divisor convolution is

\[
 \boxed{
 1*b_\star
 =\varepsilon-(1+\sqrt2)\delta_2+\sqrt2\,\delta_4.
 }
 \tag{L-90222.2}
\]

Therefore the exact divisor prefix

\[
 D_\star(x)
 =\sum_{q\le x}b_\star(q)\left\lfloor\frac{x}{q}\right\rfloor
 \tag{L-90222.3}
\]

is

\[
 \boxed{
 D_\star(0)=0,
 \qquad
 D_\star(1)=1,
 \qquad
 D_\star(x)=-\sqrt2\ (2\le x<4),
 \qquad
 D_\star(x)=0\ (x\ge4).
 }
 \tag{L-90222.4}
\]

No Möbius coefficient remains in this coordinate.

## 2. Complete central charge table

For the central split

\[
 n=\lfloor n/2\rfloor+\lceil n/2\rceil,
\]

put

\[
 Y_\star(n)
 =D_\star(n)
  -D_\star(\lfloor n/2\rfloor)
  -D_\star(\lceil n/2\rceil).
 \tag{L-90222.5}
\]

Equation (L-90222.4) gives exactly

\[
 \boxed{
 \begin{array}{c|cccccc}
 n&2&3&4&5&6&7\\ \hline
 Y_\star(n)&-2-\sqrt2&-1&2\sqrt2&2\sqrt2&2\sqrt2&\sqrt2
 \end{array}}
 \tag{L-90222.6}
\]

and

\[
 \boxed{Y_\star(n)=0\qquad(n\ge8).}
 \tag{L-90222.7}
\]

Thus the critical-neutral source is completely invisible to every central
split above state seven.

## 3. Five-coordinate bottom functional

Let `r(q)` be finitely supported on `q>=2`, with zero extension, and put

\[
 d_n=r(n)-r(n+1).
 \tag{L-90222.8}
\]

Place `d_n` on the central split at parent `n`.  The exact central residual
identity gives the load `r-mathcal T r`, where

\[
 (\mathcal T r)(q)
 =\sum_{k\ge1}
 [r(2kq-1)-r((2k+1)q)].
 \tag{L-90222.9}
\]

Pairing with `b_star` and telescoping the finite charge table yields

\[
 \boxed{
 \langle b_\star,r-\mathcal T r\rangle
 =\mathcal B_\star(r),
 }
 \tag{L-90222.10}
\]

where

\[
 \boxed{
 \begin{aligned}
 \mathcal B_\star(r)={}&
 -(2+\sqrt2)r(2)
 +(1+\sqrt2)r(3)\\
 &+(1+2\sqrt2)r(4)
 -\sqrt2\,r(7)
 -\sqrt2\,r(8).
 \end{aligned}}
 \tag{L-90222.11}
\]

All states five and six cancel from the bottom telescope.

## 4. Exact finite cascade for the hinge scalar

For real `X>=2`, put

\[
 h_X(q)=
 \left(q^{-1/2}-X^{-1/2}\right)
 \mathbf1_{2\le q\le X}.
 \tag{L-90222.12}
\]

Define the stopped central cascade

\[
 r_0=h_X,
 \qquad
 r_{a+1}=\mathcal T r_a.
 \tag{L-90222.13}
\]

Support decreases by at least a factor two, so the cascade terminates after
`O(log X)` stages.  Summing (L-90222.10) gives

\[
 \sum_{a\ge0}\mathcal B_\star(r_a)
 =\sum_{q\ge2}b_\star(q)h_X(q).
 \tag{L-90222.14}
\]

The critical-neutral scalar of `L-90221/T-90206` is therefore

\[
 \boxed{
 \mathcal K_\star(X)
 =-\sum_{a\ge0}\mathcal B_\star(r_a).
 }
 \tag{L-90222.15}
\]

This is an exact finite five-bottom-coordinate representation.  The Möbius
source has disappeared after the initial pairing.

## 5. Infinite analytic resolvent

Let

\[
 p_s(q)=q^{-s}
\]

and let `mathscr C` be the infinite shifted central operator of
`L-32301/L-32404`.  Initially for `Re s>1`, absolute convergence and
(L-90222.10) give

\[
 \boxed{
 \sum_{a\ge0}
 \mathcal B_\star(\mathscr C^a p_s)
 =\sum_{q\ge2}\frac{b_\star(q)}{q^s}
 =\frac{Q_\star(2^{-s})}{\zeta(s)}-1,
 }
 \tag{L-90222.16}
\]

where

\[
 Q_\star(t)=(1-t)(1-\sqrt2t).
\]

The analytic coefficient bank of `L-32301` continues this identity to the real
boundary `s=1/2`.  Since

\[
 Q_\star(2^{-1/2})=0,
\]

one obtains

\[
 \boxed{
 \sum_{a\ge0}
 \mathcal B_\star(\mathscr C^a p_{1/2})=-1.
 }
 \tag{L-90222.17}
\]

No reciprocal-zeta value survives in the analytic main term.

## 6. Exact cutoff-boundary correction

Put

\[
 u_a=\mathscr C^a p_{1/2}.
 \tag{L-90222.18}
\]

Combining (L-90222.15) with (L-90222.17) gives

\[
 \boxed{
 \mathcal K_\star(X)
 =1-
 \sum_{a\ge0}
 \mathcal B_\star(r_a-u_a).
 }
 \tag{L-90222.19}
\]

The finite cascade is zero after `O(log X)` stages; the analytic cascade is
absolutely summable in the `L-32301` bank.  Thus every nonconstant arithmetic
effect is one finite-cutoff Duhamel correction to the exact positive unit
main term.

The initial discrepancy is the single capped power

\[
 \boxed{
 r_0(q)-p_{1/2}(q)
 =
 \begin{cases}
 -X^{-1/2},&2\le q\le X,\\
 -q^{-1/2},&q>X.
 \end{cases}}
 \tag{L-90222.20}
\]

so no hidden source family enters the boundary state.

## 7. Full-theorem interface

Equation (L-90222.19) proves that `CN3` is equivalent to the scalar cutoff
bound

\[
 \boxed{
 \sum_{a\ge0}
 \mathcal B_\star(r_a-u_a)
 \le1.
 }
 \tag{L-90222.21}
\]

This is strictly smaller than the all-state `CBVR` theorem of PR #316 and the
Haar boundary theorem of PR #333:

- only one capped square-root profile is injected;
- every analytic descendant contracts in the existing `6/7` bank;
- the consumer sees only states `2,3,4,7,8`;
- the complete allowed budget is the exact unit in (L-90222.21).

The remaining estimate is not proved here.  Critical-line complex modes can
reside in the cutoff state, so real-exponent analytic contraction alone may
not be promoted to (L-90222.21).

## 8. Proof boundary

Proved exactly:

- the compact divisor prefix;
- the complete central charge table;
- the five-coordinate bottom functional;
- the finite central-cascade representation;
- exact cancellation of the infinite analytic critical main mode;
- reduction to one cutoff-boundary correction.

Not proved:

- the unit cutoff bound (L-90222.21);
- `CN3`;
- RH.
