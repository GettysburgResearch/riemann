# L-91032 — Every finite Euler factor preserves Green-removed Cauchy positivity

Claim ID: `L-91032`  
Status: **EXACT PRIME-LOCAL COMPLETE-POSITIVITY THEOREM**  
Created: 2026-08-12  
Depends on: the Cauchy numerator of `L-91026`  
RH status: **unproved**

## 1. One local generalized-Jordan factor

Fix `s>0` and a prime `p`. Put

\[
 \boxed{
 L_{p,s}(q)
 =\frac{1-p^{-1-s-q}}{1-p^{-1-q}}
 =1+(1-p^{-s})\sum_{k\ge1}p^{-k}e^{-qk\log p}.
 }
 \tag{L-91032.1}
\]

This is the Laplace transform of a positive discrete measure. Its endpoint factor is

\[
 c_{p,s}=1-p^{-1-s}.
\]

Moreover

\[
 \boxed{
 L_{p,s}(q)-c_{p,s}
 =p^{-1-s}
 +(1-p^{-s})\sum_{k\ge1}p^{-k}e^{-qk\log p},
 }
 \tag{L-91032.2}
\]

so the endpoint defect is also completely monotone.

## 2. Finite Euler products

For a finite prime set `P`, define

\[
 Z_P(q)=\prod_{p\in P}L_{p,s}(q),
 \qquad
 c_P=\prod_{p\in P}c_{p,s},
\]

and the formally centered channel

\[
 G_P(q)=Z_P(q)-\frac{c_P}{q}.
 \tag{L-91032.3}
\]

If `p` is not in `P`, then exactly

\[
 \boxed{
 G_{P\cup\{p\}}(q)
 =L_{p,s}(q)G_P(q)
 +\frac{c_P}{q}
  [L_{p,s}(q)-c_{p,s}].
 }
 \tag{L-91032.4}
\]

## 3. Cauchy numerator

Let

\[
 \mathcal P_a(q)=q(q+A)(q+B),
 \qquad A,B>0.
\]

Put

\[
 T_P(q)=\mathcal P_a(q)\frac{G_P(q)}{q^3}.
 \tag{L-91032.5}
\]

Then (L-91032.4) gives

\[
 \boxed{
 \begin{aligned}
 T_{P\cup\{p\}}(q)
 ={}&L_{p,s}(q)T_P(q)\\
 &+c_P[L_{p,s}(q)-c_{p,s}]
 \left[
 \frac1q+\frac{A+B}{q^2}+\frac{AB}{q^3}
 \right].
 \end{aligned}
 }
 \tag{L-91032.6}

Every factor in the second line is completely monotone.

Therefore

\[
 \boxed{
 T_P\text{ completely monotone}
 \quad\Longrightarrow\quad
 T_{P\cup\{p\}}\text{ completely monotone}.
 }
 \tag{L-91032.7}

The same statement holds after multiplication by any of the positive rational, beta/Gamma, or Erlang channels used in `L-9506/L-91031`.

## 4. Explicit Stinespring interpretation

Equation (L-91032.6) is a two-output positive dilation:

```text
inherited output:
  multiply the old positive measure by the local Euler measure L_(p,s);

new output:
  endpoint mass c_P
  tensor the positive defect measure L_(p,s)-c_(p,s)
  tensor the three positive Green kernels
  1/q, 1/q^2, 1/q^3.
```

The old state returns with coefficient exactly one. No signed local-prime port appears.

## 5. Consequence and firewall

No finite collection of Euler primes can be responsible for failure of the Green-removed positive cone. Once the cone holds before adjoining a prime, the exact local generalized-Jordan factor preserves it.

The remaining arithmetic difficulty is therefore an infinite-tail/base phenomenon associated with the simultaneous simple pole at `q=0`. This is consistent with:

- the small-`s` scaling theorem `L-91028`;
- the unit-atom terminal theorem `L-91030`;
- the compact middle interval left by those two results.

One must not start the induction from the empty finite Euler product: its artificial channel `1-1/q` is not positive. The theorem is a preservation result, not a finite-product proof of the infinite zeta source.

No critical-boundary or RH conclusion is asserted.