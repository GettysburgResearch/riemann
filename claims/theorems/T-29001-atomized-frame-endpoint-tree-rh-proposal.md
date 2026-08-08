# T-29001 — Atomized carry-frame and coupled-source proposal for RH

Claim ID: `T-29001`  
Title: The complete carry-position pole frame and positive endpoint-fiber binding reduce RH to one coupled interior Selberg source-matrix recurrence  
Status: **FULL CONDITIONAL PROPOSAL — ENDPOINT SOURCE CLOSED; ONE COUPLED INTERIOR MATRIX THEOREM OPEN**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-08  
Dependencies: `L-29001`--`L-29006`, `R-29002`; PR #241 `L-9518`; PR #269 source package; PR #289 prime-annulus commutator  
Scope: complete conditional deduction from one source-coupled recurrence; RH is not claimed proved

## 1. The vector-valued global field

Retain the carry-position variable

\[
 \theta\in[\eta,1-\eta],
 \qquad0<\eta<\frac12,
\]

through the complete square.  The atomized prime field is

\[
 \mathfrak P_\theta(t)
 =\sum_q\frac{\Lambda(q)}{\sqrt q}
   z_{\theta,\omega}(t-\log q),
\tag{T-29001.1}
\]

with transform

\[
 \widehat{\mathfrak P_\theta}(z)
 =-E(s)N_\theta(s)\frac{\zeta'}\zeta(s),
 \qquad s=z+\frac12.
\tag{T-29001.2}

`L-29001` proves that the balanced residue frame has strictly positive norm at
every nontrivial zeta zero.  Hence

\[
\boxed{
 \mathrm{RH}
 \iff
 \mathscr E_\eta(J)=e^{o(J)},
}
\tag{T-29001.3}

where

\[
 \mathscr E_\eta(J)
 =\int_J^{J+1}\int_\eta^{1-\eta}
   |\mathfrak P_\theta(t)|^2d\theta dt.
\tag{T-29001.4}

At finite scale `X=e^t`, the same energy is already the exact carry-position
normal Gram

\[
 \frac1X\int_\eta^{1-\eta}
 \left|\sum_{m\le X}\Lambda(m)Z_{X,m}(\theta)\right|^2d\theta.
\tag{T-29001.5}

No unknown physical-to-carry map remains.

`L-29004` gives the one-dimensional form

\[
 \sqrt X\,\mathfrak P_\theta(\log X)
 =A(X)-A(\theta X)-A((1-\theta)X),
\]

with

\[
 A(X)=\psi(X)-\frac32\psi(X/2)+\frac12\psi(X/4).
\]

## 2. What the ordinary row reserve proves

For one unscaled ordinary binomial row, `L-29002` proves

\[
 Q_n(j)
 :=\log^2\binom nj
 -\sum_d[\Lambda(d)\log d+(\Lambda*\Lambda)(d)]
       \chi_{n,d}(j)
 \ge0,
\tag{T-29001.6}

with equality exactly at

\[
 j\in\{0,1,n-1,n\}.
\tag{T-29001.7}

On a fixed balanced cone, the forcing consumes only

\[
 O_\eta(\log^2n/n)
\]

of the Kummer square.

This is a strong diagonal theorem, but it is not yet a theorem for an arbitrary
source superposition.  `R-29002` records two exact firewalls:

1. the row inequality is not homogeneous in a positive source amplitude;
2. the natural generalized-prime pointwise lift fails at `(n,j)=(6,2)`:
   \[
   P_{\omega,6}(2)^2-S_{\omega,6}(2)
   =\log3\log(25/32)<0.
   \]

Therefore the interior must be assembled as one coupled quadratic source
matrix.  Diagonal row positivity may not be summed after the source amplitudes
have been detached from their cross terms.

## 3. The endpoint source is now closed

The endpoint restriction of the Jensen field has coefficient sequence

\[
 A_x(r)-A_x(r-1),
 \qquad
 A_x(r)=\sum_mx_mg_m(r),
 \qquad x_m=\Lambda(m)\ge0.
\]

`L-29006` proves the exact source recombination

\[
\boxed{
 \sum_{r\ge2}[A_x(r)-A_x(r-1)]D_r
 =\sum_mx_mW_m,
}
\tag{T-29001.8}

where

\[
 W_m=D_m-\frac32D_{2m}+\frac12D_{4m}
     =\frac12E_{2m}-E_m.
\]

Thus the actual prime endpoint packet is a nonnegative superposition of the
complete filtered fibers, not an arbitrary signed endpoint sequence.

Its aggregate endpoint reserve is

\[
\boxed{
 \mathcal Q_{\rm end}(x)
 =\frac14\log^22\left(\sum_mx_m\right)^2
  +\log2\sum_mx_m\log m
  -\frac12\log^22\sum_mx_m
 \ge0.
}
\tag{T-29001.9}

On one dyadic source annulus,

\[
\boxed{
 \|f_x\|_2^2
 \le\frac{12}{\log2}\mathcal Q_{\rm end}(x),
}
\tag{T-29001.10}

and a three-color dyadic decomposition gives the corresponding global endpoint
bound with constant `36/log2`.

The endpoint-tree/source-binding alternative in the previous version of this
proposal is therefore closed for the exact ordinary-prime Jensen field.

## 4. Sole closing theorem — `CISR`

The remaining theorem is the **Coupled Interior Selberg Recurrence**.

> For one fixed `eta in (0,1/2)`, construct on every logarithmic block the
> complete source-coupled Hermitian forcing matrix, with every independent
> frequency and every ordinary-prime cross term retained, and prove
> \[
> \boxed{
> \mathscr E_\eta(J)
> +\mathscr Q_{\rm int}(J)
> +\mathscr Q_{\rm end}(J)
> \le
> C(1+J)^A
> +\sum_\nu\theta_\nu\mathscr E_\eta(J_\nu),
> }
> \tag{CISR}
> \]
> where
> \[
> \mathscr Q_{\rm int}(J)\ge0,
> \qquad
> \mathscr Q_{\rm end}(J)\ge0,
> \qquad
> J_\nu\le J-\delta,
> \qquad
> \sum_\nu\theta_\nu\le1.
> \]
> The endpoint form is the explicit source-bound form of `L-29006`.  The
> interior form must be a genuine quadratic source matrix whose diagonal
> reduces to `L-29002`; it may not be replaced by a scalar-weighted sum of the
> row reserves.

A strict coefficient below one is welcome but is not required.  A coefficient-
one recurrence with a fixed positive scale drop and a polynomial inhomogeneous
term already gives polynomial energy.

## 5. Conditional completion

Assume `CISR`.  Dropping the two nonnegative reserve forms gives

\[
 \mathscr E_\eta(J)
 \le C(1+J)^A
  +\max_{u\le J-\delta}\mathscr E_\eta(u)
\tag{T-29001.11}

in the conservative coefficient-one case.  Iteration through `O(J/delta)`
scales yields

\[
\boxed{
 \mathscr E_\eta(J)\ll(1+J)^{A+1}.
}
\tag{T-29001.12}

Thus `mathscr E_eta(J)=e^{o(J)}`.  The vector-valued pole criterion excludes
every zero with real part greater than one half, and functional-equation
symmetry gives

\[
\boxed{\mathrm{RH}.}
\tag{T-29001.13}

The averaged coordinate also proves the top-quarter prime-annulus criterion on
PR #289, and the stable fixed-ratio filters export the exact `2/3` first-cell
Mertens mutation.

## 6. Production requirements

A valid `CISR` object must emit:

1. the complete balanced carry-position partition;
2. the independent-frequency physical normal matrix;
3. every ordinary-prime source coefficient and every cross term;
4. the complete Selberg linear and convolution matrices;
5. the coupled interior Schur complement, not only its diagonal;
6. the exact endpoint source grouping of `L-29006`;
7. every annular boundary and the three-color assembly;
8. every lower-scale destination and its coefficient;
9. a proof that the polynomial channel contains no target energy;
10. the prime-annulus and `2/3` Mertens mutations.

Automatic rejection applies if the certificate:

- averages `theta` before squaring;
- drops a translate or source cross term;
- uses `P_omega^2>=S_omega`;
- scales `L-29002` linearly in a source amplitude;
- estimates endpoint rows before the `W_m` recombination;
- spends the endpoint reserve twice;
- promotes a finite matrix to the cofinal recurrence.

## 7. Exact status

```text
atomized Nyman/carry frame                    PROPOSED COMPLETE
vector-valued pole criterion                  PROPOSED COMPLETE
physical normal energy = finite carry Gram    PROPOSED COMPLETE
prime Jensen-defect scalarization             PROPOSED COMPLETE
ordinary Selberg-Kummer row reserve           PROPOSED COMPLETE
naive source-cone/generalized lift             REFUTED
positive prime endpoint-fiber binding          PROPOSED COMPLETE
endpoint physical-frame bound                  PROPOSED COMPLETE
coupled interior source matrix / CISR           OPEN / RH-BEARING
CISR -> atomized energy -> RH                   COMPLETE CONDITIONAL
Riemann Hypothesis                             UNPROVED
```

This remains a full-problem proposal.  The endpoint source is no longer the
open hinge; the exact surviving burden is the coupled interior Hermitian source
matrix.
