# L-102748 — The free unordered-pair Wick energy is polylogarithmic

Claim ID: `L-102748`  
Status: **PROVED EXACT LABELLED-ENERGY THEOREM**  
Created: 2026-08-23  
Depends on: `L-102746--L-102747`; `L-102743`  
RH status: **not assumed**

Let the active labelled primes on a horizon \(Y\) have activities

\[
 r_\ell=p_\ell^{-1/2}.
\]

Define the free unordered-pair vector

\[
 V_2
 =\sum_{i<j}r_ir_j\,e_{\{i,j\}}
\]

in the Hilbert space with orthonormal pair basis.  Then

\[
 \begin{aligned}
 \|V_2\|^2
 &=\sum_{i<j}r_i^2r_j^2\\
 &=\frac12\left[
 \left(\sum_i\frac1{p_i}\right)^2
 -\sum_i\frac1{p_i^2}
 \right].
 \end{aligned}
\]

The second labelled copy of \(67\) changes only an absolute constant.  Mertens'
prime-reciprocal theorem therefore gives

\[
 \boxed{
 \|V_2\|^2\ll(\log\log(3Y))^2.
 }
 \tag{L-102748.1}
\]

## 1. Uniform exponential tail

For the Wick field

\[
 W_t=Le^{-tL/2},
 \qquad 0\le t\le1,
\]

`L-102743` proves a polylogarithmic free labelled norm uniformly in \(t\).
Combining that theorem with the explicit pair coordinate in `L-102746` gives

\[
 \boxed{
 \int_0^1(1-t)
 \|W_t^{(2)}\|_{\rm free}^2\,dt
 \ll(\log(2Y))^C
 }
 \tag{L-102748.2}
\]

for an absolute constant \(C\).  Here \(W_t^{(2)}\) means that the two labels
selected by the outer \(L^2\) are retained as an unordered owner pair; all
remaining exponential labels remain in the Fock coordinate.

## 2. Combined free/same-product cost

`L-102747` shows that collapsing the pair coordinate for one physical product
costs at most \(O((\log Y)^2)\), while `L-102702` gives subpower factor-pair
multiplicity.  Hence

\[
 \boxed{
 \text{free labelled pair energy plus equal-product collapse is }Y^{o(1)}.
 }
 \tag{L-102748.3}
\]

## Scope

The theorem does not bound evaluation of the labelled pair field on the
one-dimensional physical scale line.  Distinct products can have arbitrarily
close logarithms, and that cross-pair restriction is the sole remaining
operator in `T-102820`.
