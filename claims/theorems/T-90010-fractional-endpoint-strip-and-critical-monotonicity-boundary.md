# T-90010 — The fractional endpoint strip and the critical monotonicity boundary

Claim ID: `T-90010` (provisional range; branch-qualified)  
Title: Every fractional Mellin smoothing order strictly above one gives an RH-equivalent eventual-negative endpoint, while order one is the first non-absolutely-summable zero boundary  
Status: **PROPOSED COMPLETE RH-EQUIVALENCE FAMILY — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Depends on: `L-90004`, `T-90008`, `T-90009`; elementary fractional Laplace calculus; the classical zero-counting bound `N(T)=O(T log T)`  
Scope: a continuum of linear endpoint criteria; no unconditional sign and no proof of RH

## 1. Logarithmic endpoint path

Let

\[
 a(t)=A(e^t),
 \qquad t\ge0,
\tag{T-90010.1}
\]

where `A` is the undifferenced prime endpoint of `L-90004`.  The path is
continuous, piecewise continuously differentiable, and

\[
 a(0)=A(1)=0.
\tag{T-90010.2}
\]

Its Laplace transform is

\[
 \widetilde a(z)=\widehat A(z)
 ={1\over z^2}\mathcal G\left(z+\frac12\right).
\tag{T-90010.3}
\]

At the origin,

\[
 \widetilde a(z)
 ={1+\zeta(1/2)\over2z^3}
 +{c_1\over z^2}+{c_0\over z}+O(1).
\tag{T-90010.4}
\]

Every nontrivial zero `rho` gives the pole

\[
 \operatorname*{Res}_{z=\rho-1/2}\widetilde a(z)
 ={m_\rho\over(\rho-1/2)^2}.
\tag{T-90010.5}
\]

## 2. Fractional endpoint family

Fix

\[
 1<\sigma\le2,
 \qquad
 \alpha=2-\sigma\in[0,1).
\tag{T-90010.6}
\]

For `sigma=2`, put

\[
 \mathscr A_2(t)=a(t).
\]

For `1<sigma<2`, define the Caputo/Riemann--Liouville derivative

\[
\boxed{
 \mathscr A_\sigma(t)
 ={1\over\Gamma(\sigma-1)}
 \int_0^t(t-u)^{\sigma-2}a'(u)\,du.
}
\tag{T-90010.7}
\]

The exponent `sigma-2` lies in `(-1,0)`, so the integral is locally integrable.
Because `a(0)=0`, the Caputo and Riemann--Liouville forms agree.  Standard
Laplace convolution gives, initially in the convergence half-plane,

\[
\boxed{
 \widetilde{\mathscr A_\sigma}(z)
 =z^{2-\sigma}\widetilde a(z)
 ={1\over z^\sigma}
  \mathcal G\left(z+\frac12\right),
}
\tag{T-90010.8}
\]

where the principal power is used on `Re z>0`.

Thus the endpoint scalar `A` is the order-two member, and the limiting
order-one object is the logarithmic derivative

\[
 \mathscr A_1(t)=a'(t)=\mathcal D_XA(X),
 \qquad X=e^t.
\tag{T-90010.9}
\]

## 3. Pole audit

At an off-line zero

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad\delta>0,
\]

(T-90010.8) has the genuine residue

\[
\boxed{
 \operatorname*{Res}_{z=\rho-1/2}
 \widetilde{\mathscr A_\sigma}(z)
 ={m_\rho\over(\rho-1/2)^\sigma}\ne0.
}
\tag{T-90010.10}
\]

Multiplication by `z^(2-sigma)` introduces no zero in the open right half-plane.
The pole at `s=1` was already canceled in `G`, and zeta has no real zero for
`s>1/2`. Therefore the transform has no singularity on the open positive real
axis.

At the origin,

\[
\boxed{
 \widetilde{\mathscr A_\sigma}(z)
 ={1+\zeta(1/2)\over2z^{\sigma+1}}
 +{c_1\over z^\sigma}
 +{c_0\over z^{\sigma-1}}
 +O(z^{2-\sigma}).
}
\tag{T-90010.11}
\]

The leading physical drift is therefore

\[
\boxed{
 {1+\zeta(1/2)\over2\Gamma(\sigma+1)}t^\sigma<0.
}
\tag{T-90010.12}
\]

## 4. RH gives eventual strict negativity for every sigma>1

Assume RH.  The zero residue series of the fractional endpoint is

\[
\sum_\rho
 {m_\rho\over(i\gamma)^\sigma}e^{i\gamma t}.
\tag{T-90010.13}
\]

The classical count

\[
 N(T)=O(T\log T)
\]

implies

\[
\boxed{
 \sum_\rho{m_\rho\over1+|\gamma|^\sigma}<\infty
 \qquad(\sigma>1).
}
\tag{T-90010.14}
\]

