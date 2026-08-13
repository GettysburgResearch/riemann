# L-91901 — Safe-real Xi Pick matrices are explicit Birman–Schwinger small-gain tests

Claim ID: `L-91901`  
Status: **EXACT FINITE-MATRIX REDUCTION; GLOBAL POSITIVITY OPEN**  
Created: 2026-08-13  
Depends on: `T-91006`, `L-91900`  
RH status: **unproved**

## 1. Safe data

Fix

\[
 0\le u<1
\]

and distinct positive real nodes

\[
 q_1,\ldots,q_N.
\]

Put

\[
 \theta_i(u)
 =\frac{\xi(1+q_i)}{\xi(1+u+q_i)}>0,
 \qquad
 D_u=\operatorname{diag}(\theta_1(u),\ldots,\theta_N(u)),
 \tag{L-91901.1}
\]

and let

\[
 \boxed{
 (C_u)_{ij}
 =\frac1{1+u+q_i+q_j}.
 }
 \tag{L-91901.2}

Every Xi value lies on the real line to the right of one.

The Cauchy matrix is strictly positive because

\[
 (C_u)_{ij}
 =\int_0^\infty
 e^{-(1+u)t}e^{-q_it}e^{-q_jt}dt
 \tag{L-91901.3}
\]

and distinct real exponentials are linearly independent.

## 2. Target Pick matrix

The safe-real de Branges--Rovnyak matrix is

\[
 \boxed{
 P_u=C_u-D_uC_uD_u.
 }
 \tag{L-91901.4
}

This is exactly the matrix of `T-91006`.

Define

\[
 \boxed{
 B_u=C_u^{1/2}D_uC_u^{-1/2},
 \qquad
 K_u=B_u^*B_u
 =C_u^{-1/2}D_uC_uD_uC_u^{-1/2}.
 }
 \tag{L-91901.5}

Then

\[
 \boxed{
 C_u^{-1/2}P_uC_u^{-1/2}
 =I-K_u.
 }
 \tag{L-91901.6}

Consequently

\[
 \boxed{
 P_u\succeq0
 \quad\Longleftrightarrow\quad
 K_u\preceq I
 \quad\Longleftrightarrow\quad
 \|B_u\|\le1.
 }
 \tag{L-91901.7}

A negative Pick direction is precisely a feedback singular value larger than
one.

## 3. Finite feedback realization

Take

\[
 A=I,
 \qquad
 G=B_u.
\]

Then `L-91900` gives

\[
 I-B_u^*B_u\succeq0
 \quad\Longleftrightarrow\quad
 K_u\preceq I.
\]

Thus every safe-real Pick test is a finite Birman--Schwinger small-gain test.
Its negative index is

\[
 \boxed{
 n_-(P_u)
 =\#\{\lambda(K_u)>1\}.
 }
 \tag{L-91901.8}

The perturbation determinant is

\[
 \boxed{
 \frac{\det P_u}{\det C_u}
 =\det(I-K_u).
 }
 \tag{L-91901.9}

When `K_u<I`, its feedback entropy is

\[
 \boxed{
 \mathcal S_u[\mathbf q]
 =-\log\frac{\det P_u}{\det C_u}
 =-\log\det(I-K_u).
 }
 \tag{L-91901.10}

The entropy diverges at the first unit-gain event.

## 4. Initial condition

At `u=0`,

\[
 D_0=I,
 \qquad
 P_0=0,
 \qquad
 K_0=I.
 \tag{L-91901.11}

The horizontal evolution therefore starts at a lossless boundary system.  The
RH problem is to show that every nonzero horizontal displacement moves the
safe-real feedback **inside**, rather than outside, the contractive cone.

This explains why a crude strict-small-gain estimate cannot start at `u=0`:
the correct object is a lossless-to-dissipative spectral flow.

## 5. RH criterion

Subject to the bounded-type/continuation interface declared in `T-91006`,

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 K_u[\mathbf q]\preceq I
 }
 \tag{L-91901.12
}

for every positive rational `u<1` and every finite positive rational node
tuple.

False RH produces one finite rational packet with

\[
 \lambda_{\max}(K_u)>1.
\]

All entries of that finite return operator are safe Euler-domain quantities.

## 6. Relation to Claude's compression

Claude's finite Gabor matrix uses a prime-side compression of Weil's form and
reads off-line pairs through inertia.  The present finite matrix is different:
it is a safe-real interpolation return operator.  It has no bandwidth-one
averaging and is in principle sensitive to a single off-line pole.  Its price
is that the small-gain inequality is exactly RH-bearing.

## 7. Exact boundary

```text
safe Cauchy metric                              EXACT
Pick matrix = C-DCD                            EXACT
Birman--Schwinger return K                      EXACT SAFE FINITE MATRIX
negative Pick index = gain-above-one count      EXACT
feedback determinant/entropy                    EXACT
all finite returns contractive                  OPEN / RH-EQUIVALENT
Riemann Hypothesis                              UNPROVED
```
