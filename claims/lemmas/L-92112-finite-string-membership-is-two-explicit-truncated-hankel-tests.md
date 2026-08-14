# L-92112 — Finite passive-string membership is two explicit truncated Hankel tests

Claim ID: `L-92112`  
Status: **PROVED EXACT FINITE MATRIX/SEPARATOR THEOREM**  
Created: 2026-08-14  
Frozen passive-string route: PR #453 at `a9cecbd3228bc26d4d0c3375c9694ee1e836f66a`  
Primary input: `L-92111`  
RH status: **unproved**

## 1. Barycentric functional

Fix distinct positive nodes

\[
 q_1=r,q_2,\ldots,q_N
 \tag{L-92112.1}
\]

and finite safe data `y_1,...,y_N`. Put

\[
 B_j(s)=\prod_{i\ne j}(q_i+s),
 \qquad
 \Delta_j=B_j(-q_j)=\prod_{i\ne j}(q_i-q_j).
 \tag{L-92112.2}
\]

The polynomials `B_j` form a basis of the real polynomials of degree at most
`N-1`. If

\[
 Q(s)=\sum_jc_jB_j(s),
 \tag{L-92112.3}
\]

then evaluation at `s=-q_j` gives

\[
 \boxed{c_j=\frac{Q(-q_j)}{\Delta_j}.}
 \tag{L-92112.4}
\]

Define the exact data functional

\[
 \boxed{
 \mathcal L_y(Q)
 =\sum_{j=1}^Ny_j\frac{Q(-q_j)}{\Delta_j}.
 }
 \tag{L-92112.5}
\]

`L-92111` uses the dual polynomial

\[
 P_c(s)=(r+s)Q(s).
 \tag{L-92112.6}
\]

Since `r+s>0` for `s>=0`,

\[
 P_c(s)\ge0\;(s\ge0)
 \iff
 Q(s)\ge0\;(s\ge0).
 \tag{L-92112.7}
\]

Therefore the finite string datum belongs to the moment cone if and only if

\[
 \mathcal L_y(Q)\ge0
 \tag{L-92112.8}
\]

for every polynomial `Q` of degree at most `N-1` nonnegative on the half-line.

## 2. Explicit moments

For `0<=k<=N-1`, define

\[
 \boxed{
 m_k=\mathcal L_y(s^k)
 =\sum_{j=1}^N
  \frac{y_j(-q_j)^k}{\Delta_j}.
 }
 \tag{L-92112.9}
\]

These are rational whenever the nodes and data are rational. Equivalently,
`m_k` is the divided difference of the sampled function `x^k y(-x)` at the
nodes `x_j=-q_j`.

## 3. Even terminal degree

Suppose

\[
 N-1=2m.
 \tag{L-92112.10}
\]

Every real polynomial of degree at most `2m` nonnegative on `[0,infinity)` has
the Markov--Lukacs representation

\[
 Q(s)=a(s)^2+s b(s)^2,
 \qquad
 \deg a\le m,
 \quad
 \deg b\le m-1.
 \tag{L-92112.11}
\]

Consequently (L-92112.8) is equivalent to the two exact PSD conditions

\[
 \boxed{
 H_m^{(0)}=(m_{i+j})_{0\le i,j\le m}\succeq0,
 }
 \tag{L-92112.12}
\]

\[
 \boxed{
 H_{m-1}^{(1)}=(m_{i+j+1})_{0\le i,j\le m-1}\succeq0.
 }
 \tag{L-92112.13}
\]

## 4. Odd terminal degree

Suppose

\[
 N-1=2m+1.
 \tag{L-92112.14}
\]

Every nonnegative polynomial of this degree bound has the representation

\[
 Q(s)=b(s)^2+s a(s)^2,
 \qquad
 \deg a,\deg b\le m.
 \tag{L-92112.15}
\]

Thus membership is equivalent to

\[
 \boxed{
 H_m^{(0)}\succeq0,
 \qquad
 H_m^{(1)}=(m_{i+j+1})_{0\le i,j\le m}\succeq0.
 }
 \tag{L-92112.16}
\]

## 5. Exact fail-closed separator

If one matrix fails, an exact vector `v` with negative quadratic form produces
a dual obstruction immediately.

- A negative vector for `H^(0)` gives
  \[
  Q(s)=\left(\sum_iv_is^i\right)^2\ge0.
  \]
- A negative vector for `H^(1)` gives
  \[
  Q(s)=s\left(\sum_iv_is^i\right)^2\ge0.
  \]

Set

\[
 \boxed{
 c_j=\frac{Q(-q_j)}{\Delta_j}.
 }
 \tag{L-92112.17}
\]

Then `P_c=(r+s)Q>=0` on the half-line while

\[
 \boxed{
 c\cdot y=\mathcal L_y(Q)<0.
 }
 \tag{L-92112.18}
\]

This is the exact polynomial Farkas separator required by `L-92111`; no root
isolation or general polynomial optimization is needed.

Conversely exact PSD factorizations of the two Hankel matrices certify every
half-line dual inequality and hence the existence of an at-most-`N`-atom
positive string.

## 6. Consequence for safe Xi

At stage `N`, the passive-string producer is now one deterministic matrix task:

```text
compute m_0,...,m_(N-1) from the N safe Xi values;
check two explicit Hankel matrices;
return exact PSD factors or one square-polynomial separator.
```

Successful stages still glue to one global string by `L-92110`. The unresolved
zeta-specific theorem is positivity of these two matrices for every finite safe
packet; the present result removes the larger general polynomial dual search.

## 7. Verification and boundary

`X-91688` checks an exact five-node positive atomic string and a deliberately
perturbed datum. The latter is separated by `Q(s)=s^2`, with exact value

\[
 -\frac{739}{176400}.
\]

```text
finite polynomial dual -> two Hankel tests       CLOSED
exact square-polynomial separator                CLOSED
finite positive string extraction                L-92111 / STANDARD
actual Xi two-Hankel positivity for every N       OPEN / RH-BEARING
near-cut uniform positive-string mechanism        OPEN
Riemann Hypothesis                                UNPROVEN
```