Hence (T-90010.13) converges absolutely and uniformly in `t`.  Applying
(T-90010.7) to the RH explicit formula of `T-90008`, or equivalently performing
the branch-point contour inversion of (T-90010.8), gives

\[
\boxed{
 \mathscr A_\sigma(t)
 ={1+\zeta(1/2)\over2\Gamma(\sigma+1)}t^\sigma
 +O_\sigma(t^{\sigma-1}+1).
}
\tag{T-90010.15}
\]

Because the leading coefficient is negative,

\[
\boxed{
 \mathrm{RH}
 \Longrightarrow
 \mathscr A_\sigma(t)<0
 \quad\text{for every sufficiently large }t.
}
\tag{T-90010.16}
\]

The assertion holds separately for every fixed `sigma>1`; no uniformity as
`sigma downarrow1` is claimed.

## 5. Eventual one-sidedness implies RH

Assume `mathscr A_sigma(t)` is eventually one-signed. Change sign if needed and
alter it on a compact interval to obtain a nonnegative locally integrable
function.

If an off-line zero existed, (T-90010.10) would give a nonreal pole in the open
right half-plane. The Laplace transform has a finite abscissa of convergence
because the original endpoint has at most `e^(t/2)` times a polynomial and the
fractional operator does not increase that exponent.

If the abscissa lay to the left of the pole, the defining integral would be
holomorphic there. If it reached or passed the pole, Landau's one-sign theorem
would force a singularity at the corresponding positive **real** boundary
point. Section 3 proves that no such real singularity exists.

Therefore

\[
\boxed{
 \mathscr A_\sigma(t)\text{ eventually one-signed}
 \Longrightarrow\mathrm{RH}.
}
\tag{T-90010.17}

Combining Sections 4 and 5:

\[
\boxed{
 \mathrm{RH}
 \iff
 \mathscr A_\sigma(t)<0\text{ eventually}
 \iff
 \mathscr A_\sigma(t)\text{ eventually one-signed}
}
\tag{T-90010.18}
\]

for every fixed `1<sigma<=2`.

## 6. The half-derivative criterion

The midpoint `sigma=3/2` is especially concrete:

\[
\boxed{
 \mathscr A_{3/2}(t)
 ={1\over\sqrt\pi}
 \int_0^t{a'(u)\over\sqrt{t-u}}\,du.
}
\tag{T-90010.19}
\]

Its zero weights are `1/(rho-1/2)^(3/2)`, still absolutely summable on RH, and
its deterministic drift is

\[
 {1+\zeta(1/2)\over2\Gamma(5/2)}t^{3/2}<0.
\]

Thus a positive-kernel half-integral of the exact weighted-Chebyshev derivative
gate remains exactly RH-equivalent while retaining an unconditional RH-side
sign under RH.

This is the closest simple member to endpoint monotonicity that still lies
strictly above the absolute-convergence threshold.

## 7. Why order one is the critical boundary

At `sigma=1`, the formal zero coefficients are

\[
 {m_\rho\over i\gamma}.
\]

But

\[
 \sum_\rho{m_\rho\over|\gamma|}=\infty.
\]

Therefore the argument of Section 4 stops exactly at order one: RH alone no
longer supplies an absolutely and uniformly bounded zero series by this method.
The order-one member is precisely

\[
 a'(t)=\mathcal D_XA(X),
\]

the endpoint-monotonicity gate of `T-90009`.

Accordingly the live hierarchy is

```text
sigma=2:
    undifferenced endpoint A;

1<sigma<2:
    fractional endpoints, RH-equivalent and RH-eventually-negative;

sigma=1:
    endpoint monotonicity, still RH-sufficient but not obtained from RH by
    absolute zero summation.
```

This identifies `sigma=1` as the exact absolute-convergence firewall, not as a
proved logical separation from RH.

## 8. Finite arithmetic form

The derivative in (T-90010.7) is already explicit on each interval by
`T-90009`:

\[
 a'(u)
 =2S_{1/2}(N)-2e^{-u/2}S_1(N)-\vartheta_{1/2}(N),
 \qquad \log N<u<\log(N+1).
\]

Therefore every fractional endpoint is a finite sum of elementary integrals
against the positive kernel `(t-u)^(sigma-2)`.  No zero data are required to
evaluate the criterion at one finite endpoint.

A future exact certificate may integrate each interval in beta/hypergeometric
coordinates.  No such cofinal sign certificate is asserted here.

## 9. Proof boundary

Closed, subject to independent review:

1. the fractional endpoint definition;
2. the exact transform `G/z^sigma`;
3. survival of every off-line zero;
4. the negative fractional drift;
5. absolute RH zero convergence for every `sigma>1`;
6. RH implies eventual strict negativity;
7. eventual one-sidedness implies RH;
8. the continuum of RH-equivalent criteria;
9. the order-one absolute-convergence firewall;
10. the explicit half-derivative criterion.

Still open:

1. unconditional eventual sign for any member;
2. endpoint monotonicity at `sigma=1`;
3. RH.
