# T-91900 — Completed safe-real small gain would prove the Riemann hypothesis

Claim ID: `T-91900`  
Status: **FULL CONDITIONAL RH PROPOSAL / SOURCE-SPECIFIC SMALL GAIN OPEN**  
Created: 2026-08-13  
Depends on: `T-91006`, `L-91900`--`L-91902`, `R-91900/R-91901`  
RH status: **unproved**

## 1. Explicit finite return operators

For every positive rational

\[
 0<u<1
\]

and finite positive rational tuple

\[
 \mathbf q=(q_1,\ldots,q_N),
\]

define

\[
 (C_u)_{ij}=\frac1{1+u+q_i+q_j},
 \qquad
 D_u=\operatorname{diag}\left(
  \frac{\xi(1+q_i)}{\xi(1+u+q_i)}
 \right)
 \tag{T-91900.1}
\]

and

\[
 \boxed{
 K_u[\mathbf q]
 =C_u^{-1/2}D_uC_uD_uC_u^{-1/2}.
 }
 \tag{T-91900.2}

Every entry is determined by safe real Xi values and a rational Cauchy matrix.
No zero ordinate or critical-strip evaluation occurs.

## 2. Completed Safe-Real Small Gain (`CSG`)

> For every rational `u` and finite rational packet `q`, prove
> 
> \[
> \boxed{
> K_u[\mathbf q]\preceq I.
> }
> \tag{T-91900.3}

Equivalently,

\[
 \boxed{
 C_u-D_uC_uD_u\succeq0.
 }
 \tag{T-91900.4}

A strict version may be sought for distinct nodes and `u>0`, but semidefinite
contractivity is the exact theorem required.

## 3. Differential sufficient theorem (`CCBR`)

A stronger constructive route is **Cauchy-Covariant Bounded Real**.
For every packet, construct from the declared completed arithmetic source a
metric-compatible connection

\[
 \Gamma_u
 =-\frac12C_u^{-1}S_u+\Omega_u,
 \qquad
 \Omega_u^*C_u+C_u\Omega_u=0,
 \tag{T-91900.5}

where

\[
 (S_u)_{ij}=(1+u+q_i+q_j)^{-2},
\]

and prove

\[
 \boxed{
 -\Big[
  (\nabla_uD_u)^*C_uD_u
  +D_uC_u(\nabla_uD_u)
 \Big]
 \succeq0,
 }
 \tag{T-91900.6
}

with

\[
 \nabla_uD_u
 =D_u'+\Gamma_uD_u-D_u\Gamma_u.
\]

Since `D_0=I`, the initial Pick defect is zero.  `L-91902` then propagates
(T-91900.4) for every `u`.

The skew connection must be built from the actual completed channels:

```text
prime returned-state/Julia cascade;
paired-eta sector change;
compact dyadic/gamma bridge;
gamma and pole connection;
compressed delays and both Hardy orientations;
the finite bridge and safe-jet connection.
```

The canonical Cauchy connection alone does not suffice (`R-91901`).

## 4. Completion to RH

`L-91901` gives

\[
 K_u\preceq I
 \quad\Longleftrightarrow\quad
 \mathcal P_u[\mathbf q]\succeq0.
\]

The countable safe-real Pick criterion `T-91006` then gives a Schur
continuation of

\[
 \Theta_u(s)=\frac{\xi(s-u)}{\xi(s)}
\]

through the moving half-plane.  An off-line zero would give an uncancelled
pole for one rational `u`, contradicting that continuation.  Therefore

\[
 \boxed{
 \mathrm{CSG}\Longrightarrow\mathrm{RH},
 \qquad
 \mathrm{CCBR}\Longrightarrow\mathrm{CSG}\Longrightarrow\mathrm{RH}.
 }
 \tag{T-91900.7}

Conversely, under RH the completed quotient is inner and every matrix
(T-91900.4) is positive.  Thus CSG is RH-equivalent, subject to the declared
bounded-type interface of `T-91006`.

## 5. Spectral-flow interpretation

At `u=0`,

\[
 K_0=I.
\]

False RH produces a finite packet and displacement for which

\[
 \lambda_{\max}(K_u)>1.
\]

By `L-91900`, this is a bound-state or negative-direction birth in the finite
feedback loop.  CSG says that the completed arithmetic interconnection never
allows a unit-gain crossing.

This corrects the overstrong radial intuition of PR #430: an off-line atom may
be created by nonlocal feedback even from a diffuse open source.  What must be
excluded is the unit-gain loop itself.

## 6. Why this target is concrete

Compared with the earlier open instructions, CSG has the following advantages:

```text
finite matrices only;
countable rational packets;
all samples in Re(s)>1;
no zero data;
no limiting Gram capture;
no unknown model-space square root;
negative failure is a finite eigenvalue >1;
connection version has an exact differential identity.
```

The price is honest: proving the small-gain inequality is precisely the
remaining RH-bearing arithmetic theorem.

## 7. Binary rejection tests

Reject a claimed proof if it:

1. replaces the Cauchy metric by an unrelated positive source metric;
2. checks only diagonal entries or determinants;
3. uses the canonical metric connection without the completed skew channels;
4. assumes positive one-Green or compound-Poisson data imply the target Pick
   kernel (`R-91005`);
5. proves finite numerical packets only;
6. defines the connection from the unknown positive Pick matrix;
7. discards the returned Euler state at a prime resonance.

## 8. Exact boundary

```text
finite safe return operator K                         EXACT
negative Pick direction = gain above one              EXACT
covariant bounded-real propagation                    EXACT
canonical connection shortcut                         REFUTED
completed source-ordered connection                    OPEN
CSG all-packet small gain                              OPEN / RH-EQUIVALENT
Riemann Hypothesis                                     UNPROVED
```
