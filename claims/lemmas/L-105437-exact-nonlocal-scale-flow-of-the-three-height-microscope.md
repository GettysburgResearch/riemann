# L-105437 — Exact nonlocal scale flow of the three-height residue microscope

Claim ID: `L-105437`  
Status: **PROVED EXACT FOURIER-MULTIPLIER IDENTITY**  
Created: 2026-08-24  
Depends on: `L-105435`  
RH status: **not assumed**

## 1. Kernel multiplier

Let

\[
\Omega_h(x)=
{36h^5\over
(x^2+h^2)(x^2+4h^2)(x^2+9h^2)}.
\]

With

\[
T_h=e^{-h|D|}
\]

the Poisson semigroup, `L-105435` gives

\[
\boxed{
\Omega_h*
={3\pi\over10}
T_h(T_h^2-4T_h+5I).
}
\tag{L-105437.1}

The spectral polynomial is strictly positive on `0<=T_h<=I`.

Let `mu` be any finite signed distribution for which the convolution is
defined and put

\[
P(\cdot,h)=\Omega_h*\mu.
\]

The critical-residue microscope is the case

\[
\mu=\sum_c\rho_c\delta_c.
\]

## 2. First-order scale equation

For one Fourier frequency, put

\[
t=e^{-h|\xi|}.
\]

The multiplier is

\[
k(t)={3\pi\over10}t(t^2-4t+5).
\]

Since

\[
k'(t)={3\pi\over10}(3t^2-8t+5)
={3\pi\over10}(1-t)(5-3t),
\]

one obtains

\[
\boxed{
\partial_h\widehat P(\xi,h)
=-|\xi|\,
{(1-t)(5-3t)\over t^2-4t+5}
\widehat P(\xi,h).
}
\tag{L-105437.2}

Equivalently,

\[
\boxed{
\partial_hP
=-|D|\,\mathcal R_hP,
\qquad
\mathcal R_h
={ (I-T_h)(5I-3T_h)
  \over T_h^2-4T_h+5I}.
}
\tag{L-105437.3}

The rational functional calculus is bounded and positive because its scalar
symbol lies in `[0,1]` for `0<=t<=1`.

There is also the third-order annihilating equation

\[
\boxed{
(\partial_h+|D|)
(\partial_h+2|D|)
(\partial_h+3|D|)P=0.
}
\tag{L-105437.4}

## 3. Fine and coarse limits

As `h downarrow 0`,

\[
\Omega_h\longrightarrow {3\pi\over5}\delta_0
\]

in distributions. Hence

\[
\boxed{
P(\cdot,h)\longrightarrow {3\pi\over5}\mu.
}
\tag{L-105437.5}

At an atom, the stronger pointwise microscope gives

\[
hP(c,h)\longrightarrow\rho_c.
\]

As `h->infinity`, every nonzero Fourier mode is dissipated. For the Xi ratio,
`L-105436` supplies the signed leading asymptotic and shows that the scalar
field approaches zero from below at coarse scales.

## 4. Why the evolution does not close the sign for free

Equation (L-105437.2) is dissipative in the direction of increasing `h`.
Negativity at a fine scale propagates to coarser scales whenever the transition
operator is positivity preserving. The RH-bearing inference requires the
opposite direction:

```text
coarse negativity  ->  fine negativity.
```

That is backward evolution, hence an anti-diffusive problem. A small positive
fine-scale atom can be smoothed away at large `h`; `R-105430` is a concrete
finite-dimensional analogue.

Therefore no maximum principle for the forward scale flow can by itself prove
the critical sign.

## 5. Typed remaining theorem

The scale formulation isolates the missing Xi-specific input:

```text
MSD105437 — microscope scale descent

For the actual Xi derivative ratio, the solution of (L-105437.2) that comes
from the completed-zeta reciprocal source cannot create a positive value as h
is run backward from the unconditional coarse region to h=0.
```

By `L-105435--L-105436`,

\[
\boxed{
\mathrm{MSD105437}
\Longrightarrow
\rho_c\le0\text{ for every critical point}
\Longrightarrow
\mathrm{RH}
}
\]

once critical-point reality and the frozen confluent interfaces are supplied.
`MSD105437` remains open.
