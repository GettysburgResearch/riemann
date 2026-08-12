# L-91319 — The pole-node arithmetic source is one explicit all-generation Jordan innovation vector

Claim ID: `L-91319`  
Status: **EXACT POSITIVE HILBERT-SOURCE CONSTRUCTION; MODEL-SPACE ISOMETRY REMAINS OPEN**  
Created: 2026-08-12  
Depends on: `L-91317/L-91318`, main `L-91029`  
RH status: **unproved**

## 1. Dyadic prime-jump measures

For `b>0`, define the finite positive prime-power measure

\[
 d\nu_b(t)
 :=d\nu_{b,1+2b}(t)
 =\sum_p\sum_{k\ge1}
 \frac{1-p^{-2bk}}{k p^{k(1+2b)}}
 \delta_{k\log p}(dt).
 \tag{L-91319.1}
\]

Its first moment is

\[
 \boxed{
 I(b):=\int_0^\infty t\,d\nu_b(t)
 =-\frac{Q_b'(1+2b)}{Q_b(1+2b)}
 =F(b)-F(2b)>0,
 }
 \tag{L-91319.2}
\]

where

\[
 F(b)=\gamma-\frac{\zeta'}{\zeta}(1+2b).
 \tag{L-91319.3}
\]

## 2. One-particle innovation vectors

Let

\[
 \mathfrak h_b^{(1)}=L^2((0,\infty),\nu_b).
 \tag{L-91319.4}
\]

Define

\[
 \boxed{
 \psi_b(t)=\sqrt t.
 }
 \tag{L-91319.5}
\]

Then

\[
 \boxed{
 \|\psi_b\|_{\mathfrak h_b^{(1)}}^2
 =I(b).
 }
 \tag{L-91319.6}
\]

This is the first-chaos prime-jump current of the compound-Poisson Fock source.
No square root of an unknown target kernel is used.

## 3. All-generation source space

Fix `a>0` and put

\[
 b_j=2^j a,
 \qquad j=0,1,2,\ldots.
 \tag{L-91319.7}
\]

Define the positive Hilbert space

\[
 \boxed{
 \mathcal J_a
 =\mathbb C e_\infty
  \oplus
  \bigoplus_{j\ge0}\mathfrak h_{b_j}^{(1)}.
 }
 \tag{L-91319.8}
\]

The terminal vector has norm

\[
 \|\sqrt\gamma\,e_\infty\|^2=\gamma.
 \tag{L-91319.9}
\]

Define the all-generation arithmetic vector

\[
 \boxed{
 \Psi_a^{\rm J}
 =\sqrt\gamma\,e_\infty
  \oplus
  \bigoplus_{j\ge0}\psi_{2^ja}.
 }
 \tag{L-91319.10}
\]

## 4. Exact norm

The telescoping identity of `L-91317` gives

\[
\begin{aligned}
 \|\Psi_a^{\rm J}\|_{\mathcal J_a}^2
 &=\gamma+\sum_{j\ge0}[F(2^ja)-F(2^{j+1}a)]\\
 &=\boxed{F(a)}.
\end{aligned}
 \tag{L-91319.11}
\]

The series converges absolutely because all terms are positive and
`F(2^ja) downarrow gamma`.

Thus the pole-normalized centered source scalar is the norm of a completely
explicit positive vector.

## 5. Completed pole amplitude

Let

\[
 A_{2a}^{\rm pole}
 =\frac{\xi(1)}{\xi(1+2a)}.
 \tag{L-91319.12}
\]

The completed arithmetic source vector is

\[
 \boxed{
 \Phi_a^{\rm arith}
 =\sqrt{A_{2a}^{\rm pole}}\,\Psi_a^{\rm J},
 }
 \tag{L-91319.13}
\]

with exact norm

\[
 \boxed{
 \|\Phi_a^{\rm arith}\|^2
 =A_{2a}^{\rm pole}
  \left[\gamma-\frac{\zeta'}{\zeta}(1+2a)\right]
 =\mathcal G_{2a}(0).
 }
 \tag{L-91319.14}
\]

Every coefficient is an absolutely convergent prime or completed-gamma value.

## 6. Product-system interpretation

Each `h_b^(1)` is the first-chaos sector of the bosonic Fock product system at
dyadic radial interval `[b,2b]`. The direct sum in (L-91319.8) is therefore the
orthogonal innovation decomposition of the coefficient-one source martingale:

```text
current scale innovation;
next scale innovation;
...
terminal Euler-constant vacuum.
```

Coassociativity of the divisor isometries makes the decomposition independent
of parenthesization.

## 7. The sole missing isometry

The arithmetic side of the pole-aligned one-node theorem is now explicit.
The remaining map is

\[
 \boxed{
 \mathfrak U_a\Phi_a^{\rm arith}
 =k_{\eta_a}^{\rm crit}
  \oplus k_{\eta_a}^{\rm stable}
  \oplus k_{\eta_a}^{\rm hyp}
  \oplus q_a^{\rm aux},
 }
 \tag{L-91319.15}
\]

where `eta_a=1/2+a` and every non-hyperbolic output must be constructed from
the declared theta/Brownian/Cauchy/`p=2` reservoirs.

The conclusion-producing exhaustion theorem is

\[
 \boxed{
 \|\Phi_a^{\rm arith}\|^2
 =\|k_{\eta_a}^{\rm crit}\|^2
  +\|k_{\eta_a}^{\rm stable}\|^2,
 }
 \tag{L-91319.16}
\]

with no auxiliary remainder. The exact model ledger then forces both
`k_hyp` and every unused auxiliary component to vanish.

## 8. Status

```text
all dyadic prime-jump measures          EXPLICIT POSITIVE
one-particle innovation vectors         EXPLICIT
all-generation source Hilbert space     EXPLICIT
source vector and its norm              EXACT
source-to-model isometry                OPEN / RH-BEARING
one-node exhaustion                     OPEN / RH-BEARING
Riemann Hypothesis                      UNPROVED
```
