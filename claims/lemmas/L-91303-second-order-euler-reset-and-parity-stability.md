# L-91303 — A second-order Euler correction pins the factor-54 reset to `c0 X+O(1)` and is absorbed by the parity shadow

Claim ID: `L-91303`  
Status: **PROVED UNIFORM ASYMPTOTIC/ROBUST-HALL THEOREM; FINAL DIVISOR-COLLAR LIFT OPEN**  
Created: 2026-08-12  
Depends on: `L-91106`, `L-91107`, `L-91109`, `L-91110`, `L-91111`  
RH status: **unproved**

## 1. Exact finite and continuum equality seeds

For integer `X>=1`, let

\[
 b_X^\star(n)
 =\sum_{k\le X/n}\frac{\mu(k)}{\sqrt k}
   \sum_{m=n}^{\lfloor X/k\rfloor}
   m^{-1/2}\log\frac{X}{km}.
\tag{L-91303.1}
\]

For `theta in [1/55,1]`, put

\[
 \mathscr B^\star(\theta)
 =\sum_{k\le1/\theta}\frac{\mu(k)}k
 \left[4(1-\sqrt{k\theta})
       +2\sqrt{k\theta}\log(k\theta)\right]
\tag{L-91303.2}
\]

as in `L-91106`, and define the first Euler density

\[
 \boxed{
 \mathscr D(\theta)
 =\theta^{-1/2}
  \sum_{k\le1/\theta}
  \frac{\mu(k)}{\sqrt k}
  \log\frac1{k\theta}.
 }
\tag{L-91303.3}
\]

## 2. Uniform Euler--Maclaurin expansion

Fix one active `k<=55` and write

\[
 g_k(u)=u^{-1/2}\log\frac1{ku},
 \qquad
 M_k=\lfloor X/k\rfloor.
\]

If `theta=n/X` and `k<=1/theta`, then

\[
 \sum_{m=n}^{M_k}m^{-1/2}\log\frac{X}{km}
 =X^{-1/2}\sum_{m=n}^{M_k}g_k(m/X).
\]

The trapezoidal Euler formula gives

\[
\begin{aligned}
 X^{-1/2}\sum_{m=n}^{M_k}g_k(m/X)
 ={}&\sqrt X\int_\theta^{M_k/X}g_k(u)du\\
 &+\frac{g_k(\theta)+g_k(M_k/X)}{2\sqrt X}
 +O(X^{-3/2}).
\end{aligned}
\tag{L-91303.4}
\]

The error is uniform because only `k<=55` occurs and
`u>=1/55`.  At the upper endpoint `u=1/k`,

\[
 g_k(1/k)=0,
 \qquad
 g_k'(1/k)=-k^{3/2}.
\]

Since `0<=1/k-M_k/X<1/X`, extending the integral to `1/k` and
removing `g_k(M_k/X)` changes (L-91303.4) by only `O(X^-3/2)`.
Therefore

\[
\boxed{
 \sum_{m=n}^{\lfloor X/k\rfloor}m^{-1/2}\log\frac{X}{km}
 =\sqrt X\int_\theta^{1/k}g_k(u)du
  +\frac{g_k(\theta)}{2\sqrt X}
  +O(X^{-3/2}).
}
\tag{L-91303.5}
\]

Summing the finite Möbius packet yields the uniform expansion

\[
\boxed{
 b_X^\star(n)
 =\sqrt X\,\mathscr B^\star(n/X)
  +\frac{1}{2\sqrt X}\mathscr D(n/X)
  +O(X^{-3/2})
}
\tag{L-91303.6}
\]

for every integer `n>=X/55`.  The implied constant is absolute and
computable from the first 55 cells.

Since the parabolic seed is exactly proportional, the equality correction of
`L-91106` satisfies

\[
\boxed{
 F_X^\star(n)
 =\sqrt X\,\mathscr F(n/X)
  +\frac{1}{2\sqrt X}\mathscr D(n/X)
  +O(X^{-3/2}).
}
\tag{L-91303.7}
\]

This improves the previous one-sided `113/sqrt(X)` corridor by two full powers
after the explicit first correction is retained.

## 3. The finite crossing is `c0 X+O(1)`

Let `c0` be the unique crossing of `mathscr F` on the fifty-fourth cell.
`L-91106` gives

\[
 \mathscr F(c_0)=0,
 \qquad
 \mathscr F'(c_0)>0.
\]

Equation (L-91303.7) and the implicit-function expansion give the continuous
finite crossing

