# D-0301 — Standard zeta, xi, and zero conventions

Claim ID: D-0301  
Title: Standard zeta, xi, and zero conventions  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: standard analytic continuation and functional equation of `zeta`  
Scope: shared normalization for issue #3 theorem cards and proof kernels  
Related counterexample candidates: none

## Definitions

For `Re(s)>1`,
\[
 \zeta(s)=\sum_{n=1}^{\infty}n^{-s}
         =\prod_p(1-p^{-s})^{-1}.
\]
Its meromorphic continuation to `C` has one simple pole at `s=1`.

Define
\[
 \xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]
With this normalization, `xi` is entire of order one, satisfies
\[
 \xi(s)=\xi(1-s),
 \qquad
 \xi(\overline{s})=\overline{\xi(s)},
\]
and its zeros, with multiplicity, are precisely the nontrivial zeros of
`zeta`, i.e. zeros in `0<Re(s)<1`.

Define
\[
 \Xi(t)=\xi\!\left(\frac12+it\right).
\]
Then `Xi` is an even entire function of `t` and is real for real `t`.

A zero `rho=beta+i gamma` is **off the critical line** if `beta != 1/2`.
The Riemann hypothesis (RH) is the assertion that every zero of `xi` is on the
critical line.

For a positively oriented rectifiable Jordan curve `C` and a meromorphic
function `f` with no zero or pole on `C`, `N_C(f)` and `P_C(f)` denote the
numbers of zeros and poles inside `C`, counted with multiplicity/order.

## Zero-sum convention

Whenever a sum over nontrivial zeros is not absolutely convergent, this
definition does not assign an arbitrary ordering.  The claim using the sum
must state its limiting convention, normally
\[
 \lim_{T\to\infty}\sum_{|\operatorname{Im}\rho|\le T}.
\]
Grouping only by visual symmetry is not a substitute for proving that the
chosen limit exists.

## Logarithm convention

`log xi(s)` is used only on a simply connected zero-free domain with a
specified analytic branch, or as a formal Taylor logarithm at a point where
`xi` is nonzero.  In particular `xi(1)=1/2`, so a unique analytic branch near
`s=1` is fixed by the real value `log xi(1)=log(1/2)`.

## Motivation

The literature uses several completed zeta normalizations that differ by
constants, changes of variable, and factors that introduce or remove trivial
zeros.  A finite certificate is only meaningful when its function, zero set,
and transform convention are fixed exactly.

## Analytic domain audit

- `zeta` is represented by its Dirichlet series only for `Re(s)>1`; elsewhere
  its meromorphic continuation is meant.
- `xi` is entire; the pole at `s=1` and trivial zeros are cancelled by the
  displayed factors.
- `Gamma(s/2)` has poles, but the product defining `xi` has removable
  singularities at the relevant points.
- No branch of `Gamma` is needed; `Gamma` itself is single-valued meromorphic.
- Every use of a logarithm requires an explicit zero-free domain.

## Dependency audit

The entireness and functional equations are classical imported facts and are
not proved in this definition.  Claim `L-0301` uses only the two displayed
symmetries once they are granted.

## Gap audit

- Do not interchange `xi(1/2+z)` and `Xi(z)=xi(1/2+iz)`.
- A rectangle for `zeta` may contain the pole at `1`; a rectangle for `xi`
  does not, but zero/pole cancellation must be understood.
- A zero of a differently normalized completed function may include an
  artificial zero at `0` or `1`.
- A zero sum can change under conditionally convergent rearrangement.

## Remaining uncertainty

Independent review should check that every imported theorem card uses this
normalization or explicitly translates its source normalization.

## Suggested next attack

Create machine-readable normalization fingerprints for `D-0001` and future
explicit-formula claims and prove their change-of-variable relation to D-0301.
