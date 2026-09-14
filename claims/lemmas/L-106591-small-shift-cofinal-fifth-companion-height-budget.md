# L-106591 — A window-adapted small shift closes the fifth-companion height budget

Claim ID: `L-106591`  
Status: **PROVED UNCONDITIONALLY FROM SELBERG, THE PINNED FIFTH-DERIVATIVE PROPORTION, AND REGULAR-WINDOW ROUCHÉ CONTINUITY**  
Created: 2026-08-25  
Depends on: `T-106590`; the pinned Conrey input `R_5/N>997/1000-o(1)`; the standard Xi-derivative strip and fixed-order Riemann--von Mangoldt count  
RH status: **not assumed**

Let

\[
F=\Xi,
\qquad Q=\Xi^{(5)}.
\]

For a positive shift `lambda`, define the fifth-endpoint denominator

\[
D_\lambda
 =(F+i\lambda F')
  (Q-i\lambda Q').
\tag{L-106591.1}
\]

Common factors are reduced before the all-pass symbol is formed.

## 1. Window-adapted companion continuity

Fix a regular dyadic rectangle whose horizontal core is `(T,2T]`, whose
boundary avoids all zeros of `F,Q`, and whose endpoint collar contains
`o(N(T,2T))` zeros. On its compact closure,

\[
F+i\lambda F'\longrightarrow F,
\qquad
Q-i\lambda Q'\longrightarrow Q
\tag{L-106591.2}
\]

uniformly as `lambda->0`.

Choose disjoint disks around the finitely many zero clusters of `F` and `Q` in
the rectangle. If a disk has multiplicity `m`, choose its radius so that the
sum of `m` times the radii over all disks is smaller than an arbitrary
`epsilon>0`. Choose every disk boundary zero-free. Rouché's theorem gives a
`lambda_(T,epsilon)>0` such that the two companion factors have exactly the
same multiplicity in every disk and no additional zero in the remaining
compact set.

It follows directly, with multiplicity, that

\[
\boxed{
\limsup_{\lambda\downarrow0}
 \mathfrak h_+(D_\lambda^{\rm red};T,2T)
\le
 \mathfrak h_+(F;T,2T)
 +\mathfrak h_+(Q;T,2T).
}
\tag{L-106591.3}

Reduction of common factors can only decrease the left side.

For real boundary values, `F+i lambda F'` and `Q-i lambda Q'` have no real
zero after common factors are removed. Hence the endpoint companion index is
constant on every positive-lambda homotopy. We may therefore choose
`lambda_T` separately on each regular dyadic window, small enough that the
error in (L-106591.3) is `o(N)`; no quantitative root-separation theorem is
required.

## 2. The Xi contribution is sublinear

`T-106590` proves from Selberg's zero-density theorem that

\[
\boxed{
\mathfrak h_+(F;T,2T)=O(T)=o(N(T,2T)).
}
\tag{L-106591.4}

The upper Xi height is one half of the functional-equation-symmetric
horizontal first moment.

## 3. The fifth-derivative contribution is at most 3/4000

All zeros of every fixed Xi derivative remain in the centered horizontal strip

\[
|\Im z|\le\frac12.
\tag{L-106591.5}

Let `N_5(T,2T)` be the fifth-derivative zero count with multiplicity and let
`R_5(T,2T)` be its real-zero count. Reality gives conjugate pairing, so

\[
\mathfrak h_+(Q;T,2T)
\le {1\over2}
 {N_5(T,2T)-R_5(T,2T)\over2}.
\tag{L-106591.6}

The fixed-order Riemann--von Mangoldt law gives

\[
N_5(T,2T)=N(T,2T)+o(N(T,2T)),
\]

and the pinned unconditional input is

\[
R_5(T,2T)>
 \left({997\over1000}-o(1)\right)N(T,2T).
\]

Consequently

\[
\boxed{
\mathfrak h_+(Q;T,2T)
\le
 \left({3\over4000}+o(1)\right)N(T,2T).
}
\tag{L-106591.7}

## 4. Closed endpoint height ledger

Choose the regular-window shift `lambda_T` as in Section 1. Equations
(L-106591.3), (L-106591.4), and (L-106591.7) give

\[
\boxed{
\mathfrak h_+(D_{\lambda_T}^{\rm red};T,2T)
\le
 \left({3\over4000}+o(1)\right)N(T,2T).
}
\tag{L-106591.8}

Thus the former cofinal statement `ENDLOC106590` is proved, with the stronger
explicit constant `3/4000` rather than merely `o(N)`.

## 5. Immediate deep/shallow split

For every fixed `eta>0`, `T-106590.10` now gives

\[
\boxed{
{\mathcal C_{>\eta}(U_T)\over N(T,2T)}
\le {3\over4000\eta}+o(1).
}
\tag{L-106591.9}

At the concrete choice

\[
\eta={1\over100},
\]

all companion directions above height `0.01` cost at most

\[
{3\over40}N+o(N).
\]

The fifth-endpoint allowance is `97/1000`, leaving the exact shallow budget

\[
\boxed{
{97\over1000}-{3\over40}
 ={11\over500}.
}
\tag{L-106591.10}

Accordingly, only the canonical-correlation defect of denominator companion
zeros of height at most `1/100` remains. This is recorded as
`SHALLOWCORR106591` in the updated `T-106590` frontier.