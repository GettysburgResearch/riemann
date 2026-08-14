# R-92300 — Arbitrarily many positive Hankel orders can hide one off-line pole pair

Claim ID: `R-92300`  
Status: **EXACT FINITE SQUARED-POLE FIREWALL**  
Created: 2026-08-14  
Depends on: `L-92204` Cauchy--Binet formula  
RH status: **unproved**

## 1. Finite squared-pole system

Fix distinct positive real poles

\[
 r_1,\ldots,r_N>0
\]

with positive weights `w_1,...,w_N`, and one nonreal conjugate pair

\[
 s=c+id,\qquad\bar s=c-id,\qquad d\ne0,
\]

with equal weight `epsilon>0`.  Put

\[
 p_\varepsilon(t)
 =\sum_{j=1}^N\frac{w_j}{t+r_j}
  +\varepsilon\left(
   \frac1{t+s}+\frac1{t+\bar s}
  \right)
\]

and

\[
 A_k(t)=\frac{(-1)^k}{k!}p_\varepsilon^{(k)}(t),
 \qquad
 H_n(t)=\bigl(A_{i+j+1}(t)\bigr)_{0\le i,j<n}.
\]

The function is real and positive on a sufficiently far positive axis, but it
is not Stieltjes because it has two nonreal poles.

## 2. Every prescribed finite initial hierarchy can remain positive

At `epsilon=0`, the moment matrix is the Gram of `N` distinct positive real
atoms.  Hence

\[
 H_n(t)\succ0
 \qquad(1\le n\le N)
\]

for every `t>0`.

On any fixed compact positive interval, the matrices depend continuously on
`epsilon`.  Therefore there exists `epsilon_0>0` such that

\[
 \boxed{
 H_n(t)\succ0
 \quad
 (1\le n\le N,\ 0<\varepsilon<\varepsilon_0)
 }
 \tag{R-92300.1}
\]

uniformly on that interval.

If `c` is chosen sufficiently large relative to `|d|` and the real poles, the
leading `O(epsilon)` term of `det H_(N+1)` is the positive real part of the two
subsets

\[
 \{r_1,\ldots,r_N,s\},
 \qquad
 \{r_1,\ldots,r_N,\bar s\}.
\]

Thus, after possibly decreasing `epsilon_0`, one can also arrange

\[
 \boxed{
 H_{N+1}(t)\succ0.
 }
 \tag{R-92300.2}
\]

## 3. The next determinant is forced negative

At order `N+2`, Cauchy--Binet has only one subset: the complete pole set.  Thus

\[
 \det H_{N+2}(t)
 =\left(\prod_{j=1}^Nw_j\right)\varepsilon^2
 \frac{
  \Delta(r_1,\ldots,r_N,s,\bar s)^2
 }{
  \prod_{j=1}^N(t+r_j)^{2N+4}
  (t+s)^{2N+4}(t+\bar s)^{2N+4}
 }.
\]

Every factor is positive real except

\[
 (s-\bar s)^2=-4d^2<0.
\]

Indeed,

\[
 (s-r_j)^2(\bar s-r_j)^2=|s-r_j|^4>0
\]

and the conjugate denominator product is positive.  Therefore

\[
 \boxed{
 \det H_{N+2}(t)<0
 \qquad(t>0).
 }
 \tag{R-92300.3}
\]

A single off-line pair can thus be invisible through an arbitrarily long
initial Hankel/Loewner hierarchy and then fail at the next order.

## 4. Exact retained control

The experiment uses

\[
 r_j\in\{1,2,4,8,16,32\},
 \quad
 s=100+i,
 \quad
 \varepsilon=10^{-12},
 \quad
 t=1.
\]

The exact rational determinants are positive through order seven and

\[
 \boxed{
 \det H_8(1)
 =-
 \frac{575671453274979755246918287556689228386931081}
 {64111855235481762964570686298724399543749225573178387629297255457844452641508889803039270788405979826138411921556326470947265625000000000000}
 <0.
 }
 \tag{R-92300.4}
\]

## 5. Consequence for the Xi programme

The verified critical reserve can make very many low-order inequalities true
without eliminating a sparse off-line pair.  In the finite model, every added
real critical pole can postpone the first forced full-determinant failure by
one order.

Therefore neither

```text
all fixed orders separately on the high axis;
a growing but subcofinal order n(x);
an enormous adjacent-minor tower;
```

is by itself a route to RH.

A conclusion-producing proof must either:

1. control all matrix orders at one finite safe point;
2. construct the complete positive Krein string directly; or
3. use a pair-adapted nonconfluent test that bypasses the long real-pole
   hierarchy.

This is the all-order analogue of the structural limitation explicitly noted
in Claude's bandwidth-one compression: sparse off-line information can be
invisible to every prescribed low-complexity certificate.

## 6. Exact boundary

```text
positive Hankel orders 1,...,N                EXACTLY POSSIBLE
positive order N+1                              EXACTLY POSSIBLE
negative order N+2                              EXACT FOR THE FINITE MODEL
arbitrarily delayed off-line witness            EXACT
finite/growing-order positivity -> RH           FALSE
actual Xi all-order hierarchy                   OPEN / RH-EQUIVALENT
Riemann Hypothesis                              UNPROVED
```
