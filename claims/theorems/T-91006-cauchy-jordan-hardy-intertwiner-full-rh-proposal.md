# T-91006 — The Cauchy–Jordan Hardy intertwiner would close the coefficient-one RH recurrence

Claim ID: `T-91006`  
Status: **FULL CONDITIONAL RH PROPOSAL / SINGLE OPEN INTERTWINER — ADVERSARIAL REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91014` through `L-91029`, especially `T-91005`  
RH status: **unproved**

## 1. Purpose

The live Cauchy/Jordan programme has now closed all of the following interfaces:

```text
positive generalized-Jordan source;
coefficient-one divisor isometry;
coassociative logarithmic coproduct;
pole-subtracted coefficient-one affine recurrence;
positive tail/Hankel forcing;
fixed-axis SO(3) Cauchy all-pass;
exact hyperbolic off-line signature;
completed xi scattering boundary;
sharp sixteenfold storage;
coefficient-one a^-4 recurrence;
one causal rational residual Hardy factor;
unconditional same-state terminal range;
compound-Poisson prime semigroup and carré du champ.
```

The only remaining conclusion-producing theorem is the compatibility of the
safe positive prime-jump carré du champ with the completed boundary Hardy
factor.

## 2. The residual Hardy test

Let

\[
 \Psi_a(u)=\sqrt{378}\,a^3
 {u(u-i\sqrt\alpha a)(u-i\sqrt\beta a)
  \over
  (u-ia)^2(u-2ia)^2(u-4ia)^2},
\]

where

\[
 \alpha={163-5\sqrt{561}\over28},
 \qquad
 \beta={163+5\sqrt{561}\over28}.
\]

Let `psi_a` be its causal inverse Fourier transform and put

\[
 \psi_{a,x}(t)=e^{ixt}\psi_a(t).
 \tag{T-91006.1}
\]

The exact modulus identity is

\[
 |\Psi_a(u)|^2
 =d_a(u)-{1\over16}d_{2a}(u).
 \tag{T-91006.2}
\]

Consequently the completed Weil form of this one test is exactly the
coefficient-one recurrence residual:

\[
 \boxed{
 a^{-4}\,\mathcal W(\psi_{a,x},\psi_{a,y})
 =\mathcal K_a(x,y)-\mathcal K_{2a}(x,y),
 }
 \tag{T-91006.3}
\]

where the diagonal is

\[
 \mathcal K_a(x,x)=\mathcal E_x(a).
\]

The normalization/orientation in (T-91006.3) is to be replayed directly from
the resident Guinand--Weil convention before promotion; no unrecorded scalar
multiple is permitted.

## 3. The safe positive source

For every safe line `sigma>1`, the generalized-Jordan source has Lévy measure

\[
 \nu_{a,\sigma}
 =\sum_{p,k}{1-p^{-2ak}\over kp^{k\sigma}}
 \delta_{k\log p}\ge0
\]

and carré du champ

\[
 \Gamma_{a,\sigma}(f,g)
 ={1\over2}\int
 (D_tf-f)^*(D_tg-g)d\nu_{a,\sigma}(t).
 \tag{T-91006.4}
\]

This is a positive independent-frequency Gram before aggregation.

The completed scattering ratio is

\[
 \Theta_a(x)
 =\Gamma_a(x)Q_a(1/2-a+ix),
 \qquad |\Theta_a(x)|=1,
 \tag{T-91006.5}
\]

and its Wigner--Smith delay is exactly the Cauchy logarithmic derivative.  Thus
the source and target belong to one analytic scattering object.

## 4. CJHI — the exact remaining theorem

> **Cauchy–Jordan Hardy Intertwiner (CJHI).**  For every `a>0`, the completed
> analytic continuation of the positive prime-jump carré du champ from a safe
> line to the symmetric xi boundary admits a lossless Stinespring realization
> whose unique scalar Hardy output is `psi_a`.  Equivalently, for every finite
> carrier family `(x_j)` there is an explicitly source-ordered operator
> `S_(a,x_j)` built from the positive divisor isometry, the prime-jump
> Lindbladian and the completed gamma/pole channel such that
> 
> \[
> \boxed{
> \left(a^{-4}\mathcal W(\psi_{a,x_j},\psi_{a,x_k})\right)_{j,k}
> =\left(\langle S_{a,x_j},S_{a,x_k}\rangle\right)_{j,k}
> \succeq0.
> }
> \tag{T-91006.6}
> \]
> 
> The realization must preserve the coefficient-one returned state, and its
> complementary output must be exactly the one causal factor of `L-91026` (or
> an explicitly unitary realification of it).  No same-scale signed remainder
> is allowed.

The phrase `explicitly source ordered` requires one finite formula assembled
from:

```text
V_(a,b) and its coassociative tensor powers;
the log-generator coproduct;
the positive Lévy measure nu_(a,sigma);
the finite exponential-polynomial impulse psi_a;
the explicit gamma/pole scattering factor Gamma_a.
```

An existential Gram factor obtained by taking a square root of the already
unknown Weil matrix does not satisfy CJHI.

## 5. Why CJHI proves RH

CJHI gives on the diagonal

\[
 \mathcal E_x(a)-\mathcal E_x(2a)\ge0
 \qquad(x\in\mathbb R,a>0).
 \tag{T-91006.7}
\]

By `T-91005`, this coefficient-one recurrence is equivalent to RH.  Explicitly,
iterate until the scale enters the unconditional terminal range of `L-91028`:

\[
 \mathcal E_x(a)
 \ge\mathcal E_x(2^Ja)\ge0.
\]

Then the original Cauchy gate is nonnegative and the terminal-pair theorem
excludes every off-line zero.

Conversely, RH makes the zero-side matrix in (T-91006.6) the Gram matrix of the
single Hardy factor, so CJHI is compatible with the expected model.

## 6. Binary rejection tests

Reject a claimed proof of CJHI if any of the following occurs.

1. **Wrong Fourier half-plane.**  The causal factor must have poles at
   `+ia,+2ia,+4ia` in the convention of `L-91026`.
2. **Loss of coefficient one.**  After the `a^-4` normalization the returned
   state must be exactly `E_x(2a)`, not `c(a)E_x(2a)` with `c<1` or `c>1`.
3. **Rowwise absolute values.**  Independent carriers must be recombined before
   taking norms.
4. **Generic CP reversal.**  Forward negative-mass contraction of `L-91020`
   cannot be inverted.
5. **Terminal-state rotation.**  Fixed-carrier positivity cannot terminate an
   unrelated rotating operator state.
6. **Source/prime type mismatch.**  `q_a`, generalized primes
   `Lambda(n)(1-n^-2a)`, ordinary `Lambda`, and pole-subtracted tails must not be
   silently interchanged.
7. **Uncompleted scattering.**  The gamma and pole factors in `Theta_a` are
   load-bearing.
8. **Extra signed port.**  Any same-scale residual outside the one causal Hardy
   factor leaves CJHI open.
9. **Finite-radius shortcut.**  Safe-line absolute convergence alone cannot
   cross the critical annulus.
10. **Numerical factorization.**  Finite PSD scans do not establish the
    all-carrier/all-scale source identity.

## 7. Review order

```text
L-91022  sixteenfold storage and residual;
L-91026  causal scalar spectral factor;
T-91005  coefficient-one recurrence equivalence;
L-91014/L-91015  positive source and pole subtraction;
L-91023/L-91027  completed scattering identity/cocycle;
L-91029  prime compound-Poisson carré du champ;
L-91028  unconditional terminal recurrence;
T-91006  proposed final intertwiner.
```

## 8. Exact boundary

```text
all algebraic/source/scattering normal forms       PROPOSED COMPLETE / EXACT
coefficient-one RH recurrence                      PROPOSED COMPLETE / RH-EQUIVALENT
unconditional terminal recurrence                  PROPOSED COMPLETE
CJHI source-to-boundary Hardy Gram                  OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVED
```
