# T-90007 — Every fixed-ratio endpoint shell is an RH-equivalent eventual-sign criterion

Claim ID: `T-90007` (provisional range; allocate before integration)  
Status: **PROPOSED COMPLETE RH EQUIVALENCE — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Depends on: `L-90004`; the contour-shift argument of `T-90006`; Landau's one-sign theorem  
Scope: the undifferenced endpoint scalar at an arbitrary fixed ratio; no unconditional sign and no proof of RH

## 1. Fixed-ratio shell

Retain

\[
A(X)=\sum_{p\le X}(\log p)r_X(p)
\]

from `L-90004`.  Fix once and for all

\[
0<c<1
\]

and define

\[
\boxed{
\mathscr T_c(X)=A(X)-A(cX).}
\tag{T-90007.1}
\]

The exact finite version may replace `cX` with `floor(cX)`; the interpolation
error is `o(1)` by `L-90004.24`.

## 2. Exact transform

Scaling in the Mellin integral gives

\[
\boxed{
\widehat{\mathscr T_c}(z)
=(1-c^z)\widehat A(z)
=\frac{1-c^z}{z^2}
\mathcal G\left(z+\frac12\right).}
\tag{T-90007.2}
\]

At the origin,

\[
1-c^z=-z\log c+O(z^2),
\]

and `L-90004.14` gives

\[
\widehat{\mathscr T_c}(z)
=\frac{\kappa_c}{z^2}+O(z^{-1}),
\tag{T-90007.3}
\]

where

\[
\boxed{
\kappa_c
=-\frac{1+\zeta(1/2)}2\log c<0.}
\tag{T-90007.4}
\]

Both factors `1+zeta(1/2)` and `log c` are negative, and the leading minus sign
therefore makes `kappa_c` strictly negative.

For `c=1/2`, this is the coefficient of `T-90006`:

\[
\kappa_{1/2}
=\frac{(1+\zeta(1/2))\log2}{2}.
\]

## 3. Off-line zeros can never be canceled by a fixed real ratio

Let

\[
\rho=\frac12+\delta+i\gamma,
\qquad \delta>0,
\]

be a hypothetical nontrivial zero to the right of the critical line, and put

\[
z_\rho=\rho-\frac12.
\]

`L-90004.18` gives the endpoint residue `m_rho/z_rho^2`.  The fixed-ratio shell
therefore has residue

\[
\boxed{
\operatorname*{Res}_{z=z_\rho}
\widehat{\mathscr T_c}(z)
=rac{m_\rho(1-c^{z_\rho})}{z_\rho^2}.}
\tag{T-90007.5}
\]

This residue is nonzero. Indeed,

\[
|c^{z_\rho}|=c^\delta<1,
\]

so `c^(z_rho)` cannot equal one.

The familiar lattice

\[
\gamma\log c\in2\pi\mathbb Z
\]

can annihilate a mode only when `delta=0`, i.e. for a zero already on the
critical line. Such a zero is allowed by RH and is irrelevant to the task of
excluding off-line zeros.

Thus a fixed real shell has **no RH-converse blind spot**.

## 4. Eventual one-sidedness implies RH directly

The pole at `s=1`, or `z=1/2`, cancels inside `mathcal G` by `L-90004.17`.
The prime-square pole is at the boundary point `z=0`; every other real
prime-zeta singularity lies on the nonpositive real axis. Therefore

\[
\widehat{\mathscr T_c}(z)
\]

has no singularity on the open positive real axis.

Assume that `mathscr T_c(X)` has one sign for every sufficiently large `X`.
Change sign if necessary and alter the function on a compact interval to obtain
a nonnegative locally integrable function of `log X`.  If an off-line zero
existed, (T-90007.5) would give a nonreal singularity in `Re z>0`, so the
Laplace transform would have positive abscissa of convergence. Landau's
one-sign theorem would then force a singularity at the corresponding positive
**real** boundary point. No such singularity exists.

Hence

\[
\boxed{
\mathscr T_c(X)\text{ eventually one-signed}
\Longrightarrow\mathrm{RH}.}
\tag{T-90007.6}
\]

This implication uses the shell transform itself.  It does not pass through
WSTS, `T-90002`, or the undifferenced endpoint functional.

## 5. RH gives eventual strict negativity

Under RH, the same contour shift as `T-90006` gives, for every fixed
`0<eta<1/6`,

\[
\boxed{
\begin{aligned}
\mathscr T_c(X)
={}&\kappa_c\log X+C_c\\
&+\sum_\rho
\frac{m_\rho(1-c^{\rho-1/2})}
     {(\rho-1/2)^2}
X^{\rho-1/2}
+O_{c,\eta}(X^{-\eta}\log^2(2X)).
\end{aligned}}
\tag{T-90007.7}
\]

The zero series is absolutely and uniformly convergent because

\[
|1-c^{i\gamma}|\le2,
\qquad
\sum_\rho\frac{m_\rho}{1+\gamma^2}<\infty.
\]

Thus

\[
\boxed{
\mathscr T_c(X)=\kappa_c\log X+O_c(1),
\qquad \kappa_c<0,}
\tag{T-90007.8}
\]

and `mathscr T_c(X)<0` for every sufficiently large `X`.

Combining Sections 4 and 5:

\[
\boxed{
\mathrm{RH}
\iff
\mathscr T_c(X)<0\text{ eventually}
\iff
\mathscr T_c(X)\text{ is eventually one-signed}.}
\tag{T-90007.9}
\]

The equivalence holds separately for **every fixed** ratio `c in (0,1)`.

## 6. Exact integer ratios and the dyadic front door

For rational `c=a/b`, restrict if desired to endpoints divisible by `b`, so
`cX` is exact. For arbitrary integer endpoints, replacing `cX` by `floor(cX)`
changes the shell by

\[
O_c\left(\frac{\log(2X)}{\sqrt X}\right),
\]

which cannot affect eventual negativity or the Landau implication.

At `c=1/2`, `T-90002` adds the separate finite-geometric fact that the entire
maximum over tail thresholds is controlled by the endpoint.  Therefore

\[
\mathrm{RH}\iff B_X=0\text{ eventually}.
\]

But the simpler endpoint equivalence (T-90007.9) does not require that
z-collapse theorem.

## 7. Correction to the old blind-spot warning

The historical warning in `T-90001` says that any fixed-ratio shell-only
converse is incomplete because `1-2^{-i\gamma}` vanishes on a frequency
lattice.  The warning is relevant only if one tries to retain every
**critical-line** zero mode. It is not an obstruction to proving RH:

```text
off-line zero: Re(rho-1/2)>0
=> |c^(rho-1/2)|<1
=> 1-c^(rho-1/2) != 0.
```

The correct scope statement is:

```text
A fixed-ratio shell may be blind to selected zeros already on the critical line,
but it is never blind to a zero to the right of that line.
```

Consequently eventual one-sidedness of the shell is a complete RH criterion.

## 8. Proof boundary

Closed, subject to independent review:

1. the exact arbitrary-ratio transform;
2. the universal negative drift coefficient;
3. noncancellation of every off-line zero;
4. direct Landau implication from shell one-sidedness to RH;
5. RH asymptotic and eventual negativity;
6. the equivalence for every fixed ratio;
7. correction of the shell blind-spot scope.

Still open:

- unconditional eventual one-sidedness for any fixed ratio;
- RH.
