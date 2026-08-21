# L-91015 — Exact pole-subtracted sieve recurrence and its positive tail channel

Claim ID: `L-91015`  
Status: **PROPOSED COMPLETE EXACT BOUNDARY-STATE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91014`  
RH status: **unproved**

## 1. Pole-subtracted flow

For `c>0`, set

\[
 \kappa_c=\frac1{\zeta(1+2c)},
 \qquad
 H_c(s)=Q_c(s)-\frac{\kappa_c}{s-1}.
 \tag{L-91015.1}
\]

The pole at `s=1` is the universal Hardy/continuum state.  The function `H_c`
is the arithmetic fluctuation around that state.

For `a,b>0`, put

\[
 R_{a,b}=Q_b(1+2a)=\frac{\kappa_{a+b}}{\kappa_a}.
 \tag{L-91015.2}
\]

## 2. Exact coefficient-one affine recurrence

The positive sieve cocycle gives

\[
\begin{aligned}
 H_{a+b}(s)
 ={}&H_a(s)Q_b(s+2a)\\
 &+\kappa_a
 \frac{Q_b(s+2a)-Q_b(1+2a)}{s-1}.
\end{aligned}
 \tag{L-91015.3}
\]

Define the divided-difference channel

\[
 D_{a,b}(s)
 =\frac{Q_b(s+2a)-Q_b(1+2a)}{s-1}.
 \tag{L-91015.4}
\]

Then

\[
 \boxed{
 H_{a+b}=H_a\,Q_b(\cdot+2a)+\kappa_a D_{a,b}.
 }
 \tag{L-91015.5}
\]

After normalising by the pole residue,

\[
 \widetilde H_c=H_c/\kappa_c,
 \qquad
 M_{a,b}(s)=\frac{Q_b(s+2a)}{R_{a,b}},
\]

one obtains

\[
 \boxed{
 \widetilde H_{a+b}(s)
 =\widetilde H_a(s)M_{a,b}(s)
  +\frac{D_{a,b}(s)}{R_{a,b}}.
 }
 \tag{L-91015.6}
\]

The inherited pole-normalised state has coefficient exactly one.  The second
term is emitted once and is not returned at current scale.

## 3. Positive tail representation of the emitted channel

For `Re(s)>1-2a`, the difference quotient has the absolutely convergent
Laplace representation

\[
 \boxed{
 D_{a,b}(s)
 =-\int_0^\infty e^{-(s-1)t}W_{a,b}(t)\,dt,
 }
 \tag{L-91015.7}
\]

where

\[
 \boxed{
 W_{a,b}(t)
 =\sum_{\log n\ge t}
   \frac{q_b(n)}{n^{1+2a}}
 \ge0.
 }
 \tag{L-91015.8}
\]

Indeed,

\[
 \frac{n^{-(s-1)}-1}{s-1}
 =-\int_0^{\log n}e^{-(s-1)t}\,dt,
\]

and summing against `q_b(n)n^(-1-2a)` gives (L-91015.7).

Since `W_(a,b)(t)=O_(a,b)(e^(-2at))`, the emitted channel reaches the critical
line whenever `a>1/4`.  More generally it is holomorphic in the sharp elementary
half-plane

\[
 \Re s>1-2a.
 \tag{L-91015.9}
\]

## 4. Source-side Hankel positivity

For real `sigma>1-2a`, put

\[
 d_j(\sigma)
 =(-1)^{j+1}D_{a,b}^{(j)}(\sigma)
 =\int_0^\infty t^j e^{-(\sigma-1)t}W_{a,b}(t)\,dt.
 \tag{L-91015.10}
\]

Thus every shifted Hankel matrix

\[
 (d_{i+j+\ell}(\sigma))_{0\le i,j\le m}
\]

is positive semidefinite, with the exact Gram formula

\[
 \sum_{i,j}\bar c_i c_jd_{i+j+\ell}
 =\int_0^\infty
  t^\ell\left|\sum_jc_jt^j\right|^2
  e^{-(\sigma-1)t}W_{a,b}(t)\,dt.
 \tag{L-91015.11}
\]

The forcing in the pole-subtracted recurrence is therefore a genuine positive
moment channel before the critical-boundary recombination.

## 5. Dyadic specialization

For `b=a`,

\[
 \boxed{
 \widetilde H_{2a}
 =\widetilde H_a
   \frac{Q_a(\cdot+2a)}{Q_a(1+2a)}
 +\frac1{Q_a(1+2a)}
  \frac{Q_a(\cdot+2a)-Q_a(1+2a)}{\cdot-1}.
 }
 \tag{L-91015.12}
\]

This has precisely the required delayed orientation:

```text
one inherited normalised state with coefficient one
+ one new positive tail/moment channel.
```

Together with the two emitted rational channels of the `SO(3)` Cauchy
all-pass completion, it provides a source-complete finite state ledger.  What
is not yet proved is that the physical/windowed recombination identifies the
positive moment channel with the full Hermitian detail energy without a signed
boundary remainder.

## 6. Sharp outer-interface boundary

At the critical line `Re(s)=1/2`, the explicit positive tail formula
(L-91015.7) is absolutely convergent for `a>1/4`.  At `a=1/4` it reaches its
natural logarithmic boundary.  Thus the same radius-three-quarters / quarter-
depth wall found in the safe-line and radial-curvature programmes appears here
as the exact source-side convergence threshold.

This is not a proof of the gate for `a>1/4`: the inherited fluctuation remains
present.  It does prove that the new emitted forcing has no hidden Type-II,
Möbius, or sign obligation in that outer range.

## 7. Boundary

Closed here:

```text
exact pole subtraction compatible with the sieve cocycle;
coefficient-one inherited state;
explicit one-shot divided-difference forcing;
positive Laplace-tail representation;
all-order Hankel/SOS positivity of the forcing;
sharp critical-line threshold a=1/4.
```

Open:

```text
source/scattering physical intertwiner at the critical boundary;
positivity of the complete dyadic detail after recombination;
iteration below the quarter-depth wall;
RH.
```
