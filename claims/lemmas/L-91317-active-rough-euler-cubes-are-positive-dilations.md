# L-91317 — Fully active rough Euler cubes are positive dilations, and every truncated factor splits into a positive pair plus one contracted frontier

Claim ID: `L-91317`  
Status: **PROVED EXACT POSITIVE-FACTOR / SUPPORT-CONTRACTION THEOREM — PROJECTIVE CONE CONVERSION OPEN**  
Created: 2026-08-12  
Depends on: `L-91109/L-91113`, `L-91316`  
RH status: **unproved**

## 1. The elementary square-root ramp

For `a in {1,2}`, real `x>=1`, and integer `n<=x`, put

\[
 \boxed{
 w_a(x,n)
 =\frac1{\sqrt n}\left(a\sqrt{\frac xn}-1\right)
 =\frac{a\sqrt x}{n}-\frac1{\sqrt n}.
 }
\tag{L-91317.1}
\]

These are the positive squarefree-parity atoms of `L-91109`. Let `p` be a prime
and write

\[
 r=p^{-1/2}.
\]

## 2. One active Euler factor is exactly a positive dilation

If `pn<=x`, then

\[
\begin{aligned}
 w_a(x,n)-w_a(x,pn)
 &=(1-r^2)\frac{a\sqrt x}{n}
   -(1-r)\frac1{\sqrt n}\\
 &=(1-r)
   \left[
    (1+r)\frac{a\sqrt x}{n}-\frac1{\sqrt n}
   \right].
\end{aligned}
\]

Therefore

\[
 \boxed{
 w_a(x,n)-w_a(x,pn)
 =(1-p^{-1/2})
  w_a\!\left(x(1+p^{-1/2})^2,n\right)>0.
 }
\tag{L-91317.2}
\]

The cancellation of one Möbius Euler factor is not merely sign-favorable. It is
exactly a positive scalar times another atom of the same family.

In the component-row coordinates of `L-91112.25`, the same identity may be
applied termwise to every nonnegative ramp feature. Thus an active rough Euler
factor has a source-faithful positive row and ordinary-carry realization.

## 3. A fully active finite Euler cube

Let `Q` be a finite set of primes and put

