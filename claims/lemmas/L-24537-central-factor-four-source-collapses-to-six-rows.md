# L-24537 — The factor-four opposite-parity source has support on only six central rows

Claim ID: `L-24537`  
Title: Pairing any exact central carry certificate with the source `omega_2` eliminates every parent above seven and turns the RH-bearing Riesz coordinate into one explicit six-coefficient functional  
Status: **PROPOSED COMPLETE — exact finite convolution and carry algebra**  
Authoring agent: `gpt56-pro-25`  
Created: 2026-08-08  
Issue: #245  
Dependencies: `L-24523`; PR #268 source normalization  
Scope: central-split counterpart of the bottom-charge/factor-five source

## 1. Source and finite divisor prefix

Define

\[
\omega_2
 =\mu-\frac32\,\delta_2*\mu
      +\frac12\,\delta_4*\mu.
\tag{L-24537.1}
\]

Its Dirichlet series is

\[
\sum_{n\ge1}{\omega_2(n)\over n^s}
 ={(1-2^{-s})(1-2^{-s-1})\over\zeta(s)}.
\tag{L-24537.2}
\]

Convolution with the constant-one sequence gives

\[
\boxed{
\mathbf1*\omega_2
 =\varepsilon-\frac32\delta_2+\frac12\delta_4.
}
\tag{L-24537.3}
\]

Consequently the divisor prefix

\[
D_\omega(x)
 =\sum_{q\le x}\omega_2(q)\left\lfloor{x\over q}\right\rfloor
\]

is the elementary three-step function

\[
\boxed{
D_\omega(x)=
\begin{cases}
1,&1\le x<2,\\
-1/2,&2\le x<4,\\
0,&x\ge4.
\end{cases}}
\tag{L-24537.4}
\]

## 2. Central-row source image

For a central split parent `n>=2`, put

\[
z_\omega(n)
 =\sum_{q=2}^{n}\omega_2(q)\chi_n^{\rm c}(q).
\tag{L-24537.5}
\]

The `q=1` carry indicator is zero, so (L-24537.4) gives

\[
z_\omega(n)
 =D_\omega(n)
  -D_\omega(\lfloor n/2\rfloor)
  -D_\omega(\lceil n/2\rceil).
\tag{L-24537.6}
\]

Direct evaluation yields

\[
\boxed{
\begin{array}{c|rrrrrr}
 n&2&3&4&5&6&7\\ \hline
 z_\omega(n)&-5/2&-1&1&1&1&1/2,
\end{array}}
\tag{L-24537.7}
\]

and

\[
\boxed{z_\omega(n)=0\qquad(n\ge8).}
\tag{L-24537.8}
\]

Indeed, for `n>=8` the parent and both children lie in the zero region of
(L-24537.4).

## 3. Six-row identity for every exact central saturation

Let `A(2),...,A(X)` satisfy

\[
\sum_{n=q}^{X}A(n)\chi_n^{\rm c}(q)=w(q)
\qquad(2\le q\le X).
\tag{L-24537.9}
\]

Pair with `omega_2(q)` and use (L-24537.7)--(L-24537.8).  One obtains the exact
finite identity

\[
\boxed{
\sum_{q=2}^{X}\omega_2(q)w(q)
 =-\frac52A(2)-A(3)
   +A(4)+A(5)+A(6)+\frac12A(7).
}
\tag{L-24537.10}
\]

Every coefficient `A(n)` above seven disappears, with no sign or positivity
hypothesis.

For the explicit central-Neumann vector `A_X` of `L-24523`, the right side is
computed by the terminating recurrence alone.

## 4. Complete Riesz coordinate

For the critical target, define

\[
\widetilde{\mathcal R}_{\omega}(X)
 =\sum_{q\le X}{\omega_2(q)\over\sqrt q}\log{X\over q}.
\tag{L-24537.11}
\]

Since `omega_2(1)=1`, equations (L-24537.10)--(L-24537.11) give

\[
\boxed{
\widetilde{\mathcal R}_{\omega}(X)
 =\log X
  -\frac52A_X(2)-A_X(3)
  +A_X(4)+A_X(5)+A_X(6)+\frac12A_X(7).
}
\tag{L-24537.12}
\]

Its Mellin transform is initially

\[
\boxed{
{(1-2^{-z-1/2})(1-2^{-z-3/2})
 \over z^2\zeta(z+1/2)}.
}
\tag{L-24537.13}
\]

The two finite Euler factors have zeros only on `Re(z)=-1/2` and
`Re(z)=-3/2`.  Hence no hypothetical zeta zero with real part greater than
`1/2` is canceled.

Therefore

\[
\widetilde{\mathcal R}_{\omega}(X)=X^{o(1)}
\tag{L-24537.14}
\]

is a valid RH criterion.

## 5. Relation to existing bottom charges

PR #268 proves that the same source has a compact image on the average-row
carry matrix and obtains the two-coefficient charge

\[
5c_X(2)+3c_X(3).
\]

Equation (L-24537.12) is the central-split gauge of that source.  The two
formulas are not separate arithmetic hypotheses; both are finite source images
of the same Riesz coordinate.

The central gauge has a proof-production advantage: `A_X(2),...,A_X(7)` are
outputs of one explicit nilpotent recurrence.  It has a disadvantage: their
required signed combination remains RH-bearing.

## 6. Stage form

With

\[
A_X(n)=\sum_j[f_{X,j}(n)-f_{X,j}(n+1)],
\]

summation by parts in the six-row functional expresses
`widetilde R_omega(X)` using only stage values

\[
f_{X,j}(2),...,f_{X,j}(8).
\]

Thus a production recurrence may use a fixed seven-dimensional bottom state;
no growing endpoint vector is required by the final consumer.

The finite state must still receive all boundary injections before they are
projected.  A bound on the seven low coordinates which omits the outer-anchor
source is invalid.

## 7. Proof boundary

Proved exactly:

- finite source convolution;
- compact central-row image;
- six-coefficient certificate identity;
- uncancelled reciprocal-zeta Mellin factor.

Open:

- a subpower estimate for the six-row combination;
- a strict finite-state lower-scale recurrence;
- RH.
