# L-105647 — The logarithmic midline defect is the exact clipped all-pass index

Claim ID: `L-105647`  
Status: **PROVED EXACT FOR FINITE REDUCED INNER QUOTIENTS**  
Created: 2026-08-25  
Depends on: `L-105640--L-105643`; sibling `L-106431`, `L-106512--L-106514`  
RH status: **not assumed**

## 1. Reduced inner quotient

Let

\[
U(z)=\omega\,{A(z)\over B(z)}
\]

be a finite reduced upper-half-plane inner quotient, where `A` and `B` are
finite Blaschke products, have no common factor, and are canonically normalized
at infinity.  Write their upper-half-plane zeros, with multiplicity, as

\[
a_j=\alpha_j+i\eta_j,
\qquad
b_k=\beta_k+i\delta_k,
\qquad
\eta_j,\delta_k>0.
\]

Any exponential inner carrier must be removed before the integral below is
formed.  This is exactly the same carrier normalization required by the finite
all-pass phase-angle identities on the sibling endpoint programme.

For `y>0`, define the logarithmic midline defect

\[
\boxed{
\mathfrak J_y(U)
={1\over4\pi y}
\int_{\mathbb R}\log|U(x+iy)|^2\,dx.
}
\tag{L-105647.1}

The logarithmic singularity is integrable even when the line passes through a
zero or pole.

## 2. One Blaschke factor

For

\[
B_b(z)={z-b\over z-\overline b},
\qquad b=\beta+i\delta,
\]

one has

\[
|B_b(x+iy)|^2
={
 (x-\beta)^2+(y-\delta)^2
 \over
 (x-\beta)^2+(y+\delta)^2
}.
\]

The elementary identity

\[
\int_{\mathbb R}
\log{x^2+a^2\over x^2+c^2}\,dx
=2\pi(a-c)
\qquad(a,c\ge0)
\]

gives

\[
\boxed{
-{1\over4\pi y}
\int_{\mathbb R}\log|B_b(x+iy)|^2\,dx
=
\min\left(1,{\delta\over y}\right).
}
\tag{L-105647.2}

The horizontal coordinate disappears completely.

## 3. Exact finite-quotient formula

Logarithms turn products into sums.  Applying (L-105647.2) to every factor
proves

\[
\boxed{
\mathfrak J_y(U)
=
\sum_k\min\left(1,{\delta_k\over y}\right)
-
\sum_j\min\left(1,{\eta_j\over y}\right).
}
\tag{L-105647.3}

Thus `mathfrak J_y` is a signed, clipped vertical divisor.  It is additive
under multiplication, insensitive to horizontal collisions, and automatically
retains multiplicity.  No model-space Gram inverse or zero-separation constant
occurs.

For every `y` below the shallowest upper factor,

\[
\boxed{
\mathfrak J_y(U)
=\deg B-\deg A
=-\operatorname{wind}U.
}
\tag{L-105647.4}

In general,

\[
\boxed{
\lim_{y\downarrow0}\mathfrak J_y(U)
=-\operatorname{wind}U.
}
\tag{L-105647.5}

This is an exact interior regularization of the signed all-pass index.

## 4. Coarea recovers the complete vertical divisor

Multiplying (L-105647.3) by `y` gives

\[
\boxed{
y\mathfrak J_y(U)
=
\sum_k\min(y,\delta_k)
-
\sum_j\min(y,\eta_j).
}
\tag{L-105647.6}

Consequently, for almost every `y>0`,

\[
\boxed{
{d\over dy}\bigl[y\mathfrak J_y(U)\bigr]
=
\#\{k:\delta_k>y\}
-
\#\{j:\eta_j>y\}.
}
\tag{L-105647.7}

Distributionally,

\[
\boxed{
-{d^2\over dy^2}\bigl[y\mathfrak J_y(U)\bigr]
=
\sum_k\delta_{\delta_k}
-
\sum_j\delta_{\eta_j}.
}
\tag{L-105647.8}

Hence the complete signed vertical divisor is recoverable from one scalar
scale family.  The hard-band signed complement, the shell count, and the
height-flow atoms are three readings of the same coarea object.

## 5. Xi interpretation

For a finite regular canonical-product truncation of

\[
U_H(z)={\Xi'(z-iH)\over\Xi'(z+iH)},
\]

remove the oriented exponential carrier and common real factors.  Then
`mathfrak J_y(U_H)` is the signed clipped count of the inner and anti-inner
shifted `Xi'` factors.  In particular, a zero penetrating only depth `delta`
becomes a complete integer as soon as the interior sampling line satisfies
`y<delta`.

This proves that the microscopic collar is not a failure of index
representation.  It is the requirement that the sampling scale descend with
the shallowest factor.

## 6. Scope

The logarithmic charge controls the **signed index**, not the oriented Hankel
energy or the pointwise differential microscope.  Equal numerator and
denominator degrees can give `mathfrak J_y=0` for every sufficiently small `y`
while retaining a positive phase-angle/Hankel charge.  That exact firewall is
recorded in `R-105647`.  Cofinal passage for Xi must also retain the exponential
carrier, horizontal endpoints, common-zero confluence, and the finite-window
argument-principle ledger.  RH remains unproved.
