# L-28302 — Sibling switches factor the central lattice commutator

Claim ID: `L-28302`  
Title: The forced `2kq-1` endpoint error is an exact adjacent divisor-transport source at half scale  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #283  
Dependencies: PR #280 `L-27701/L-27702`; PR #272 `L-27204`  
Scope: carry/Pascal algebra; no debt estimate and no RH conclusion

## 1. Central and sibling splits

For a split of `n` into `j` and `n-j`, put

\[
\chi_{n,j}(q)
=
\left\lfloor\frac nq\right\rfloor
-
\left\lfloor\frac jq\right\rfloor
-
\left\lfloor\frac{n-j}q\right\rfloor.
\]

For an even parent `n=2h`, compare the central split

\[
[h+h]
\]

with its nearest sibling split

\[
[(h-1)+(h+1)].
\]

Direct floor subtraction gives

\[
\begin{aligned}
&\chi_{2h,h-1}(q)-\chi_{2h,h}(q)\\
&\qquad=
2\left\lfloor\frac hq\right\rfloor
-\left\lfloor\frac{h-1}q\right\rfloor
-\left\lfloor\frac{h+1}q\right\rfloor.
\end{aligned}
\]

Using consecutive floor increments,

\[
\boxed{
\chi_{2h,h-1}(q)-\chi_{2h,h}(q)
=
\mathbf1_{q\mid h}-\mathbf1_{q\mid h+1}.
}
\tag{L-28302.1}
\]

For the fixed balanced window `eta<=1/4`, both splits are allowed whenever
`h>=2`.

## 2. Exact entropy and prime-objective cost

The corresponding binomial values satisfy

\[
\frac{\binom{2h}{h-1}}{\binom{2h}{h}}
=
\frac h{h+1}.
\]

Therefore a switch of amount `t` from the central edge to the sibling edge
changes the entropy by

\[
\boxed{
\Delta\mathcal H
=t\log\frac h{h+1}.
}
\tag{L-28302.2}
\]

The von Mangoldt-weighted carry change gives the identical scalar:

\[
\sum_{q=p^a}\Lambda(q)
\left(
 \mathbf1_{q\mid h}-\mathbf1_{q\mid h+1}
\right)
=
\log\frac h{h+1}.
\tag{L-28302.3}
\]

Thus the local cycle correction has a complete exact objective ledger.

## 3. Central lattice commutator

Let `r` be any finitely supported sequence, extended by zero, and put

\[
a(m)=r(m)-r(m+1).
\]

The discrete/continuum mismatch of PR #280 is

\[
(\mathcal Er)(q)
=
\sum_{k\ge1}
\bigl[r(2kq-1)-r(2kq)\bigr].
\]

Since each bracket is `a(2kq-1)`, write

\[
\sigma(h)=a(2h-1).
\tag{L-28302.4}
\]

Then

\[
\boxed{
(\mathcal Er)(q)
=
\sum_{q\mid h}\sigma(h).
}
\tag{L-28302.5}
\]

The forced endpoint error is exactly the divisor-zeta transform of an odd-edge
source on the half-scale index `h`.

Consequently Möbius inversion gives

\[
\boxed{
\sigma(h)
=
\sum_{k\ge1}\mu(k)(\mathcal Er)(hk),
}
\tag{L-28302.6}
\]

with the finite endpoint convention.

## 4. A family of sibling switches

Apply a sibling switch of amount `t_h` at every parent `2h`.  Equation
(L-28302.1) shows that the complete carry change is

\[
\begin{aligned}
\Delta L_q
&=
\sum_h t_h
\left(\mathbf1_{q\mid h}-\mathbf1_{q\mid h+1}\right)\\
&=
\sum_{q\mid u}(t_u-t_{u-1}),
\end{aligned}
\tag{L-28302.7}
\]

where `t_0=0` and the terminal value is extended by zero.

Thus sibling switches act on the half-scale divisor source by the ordinary
first-difference operator

\[
\boxed{
\sigma(u)\longmapsto
\sigma(u)-(t_u-t_{u-1}).
}
\tag{L-28302.8}
\]

At the event level, taking

\[
t_u-t_{u-1}=\sigma(u)
\]

cancels the commutator exactly.  The cumulative solution is

\[
t_u=\sum_{v\le u}\sigma(v).
\tag{L-28302.9}
\]

Equation (L-28302.9) is not automatically an admissible nonnegative edge
replacement: `t_u` may exceed the available central coefficient.  That capacity
constraint is exactly where the complete Pascal fundamental-cycle space and its
weighted negative debt enter.

## 5. Pascal-cycle interpretation

The central and sibling edges have the same parent but different child
divergence.  Their difference is completed to a divergence-zero deformation by
the elementary/fundamental Pascal cycles of PR #272.  Hence any admissible
sibling-switch schedule can be represented by explicit cycle coordinates and
replayed without changing the target node divergence.

The source, destination, and objective of every correction are now visible:

```text
lattice error       sigma(h)=r(2h-1)-r(2h);
carry image         divisor transform of sigma;
local correction    central/sibling switch at parent 2h;
source update       sigma -> sigma-Delta t;
objective cost      t_h log(h/(h+1));
scale               h,h+1 <= (2h+1)/2.
```

This is a strict half-scale state transition, not a same-scale generic norm.

## 6. Relation to the state-dependent carry factor

The Markov kernel of `L-28301` keeps the carry state instead of averaging it into
one scalar convolution factor.  Equations (L-28302.5)--(L-28302.8) identify the
finite state needed by the central cascade: the quotient/divisor index `h` and
its adjacent transition `h->h+1`.

The proposed `SAPC` certificate uses these exact transitions to realize the
positive Markov transport in the finite Pascal cone before taking any negative
part.

## 7. Proof boundary

Closed exactly:

- the central-to-sibling carry identity;
- the entropy/von-Mangoldt objective identity;
- the divisor factorization of the lattice commutator;
- its Möbius inverse;
- the first-difference action of a switch family;
- strict half-scale routing.

Open:

- a capacity-feasible cycle schedule with a contracting debt recurrence;
- SAPC;
- RH.