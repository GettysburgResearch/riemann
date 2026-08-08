# T-27601 — Prime-annulus commutator criterion for RH

Claim ID: `T-27601`  
Title: A critical local-energy bound for one explicit top-quarter prime contrast is equivalent to the Riemann Hypothesis  
Status: **FULL CONDITIONAL PROPOSAL — ONE UNIFORM PRIME-ANNULUS ENERGY THEOREM OPEN**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-27601`--`L-27604`; PR #269 source/factor-five package; elementary Mellin theory and the functional equation  
Scope: direct global attack on the complete rightmost-zero spectrum; RH is not claimed proved

## 1. The finite prime-annulus statistic

Let

\[
 W_X(q)=
 \begin{cases}
  2q/X-1,&X/2<q\le X,\\[1mm]
  1/2-4q/X,&X/4<q\le X/2,\\[1mm]
  0,&q\le X/4,
 \end{cases}
\tag{T-27601.1}
\]

with `q=X/4` assigned weight zero. Define

\[
\boxed{
 \mathfrak P(X)
 =\frac1{\sqrt X}
  \sum_{q\le X}\Lambda(q)W_X(q).
}
\tag{T-27601.2}
\]

Every value is a completely finite ordinary-prime-power sum on the fixed annulus `(X/4,X]`.

`L-27603` proves that this is the physical output of the compact two-band kernel

\[
 z_\omega(u)=
 \begin{cases}
  2e^{-3u/2}-e^{-u/2},&0\le u<\log2,\\
  \frac12e^{-u/2}-4e^{-3u/2},&\log2\le u<2\log2,\\
  0,&u\ge2\log2.
 \end{cases}
\tag{T-27601.3}
\]

Namely,

\[
 \mathfrak P(e^t)
 =\sum_q\frac{\Lambda(q)}{\sqrt q}
 z_\omega(t-\log q).
\tag{T-27601.4}
\]

## 2. Exact transform and the rightmost-zero mode

Put

\[
 \sigma=z+\frac12,
 \qquad
 E(\sigma)=(1-2^{-\sigma})(1-2^{-\sigma-1}),
\]

and

\[
 R(\sigma)=\frac{\sigma-1}{\sigma(\sigma+1)}.
\]

For `Re z>1/2`, absolute convergence gives

\[
\boxed{
 \int_0^\infty
 \mathfrak P(e^t)e^{-zt}\,dt
 =-E(\sigma)R(\sigma)
   \frac{\zeta'}\zeta(\sigma).
}
\tag{T-27601.5}
\]

If `rho` is a nontrivial zero of multiplicity `m_rho`, the right side has residue

\[
\boxed{
 -m_\rho E(\rho)R(\rho)\ne0
}
\tag{T-27601.6}
\]

at `z=rho-1/2`. Thus no off-line zero is canceled, including a multiple zero.

## 3. Pointwise criterion

Suppose that, for every `epsilon>0`,

\[
\boxed{
 \mathfrak P(X)=O_\varepsilon(X^\varepsilon).
}
\tag{PAC-P}

Then the Laplace integral in (T-27601.5) converges normally for `Re z>0`. It therefore supplies a holomorphic continuation of the right side to that half-plane.

A zero with `Re rho>1/2` would create the genuine pole (T-27601.6), a contradiction. Functional-equation symmetry gives RH.

Conversely, RH gives

\[
 \psi(x)=x+O_\varepsilon(x^{1/2+\varepsilon}),
\]

and the main density is annihilated by `W_X`. Partial summation therefore gives `PAC-P`.

Hence

\[
\boxed{
 \mathrm{RH}
 \iff
 \mathfrak P(X)=O_\varepsilon(X^\varepsilon)
 \quad\text{for every }\varepsilon>0.
}
\tag{T-27601.7}

## 4. Positive local-energy criterion

Define

\[
\boxed{
 \mathfrak E(J)
 =\int_J^{J+1}|\mathfrak P(e^t)|^2\,dt.
}
\tag{T-27601.8}

The following condition is equivalent to RH:

\[
\boxed{
 \mathfrak E(J)=e^{o(J)}.
}
\tag{PAC-E}

Indeed, under `PAC-E`, Cauchy--Schwarz on every unit block makes the Laplace integral converge normally for every `Re z>0`. The pole argument then gives RH. The converse follows from `PAC-P`.

The energy is an exact finite positive Gram:

\[
\boxed{
\begin{aligned}
 \mathfrak E(J)
 =\sum_{q,r}\frac{\Lambda(q)\Lambda(r)}{\sqrt{qr}}
 \int_J^{J+1}
 z_\omega(t-\log q)
 z_\omega(t-\log r)\,dt.
\end{aligned}}
\tag{T-27601.9}
\]

Only prime powers in one fixed multiplicative collar occur. This is the correct independent-frequency normal orientation; no one-frequency analytic square is substituted.

## 5. Exact carry source map

`L-27604` proves, for integer `X>=5`,

\[
\boxed{
 \mathcal R_X^{\rm cont}
 =\mathcal R_X^{\rm disc}
 +\frac{2}{X(X+1)}
 \left[
 B(X)-3B(X/2)+2B(X/4)-\log2
 \right],
}
\tag{T-27601.10}

where

\[
 B(Y)=\sum_{n\le Y}n\Lambda(n),
\]

and the continuum commutator differs from `sqrt(X) mathfrak P(X)` only by the explicit exponentially decaying gauge of `L-27603`.

The boundary in (T-27601.10) tends to `3/8`. The discrete term is exactly

\[
\boxed{
 \mathcal R_X^{\rm disc}
 =\frac1{X+1}
  \sum_{j=0}^{X}
  \sum_{m\le X}\Lambda_\omega(m)Z_{X,m}(j).
}
\tag{T-27601.11}

Thus the former abstract boundary-commutator map has been constructed at scalar level:

```text
physical pole-preserving prime annulus
 = exact factor-five carry scalar
   + explicit bounded prime-density boundary
   + explicit decaying gauge.