\[
\boxed{
 \theta_X
 =c_0-\frac{\mathscr D(c_0)}
              {2\mathscr F'(c_0)}\frac1X
  +O(X^{-2}).
}
\tag{L-91303.8}
\]

Equivalently,

\[
\boxed{
 X\theta_X
 =c_0X-\frac{\mathscr D(c_0)}{2\mathscr F'(c_0)}
  +O(X^{-1}).
}
\tag{L-91303.9}
\]

Hence there is an absolute integer `C0` such that the finite outer peel may use

\[
\boxed{
 K_X\le c_0X+C_0.
}
\tag{L-91303.10}
\]

This is the exact scale requirement H1 of `T-91101`; no `epsilon X` retreat is
needed.  Numerical reconnaissance gives

\[
 -\frac{\mathscr D(c_0)}{2\mathscr F'(c_0)}
 =1.2277\ldots,
\]

but the theorem uses only the certified simple crossing and finite cell bounds.
The bounded top endpoint collar remains a separate direct finite check.

## 4. The corrected remainder is negligible in every inherited column

Define

\[
 E_X(n)=F_X^\star(n)
 -\sqrt X\mathscr F(n/X)
 -\frac1{2\sqrt X}\mathscr D(n/X).
\]

Then

\[
 |E_X(n)|\le C X^{-3/2}
 \qquad(n\ge X/55).
\tag{L-91303.11}
\]

If `q>=X/55`, at most 55 multiples occur in its carry response.  Therefore

\[
\boxed{
 |v_q(E_X)|\le110C X^{-3/2},
}
\tag{L-91303.12}
\]

and

\[
\boxed{
 |\mathcal D_4v_q(E_X)|\le330C X^{-3/2}.
}
\tag{L-91303.13}
\]

On an interior detail column `q<=X/4`,

\[
 \Omega_X(q)=\frac{\log4}{\sqrt q}
 \ge\frac{2\log4}{\sqrt X},
\]

so

\[
\boxed{
 \frac{|\mathcal D_4v_q(E_X)|}{\Omega_X(q)}
 =O(X^{-1}).
}
\tag{L-91303.14}
\]

Thus the finite-target mismatch remaining after the first Euler correction costs
only a `1-O(1/X)` safety factor.  The larger `O(X^-1/2)` safety factor in
`L-91111` is entirely due to the positive martingale-quantization collar.

## 5. Endpoint inverse of the Euler correction

Let

\[
 \mathcal E f(\theta)
 =\frac{2\theta^2f''(\theta)-\theta f'(\theta)+f(\theta)}
        {2\sqrt\theta}
\]

be the endpoint inverse of `L-91107`, interpreted distributionally at quotient
knots.

On one open cell, put

\[
 m_N=\sum_{k\le N}\frac{\mu(k)}{\sqrt k},
 \qquad
 \ell_N=\sum_{k\le N}\frac{\mu(k)\log k}{\sqrt k}.
\]

Then

\[
 \mathscr D(\theta)
 =\theta^{-1/2}[-\ell_N-m_N\log\theta]
\]

and direct differentiation gives

\[
\boxed{
 \mathcal E\mathscr D(\theta)
 =\frac{-3\ell_N-3m_N\log\theta+5m_N}{2\theta}.
}
\tag{L-91303.15}
\]

With `x=1/theta`, this is

\[
\boxed{
 \mathcal E\mathscr D(1/x)
 =\frac x2
  \sum_{k\le x}\frac{\mu(k)}{\sqrt k}
  [3\log(x/k)+5].
}
\tag{L-91303.16}
\]

Every unsigned coefficient in (L-91303.16) is strictly positive.  The first
finite correction therefore splits canonically into positive even- and
odd-squarefree parity measures; no new signed state is introduced.

At a reciprocal knot `theta=1/N`, the entering term in `mathscr D` is continuous
but its first derivative jumps.  The distributional endpoint inverse contains
the exact atom

\[
\boxed{
 \frac{\mu(N)}{\sqrt N}\,\delta_{1/N}.
}
\tag{L-91303.17}
\]

Thus the full first correction consists of a positive-parity bulk packet plus
finitely many explicit quotient-knot atoms.  Both are in the existing parity
and adjacent-butterfly coordinates.

## 6. Robust Hall absorption

The normalized endpoint-density correction in (L-91303.7) is

\[
 \frac1{2X}\mathcal E\mathscr D.
\]

On `1<=x<=55`, its unsigned bulk mass is at most

\[
 \frac{C_{54}}X,
\]

where

\[
 C_{54}
 =\frac14\max_{1\le x\le55}
 x\sum_{k\le x}\frac{|\mu(k)|}{\sqrt k}
 [3\log(x/k)+5]
 <\infty.
\tag{L-91303.18}
\]

The total unsigned knot mass is also `O(1/X)`.

A nested-neighborhood Hall transport with margin `h>0` survives any signed
capacity/demand perturbation whose adverse prefix variation is below `h`.
Indeed every perturbed Hall margin is at least the old margin minus that adverse
variation.

`L-91109` supplies the fixed equality margin `h>11/100`.  Hence, for every
sufficiently large `X`, the exact first Euler correction and all reciprocal-knot
atoms are absorbed by the same one-step equality shadow.  The reserve margin is
larger still.

Therefore the finite-versus-continuum mismatch is closed at the
endpoint-density/parity-transport level.

## 7. Combination with the positive quantization collar

`L-91111` proves that the B-spline quantization collar is coefficientwise
positive and costs only `O(X^-1/2)` of the interior detail target, hence `O(1)`
score per generation.  The present theorem adds:

```text
reset splice position      c0 X+O(1);
first lattice correction   explicit parity packet of size O(1/X);
remaining carry mismatch   relative O(1/X);
quotient-knot corrections  finite adjacent collars of size O(1/X).
```

Thus neither the finite equality transfer nor its quotient knots can be the
source of unbounded reset debt.

## 8. Exact remaining reset gate

After `L-91303`, the factor-54 route is reduced to one genuinely finite local
statement:

> Lift the robust parity transport and the bounded terminal quotient cells
> through the three-integer divisor stencils of `L-91105`, preserving endpoint
> nonnegativity and coefficient-one transfer of the residual `(L,R)` state.

The analytic finite-to-continuum error, the splice drift, the score curvature,
and the bulk carry disturbance are all already paid.

## 9. Proof boundary

```text
uniform first Euler correction                     EXACT
finite crossing c0 X+O(1)                          EXACT
O(X^-3/2) corrected seed remainder                  EXACT
O(X^-1) relative interior carry loss                EXACT
endpoint inverse of the correction                  EXACT
positive parity split and quotient-knot atoms       EXACT
robust Hall absorption for large X                  EXACT
three-integer divisor/capacity lift                  OPEN
terminal finite collar and coefficient-one reset    OPEN
Riemann Hypothesis                                  UNPROVED
```
