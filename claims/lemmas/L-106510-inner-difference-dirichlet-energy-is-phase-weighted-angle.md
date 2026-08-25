# L-106510 — Inner-difference Dirichlet energy is a phase-weighted angle

Claim ID: `L-106510`  
Status: **PROVED EXACT FOR FINITE INNER FUNCTIONS**  
Created: 2026-08-25  
Depends on: `L-106507`; the boundary representation of the analytic Dirichlet seminorm  
RH status: **not assumed**

Let `B_+,B_-` be finite inner functions in the disk normalization and write on
the boundary

\[
B_+(e^{it})=e^{i\alpha(t)},
\qquad
B_-(e^{it})=e^{i\beta(t)}.
\]

Their inner phase densities satisfy

\[
\alpha'(t)\ge0,
\qquad
\beta'(t)\ge0,
\]

and integrate to `2 pi deg B_+` and `2 pi deg B_-`, respectively.

## 1. Exact boundary identity

For every analytic polynomial or finite Dirichlet function `f`,

\[
\|f\|_{\mathcal D}^2
={1\over2\pi}
\operatorname{Re}\int_0^{2\pi}
\overline{f(e^{it})}{1\over i}{d\over dt}f(e^{it})\,dt.
\tag{L-106510.1}

Put `f=B_+-B_-`.  Direct substitution gives

\[
\operatorname{Re}
\left[
(\overline{B_+}-\overline{B_-})
(\alpha'B_+-\beta'B_-)
\right]
=(\alpha'+\beta')
\left(1-\cos(\alpha-\beta)\right).
\]

Therefore

\[
\boxed{
\|B_+-B_-\|_{\mathcal D}^2
={1\over2\pi}
\int_0^{2\pi}
(\alpha'+\beta')
\left(1-\cos(\alpha-\beta)\right)dt.
}
\tag{L-106510.2}

Equivalently,

\[
\boxed{
\|B_+-B_-\|_{\mathcal D}^2
={1\over4\pi}
\int_0^{2\pi}
(\alpha'+\beta')|B_+-B_-|^2dt.
}
\tag{L-106510.3}

This is positive term by term and calibrates a single unmatched inner factor
to one Dirichlet unit.

## 2. Outer-normalized endpoint form

For the common-outer factorization

\[
N=OB_+,
\qquad D=OB_-,
\]

one has on the boundary

\[
|B_+-B_-|^2
={|N-D|^2\over|D|^2}.
\]

For the odd endpoint pair of `L-106501`,

\[
|N-D|^2=4\lambda^2\mathcal L_K^2
\]

and

\[
|D|^2
=(F^2+\lambda^2F'^2)
((F^{(K)})^2+\lambda^2(F^{(K+1)})^2).
\]

Hence

\[
\boxed{
\left\|{N-D\over O}\right\|_{\mathcal D}^2
={\lambda^2\over\pi}
\int
(\alpha'+\beta')
{\mathcal L_K(t)^2
 \over
(F^2+\lambda^2F'^2)
((F^{(K)})^2+\lambda^2(F^{(K+1)})^2)}\,dt.
}
\tag{L-106510.4)

The integral is over the regular compactified boundary; the half-plane form
is obtained by conformal transport and includes the point at infinity.

## 3. Fifth endpoint

At `K=5`, the exact open scalar becomes

\[
\boxed{
\mathcal E_{5,\lambda}
={\lambda^2\over\pi}
\int
(\alpha_5'+\beta_5')
{(F'F^{(5)}-FF^{(6)})^2
 \over
(F^2+\lambda^2F'^2)
((F^{(5)})^2+\lambda^2(F^{(6)})^2)}\,dt.
}
\tag{L-106510.5)

By `L-106507`,

\[
\|H_{U_{5,\lambda}}\|_{\mathcal S_2}^2
\le\mathcal E_{5,\lambda}.
\]

Thus `OUTERDIR106520` is a positive phase-weighted mean-value estimate, not an
abstract inverse-frame statement.

## 4. Scope

The phase densities are those of the reduced inner factors, not the raw
argument derivatives of `N` and `D`; their common outer phase must be removed.
No estimate of (L-106510.4)--(L-106510.5) is asserted here.