\[
 P_Q=\prod_{p\in Q}p,
 \qquad
 \beta_Q=\prod_{p\in Q}(1-p^{-1/2}),
 \qquad
 \Gamma_Q=\prod_{p\in Q}(1+p^{-1/2}).
\tag{L-91317.3}

If

\[
 nP_Q\le x,
\]

then every Boolean subproduct is active. Direct summation gives

\[
\begin{aligned}
 \sum_{d\mid P_Q}\mu(d)w_a(x,nd)
 &=\frac{a\sqrt x}{n}
   \prod_{p\in Q}\left(1-\frac1p\right)
  -\frac1{\sqrt n}
   \prod_{p\in Q}(1-p^{-1/2})\\
 &=\beta_Q
   \left[
    \Gamma_Q\frac{a\sqrt x}{n}-\frac1{\sqrt n}
   \right].
\end{aligned}
\]

Hence

\[
 \boxed{
 \sum_{d\mid P_Q}\mu(d)w_a(x,nd)
 =\beta_Q\,w_a(x\Gamma_Q^2,n)>0.
 }
\tag{L-91317.4}
\]

Here we used the exact factorization

\[
 \beta_Q\Gamma_Q
 =\prod_{p\in Q}\left(1-\frac1p\right).
\]

Thus every fully active rough-prime Boolean cube is a single positive dilated
atom. Sign can occur only on a multiplicative activation frontier.

## 4. Exact truncated one-factor decomposition

Let `nu(n)>=0` be finitely supported. Define the truncated Euler action

\[
 \mathcal E_{p,a}[\nu](x)
 =\sum_{n\le x}\nu(n)w_a(x,n)
  -\sum_{n\le x/p}\nu(n)w_a(x,pn).
\tag{L-91317.5}
\]

Splitting the first sum at `x/p` and using (L-91317.2) yields

\[
 \boxed{
\begin{aligned}
 \mathcal E_{p,a}[\nu](x)
 ={}&(1-p^{-1/2})
 \sum_{n\le x/p}\nu(n)
 w_a\!\left(x(1+p^{-1/2})^2,n\right)\\
 &+\sum_{x/p<n\le x}\nu(n)w_a(x,n).
\end{aligned}}
\tag{L-91317.6}
\]

Both terms are nonnegative. The second term is the complete activation frontier;
the first is the paired positive interior.

This is a positive factorization at finite cutoff, not merely after all Boolean
states have activated.

## 5. Factor-54 support split for every rough prime

Let `c_0` be the certified reset constant of `L-91106`, and let `p>=59`. Then

\[
 \frac1p<c_0.
\tag{L-91317.7}
\]

The paired term in (L-91317.6) is supported on

\[
 n\le\frac xp<c_0x.
\tag{L-91317.8}
\]

The frontier admits the exact split

\[
 \frac xp<n\le c_0x
 \qquad\text{and}\qquad
 c_0x<n\le x.
\tag{L-91317.9}
\]

Thus every truncated rough Euler factor decomposes into:

```text
positive paired interior supported below the contracted reset scale;
positive inner-frontier slice supported below the contracted reset scale;
positive outer-frontier slice lying in the already paid factor-54 window.
```

No part remains at an uncontrolled intermediate support.

The coefficients of the child term are exactly the natural Euler coefficients
`p^-1/2`; no multiplicative norm loss is introduced.

## 6. Least-prime routing removes branching ambiguity

In the positive automaton of `L-91109`, every nontrivial rough integer has a
unique least prime. Therefore the decompositions (L-91317.6)--(L-91317.9) may be
assigned by the least-prime label without duplicating one source atom among
several branches.

Equivalently, each rough branch has one of two destinations:

1. the already feasible outer endpoint block;
2. a state supported at endpoint at most `c_0X`.

This supplies a coefficient-one **support** allocation for the complete rough
Euler tree.

## 7. Diagonal mode action and the remaining cone obstruction

The two diagonal modes of `L-91311` are

\[
 X=\sqrt x\,B(x),
 \qquad
 Y=A(x).
\]

One Euler factor acts on their neutral amplitudes by

\[
 \boxed{
 X\mapsto(1-p^{-1})X,
 \qquad
 Y\mapsto(1-p^{-1/2})Y.
 }
\tag{L-91317.10}

Returning to

\[
 L=2X-Y,
 \qquad
 R=X-Y,
\]

gives the matrix

\[
 \boxed{
 M_p=
 \begin{pmatrix}
  2a_p-b_p&2(b_p-a_p)\\
  a_p-b_p&2b_p-a_p
 \end{pmatrix},
 \quad
 a_p=1-p^{-1},
 \quad
 b_p=1-p^{-1/2}.
 }
\tag{L-91317.11}

Since `a_p>b_p`, the lower-left entry is positive but the upper-right entry is
negative. Hence diagonal positivity and support contraction do not automatically
preserve the original positive `(L,R)` cone.

This is the sole remaining projective obstruction: convert the contracted
square-root/constant mode packet back into the admissible `(L,R)` wedge using
the strict endpoint Schur reserve of `L-91316` and the positive reserve
coefficient `2-kappa_*` of `L-91315`.

## 8. Consequence for the reset frontier

The infinite rough-prime problem has now separated into two exact pieces:

```text
multiplicative support routing:
    coefficient-one and positive by least-prime Euler factorization;

state-type routing:
    a two-dimensional projective cone conversion.
```

The former is closed by this theorem. The latter is finite-dimensional but still
must be implemented in ordinary/radix-four capacity coordinates.

```text
one active Euler factor = positive dilation       EXACT
fully active finite cube = positive dilation      EXACT
truncated factor = positive interior + frontier   EXACT
p>=59 support enters outer-paid/contracted blocks EXACT
least-prime coefficient-one support allocation    EXACT
(L,R) projective cone conversion                  OPEN
Riemann Hypothesis                                UNPROVED
```
