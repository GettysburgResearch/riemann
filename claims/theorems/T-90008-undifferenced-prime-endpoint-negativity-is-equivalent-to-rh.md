# T-90008 — Eventual negativity of the undifferenced prime endpoint is equivalent to RH

Claim ID: `T-90008` (provisional range; allocate before integration)  
Status: **PROPOSED COMPLETE RH EQUIVALENCE — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Depends on: `L-90004`; Landau's one-sign theorem; the contour-shift argument of `T-90006`  
Scope: the single undifferenced endpoint scalar; no unconditional sign and no proof of RH

## 1. Statement

Retain

\[
\boxed{
A(X)=\sum_{p\le X}(\log p)r_X(p)
=J_{\mathbb P}(X)-P_{\mathbb P}(X)
}
\tag{T-90008.1}
\]

from `L-90004`, where the parabolic seed and prime ramp are exactly those of
`T-90001`.

Then the following are equivalent:

1. RH;
2. `A(X)<0` for every sufficiently large real `X`;
3. `A(X)` has one sign for every sufficiently large real `X`;
4. `A_N<0` for every sufficiently large integer `N`.

Under RH there are real constants `C_1,C_0` such that, for every fixed
`0<eta<1/6`,

\[
\boxed{
\begin{aligned}
A(X)
={}&\frac{1+\zeta(1/2)}4\log^2X
+C_1\log X+C_0\\
&+\sum_\rho
\frac{m_\rho}{(\rho-1/2)^2}
X^{\rho-1/2}
+O_\eta(X^{-\eta}\log^2(2X)).
\end{aligned}}
\tag{T-90008.2}
\]

The zero series is absolutely and uniformly convergent under RH. Since

\[
\frac{1+\zeta(1/2)}4
=-0.1150886272023967032223747881\ldots<0,
\tag{T-90008.3}
\]

one has

\[
\boxed{
A(X)=\frac{1+\zeta(1/2)}4\log^2X+O(\log X)<0
}
\tag{T-90008.4}
\]

for every sufficiently large `X`.

Thus the entire post-`z`-collapse front door can be compressed to one finite
prime-weighted inequality with no scale ratio and no tail threshold.

## 2. Exact transform

`L-90004` proves

\[
\boxed{
\widehat A(z)
=\int_1^\infty A(X)X^{-z-1}\,dX
=\frac1{z^2}\mathcal G\left(z+\frac12\right),
}
\tag{T-90008.5}
\]

initially for `Re z>1/2`, with meromorphic continuation to the region needed
below.

At the origin,

\[
\mathcal G\left(\frac12+z\right)
=\frac{1+\zeta(1/2)}{2z}+O(1),
\]

so

\[
\boxed{
\widehat A(z)
=\frac{1+\zeta(1/2)}{2z^3}
+\frac{c_1}{z^2}+\frac{c_0}{z}+O(1).
}
\tag{T-90008.6}
\]

The third-order pole contributes

\[
\frac12\cdot\frac{1+\zeta(1/2)}2\log^2X
=\frac{1+\zeta(1/2)}4\log^2X,
\]

which gives (T-90008.3).

## 3. Pole audit

`L-90004` also proves:

- the apparent pole at `z=1/2`, coming from the main zeta pole, cancels;
- every nontrivial zero `rho` gives the genuine simple pole
  \[
  \boxed{
  \operatorname*{Res}_{z=\rho-1/2}\widehat A(z)
  =\frac{m_\rho}{(\rho-1/2)^2};
  }
  \tag{T-90008.7}
  \]
- the prime-square main-pole copy is the boundary pole at `z=0` already
  extracted in (T-90008.6);
- every further main-pole copy and every `m>=2` nontrivial-zero copy lies in the
  open left half-plane.

There is no singularity on the open positive real axis.  Indeed zeta has no real
zero for `s>1/2`, the only real pole at `s=1` has canceled, and all prime-zeta
copies with index at least two lie at `Re z<=0`.