```

No unknown physical remainder remains in this scalar comparison.

## 6. Second commutator and proposed completion

`L-27602` proves the exact second-commutator identity

\[
 \beta_\omega*(U^2k)
 =U^2z_\omega
  +2\lambda_\omega*(Uz_\omega)
  +C_\omega*z_\omega,
\tag{T-27601.12}
\]

where

\[
 C_\omega
 =\Lambda_\omega\log
  +\Lambda_\omega*\Lambda_\omega
 \ge0.
\]

The proposed closing theorem is now concrete:

> **Prime-Annulus Energy (`PAE`).** Prove `PAC-E` by applying the complete two-frequency Selberg identity to the fixed kernel `z_omega`, retaining the explicit continuum/discrete boundary (T-27601.10), the factor-five carry rows in (T-27601.11), and every cross term from (T-27601.12).

A proof-producing recurrence may have the form

\[
\boxed{
 \mathfrak E(J)
 \le C(1+J)^A
  +\sum_\beta\theta_\beta
    \mathfrak E(J_\beta),
 \qquad
 J_\beta\le J-\delta,
 \qquad
 \sum_\beta\theta_\beta\le1.
}
\tag{T-27601.13}

A strict coefficient below one is sufficient but not required when every child is at a fixed smaller scale and the inhomogeneous term is polynomial.

## 7. Why this is a full-problem attack

The statistic `mathfrak P` is not another carry feasibility debt. It is a direct fixed-window wavelet coefficient of the ordinary von Mangoldt measure whose transform contains every nontrivial zeta zero.

The construction simultaneously resolves three earlier mismatches:

1. **pole cancellation:** the first logarithmic commutator differentiates the carry zeta factor and restores every zero;
2. **physical/carry map:** the exact discretization boundary is (T-27601.10), not an abstract source projection;
3. **growing packet:** the physical source is one fixed two-band top-quarter kernel.

The remaining theorem `PAE` is still RH-bearing. It has not been proved.

## 8. Review mutations

Reject a proposed completion if it:

```text
uses the zeroth carry window, which cancels the zeta pole;
omits the logarithmic commutator;
changes an endpoint in W_X;
drops the explicit 3/8 boundary ledger;
uses one frequency instead of the finite normal Gram;
takes absolute values before the two annulus bands recombine;
omits the Selberg convolution term;
quotes the factor-five carry reserve without the exact scalar map;
promotes finite prime computations to PAC-E.
```

## 9. Exact status

```text
averaged carry / canonical resolvent identity       PROPOSED COMPLETE
compact omega_2 wavelet                              PROPOSED COMPLETE
pole-preserving first commutator                     PROPOSED COMPLETE
ordinary-prime top-quarter formula                   PROPOSED COMPLETE
continuum/discrete factor-five boundary map          PROPOSED COMPLETE
second commutator / Selberg bridge                   PROPOSED COMPLETE
PAC-P / PAC-E -> RH                                  COMPLETE CONDITIONAL
Prime-Annulus Energy                                 OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
