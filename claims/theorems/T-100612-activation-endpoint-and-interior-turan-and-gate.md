# T-100612 — Activation endpoints and interior Turán witnesses form an exact AND gate to RH

Claim ID: `T-100612`  
Status: **PROVED EXACT CONJUNCTION/INTERFACE THEOREM; TWO ARITHMETIC WITNESS CLASSES OPEN**  
Created: 2026-08-20  
Depends on: PRs #672, #676, #679; `L-100610--L-100616`  
RH status: **unproved**

Let `B` be a finite labelled prime multiset, allowing the second labelled copy
of `67`, and put

\[
P_A=\prod_{q\in A}q,\qquad \epsilon_A=(-1)^{|A|},
\qquad
\Delta_B=\prod_{q\in B}(1-q^{-3/2}).
\]

For `x>=1`, define

\[
S_\sigma(x)=\sum_{P_A\le x}\epsilon_AP_A^{-\sigma}
\qquad(\sigma=1/2,1,3/2)
\]

and

\[
\overline S_{3/2}(x)=\Delta_B-S_{3/2}(x).
\]

The critical quadratic-envelope packet is

\[
\mathcal E_B(x)=
16\overline S_{3/2}(x)
+24x^{-1/2}S_1(x)
-9x^{-1}S_{1/2}(x).
\tag{T-100612.1}
\]

PR #679 proves that on every open activation cell

\[
\mathcal E_B'(x)
=-3x^{-2}\bigl(4\sqrt x\,S_1-3S_{1/2}\bigr).
\tag{T-100612.2}
\]

Hence every cell minimum is of exactly one of the following two types.

## Witness class A — downward activation endpoints

At a labelled subset product `d`, let

\[
b_B(d)=\sum_{A:P_A=d}\epsilon_A.
\]

The exact jump is

\[
\mathcal E_B(d)-\mathcal E_B(d^-)
=-b_B(d)d^{-3/2}.
\tag{T-100612.3}
\]

Only `b_B(d)>0` can create a new downward endpoint minimum.  Define

```text
AEP100612:
  E_B(d)>=0 at every actual positive-parity activation d.
```

## Witness class B — double-negative interior critical points

An interior minimum can occur only when

\[
S_1<0,\qquad S_{1/2}<0.
\]

Its unique possible location is

\[
x_*=\left(\frac{3S_{1/2}}{4S_1}\right)^2,
\tag{T-100612.4}
\]

provided that `x_*` lies in the current cell.  At this point

\[
\mathcal E_B(x_*)
=16\left(\overline S_{3/2}+\frac{S_1^2}{S_{1/2}}\right).
\]

Since `S_(1/2)<0`, nonnegativity is equivalent to

\[
\boxed{
S_1^2+\overline S_{3/2}S_{1/2}\le0.
}
\tag{T-100612.5}
\]

Define

```text
DNT100612:
  inequality (T-100612.5) holds at every actual double-negative cell whose
  critical point lies in the cell.
```

## Exact conjunction

Every other point of every cell is dominated by one of these witnesses.
Therefore, first for every finite labelled source and then by absolute
convergence at exponent `3/2` for the complete prime source,

\[
\boxed{
AEP100612\ \wedge\ DNT100612
\iff
\mathcal E_2(X)\ge0\quad(X\ge1).
}
\tag{T-100612.6}

The Mellin transform of `E_2` is holomorphic at every positive real point and
retains every reciprocal-zeta pole associated with a zero `rho` satisfying
`Re rho>1/2`.  The frozen nonnegative-density Landau theorem therefore gives

\[
\boxed{
AEP100612\ \wedge\ DNT100612
\Longrightarrow RH.
}
\tag{T-100612.7}

## Why this is genuinely an AND gate

The two witness classes are logically independent at the cell-calculus level.
A monotone cell may start below zero while having no interior critical minimum;
then `DNT` is vacuous but `AEP` fails.  Conversely, a quadratic-in-`x^(-1/2)`
cell can have positive endpoints and a negative interior minimum; then `AEP`
holds while `DNT` fails.  Thus neither witness class alone gives
(T-100612.6).

## Repository implication matrix

The two sides have different existing inputs.

```text
AEP side:
  largest-prime ownership
  + activation-jump ledger
  + finite critical squaring of low primes
  + hereditary terminal corridors;

DNT side:
  first-owner / Hankel moment state
  + complex shifted-quadratic positivity
  + double-owner interval matrix
  + short-interval and fully-active positivity.
```

The proved regions include every one- and two-label block, every fully active
block, the ratio-eight interval sector, the `A<exp(3/4)` asymptotic interval
sector, and the finite-completion small-prime corridor.  The remaining cases
are long, genuinely mixed actual-prime activation collars.

```text
cell classification                    PROVED EXACT
AEP and DNT are exhaustive             PROVED EXACT
AEP and DNT are logically independent  PROVED
AEP AND DNT -> quadratic envelope       PROVED EXACT
quadratic envelope -> RH                INHERITED EXACT
AEP100612                               OPEN ON LONG MIXED COLLARS
DNT100612                               OPEN ON LONG MIXED COLLARS
Riemann Hypothesis                      UNPROVED
```