## 4. Eventual one-sidedness implies RH

Assume that `A(X)` is eventually one-signed.  Change sign if needed and alter it
on a compact interval so that

\[
f(t)=\pm A(e^t)\ge0
\]

for every `t>=0`.

Suppose an off-line zero exists,

\[
\rho=\frac12+\delta+i\gamma,
\qquad \delta>0.
\]

By (T-90008.7), the Laplace transform of `f` has a genuine nonreal singularity
at `z=delta+i gamma`.

Let `sigma_c` be its finite abscissa of convergence. If `sigma_c<delta`, the
defining Laplace integral is holomorphic at that point, contradicting the pole.
If `sigma_c>=delta`, Landau's one-sign theorem forces a singularity at the real
point `sigma_c>0`, contradicting the positive-real pole audit in Section 3.

Therefore no nontrivial zero lies to the right of the critical line. The
functional equation gives

\[
\boxed{
A(X)\text{ eventually one-signed}\Longrightarrow\mathrm{RH}.}
\tag{T-90008.8}
\]

This is a direct argument. It does not use WSTS, a fixed-ratio shell, z-collapse,
or square-screw transport.

## 5. RH gives eventual negativity

Assume RH and shift the Mellin contour as in `T-90006` to

\[
\Re z=-\eta,
\qquad0<\eta<1/6.
\]

The residues crossed are:

1. the order-three origin pole (T-90008.6);
2. every critical-line zero pole (T-90008.7).

The remaining prime-zeta descendants lie to the left of the new line, and the
vertical remainder is

\[
O_\eta(X^{-\eta}\log^2(2X)).
\]

This proves (T-90008.2). On RH, writing `rho=1/2+i gamma`,

\[
\sum_\rho
\left|\frac{m_\rho X^{i\gamma}}{(i\gamma)^2}\right|
\le
\sum_\rho\frac{m_\rho}{\gamma^2}<\infty.
\]

Hence the zero series is bounded, and the negative quadratic logarithmic term
dominates. This proves (T-90008.4).

## 6. Integer endpoints

`L-90004.24` gives

\[
A(X)-A(\lfloor X\rfloor)
=O\left(\frac{\log(2X)}{\sqrt X}\right).
\]

Thus eventual negativity on real endpoints and on integer endpoints are
equivalent. No endpoint jump can compete with the quadratic logarithmic drift.

## 7. Relation to the shell criteria

`T-90007` follows by applying a fixed scale difference to `A`:

\[
A(X)-A(cX)
=-\frac{1+\zeta(1/2)}2\log c\,\log X+O_c(1)
\]

under RH.  The scale difference reduces the degree of the deterministic drift
from two to one but is not needed for the RH converse.

At `c=1/2`, `T-90002` additionally converts the endpoint shell sign into the
full statement `B_X=0` eventually.

The logical hierarchy is therefore

```text
A(X)<0 eventually                    <=> RH;
A(X)-A(cX)<0 eventually, fixed c     <=> RH;
B_X=0 eventually, dyadic z-collapse <=> RH.
```

The first line is the smallest finite scalar statement.

## 8. Finite evidence and exact boundary

The exact radical-switching implementation in `X-90007` gives

```text
A(10^5) = -12.549075127689093...
A(2*10^5) = -14.253996650994623...
A(5*10^5) = -16.711392164913832...
A(10^6) = -18.736439240246455...
```

These values are regression evidence only. The theorem's cofinal implication is
analytic and does not extrapolate from the scan.

Closed, subject to independent review:

1. the direct undifferenced Landau criterion;
2. the RH explicit formula (T-90008.2);
3. the negative quadratic drift coefficient;
4. RH implies eventual strict negativity;
5. real/integer endpoint equivalence;
6. the four-way equivalence in Section 1.

Still open:

- an unconditional proof that `A(X)<0` eventually;
- RH.
