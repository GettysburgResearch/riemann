# L-92113 — RH gives strict positivity of every finite safe-Xi barycentric Hankel pair

Claim ID: `L-92113`  
Status: **PROVED EXACT CONSEQUENCE OF RH; USED AS A COROLLARY OF THE FACTOR-67 PROPOSAL**  
Created: 2026-08-14  
Primary inputs: the centered Hadamard product; `L-92112`  
RH status: **equivalent direction proved here: RH implies the finite Hankel signs**

## 1. Centered Xi product under RH

Write

\[
\Xi_c(z)=\xi\!\left(\frac12+z\right).
\]

The function is even. Under RH, its nonzero zeros are

\[
z=\pm i\gamma,
\qquad
\gamma>0,
\]

with multiplicities retained. Since

\[
\sum_{\gamma>0}\gamma^{-2}<\infty,
\]

the paired Hadamard product is

\[
\boxed{
\Xi_c(z)=\Xi_c(0)
\prod_{\gamma>0}
\left(1+\frac{z^2}{\gamma^2}\right).
}
\tag{L-92113.1}
\]

For `q>0`, logarithmic differentiation gives

\[
\boxed{
y(q):=
\frac{\Xi_c'(\sqrt q)}
{\sqrt q\,\Xi_c(\sqrt q)}
=2\sum_{\gamma>0}\frac{1}{q+\gamma^2}.
}
\tag{L-92113.2}
\]

The series converges locally uniformly on the safe half-line.

## 2. Finite barycentric moments

Fix distinct safe nodes

\[
q_1,\ldots,q_N>0,
\]

put

\[
D(s)=\prod_{i=1}^N(q_i+s),
\qquad
\Delta_j=\prod_{i\ne j}(q_i-q_j),
\]

and define the barycentric moments of `L-92112`:

\[
m_k=\sum_{j=1}^N
\frac{y(q_j)(-q_j)^k}{\Delta_j},
\qquad 0\le k\le N-1.
\tag{L-92113.3}
\]

For every polynomial `Q` of degree at most `N-1`, the partial-fraction identity

\[
\frac{Q(s)}{D(s)}
=\sum_{j=1}^N
\frac{Q(-q_j)}{\Delta_j(q_j+s)}
\tag{L-92113.4}
\]

and (L-92113.2) give

\[
\boxed{
\mathcal L_y(Q):=
\sum_{j=1}^Ny(q_j)\frac{Q(-q_j)}{\Delta_j}
=2\sum_{\gamma>0}\frac{Q(\gamma^2)}{D(\gamma^2)}.
}
\tag{L-92113.5}
\]

In particular

\[
\boxed{
m_k=2\sum_{\gamma>0}
\frac{\gamma^{2k}}{D(\gamma^2)}.}
\tag{L-92113.6}
\]

The last series converges even for `k=N-1`, because its terms are
`O(gamma^-2)`.

## 3. The two Hankel forms

Let

\[
a(s)=\sum_{i=0}^m v_i s^i.
\]

For every nonzero real vector `v`,

\[
\begin{aligned}
v^TH_m^{(0)}v
&=\mathcal L_y(a^2)\\
&=2\sum_{\gamma>0}
\frac{a(\gamma^2)^2}{D(\gamma^2)}>0.
\end{aligned}
\tag{L-92113.7}
\]

The strict inequality holds because a nonzero polynomial has only finitely many
zeros, while Xi has infinitely many positive ordinates.

Likewise,

\[
\begin{aligned}
v^TH_m^{(1)}v
&=\mathcal L_y(sa^2)\\
&=2\sum_{\gamma>0}
\frac{\gamma^2a(\gamma^2)^2}{D(\gamma^2)}>0.
\end{aligned}
\tag{L-92113.8}
\]

Therefore every matrix required by the parity cases of `L-92112` is positive
definite. In particular, for every finite safe Xi packet,

\[
\boxed{H_N^{(0)}\succeq0,\qquad H_N^{(1)}\succeq0.}
\tag{L-92113.9}
\]

## 4. Positive-string representation

Fix an anchor `r>0` and put

\[
d\nu_r(s)=2\sum_{\gamma>0}
\frac{\delta_{\gamma^2}(ds)}{r+\gamma^2}.
\]

Its total mass is `y(r)<infinity`, and

\[
\boxed{
y(q)=\int_{[0,\infty)}\frac{r+s}{q+s}\,d\nu_r(s).}
\tag{L-92113.10}
\]

Thus the same argument directly supplies the finite positive-string membership
of `L-92111`.

## 5. Use in the triple proposal

`T-91660`, together with the frozen one-sided endpoint consumer, is a proposed
proof of RH. If that factor-67 proposal survives independent reconstruction,
the present theorem applies and closes statement C without any additional
near-cut asymptotic argument.

Conversely, `L-92110--L-92112` show that all finite safe packets imply a global
Stieltjes realization and then RH. Hence this all-order finite positivity is not
a weaker routine estimate; it is an exact RH-level conclusion.

```text
RH -> paired centered Xi product               EXACT
RH -> positive Stieltjes zero measure          EXACT
barycentric moment formula                     EXACT
both finite Hankel pairs positive definite     EXACT
factor-67 proposal -> RH                       FROZEN / REVIEW
unconditional acceptance of C                  PENDING THAT REVIEW
```
